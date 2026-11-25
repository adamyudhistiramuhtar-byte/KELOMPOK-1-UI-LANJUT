# User flow dan sitemap — DRAFT

```text
/ Beranda → /team → /team/:id → /team
          → /projects → /projects/:id → /team/:id atau /projects
Navigasi → /contact → tautan profesional yang disetujui
```

Pencarian dan filter dilakukan di `/projects`. Request data: loading → hasil / empty / error; dari error pengunjung dapat retry. Jika proyek unggulan belum tersedia, tidak ada tautan fiktif. Ini adalah alur sistem usulan, bukan proses AS-IS yang telah diobservasi. Detail: [use case](use-case.md).
