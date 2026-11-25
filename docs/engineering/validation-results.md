# Governance validation evidence — 25 November 2026

Environment: isolated macOS checkout, Python 3.9.6, Git, temporary repositories and synthetic fixtures. `python3 -m unittest discover -s tests -v`: 10 tests passed, 0 failed. Syntax compilation passed after an initial sandbox denial for the macOS Python cache and a rerun with the required permission. An initial valid push was rejected because the hook parsed the issue number incorrectly; the parser was corrected and a valid-push fixture was added. No live credentials are used in test fixtures.

| Scenario | Expected | Actual |
| --- | --- | --- |
| Valid/invalid branch and commit | Accept valid, reject invalid or missing issue | Pass in unit tests |
| Direct commit/push to main | Reject | Pass using local hooks and temporary bare remote |
| Forbidden path and credential signatures | Reject without printing values | Pass with staged synthetic fixtures for private paths and credential signatures |
| Valid SRS, token JSON, source, lockfile and environment example | Accept path | Pass in path checks; environment example committed in fixture |
| File added then removed in later commit | Reject outgoing history | Pass in temporary history |
| Invalid PR title and conflict marker | Reject | Pass in unit-level checks |
| Failing test suite / unconfigured app | Non-zero / blocked | Pass in temporary fixture |
| Git ignore patterns | Ignore private paths, retain legitimate paths | 12 local check-ignore checks passed |
| Application build, lint and integration | Not applicable until stack exists | NOT RUN; no application manifest |
| GitHub Actions | Run policy and governance tests on PR | PASS on prior PR head: [policy](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/actions/runs/45645812282), [tests](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/actions/runs/45645811867); newer commits require fresh runs |
| Branch protection | Apply only after independent review and merge | PENDING; no claim of remote enforcement |

These checks are limited to tested patterns; no scanner guarantees detection of every secret or private transcript. CI and local hooks do not prevent a file from reaching a remote by other means. Required server controls need the approved rollout and actual workflow results.

## Additional audit — 26 November 2026

The current session adds tests for nested and mixed-case paths, spaces, missing remote tracking, multiple refs, mismatched issue/branch, PR author assignment and the exact-SHA legacy exception. Four legacy branch ranges were scanned locally with content checks retained. A temporary package-manager fixture verifies that configured format and lint scripts can execute, and failures remain blocking. The current local suite ran 14 tests with 14 pass, 0 fail. A first pre-push test run exposed seven fixture-isolation errors caused by inherited Git hook environment; after isolating the fixture process, the same suite passed during subsequent PR #35 and #38 pushes. Current PR #40 HEAD must be rechecked in GitHub Actions after these changes. The original DOCX and UI application are not tested by this governance suite.

The proposed legacy scanner passed for #35 and #37. #36 has pre-existing whitespace findings in its outgoing diff. #38 contains commit `fc5242c20064003573df2884e8173a83a18f3280` with an incorrect synthetic fixture author caused by the initially unisolated test run; its author is rejected. Correction requires an explicitly approved non-destructive migration; no author exception or history rewrite was applied. These findings do not justify disabling validation.
