# Developer onboarding

1. Clone the repository, authenticate the correct GitHub account, and verify repository and private Project access.
2. Read CONTRIBUTING, engineering standards, the relevant SRS/design and your assigned issue. Confirm scope, readiness and dependencies; use My Work in the Project.
3. Install Python 3 and Git; install application dependencies only after the team agrees a stack and lockfile. No application setup command exists yet.
4. From the repository root run `sh scripts/install-hooks` on macOS/Linux or Git Bash for Windows. It sets only repository-local hooksPath and refuses to overwrite existing hooks. Inspect and migrate personal hooks first. Windows users need Git for Windows and Python 3 available as `python3`; configure an equivalent local launcher if necessary.
5. Run `python3 -m unittest discover -s tests -v`; check the validation output. Local hooks are technically bypassable, so CI and protected main are also required.
6. Create an issue branch from current main, implement only the assigned scope, run available checks, inspect and stage explicit paths, commit with the issue footer, push, open a PR, request independent review and update Project based on evidence.
7. Never publish private tool instructions, prompts or secrets. Update Project status only when the corresponding conditions are met.
