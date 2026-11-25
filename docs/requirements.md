# Requirements — Draft

ID SRS resmi belum tersedia; label berikut adalah referensi sementara dan perlu dipetakan ke SRS yang disepakati.

| Referensi sementara | Kebutuhan dan kriteria penerimaan |
| --- | --- |
| Beranda | `/` memuat identitas, headline dan deskripsi yang ditentukan, nilai, CTA tim/proyek dan tautan teks proyek unggulan; tidak menampilkan seluruh kartu. |
| Tim | `/team` menampilkan enam kartu responsif; setiap kartu dapat diakses keyboard/pointer dan membuka profil. |
| Profil | `/team/:id` memuat identitas, about, skills, 3–5 screenshot karya, deskripsi, teknologi, tautan tersedia dan kontak yang disetujui; kembali ke Tim. |
| Proyek | `/projects` menampilkan minimal tiga proyek, informasi kartu, pencarian dan filter kategori. |
| Detail | `/projects/:id` memuat latar, tujuan, fitur, teknologi, visual, kontribusi, tautan tersedia dan navigasi ke proyek/profil. |
| Kontak | `/contact` menampilkan kontak profesional anggota yang disetujui; tanpa formulir atau email kolektif. |
| API | Minimal satu API relevan berkomunikasi request-response nyata; loading, error, empty dan retry dapat diperiksa. |
| Kualitas | Komponen reusable, props/composition, routing, state, responsif, aksesibilitas, test case dan hasil aktual. |
| Deliverables | Website dapat diakses, repository, board, SRS, flow, arsitektur, kontrak API, hasil uji, deck, kontribusi dan proses Scrum. |
