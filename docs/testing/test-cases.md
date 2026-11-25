# Test cases — DRAFT / NOT RUN

Skenario berikut belum dijalankan; hasil aktual hanya dicatat di [test-results](test-results.md). Data dan izin perlu disiapkan oleh tim.

| ID | Persiapan dan langkah | Hasil yang diharapkan |
| --- | --- | --- |
| TC-FR-01 | Pada /, sediakan permintaan / dan jalankan skenario menampilkan identitas dan hero. | Nama, headline dan deskripsi persis sesuai baseline. |
| TC-FR-02 | Pada /, sediakan pilihan navigasi dan jalankan skenario menampilkan navigasi utama. | Setiap tautan menuju route yang ditetapkan. |
| TC-FR-03 | Pada /, sediakan referensi proyek yang disetujui dan jalankan skenario menampilkan tautan proyek unggulan. | Jika tersedia, tautan membuka detail proyek yang sesuai. |
| TC-FR-04 | Pada /team, sediakan data anggota dan jalankan skenario menampilkan daftar anggota. | Enam kartu sesuai data dan dapat dipilih. |
| TC-FR-05 | Pada /team → /team/:id, sediakan pilihan kartu dan id dan jalankan skenario membuka profil anggota. | Setiap kartu membuka profil yang sesuai dan dapat digunakan dengan keyboard. |
| TC-FR-06 | Pada /team/:id, sediakan id dan data anggota dan jalankan skenario menampilkan identitas dan kompetensi. | Elemen yang tersedia dan disetujui sesuai anggota yang dipilih. |
| TC-FR-07 | Pada /team/:id, sediakan data karya dan persetujuan dan jalankan skenario menampilkan galeri karya. | Setiap anggota memiliki 3–5 screenshot dan metadata sesuai sumber yang disetujui. |
| TC-FR-08 | Pada /team/:id, sediakan tautan yang diizinkan dan jalankan skenario menampilkan tautan personal. | Tautan yang tampil sesuai data yang disetujui dan dapat dibuka. |
| TC-FR-09 | Pada /projects, sediakan data proyek dan jalankan skenario menampilkan showcase proyek. | Minimal tiga kartu dengan atribut yang ditentukan ditampilkan. |
| TC-FR-10 | Pada /projects, sediakan teks pencarian dan jalankan skenario mencari proyek. | Hasil cocok dengan aturan pencarian yang disepakati; query tanpa hasil menampilkan empty state. |
| TC-FR-11 | Pada /projects, sediakan kategori terpilih dan jalankan skenario memfilter kategori. | Hasil hanya mencakup kategori terpilih dan menghormati query aktif. |
| TC-FR-12 | Pada /projects/:id, sediakan id proyek dan jalankan skenario menampilkan detail proyek. | Data detail sesuai proyek dan link ke profil kontributor tersedia. |
| TC-FR-13 | Pada /contact, sediakan data kontak yang disetujui dan jalankan skenario menampilkan direktori kontak. | Enam entri memuat informasi yang diizinkan; tidak ada email kolektif atau form tim. |
| TC-FR-14 | Pada /projects, sediakan status request dan respons dan jalankan skenario menampilkan status pengambilan data. | Tiap kondisi memunculkan state yang berbeda dan dapat dipahami. |
| TC-FR-15 | Pada /projects, sediakan aktivasi retry dan jalankan skenario mengulangi request gagal. | Retry memicu request baru dan hasilnya ditampilkan. |
| TC-FR-16 | Pada /team/:id; /projects/:id, sediakan aktivasi tautan kembali dan jalankan skenario mengembalikan pengunjung. | Tautan profil menuju /team dan tautan detail menuju /projects. |
