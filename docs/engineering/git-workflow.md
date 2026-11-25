# Git workflow

`main` is the integration branch. Start only after checking the assigned issue, acceptance criteria, dependency and design gate; inspect the working tree, existing branch and PR first. Fetch without overwriting uncommitted work. Use `feature|fix|docs|refactor|test|chore|hotfix/<issue-number>-<lowercase-kebab-description>`. One issue per branch unless a documented dependency is agreed.

Commit format: `type(scope): imperative summary`, at most 72 ASCII characters, followed by a separate `Refs: #<issue>` footer matching the branch issue. Allowed types: feat, fix, docs, style, refactor, test, chore, build, ci, perf and revert. Preserve legitimate authorship and required attribution. Controlled exceptions: a Git-generated merge message is allowed only for a real merge commit; a Git-generated revert must reference an existing commit and include the matching `Refs: #issue` footer. Both remain subject to independent review and range scanning. Historical commits are not rewritten; older open PRs need an agreed migration before strict checks become required.

Inspect `git status`, unstaged and staged diffs; stage explicit paths and run `git diff --cached --check`. Do not use broad staging without inspecting all changes, `--no-verify`, hard reset, destructive clean or force push. Run relevant checks before pushing. A PR title follows `type(scope): summary (#issue)` and includes a matching `Refs: #issue` line. No direct push to main, premature merge, self-approval or automatic Done on merge.

## Historical migration and application foundation

The [legacy migration proposal](legacy-migration.md) identifies exact historical commit IDs and never exempts content scanning or future commits; it requires independent review. The CI policy uses the base-branch validator when available. Bootstrap is confined to PR #40 on the observed original main SHA; human review remains necessary to protect the workflow definition itself.

When an application manifest is introduced, hooks require one committed lockfile and the agreed package scripts: `format:check` and `lint` for pre-commit, `test` and `build` for pre-push; `typecheck` also runs if present. The corresponding package manager must already be installed; hooks do not install dependencies. The checked-out manifest and tracked working files must match the version being validated. The application CI currently fails closed if a manifest appears until the application owner configures reviewed installation and checks. This contract needs Alexius's review; it does not select a framework.
