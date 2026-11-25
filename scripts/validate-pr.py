#!/usr/bin/env python3
"""Check PR metadata and assigned issue without printing private content."""
import json
import os
import re
import sys
import urllib.error
import urllib.request
from policy import branch_ok, title_ok


def main():
    branch = os.environ['PR_BRANCH']
    title = os.environ['PR_TITLE']
    body = os.environ.get('PR_BODY', '')
    if not branch_ok(branch) or not title_ok(title):
        raise ValueError('Invalid branch or PR title')
    issue = branch.split('/', 1)[1].split('-', 1)[0]
    if not title.endswith('(#' + issue + ')') or not re.search(r'(?im)^Refs:\s*#' + issue + r'\s*$', body):
        raise ValueError('PR title and Refs footer must match branch issue')
    url = 'https://api.github.com/repos/' + os.environ['REPOSITORY'] + '/issues/' + issue
    request = urllib.request.Request(url, headers={'Authorization': 'Bearer ' + os.environ['GH_TOKEN'], 'Accept': 'application/vnd.github+json', 'User-Agent': 'repository-policy'})
    with urllib.request.urlopen(request, timeout=15) as response:
        data = json.load(response)
    if 'pull_request' in data or data.get('state') != 'open':
        raise ValueError('Referenced issue is not an open issue')
    author = os.environ['PR_AUTHOR'].lower()
    if author not in {user['login'].lower() for user in data.get('assignees', [])}:
        raise ValueError('PR author is not assigned; coordinate reassignment before PR')
    print('Branch, title, issue reference and assignee verified')


if __name__ == '__main__':
    try:
        main()
    except (KeyError, ValueError, OSError, urllib.error.URLError):
        print('PR metadata validation failed or could not verify GitHub issue', file=sys.stderr)
        sys.exit(1)
