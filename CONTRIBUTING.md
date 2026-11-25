# Contributing — usulan untuk disepakati

Gunakan GitHub Flow: issue → branch (`feature/issue-number-short-description`, `fix/…`, `docs/…`, `test/…`) → commit → pull request → minimal satu peer review → merge → Done. Usulan Conventional Commits: `feat:`, `fix:`, `docs:`, `style:`, `refactor:`, `test:`, `chore:`. PR memuat deskripsi, issue terkait, screenshot untuk UI, dan hasil uji relevan. Jangan memublikasikan data personal atau karya tanpa persetujuan. Jangan mengubah branch protection tanpa kesepakatan yang diperlukan.

## Branch dan review

Nama yang diusulkan: `feature/<issue>-<ringkasan>`, `fix/<issue>-<ringkasan>`, `docs/<issue>-<ringkasan>`, `test/<issue>-<ringkasan>`. Gunakan `Refs #N` saat PR belum memenuhi seluruh DoD; `Closes #N` hanya bila merge memenuhi syarat penutupan. PR menuju main setelah update dari main, minimal satu peer review, perbaikan temuan dan merge oleh anggota yang berwenang. Jangan force push atau memalsukan identitas commit. Penggunaan bantuan AI harus dicatat sesuai kebijakan akademik dan kesepakatan tim; ketentuannya belum dikonfirmasi.


## Operasi dan quality gate — usulan

PR menjelaskan objective, requirement, perubahan, evidence, test, limitations dan issue. Minimal satu peer review selain author sebelum merge; selesaikan percakapan. Squash merge adalah usulan default jika disetujui. CI checks hanya dijadikan required setelah benar-benar tersedia; pengaturan proteksi administratif memerlukan persetujuan yang relevan.
