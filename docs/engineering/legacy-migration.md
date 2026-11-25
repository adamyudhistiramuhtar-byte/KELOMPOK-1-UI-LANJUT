# Legacy PR compatibility — proposed, awaiting PR #40 review

The baseline PRs predate mandatory commit subjects and issue footers. The following exact immutable SHAs are proposed for a **message-only** exception, bound to the matching issue number. The validator still scans every legacy commit's changed content and paths, including added-then-deleted files, and examines commit messages for credential patterns. New commit SHAs must satisfy the standard. A matching SHA for a different issue is not exempt. This proposal does not rewrite history or approve any PR.

| PR / issue | Historical commit SHA | Review required |
| --- | --- | --- |
| #35 / #1 | `483d9c422a268fe39c652c482e7a6b40a149c9da` | Yes |
| #35 / #1 | `1c7c36354f70d2d37dacda851c70ced35c916ca4` | Yes |
| #35 / #1 | `16c612f7a50375e52c30c5b54bd8d943939f4408` | Yes |
| #35 / #1 | `ad9092c2a0d13d3b5cd51f162c656914502b1808` | Yes |
| #36 / #2 | `c6b39f63d180adb89cedbf6b888f67ef43690be0` | Yes |
| #36 / #2 | `70703a3c448e0b3fc6f9e9ddebe68b5e2727e035` | Yes |
| #36 / #2 | `6965f64bc55a487fb4419862159b8a7488901f70` | Yes |
| #37 / #8 | `d585a80d6a20217f75cbdbb9fe055fff4477c1cf` | Yes |
| #38 / #13 | `61053614dfd1dd6a5ee7550980e7b0abb5316ea6` | Yes |
| #38 / #13 | `368cf93414ce60b0c346ab8cedfaf762677fece8` | Yes |

The checked-in allowlist is active only if the reviewed governance change is merged. No author, branch, date, entire PR, file content or future commit receives a blanket exception. Never add a SHA simply to hide a violation; amendments require independent review. Before merging #40, its workflow can only bootstrap itself from its own proposed code on the exact original base and PR number; therefore independent review is indispensable. Once merged, the policy workflow reads validator and allowlist from the protected base revision, but workflow-definition changes still require CODEOWNERS and branch-protection enforcement.

## Documentation overlap

A three-way comparison on 26 November 2026 between main, #36 and #40 found one conflict block each in README.md, CONTRIBUTING.md and .github/PULL_REQUEST_TEMPLATE.md. Integrate #40 only after peer approval, then merge main into #36 without force push; preserve the project/Scrum content and governance requirements, run checks, and obtain required re-review. No conflict was resolved before the chosen base change.

## Attribution incident — #38

Commit `fc5242c20064003573df2884e8173a83a18f3280` was created with an incorrect synthetic fixture author after a local test inherited Git environment variables. It is not on the legacy allowlist, and author validation correctly rejects it. The local fixture isolation was corrected and the temporary clone configuration restored. Do not merge this commit as-is or rewrite history/replace the PR without explicit authorization. A replacement branch/PR preserving the actual changes and truthful attribution is one possible action, subject to maintainer approval and coordination.
