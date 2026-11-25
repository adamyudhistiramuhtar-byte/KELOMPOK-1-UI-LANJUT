# Repository hygiene

Never publish private assistant instructions, conversation transcripts, private memory, personal tool settings, tokens, private keys or personal data without permission. Shared engineering policies, source files, design documentation, SRS, lockfiles and approved evidence remain legitimate. Environment examples contain placeholders only. Review staged paths and content, all newly introduced commits, PR diffs and published artifacts. Ignore rules are not a security boundary.

The scanner uses explicit path patterns and limited high-confidence credential patterns; it cannot guarantee detection of every secret or private transcript. It never prints matched secret content. If a secret reaches a remote, notify the owner and rotate or revoke it; do not rewrite history without coordinated approval. Agent disclosures required by academic or licence policy must not be suppressed.
