# Requirements Traceability Matrix — DRAFT

ID FR/NFR sementara diturunkan dari instruksi pengguna, belum dipetakan ke SRS asli. TC-FR adalah rancangan uji; belum dijalankan. Status setiap baris: usulan / belum diverifikasi.

| Requirement ID | Deskripsi | Sumber | Use case | Screen | Acceptance criteria | Test case | GitHub issue | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FR-01 | Menampilkan identitas dan hero | Instruksi pengguna | UC-01 | / | Nama, headline dan deskripsi persis sesuai baseline | TC-FR-01 | [#8](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/8) | Usulan; belum diuji |
| FR-02 | Menampilkan navigasi utama | Instruksi pengguna | UC-01 | / | Setiap tautan menuju route yang ditetapkan | TC-FR-02 | [#7](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/7), [#8](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/8) | Usulan; belum diuji |
| FR-03 | Menampilkan tautan proyek unggulan | Instruksi pengguna | UC-01 | / | Jika tersedia, tautan membuka detail proyek yang sesuai | TC-FR-03 | [#8](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/8), [#20](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/20) | Usulan; belum diuji |
| FR-04 | Menampilkan daftar anggota | Instruksi pengguna | UC-02 | /team | Enam kartu sesuai data dan dapat dipilih | TC-FR-04 | [#9](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/9), [#11](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/11), [#12](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/12) | Usulan; belum diuji |
| FR-05 | Membuka profil anggota | Instruksi pengguna | UC-02 | /team → /team/:id | Setiap kartu membuka profil yang sesuai dan dapat digunakan dengan keyboard | TC-FR-05 | [#9](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/9), [#10](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/10), [#12](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/12) | Usulan; belum diuji |
| FR-06 | Menampilkan identitas dan kompetensi | Instruksi pengguna | UC-03 | /team/:id | Elemen yang tersedia dan disetujui sesuai anggota yang dipilih | TC-FR-06 | [#10](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/10), [#15](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/15) | Usulan; belum diuji |
| FR-07 | Menampilkan galeri karya | Instruksi pengguna | UC-03 | /team/:id | Setiap anggota memiliki 3–5 screenshot dan metadata sesuai sumber yang disetujui | TC-FR-07 | [#11](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/11), [#14](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/14), [#15](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/15) | Usulan; belum diuji |
| FR-08 | Menampilkan tautan personal | Instruksi pengguna | UC-03 | /team/:id | Tautan yang tampil sesuai data yang disetujui dan dapat dibuka | TC-FR-08 | [#15](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/15), [#29](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/29) | Usulan; belum diuji |
| FR-09 | Menampilkan showcase proyek | Instruksi pengguna | UC-04 | /projects | Minimal tiga kartu dengan atribut yang ditentukan ditampilkan | TC-FR-09 | [#17](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/17), [#20](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/20), [#21](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/21) | Usulan; belum diuji |
| FR-10 | Mencari proyek | Instruksi pengguna | UC-04 | /projects | Hasil cocok dengan aturan pencarian yang disepakati; query tanpa hasil menampilkan empty state | TC-FR-10 | [#18](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/18) | Usulan; belum diuji |
| FR-11 | Memfilter kategori | Instruksi pengguna | UC-04 | /projects | Hasil hanya mencakup kategori terpilih dan menghormati query aktif | TC-FR-11 | [#18](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/18) | Usulan; belum diuji |
| FR-12 | Menampilkan detail proyek | Instruksi pengguna | UC-05 | /projects/:id | Data detail sesuai proyek dan link ke profil kontributor tersedia | TC-FR-12 | [#19](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/19), [#20](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/20) | Usulan; belum diuji |
| FR-13 | Menampilkan direktori kontak | Instruksi pengguna | UC-06 | /contact | Enam entri memuat informasi yang diizinkan; tidak ada email kolektif atau form tim | TC-FR-13 | [#11](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/11), [#16](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/16), [#29](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/29) | Usulan; belum diuji |
| FR-14 | Menampilkan status pengambilan data | Instruksi pengguna | UC-04 | /projects | Tiap kondisi memunculkan state yang berbeda dan dapat dipahami | TC-FR-14 | [#21](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/21), [#22](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/22) | Usulan; belum diuji |
| FR-15 | Mengulangi request gagal | Instruksi pengguna | UC-04 | /projects | Retry memicu request baru dan hasilnya ditampilkan | TC-FR-15 | [#21](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/21), [#22](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/22) | Usulan; belum diuji |
| FR-16 | Mengembalikan pengunjung | Instruksi pengguna | UC-03 | /team/:id; /projects/:id | Tautan profil menuju /team dan tautan detail menuju /projects | TC-FR-16 | [#10](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/10), [#19](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/19) | Usulan; belum diuji |

## Cakupan seluruh issue

Pemetaan berikut adalah **usulan**, bukan penggantian ID resmi SRS atau perubahan scope PIC lain. Process/deliverable tidak dipaksakan menjadi FR.

| Issue | Referensi sementara | Status |
| --- | --- | --- |
| [#1](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/1) | Deliverable SRS/brief; FR-01–16, NFR-01–10 | Menunggu review PIC dan rekonsiliasi SRS |
| [#2](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/2) | Process Scrum dan GitHub Flow | Menunggu review PIC dan rekonsiliasi SRS |
| [#3](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/3) | FR-01–16; NFR-09 | Menunggu review PIC dan rekonsiliasi SRS |
| [#4](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/4) | FR-04–15; kontrak API | Menunggu review PIC dan rekonsiliasi SRS |
| [#5](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/5) | NFR-05, NFR-06, NFR-09 | Menunggu review PIC dan rekonsiliasi SRS |
| [#6](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/6) | NFR-09 | Menunggu review PIC dan rekonsiliasi SRS |
| [#7](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/7) | FR-02, NFR-05, NFR-06 | Menunggu review PIC dan rekonsiliasi SRS |
| [#8](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/8) | FR-01–03, NFR-05, NFR-06 | Menunggu review PIC dan rekonsiliasi SRS |
| [#9](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/9) | FR-04, FR-05 | Menunggu review PIC dan rekonsiliasi SRS |
| [#10](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/10) | FR-05, FR-06, FR-16 | Menunggu review PIC dan rekonsiliasi SRS |
| [#11](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/11) | BR-01, BR-02, BR-04; NFR-07 | Menunggu review PIC dan rekonsiliasi SRS |
| [#12](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/12) | FR-04–06; integrasi sumber | Menunggu review PIC dan rekonsiliasi SRS |
| [#13](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/13) | Process Sprint Review dan Retrospective | Menunggu review PIC dan rekonsiliasi SRS |
| [#14](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/14) | FR-07 | Menunggu review PIC dan rekonsiliasi SRS |
| [#15](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/15) | FR-06–08 | Menunggu review PIC dan rekonsiliasi SRS |
| [#16](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/16) | FR-13 | Menunggu review PIC dan rekonsiliasi SRS |
| [#17](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/17) | FR-09 | Menunggu review PIC dan rekonsiliasi SRS |
| [#18](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/18) | FR-10, FR-11 | Menunggu review PIC dan rekonsiliasi SRS |
| [#19](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/19) | FR-12, FR-16 | Menunggu review PIC dan rekonsiliasi SRS |
| [#20](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/20) | FR-03, FR-09, FR-12 | Menunggu review PIC dan rekonsiliasi SRS |
| [#21](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/21) | FR-09, FR-14, FR-15; API nyata | Menunggu review PIC dan rekonsiliasi SRS |
| [#22](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/22) | FR-14, FR-15 | Menunggu review PIC dan rekonsiliasi SRS |
| [#23](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/23) | NFR-05, NFR-06 | Menunggu review PIC dan rekonsiliasi SRS |
| [#24](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/24) | FR-01–16; integrasi | Menunggu review PIC dan rekonsiliasi SRS |
| [#25](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/25) | Process Sprint Review dan Retrospective | Menunggu review PIC dan rekonsiliasi SRS |
| [#26](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/26) | FR-14, FR-15; NFR-03, NFR-10 | Menunggu review PIC dan rekonsiliasi SRS |
| [#27](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/27) | NFR-01, NFR-05, NFR-06 | Menunggu review PIC dan rekonsiliasi SRS |
| [#28](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/28) | FR-02, FR-05, FR-10, FR-11, FR-16 | Menunggu review PIC dan rekonsiliasi SRS |
| [#29](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/29) | BR-01, BR-04; NFR-07 | Menunggu review PIC dan rekonsiliasi SRS |
| [#30](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/30) | NFR-03, NFR-10; defect | Menunggu review PIC dan rekonsiliasi SRS |
| [#31](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/31) | Deliverable website dapat diakses; NFR-08 | Menunggu review PIC dan rekonsiliasi SRS |
| [#32](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/32) | Deliverable dokumentasi dan kontribusi | Menunggu review PIC dan rekonsiliasi SRS |
| [#33](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/33) | Deliverable pitch deck dan final acceptance | Menunggu review PIC dan rekonsiliasi SRS |
| [#34](https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT/issues/34) | Process weekly status dan koordinasi | Menunggu review PIC dan rekonsiliasi SRS |
