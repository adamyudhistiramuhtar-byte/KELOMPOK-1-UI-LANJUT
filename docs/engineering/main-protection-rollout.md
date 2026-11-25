# Main branch protection — prepared, not activated

Only apply after PR #40 has independent approval, its reviewed code is integrated into main, the current `policy` and `governance-tests` check runs have succeeded, and the precise-SHA legacy migration has been reviewed. Check existing protection/rulesets again before applying; preserve any unrelated protections and confirm that eligible non-author CODEOWNERS can review each path.

## Candidate controls for administrator review

- Require a pull request and one independent approval; dismiss stale approvals and require resolution of review conversations.
- Require the observed GitHub Actions check-run contexts `policy` and `governance-tests`. Re-verify exact job names, event coverage, and successful current-main runs before making either required. Do not require nonexistent application checks.
- Require CODEOWNERS review only after validating permissions and avoiding single-reviewer deadlock. The author cannot satisfy their own approval.
- Enforce protections for administrators if the repository plan supports it; disable force pushes and branch deletion. Do not add unrestricted bypass.
- Do not enable linear history until squash merge is agreed. Do not lock the branch or restrict ordinary feature branches unnecessarily.

GitHub's [branch protection API](https://docs.github.com/en/rest/branches/branch-protection) exposes the relevant review, checks, administrator and conversation-resolution settings. No API mutation is run by this document. Verify the actual configuration and test a normal feature-branch PR after activation without pushing secrets or deliberately breaking the real repository. Keep an administrator-led recovery path for configuration mistakes, without routine bypass.

## Outstanding blockers

PR #40 has not received peer approval and is not merged. PR #36 has documentation conflicts and whitespace findings; PR #38 has a known incorrect fixture author which must not be exempted. Project automation includes enabled Auto-close issue and Pull request merged workflows; inspect their actions through GitHub UI before relying on them for DoD. User-level Project visibility and collaborator permissions must be verified separately.
