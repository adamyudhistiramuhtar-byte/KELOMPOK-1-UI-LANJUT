#!/usr/bin/env python3
"""Cek keterlacakan dokumen usulan; tidak menguji produk atau persetujuan."""
from pathlib import Path
import re
root = Path(__file__).resolve().parents[1]
req = (root / 'requirements.md').read_text()
rtm = (root / 'requirements-traceability.md').read_text()
cases = (root / 'testing/test-cases.md').read_text()
uc = (root / 'use-case.md').read_text()
fr = re.findall(r'^### (FR-\d+)', req, re.M)
nfr = re.findall(r'^\| (NFR-\d+)', req, re.M)
ucs = re.findall(r'^## (UC-\d+)', uc, re.M)
checks = {
    '16 unique FR IDs': len(fr) == len(set(fr)) == 16,
    '10 unique NFR IDs': len(nfr) == len(set(nfr)) == 10,
    '6 unique use case descriptions': len(ucs) == len(set(ucs)) == 6,
    'each FR has traceability and a test case': all(f'| {f} |' in rtm and 'TC-'+f in cases for f in fr),
    '34 issues referenced in RTM': all(f'/issues/{i})' in rtm for i in range(1, 35)),
    'source status is draft': 'DRAFT' in req,
}
for name, ok in checks.items():
    print(('PASS' if ok else 'FAIL') + ': ' + name)
raise SystemExit(0 if all(checks.values()) else 1)
