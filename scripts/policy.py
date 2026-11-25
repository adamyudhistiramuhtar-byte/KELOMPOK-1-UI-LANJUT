#!/usr/bin/env python3
"""Shared Git policy checks. Never print matching secret content."""
import fnmatch
import json
from pathlib import Path
import os
import re
import shutil
import subprocess
import sys

BRANCH = re.compile(r'^(feature|fix|docs|refactor|test|chore|hotfix)/[1-9][0-9]*-[a-z0-9]+(?:-[a-z0-9]+)*$')
SUBJECT = re.compile(r'^(feat|fix|docs|style|refactor|test|chore|build|ci|perf|revert)\([a-z0-9]+(?:-[a-z0-9]+)*\): [a-z][\x20-\x7e]*$')
ISSUE = re.compile(r'(?mi)^Refs:\s*#[1-9][0-9]*\s*$')
PR = re.compile(r'^(feat|fix|docs|style|refactor|test|chore|build|ci|perf|revert)\([a-z0-9]+(?:-[a-z0-9]+)*\): [a-z][\x20-\x7e]* \(#[1-9][0-9]*\)$')
PRIVATE_NAMES = {n.lower() for n in ('AGENTS.md AGENTS.local.md AGENTS.override.md AGENT.md CLAUDE.md CLAUDE.local.md GEMINI.md CODEX.md .cursorrules .windsurfrules .roomodes .clinerules .cursorignore .cursorindexingignore AGENT_RULES.md AGENT_INSTRUCTIONS.md AI_INSTRUCTIONS.md AI_RULES.md SYSTEM_PROMPT.md MASTER_PROMPT.md PROMPT.md PROMPTS.md AGENT_NOTES.md AI_NOTES.md .mcp.json mcp.json credentials.json secrets.json').split()}
PRIVATE_DIRS = {n.lower() for n in ('.claude .codex .cursor .windsurf .gemini .continue .roo .cline .amazonq .kiro .augment .crush .opencode .mcp').split()}
ROOT_PRIVATE_DIRS = {n.lower() for n in ('.ai .agent .agents .prompts prompts agent-output agent-logs ai-output ai-logs chat-logs conversation-history session-history local-notes .local').split()}
SECRET_PATTERNS = [re.compile(rb'-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----'), re.compile(rb'gh[pousr]_[A-Za-z0-9]{30,}'), re.compile(rb'github_pat_[A-Za-z0-9_]{40,}'), re.compile(rb'AKIA[0-9A-Z]{16}'), re.compile(rb'(?i)(?:api[_-]?key|secret[_-]?key|access[_-]?token)\s*[:=]\s*[\x22\x27][A-Za-z0-9_\-/+=]{24,}[\x22\x27]')]
CONFLICT = re.compile(rb'(?m)^(?:<{7}(?: |$)|={7}\s*$|>{7}(?: |$))')


def run(*args, input_data=None, check=True):
    result = subprocess.run(args, input=input_data, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if check and result.returncode:
        raise RuntimeError('Command failed: ' + ' '.join(args[:2]))
    return result



def author_ok(name, email):
    name = name.strip()
    email = email.strip().lower()
    return bool(name and name.lower() != 'fixture' and '@' in email and not email.endswith(('.invalid', '.example', '.test')))


def branch_ok(name):
    return bool(BRANCH.fullmatch(name))


def message_ok(message):
    lines = message.splitlines()
    if not lines or len(lines[0]) > 72 or lines[0].endswith('.'):
        return False
    if any(ord(c) > 127 for c in lines[0]):
        return False
    if not SUBJECT.fullmatch(lines[0]) or not ISSUE.search(message):
        return False
    return not any(p.search(message.encode('utf-8')) for p in SECRET_PATTERNS)



def generated_message_ok(message, parent_count, issue=None, allow_revert=False):
    lines = message.splitlines()
    if not lines or any(p.search(message.encode('utf-8')) for p in SECRET_PATTERNS):
        return False
    if parent_count >= 2 and re.fullmatch(r'Merge (?:branch|remote-tracking branch) .+', lines[0]):
        return True
    if allow_revert and re.fullmatch(r'Revert ".+"', lines[0]):
        reference = re.search(r'(?m)^This reverts commit ([0-9a-f]{40})\.$', message)
        footer = re.search(r'(?mi)^Refs:\s*#([1-9][0-9]*)\s*$', message)
        return bool(reference and footer and (not issue or footer.group(1) == issue)
                    and run('git', 'cat-file', '-e', reference.group(1) + '^{commit}', check=False).returncode == 0)
    return False


def title_ok(title):
    return len(title) <= 100 and bool(PR.fullmatch(title)) and not title.endswith('.)')


def forbidden(path):
    path = path.replace('\\', '/').lower()
    if path.startswith('./'):
        path = path[2:]
    parts = path.split('/')
    name = parts[-1]
    if name in PRIVATE_NAMES or name.startswith('.aider'):
        return True
    if any(x in PRIVATE_DIRS for x in parts[:-1]) or (len(parts) > 1 and parts[0] in ROOT_PRIVATE_DIRS):
        return True
    if path.startswith(('.github/instructions/', '.github/prompts/', '.github/agents/', '.github/skills/')) or path == '.github/copilot-instructions.md':
        return True
    if name == '.env' or (name.startswith('.env.') and name not in ('.env.example', '.env.sample', '.env.template')):
        return True
    if any(fnmatch.fnmatch(name, p) for p in ('*.pem', '*.key', '*.p12', '*.pfx', '*.jks', '*.keystore', '*.tfstate', '*.tfstate.*', '*.prompt.md', '*.prompt.txt', '*.prompt.json', '*.agent.md', '*.instructions.md', '*.chat.json', '*.chatlog', '*.session.json')):
        return True
    return False


def content_problem(data):
    if any(pattern.search(data) for pattern in SECRET_PATTERNS):
        return 'possible credential or private key'
    if b'\x00' not in data and CONFLICT.search(data):
        return 'unresolved conflict marker'
    return None


def scan(path, data):
    problems = []
    if forbidden(path):
        problems.append('forbidden path')
    problem = content_problem(data)
    if problem:
        problems.append(problem)
    if problems:
        print('Policy violation:', repr(path), ', '.join(problems), file=sys.stderr)
    return not problems


def paths(raw):
    return [os.fsdecode(x) for x in raw.split(b'\0') if x]


def staged():
    name = run('git', 'branch', '--show-current').stdout.decode().strip()
    if not branch_ok(name):
        raise RuntimeError('Commit requires a valid issue branch; main and detached HEAD are prohibited')
    if run('git', 'diff', '--cached', '--check', check=False).returncode:
        raise RuntimeError('Staged whitespace or conflict error')
    ok = True
    for path in paths(run('git', 'ls-files', '-z').stdout):
        if forbidden(path):
            print('Policy violation:', repr(path), 'forbidden tracked path', file=sys.stderr)
            ok = False
    for path in paths(run('git', 'diff', '--cached', '--name-only', '--diff-filter=ACMR', '-z').stdout):
        obj = run('git', 'show', ':' + path).stdout
        ok = scan(path, obj) and ok
    return ok


def commits(base, head, check_messages=True, issue=None):
    if run('git', 'merge-base', '--is-ancestor', base, head, check=False).returncode:
        raise RuntimeError('Base is not an ancestor; cannot safely validate commit range')
    ids = run('git', 'rev-list', '--reverse', base + '..' + head).stdout.decode().splitlines()
    if not ids:
        raise RuntimeError('Empty commit range; nothing can be verified')
    ok = True
    if run('git', 'diff', '--check', base, head, check=False).returncode:
        print('Whitespace or conflict error in outgoing diff', file=sys.stderr)
        ok = False
    legacy_path = Path(__file__).with_name('legacy-commits.json')
    legacy = json.loads(legacy_path.read_text(encoding='utf-8'))['commits']
    for commit in ids:
        message = run('git', 'show', '-s', '--format=%B', commit).stdout.decode('utf-8', 'replace')
        author = run('git', 'show', '-s', '--format=%an%x00%ae', commit).stdout.rstrip(b'\n').split(b'\0', 1)
        if len(author) != 2 or not author_ok(*(value.decode('utf-8', 'replace') for value in author)):
            print('Invalid commit author:', commit[:12], file=sys.stderr)
            ok = False
        if any(pattern.search(message.encode('utf-8')) for pattern in SECRET_PATTERNS):
            print('Possible credential in commit message:', commit[:12], file=sys.stderr)
            ok = False
        parents = run('git', 'show', '-s', '--format=%P', commit).stdout.split()
        normal = message_ok(message) and (not issue or bool(re.search(r'(?mi)^Refs:\s*#' + re.escape(issue) + r'\s*$', message)))
        legacy_match = issue is not None and str(legacy.get(commit, '')) == issue
        if check_messages and not (normal or legacy_match or generated_message_ok(message, len(parents), issue, allow_revert=True)):
            print('Invalid commit message:', commit[:12], file=sys.stderr)
            ok = False
        changed = paths(run('git', 'diff-tree', '--root', '-m', '--no-commit-id', '--name-only', '-r', '-z', '--diff-filter=ACMR', commit).stdout)
        for path in set(changed):
            obj = run('git', 'show', commit + ':' + path, check=False)
            if obj.returncode:
                raise RuntimeError('Cannot inspect content in commit ' + commit[:12])
            ok = scan(path, obj.stdout) and ok
    return ok


def app_checks(ref=None, staged=False):
    if staged:
        manifest = run('git', 'show', ':package.json', check=False)
    elif ref:
        if run('git', 'cat-file', '-e', ref + '^{commit}', check=False).returncode:
            raise RuntimeError('Outgoing commit cannot be inspected')
        manifest = run('git', 'show', ref + ':package.json', check=False)
    else:
        if not os.path.exists('package.json'):
            print('Application checks NOT RUN: package.json and agreed stack absent')
            return True
        manifest = None
    if manifest is not None and manifest.returncode:
        print('Application checks NOT RUN: package.json and agreed stack absent')
        return True
    data = manifest.stdout if manifest is not None else Path('package.json').read_bytes()
    try:
        config = json.loads(data)
    except (ValueError, UnicodeDecodeError) as exc:
        raise RuntimeError('Application manifest cannot be parsed') from exc
    if not isinstance(config, dict):
        raise RuntimeError('Application manifest must be an object')
    scripts = config.get('scripts', {})
    names = ['format:check', 'lint'] if staged else ['test', 'build']
    if not staged and 'typecheck' in scripts:
        names.append('typecheck')
    if not isinstance(scripts, dict) or any(not isinstance(scripts.get(n), str) or not scripts[n].strip() for n in names):
        raise RuntimeError('Required application scripts are not configured: ' + ', '.join(names))
    if not Path('package.json').is_file() or Path('package.json').read_bytes() != data:
        raise RuntimeError('Working manifest differs from the version being validated')
    if run('git', 'diff', '--quiet', check=False).returncode:
        raise RuntimeError('Tracked working files differ from the index; cannot validate staged content safely')
    if ref and run('git', 'rev-parse', 'HEAD').stdout.decode().strip() != ref:
        raise RuntimeError('Application checks require the outgoing commit to match the checked-out HEAD')
    location = ':' if staged else ref + ':' if ref else ':'
    locks = [('package-lock.json', 'npm'), ('pnpm-lock.yaml', 'pnpm'), ('yarn.lock', 'yarn')]
    available = [(path, tool) for path, tool in locks if run('git', 'cat-file', '-e', location + path, check=False).returncode == 0]
    if len(available) != 1:
        raise RuntimeError('Exactly one committed package-manager lockfile is required')
    tool = available[0][1]
    if not shutil.which(tool):
        raise RuntimeError('Required package manager is unavailable: ' + tool)
    for name in names:
        result = subprocess.run([tool, 'run', name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode:
            raise RuntimeError('Application check failed: ' + name)
        print('Application check passed:', name)
    return True


def pre_push(remote, url, lines):
    configured = run('git', 'remote', 'get-url', remote).stdout.decode().strip()
    if remote != 'origin' or configured != url:
        raise RuntimeError('Push destination must match configured origin')
    if not lines.strip():
        raise RuntimeError('Push references unavailable')
    ok = True
    checked = []
    for line in lines.splitlines():
        parts = line.split()
        if len(parts) != 4:
            raise RuntimeError('Malformed pre-push reference')
        local_ref, new, remote_ref, old = parts
        if remote_ref == 'refs/heads/main':
            raise RuntimeError('Direct push or deletion of main is prohibited')
        if not remote_ref.startswith('refs/heads/') or not branch_ok(remote_ref[len('refs/heads/'):]):
            raise RuntimeError('Invalid remote branch or unsupported ref')
        if set(new) == {'0'}:
            raise RuntimeError('Branch deletion requires separate manual review')
        if local_ref != remote_ref:
            raise RuntimeError('Local and remote branch names must match')
        if set(old) == {'0'}:
            base = run('git', 'merge-base', new, 'refs/remotes/origin/main').stdout.decode().strip()
        else:
            base = old
        ok = commits(base, new, issue=remote_ref[len('refs/heads/'):].split('/', 1)[1].split('-', 1)[0]) and ok
        checked.append(new)
    return ok and all(app_checks(ref) for ref in checked)


def main(args):
    if not args:
        raise RuntimeError('Expected staged, branch, commit-message, pr-title, range or pre-push')
    command = args[0]
    if command == 'staged':
        return staged()
    if command == 'application-staged':
        return app_checks(staged=True)
    if command == 'branch':
        return branch_ok(args[1])
    if command == 'commit-message':
        with open(args[1], encoding='utf-8') as f:
            message = f.read()
        branch = run('git', 'branch', '--show-current').stdout.decode().strip()
        ident = run('git', 'var', 'GIT_AUTHOR_IDENT', check=False)
        match = re.match(r'^(.+?) <([^>]+)> ', ident.stdout.decode('utf-8', 'replace')) if ident.returncode == 0 else None
        if not branch_ok(branch) or not match or not author_ok(match.group(1), match.group(2)):
            return False
        issue = branch.split('/', 1)[1].split('-', 1)[0]
        normal = message_ok(message) and bool(re.search(r'(?mi)^Refs:\s*#' + re.escape(issue) + r'\s*$', message))
        merge = run('git', 'rev-parse', '--verify', 'MERGE_HEAD', check=False).returncode == 0
        revert = run('git', 'rev-parse', '--verify', 'REVERT_HEAD', check=False).returncode == 0
        return normal or generated_message_ok(message, 2 if merge else 1, issue, allow_revert=revert)
    if command == 'pr-title':
        return title_ok(args[1])
    if command == 'range':
        return commits(args[1], args[2], issue=args[3] if len(args) > 3 else None)
    if command == 'pre-push':
        return pre_push(args[1], args[2], sys.stdin.read())
    raise RuntimeError('Unknown policy command')


if __name__ == '__main__':
    try:
        success = main(sys.argv[1:])
        if not success:
            print('Policy validation failed', file=sys.stderr)
        sys.exit(0 if success else 1)
    except (RuntimeError, OSError, IndexError) as exc:
        print('Policy validation blocked:', str(exc), file=sys.stderr)
        sys.exit(1)
