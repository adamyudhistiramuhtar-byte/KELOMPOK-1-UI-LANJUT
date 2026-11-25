import importlib.util
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

# Git invokes hooks with repository-specific environment variables; fixtures need isolation.
for key in tuple(os.environ):
    if key.startswith('GIT_'):
        del os.environ[key]

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('policy', ROOT / 'scripts/policy.py')
policy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(policy)


def git(cwd, *args, data=None, check=True):
    return subprocess.run(['git', *args], cwd=cwd, input=data, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=check)


class PolicyTests(unittest.TestCase):
    def test_branch_names(self):
        self.assertTrue(policy.branch_ok('feature/8-landing-page'))
        for name in ('main', 'Feature/8-Page', 'feature/8_page', 'feature/landing-page'):
            self.assertFalse(policy.branch_ok(name))

    def test_commit_and_pr(self):
        self.assertTrue(policy.message_ok('feat(home): implement hero\n\nRefs: #8\n'))
        self.assertFalse(policy.message_ok('update\n'))
        self.assertFalse(policy.message_ok('feat(home): implement hero\n'))
        self.assertTrue(policy.title_ok('feat(home): implement hero (#8)'))
        self.assertFalse(policy.title_ok('update'))

    def test_paths_are_specific_and_case_insensitive(self):
        for path in ('AGENTS.md', '.cursor/rules/file', 'notes.prompt.md', '.env', 'x/SECRET.PEM'):
            self.assertTrue(policy.forbidden(path), path)
        for path in ('.env.example', 'docs/SRS.md', 'docs/design-tokens.json', 'src/model.js', 'package-lock.json', 'docs/prompts/example.md', 'docs/engineering/engineering-standards.md'):
            self.assertFalse(policy.forbidden(path), path)

    def test_secrets_and_conflicts(self):
        fake = b'gh' + b'p_' + b'A' * 36
        self.assertIsNotNone(policy.content_problem(fake))
        self.assertIsNotNone(policy.content_problem(b'<' * 7 + b' HEAD\n'))
        self.assertIsNone(policy.content_problem(b'API_URL=https://example.invalid\n'))

    def test_staged_private_paths_and_secret_are_rejected(self):
        with tempfile.TemporaryDirectory() as name:
            root = Path(name)
            git(root, 'init', '-q', '-b', 'main')
            git(root, 'config', 'user.name', 'Fixture')
            git(root, 'config', 'user.email', 'fixture@example.invalid')
            (root / 'README.md').write_text('base\n')
            git(root, 'add', 'README.md')
            git(root, 'commit', '-qm', 'fixture base')
            git(root, 'switch', '-qc', 'feature/8-private-fixture')
            fixtures = {
                '.cursor/rules/local.mdc': b'private fixture\n',
                'nested path/AgEnTs.Md': b'private fixture\n',
                'nested path/file with space.prompt.md': b'private fixture\n',
                'notes.prompt.txt': b'private fixture\n',
                'source.js': b'gh' + b'p_' + b'A' * 36,
            }
            previous = os.getcwd()
            try:
                os.chdir(root)
                for path, data in fixtures.items():
                    f = root / path
                    f.parent.mkdir(parents=True, exist_ok=True)
                    f.write_bytes(data)
                    git(root, 'add', '-f', '--', path)
                    self.assertFalse(policy.staged(), path)
                    git(root, 'reset', '-q', '--', path)
            finally:
                os.chdir(previous)

    def test_pre_push_accepts_valid_branch(self):
        with tempfile.TemporaryDirectory() as name:
            root = Path(name)
            git(root, 'init', '-q', '-b', 'main')
            git(root, 'config', 'user.name', 'Fixture')
            git(root, 'config', 'user.email', 'fixture@example.invalid')
            git(root, 'remote', 'add', 'origin', 'example')
            (root / 'README.md').write_text('base\n')
            git(root, 'add', 'README.md')
            git(root, 'commit', '-qm', 'fixture base')
            base = git(root, 'rev-parse', 'HEAD').stdout.decode().strip()
            git(root, 'update-ref', 'refs/remotes/origin/main', base)
            git(root, 'switch', '-qc', 'feature/8-test-valid')
            (root / 'source.js').write_text('export const value = 1;\n')
            git(root, 'add', 'source.js')
            git(root, 'commit', '-qm', 'feat(home): add source\n\nRefs: #8')
            head = git(root, 'rev-parse', 'HEAD').stdout.decode().strip()
            ref = 'refs/heads/feature/8-test-valid'
            previous = os.getcwd()
            try:
                os.chdir(root)
                self.assertTrue(policy.pre_push('origin', 'example', f'{ref} {head} {ref} ' + '0' * 40 + '\n'))
                self.assertFalse(policy.commits(base, head, issue='9'))
                with self.assertRaisesRegex(RuntimeError, 'Direct push'):
                    policy.pre_push('origin', 'example', f'{ref} {head} {ref} ' + '0' * 40 + f'\nrefs/heads/main {head} refs/heads/main {base}\n')
            finally:
                os.chdir(previous)

    def test_legacy_allowlist_is_exact_and_still_scans_content(self):
        import json
        with tempfile.TemporaryDirectory() as name:
            root = Path(name)
            git(root, 'init', '-q', '-b', 'main')
            git(root, 'config', 'user.name', 'Fixture')
            git(root, 'config', 'user.email', 'fixture@example.invalid')
            (root / 'README.md').write_text('base\n')
            git(root, 'add', 'README.md')
            git(root, 'commit', '-qm', 'base')
            base = git(root, 'rev-parse', 'HEAD').stdout.decode().strip()
            (root / 'legitimate.md').write_text('safe\n')
            git(root, 'add', 'legitimate.md')
            git(root, 'commit', '-qm', 'legacy subject')
            safe = git(root, 'rev-parse', 'HEAD').stdout.decode().strip()
            (root / 'AGENTS.md').write_text('fixture\n')
            git(root, 'add', 'AGENTS.md')
            git(root, 'commit', '-qm', 'legacy forbidden subject')
            bad = git(root, 'rev-parse', 'HEAD').stdout.decode().strip()
            (root / 'legacy-commits.json').write_text(json.dumps({'commits': {safe: 1, bad: 1}}))
            previous, original = os.getcwd(), policy.__file__
            try:
                os.chdir(root)
                policy.__file__ = str(root / 'policy.py')
                self.assertTrue(policy.commits(base, safe, issue='1'))
                self.assertFalse(policy.commits(base, safe, issue='2'))
                self.assertFalse(policy.commits(base, bad, issue='1'))
            finally:
                os.chdir(previous)
                policy.__file__ = original

    def test_pull_request_author_must_be_assigned(self):
        import io
        from unittest.mock import patch
        sys.modules['policy'] = policy
        pspec = importlib.util.spec_from_file_location('validate_pr', ROOT / 'scripts/validate-pr.py')
        module = importlib.util.module_from_spec(pspec)
        pspec.loader.exec_module(module)
        environment = {'PR_BRANCH': 'feature/8-home', 'PR_TITLE': 'feat(home): build hero (#8)',
                       'PR_BODY': 'Refs: #8', 'PR_AUTHOR': 'not-assigned',
                       'REPOSITORY': 'owner/repository', 'GH_TOKEN': 'fixture'}
        class Response(io.BytesIO):
            def __enter__(self): return self
            def __exit__(self, *args): self.close()
        with patch.dict(os.environ, environment), patch.object(module.urllib.request, 'urlopen', return_value=Response(b'{"state":"open","assignees":[{"login":"assigned"}]}')):
            with self.assertRaisesRegex(ValueError, 'not assigned'):
                module.main()
        environment['PR_BRANCH'] = 'invalid-branch'
        with patch.dict(os.environ, environment):
            with self.assertRaisesRegex(ValueError, 'Invalid branch'):
                module.main()

    def test_application_scripts_run_when_configured(self):
        import json
        with tempfile.TemporaryDirectory() as name:
            root = Path(name)
            git(root, 'init', '-q', '-b', 'main')
            (root / 'package.json').write_text(json.dumps({'scripts': {'format:check': 'format', 'lint': 'lint', 'test': 'test', 'build': 'build'}}))
            (root / 'package-lock.json').write_text('{}')
            git(root, 'add', 'package.json', 'package-lock.json')
            bindir = root / 'bin'
            bindir.mkdir()
            npm = bindir / 'npm'
            npm.write_text('#!/bin/sh\nexit 0\n')
            npm.chmod(0o755)
            previous, path = os.getcwd(), os.environ.get('PATH', '')
            try:
                os.chdir(root)
                os.environ['PATH'] = str(bindir) + os.pathsep + path
                self.assertTrue(policy.app_checks(staged=True))
                npm.write_text('#!/bin/sh\nexit 1\n')
                with self.assertRaisesRegex(RuntimeError, 'Application check failed'):
                    policy.app_checks(staged=True)
            finally:
                os.chdir(previous)
                os.environ['PATH'] = path

    def test_untracked_main_ref_fails_closed(self):
        with tempfile.TemporaryDirectory() as name:
            root = Path(name)
            git(root, 'init', '-q', '-b', 'main')
            git(root, 'config', 'user.name', 'Fixture')
            git(root, 'config', 'user.email', 'fixture@example.invalid')
            git(root, 'remote', 'add', 'origin', 'example')
            (root / 'README.md').write_text('base\n')
            git(root, 'add', 'README.md')
            git(root, 'commit', '-qm', 'fixture base')
            head = git(root, 'rev-parse', 'HEAD').stdout.decode().strip()
            previous = os.getcwd()
            try:
                os.chdir(root)
                ref = 'refs/heads/feature/8-no-tracking'
                with self.assertRaises(RuntimeError):
                    policy.pre_push('origin', 'example', f'{ref} {head} {ref} ' + '0' * 40 + '\n')
            finally:
                os.chdir(previous)

    def test_unconfigured_application_fails_closed(self):
        with tempfile.TemporaryDirectory() as name:
            previous = os.getcwd()
            try:
                os.chdir(name)
                Path('package.json').write_text('{}')
                with self.assertRaises(RuntimeError):
                    policy.app_checks()
            finally:
                os.chdir(previous)

    def test_failing_test_suite_returns_nonzero(self):
        with tempfile.TemporaryDirectory() as name:
            Path(name, 'test_failure.py').write_text('import unittest\nclass Failure(unittest.TestCase):\n def test_fail(self): self.fail()\n')
            result = subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s', name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.assertNotEqual(result.returncode, 0)

    def test_staging_and_history(self):
        with tempfile.TemporaryDirectory() as name:
            root = Path(name)
            git(root, 'init', '-q', '-b', 'main')
            git(root, 'config', 'user.name', 'Fixture')
            git(root, 'config', 'user.email', 'fixture@example.invalid')
            (root / 'README.md').write_text('base\n')
            git(root, 'add', 'README.md')
            git(root, 'commit', '-qm', 'fixture base')
            base = git(root, 'rev-parse', 'HEAD').stdout.decode().strip()
            (root / 'clean.txt').write_text('clean\n')
            git(root, 'add', 'clean.txt')
            prev = os.getcwd()
            try:
                os.chdir(root)
                with self.assertRaises(RuntimeError):
                    policy.staged()
            finally:
                os.chdir(prev)
            git(root, 'reset', '-q')
            git(root, 'remote', 'add', 'origin', 'example')
            git(root, 'switch', '-qc', 'feature/8-test-history')
            (root / 'AGENTS.md').write_text('synthetic fixture\n')
            git(root, 'add', 'AGENTS.md')
            os.chdir(root)
            try:
                self.assertFalse(policy.staged())
            finally:
                os.chdir(prev)
            git(root, 'commit', '-qm', 'docs(testing): add fixture\n\nRefs: #8')
            git(root, 'rm', '-q', 'AGENTS.md')
            git(root, 'commit', '-qm', 'docs(testing): remove fixture\n\nRefs: #8')
            head = git(root, 'rev-parse', 'HEAD').stdout.decode().strip()
            os.chdir(root)
            try:
                self.assertFalse(policy.commits(base, head))
                with self.assertRaisesRegex(RuntimeError, 'Direct push'):
                    policy.pre_push('origin', 'example', 'refs/heads/main ' + head + ' refs/heads/main ' + base + '\n')
            finally:
                os.chdir(prev)


class HookIntegrationTests(unittest.TestCase):
    def test_hooks_and_push_guard(self):
        import shutil
        with tempfile.TemporaryDirectory() as name:
            root = Path(name) / 'work'
            remote = Path(name) / 'remote.git'
            root.mkdir()
            git(remote.parent, 'init', '--bare', '-q', str(remote))
            git(root, 'init', '-q', '-b', 'main')
            git(root, 'config', 'user.name', 'Fixture')
            git(root, 'config', 'user.email', 'fixture@example.invalid')
            git(root, 'remote', 'add', 'origin', str(remote))
            (root / 'README.md').write_text('base\n')
            git(root, 'add', 'README.md')
            git(root, 'commit', '-qm', 'fixture base')
            base = git(root, 'rev-parse', 'HEAD').stdout.decode().strip()
            git(root, 'update-ref', 'refs/remotes/origin/main', base)
            shutil.copytree(ROOT / 'scripts', root / 'scripts')
            shutil.copytree(ROOT / '.githooks', root / '.githooks')
            shutil.copytree(ROOT / 'tests', root / 'tests', ignore=shutil.ignore_patterns('__pycache__'))
            installer = subprocess.run(['sh', str(root / 'scripts/install-hooks')], cwd=root, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.assertEqual(installer.returncode, 0)
            (root / 'main-only.txt').write_text('x\n')
            git(root, 'add', 'main-only.txt')
            result = git(root, 'commit', '-m', 'docs(testing): reject main', '-m', 'Refs: #8', check=False)
            self.assertNotEqual(result.returncode, 0)
            git(root, 'reset', '-q')
            git(root, 'switch', '-qc', 'feature/8-test-hooks')
            (root / '.env.example').write_text('API_URL=https://example.invalid\n')
            git(root, 'add', '.env.example')
            invalid = git(root, 'commit', '-m', 'update', check=False)
            self.assertNotEqual(invalid.returncode, 0)
            valid = git(root, 'commit', '-m', 'test(testing): verify hooks', '-m', 'Refs: #8', check=False)
            self.assertEqual(valid.returncode, 0, valid.stderr.decode())
            invalid_push = git(root, 'push', 'origin', 'HEAD:refs/heads/main', check=False)
            self.assertNotEqual(invalid_push.returncode, 0)


if __name__ == "__main__":
    unittest.main()
