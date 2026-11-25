# Software Requirements Specification — DRAFT / PERLU KONFIRMASI

Dokumen ini merevisi kerangka repository berdasarkan instruksi pengguna. SRS-Kelompok-1-v0.1, panduan Week 08/09, DESIGN-v5 dan design-tokens-v5 belum ditemukan; draft ini bukan salinan dokumen tersebut. Referensi ID yang dipakai bersifat sementara dan wajib direkonsiliasi tanpa mengubah ID sumber secara diam-diam.

## BAB I — Pendahuluan
### Latar belakang
Website portofolio kelompok diusulkan sebagai sarana penyajian anggota, kompetensi dan karya dalam satu ruang. Klaim mengenai masalah aktual pengguna belum didukung wawancara atau observasi.
### Tujuan pengembangan dan dokumen
Menyediakan informasi portofolio yang dapat diakses dan mendefinisikan dasar bersama untuk desain, implementasi, pengujian dan penerimaan. Dokumen ini belum disetujui.
### Ruang lingkup
Enam route dan batasannya terdapat di [project brief](project-brief.md) dan [requirements](requirements.md). Login, registrasi, pembayaran, CMS, dashboard admin, form kontak tim dan email kolektif di luar scope.
### Definisi
FR: functional requirement; NFR: non-functional requirement; UC: use case; API: application programming interface; RTM: requirements traceability matrix; PIC: penanggung jawab utama.
### Referensi
Instruksi pengguna dan issue GitHub saat audit 25 November 2026. Dokumen tugas dan rancangan asli: [DATA BELUM TERSEDIA].

## BAB II — Deskripsi Umum Sistem
### Perspektif dan product goal
Website publik yang menyajikan informasi anggota dan proyek; sumber API dan stack belum diputuskan. Goal dan stakeholder di [brief](project-brief.md).
### Fungsi utama dan pengguna
Pengunjung menelusuri beranda, anggota, profil, proyek, detail dan kontak. Tidak diasumsikan adanya peran admin atau akun pengguna.
### Lingkungan dan batasan
Web responsif; versi browser, hosting, API dan lingkungan uji menunggu kesepakatan. Konten personal wajib mendapat izin; integrasi API minimal satu request-response nyata.
### Asumsi dan dependency
Ketersediaan konten/izin, fondasi desain, router, komponen, API dan persetujuan tim menentukan implementasi. Proses AS-IS dan BPMN AS-IS tidak disusun karena bukti proses berjalan belum tersedia.

## BAB III — Analisis Kebutuhan
### Kebutuhan pengguna dan tugas
Pengunjung membutuhkan akses terstruktur ke identitas, kompetensi, karya, proyek dan kontak profesional. Ini merupakan tujuan yang diberikan, bukan hasil riset pengguna. Daftar rinci input, aturan, output, exception, prioritas dan kriteria berada pada [requirements](requirements.md).
### Aturan bisnis
BR-01: hanya data dan karya yang disetujui dipublikasikan. BR-02: enam anggota ditampilkan saat konten siap. BR-03: minimal tiga proyek anggota ditampilkan. BR-04: galeri berisi 3–5 screenshot karya per anggota. BR-05: tautan opsional ditampilkan hanya bila tersedia dan diizinkan. BR-06: tidak ada email kolektif/form tim. Semua bersumber dari instruksi pengguna; penerapan perlu diuji.
### Prioritas dan acceptance
Prioritas High pada FR adalah usulan untuk kebutuhan wajib, perlu validasi tim. Setiap FR memiliki acceptance criteria di requirements; penerimaan produk memerlukan bukti implementasi, tes dan review.

## BAB IV — Pemodelan Kebutuhan Sistem
Aktor: Pengunjung. [Use case diagram dan enam deskripsi](use-case.md) adalah model usulan yang diturunkan dari kebutuhan, bukan enam UC SRS asli yang belum tersedia. [User flow](user-flow.md) dan [RTM](requirements-traceability.md) memetakan route, UC, kebutuhan dan issue. Activity, sequence dan class diagram tidak diklaim telah dibuat.

## BAB V — Spesifikasi Antarmuka dan Data
### Screen inventory dan antarmuka
`/`, `/team`, `/team/:id`, `/projects`, `/projects/:id`, `/contact`; lihat requirements untuk isi tiap layar. Arah desain: people-first editorial; design dan token resmi menunggu persetujuan #5.
### Data dan API
Data anggota meliputi identitas, foto, role, about, skills, karya dan kontak yang disetujui. Data proyek meliputi judul, ringkasan, kategori, teknologi, visual dan kontributor. Endpoint, skema, provider dan autentikasi API belum disepakati; kontrak direncanakan oleh #4. Tidak mengklaim integrasi backend tersedia.
### State dan error
State request membedakan loading, data tersedia, empty dan error; retry melakukan request baru. Aturan filter dan state UI dirinci dalam requirements dan harus selaras dengan kontrak API.

## BAB VI — Verification and Validation
Verifikasi dilakukan dengan peninjauan konsistensi dokumen, RTM dan test case; validasi pengguna memerlukan tim/dosen. [Rencana uji](testing/test-plan.md), [test cases](testing/test-cases.md), [hasil aktual](testing/test-results.md), [RTM](requirements-traceability.md), [risiko](risk-register.md) dan [keputusan](decision-log.md). Belum ada hasil uji produk atau approval. Pertanyaan terbuka: dokumen sumber/ID resmi, pilihan stack/API, ketersediaan konten dan izin, browser, target performa, design tokens, jadwal presentasi dan peran Scrum.
