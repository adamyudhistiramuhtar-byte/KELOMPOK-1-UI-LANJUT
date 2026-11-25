#!/usr/bin/env python3
"""Shared Git policy checks. Never print matching secret content."""
import fnmatch
import os
import re
import subprocess
import sys

BRANCH = re.compile(r'^(feature|fix|docs|refactor|test|chore|hotfix)/[1-9][0-9]*-[a-z0-9]+(?:-[a-z0-9]+)*$')
SUBJECT = re.compile(r'^(feat|fix|docs|style|refactor|test|chore|build|ci|perf|revert)\([a-z0-9]+(?:-[a-z0-9]+)*\): [a-z][\x20-\x7e]*$')
ISSUE = re.compile(r'(?mi)^Refs:\s*#[1-9][0-9]*\s*$')
PR = re.compile(r'^(feat|fix|docs|style|refactor|test|chore|build|ci|perf|revert)\([a-z0-9]+(?:-[a-z0-9]+)*\): [a-z][\x20-\x7e]* \(#[1-9][0-9]*\)$')
PRIVATE_NAMES = {n.lower() for n in ('AGENTS.md AGENTS.local.md AGENTS.override.md AGENT.md CLAUDE.md CLAUDE.local.md GEMINI.md CODEX.md .cursorrules .windsurfrules .roomodes .clinerules .cursorignore .cursorindexingignore AGENT_RULES.md AGENT_INSTRUCTIONS.md AI_INSTRUCTIONS.md AI_RULES.md SYSTEM_PROMPT.md MASTER_PROMPT.md PROMPT.md PROMPTS.md AGENT_NOTES.md AI_NOTES.md .mcp.json mcp.json credentials.json secrets.json').split()}
PRIVATE_DIRS = {n.lower() for n in ('.claude .codex .cursor .windsurf .gemini .continue .roo .cline .amazonq .kiro .augment .crush .opencode .mcp .ai .agent .agents .prompts prompts agent-output agent-logs ai-output ai-logs chat-logs conversation-history session-history local-notes .local').split()}
SECRET_PATTERNS = [re.compile(rb'-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----'), re.compile(rb'gh[pousr]_[A-Za-z0-9]{30,}'), re.compile(rb'github_pat_[A-Za-z0-9_]{40,}'), re.compile(rb'AKIA[0-9A-Z]{16}'), re.compile(rb'(?i)(?:api[_-]?key|secret[_-]?key|access[_-]?token)\s*[:=]\s*[\x22\x27][A-Za-z0-9_\-/+=]{24,}[\x22\x27]')]
CONFLICT = re.compile(rb'(?m)^(?:<{7}(?: |$)|={7}\s*$|>{7}(?: |$))')


def run(*args, input_data=None, check=True):
    result = subprocess.run(args, input=input_data, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if check and result.returncode:
        raise RuntimeError('Command failed: ' + ' '.join(args[:2]))
    return result


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
    if any(x in PRIVATE_DIRS for x in parts[:-1]):
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
    for commit in ids:
        message = run('git', 'show', '-s', '--format=%B', commit).stdout.decode('utf-8', 'replace')
        parents = run('git', 'show', '-s', '--format=%P', commit).stdout.split()
        normal = message_ok(message) and (not issue or bool(re.search(r'(?mi)^Refs:\s*#' + re.escape(issue) + r'\s*$', message)))
        if check_messages and not (normal or generated_message_ok(message, len(parents), issue, allow_revert=True)):
            print('Invalid commit message:', commit[:12], file=sys.stderr)
            ok = False
        changed = paths(run('git', 'diff-tree', '--root', '-m', '--no-commit-id', '--name-only', '-r', '-z', '--diff-filter=ACMR', commit).stdout)
        for path in set(changed):
            obj = run('git', 'show', commit + ':' + path, check=False)
            if obj.returncode:
                raise RuntimeError('Cannot inspect content in commit ' + commit[:12])
            ok = scan(path, obj.stdout) and ok
    return ok


def app_checks(ref=None):
    present = run('git', 'cat-file', '-e', ref + ':package.json', check=False).returncode == 0 if ref else os.path.exists('package.json')
    if not present:
        print('Application checks NOT RUN: package.json and agreed stack absent')
        return True
    raise RuntimeError('Application exists but agreed formatter, lint, test and build commands are not configured in governance policy')


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
    if command == 'branch':
        return branch_ok(args[1])
    if command == 'commit-message':
        with open(args[1], encoding='utf-8') as f:
            message = f.read()
        branch = run('git', 'branch', '--show-current').stdout.decode().strip()
        if not branch_ok(branch):
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
