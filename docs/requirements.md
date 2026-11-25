# Requirements — DRAFT / PERLU KONFIRMASI

Sumber: kebutuhan eksplisit pengguna dan issue GitHub; SRS-Kelompok-1-v0.1 dan panduan Week 08/09 belum tersedia. ID FR/NFR di bawah adalah **ID sementara usulan**, bukan ID SRS asli. Aktor utama seluruh FR: Pengunjung. Prioritas FR: High (usulan berdasarkan scope wajib); pengecualian dan pemrosesan bersifat spesifikasi usulan untuk review, bukan bukti implementasi.

### FR-01 — Menampilkan identitas dan hero

- Modul: Beranda; prioritas: High (usulan); aktor: Pengunjung.
- Kebutuhan: Sistem harus menampilkan identitas Kelompok 1, headline dan deskripsi yang ditentukan ketika pengunjung membuka beranda.
- Input: Permintaan /.
- Aturan pemrosesan: Menyajikan naskah yang disepakati.
- Output: Identitas dan hero.
- Kondisi pengecualian: Konten belum tersedia: tandai untuk perbaikan.
- Kriteria penerimaan: Nama, headline dan deskripsi persis sesuai baseline.
- Sumber: instruksi produk pengguna; use case: UC-01; issue: #8.

### FR-02 — Menampilkan navigasi utama

- Modul: Beranda; prioritas: High (usulan); aktor: Pengunjung.
- Kebutuhan: Sistem harus menyediakan navigasi ke Tim, Proyek dan Kontak dari beranda.
- Input: Pilihan navigasi.
- Aturan pemrosesan: Mengikuti route tujuan.
- Output: Halaman tujuan.
- Kondisi pengecualian: Route belum tersedia: jangan klaim berhasil.
- Kriteria penerimaan: Setiap tautan menuju route yang ditetapkan.
- Sumber: instruksi produk pengguna; use case: UC-01; issue: #7, #8.

### FR-03 — Menampilkan tautan proyek unggulan

- Modul: Beranda; prioritas: High (usulan); aktor: Pengunjung.
- Kebutuhan: Sistem harus menampilkan maksimal satu tautan teks ke proyek unggulan yang valid ketika proyek yang disetujui tersedia.
- Input: Referensi proyek yang disetujui.
- Aturan pemrosesan: Memeriksa ketersediaan referensi.
- Output: Tautan teks proyek.
- Kondisi pengecualian: Belum tersedia: tidak menampilkan tautan rusak.
- Kriteria penerimaan: Jika tersedia, tautan membuka detail proyek yang sesuai.
- Sumber: instruksi produk pengguna; use case: UC-01; issue: #8, #20.

### FR-04 — Menampilkan daftar anggota

- Modul: Tim; prioritas: High (usulan); aktor: Pengunjung.
- Kebutuhan: Sistem harus menampilkan enam anggota dalam kartu pada halaman Tim ketika data yang disetujui tersedia.
- Input: Data anggota.
- Aturan pemrosesan: Menampilkan foto, nama dan role masing-masing.
- Output: Enam kartu.
- Kondisi pengecualian: Data belum tersedia: tampilkan status relevan.
- Kriteria penerimaan: Enam kartu sesuai data dan dapat dipilih.
- Sumber: instruksi produk pengguna; use case: UC-02; issue: #9, #11, #12.

### FR-05 — Membuka profil anggota

- Modul: Tim; prioritas: High (usulan); aktor: Pengunjung.
- Kebutuhan: Sistem harus membuka profil anggota yang dipilih dari kartu anggota.
- Input: Pilihan kartu dan ID.
- Aturan pemrosesan: Mencocokkan ID anggota.
- Output: Profil anggota sesuai.
- Kondisi pengecualian: ID tidak ditemukan: tampilkan pesan dan jalan kembali.
- Kriteria penerimaan: Setiap kartu membuka profil yang sesuai dan dapat digunakan dengan keyboard.
- Sumber: instruksi produk pengguna; use case: UC-02; issue: #9, #10, #12.

### FR-06 — Menampilkan identitas dan kompetensi

- Modul: Profil; prioritas: High (usulan); aktor: Pengunjung.
- Kebutuhan: Sistem harus menampilkan foto, nama, role, about dan skills anggota pada profil yang sesuai.
- Input: ID dan data anggota.
- Aturan pemrosesan: Memilih data anggota yang sesuai.
- Output: Identitas dan kompetensi.
- Kondisi pengecualian: Data opsional tidak tersedia: tidak mengarang.
- Kriteria penerimaan: Elemen yang tersedia dan disetujui sesuai anggota yang dipilih.
- Sumber: instruksi produk pengguna; use case: UC-03; issue: #10, #15.

### FR-07 — Menampilkan galeri karya

- Modul: Profil; prioritas: High (usulan); aktor: Pengunjung.
- Kebutuhan: Sistem harus menampilkan tiga sampai lima screenshot karya website yang disetujui beserta judul, deskripsi dan teknologi pada profil.
- Input: Data karya dan persetujuan.
- Aturan pemrosesan: Menampilkan hanya karya yang disetujui.
- Output: Galeri karya.
- Kondisi pengecualian: Konten kurang: tandai belum lengkap; jangan mengarang.
- Kriteria penerimaan: Setiap anggota memiliki 3–5 screenshot dan metadata sesuai sumber yang disetujui.
- Sumber: instruksi produk pengguna; use case: UC-03; issue: #11, #14, #15.

### FR-08 — Menampilkan tautan personal

- Modul: Profil; prioritas: High (usulan); aktor: Pengunjung.
- Kebutuhan: Sistem harus menampilkan tautan live website, repository dan kontak profesional personal ketika tersedia dan disetujui.
- Input: Tautan yang diizinkan.
- Aturan pemrosesan: Menyajikan tautan hanya bila tersedia.
- Output: Tautan personal.
- Kondisi pengecualian: Tautan opsional tidak ada: tidak ditampilkan.
- Kriteria penerimaan: Tautan yang tampil sesuai data yang disetujui dan dapat dibuka.
- Sumber: instruksi produk pengguna; use case: UC-03; issue: #15, #29.

### FR-09 — Menampilkan showcase proyek

- Modul: Proyek; prioritas: High (usulan); aktor: Pengunjung.
- Kebutuhan: Sistem harus menampilkan minimal tiga proyek anggota dalam kartu yang memuat judul, ringkasan, kategori, teknologi dan kontributor ketika data tersedia.
- Input: Data proyek.
- Aturan pemrosesan: Membentuk kartu dari data proyek.
- Output: Daftar proyek.
- Kondisi pengecualian: Data kosong atau gagal mengikuti FR-14.
- Kriteria penerimaan: Minimal tiga kartu dengan atribut yang ditentukan ditampilkan.
- Sumber: instruksi produk pengguna; use case: UC-04; issue: #17, #20, #21.

### FR-10 — Mencari proyek

- Modul: Proyek; prioritas: High (usulan); aktor: Pengunjung.
- Kebutuhan: Sistem harus menyaring daftar proyek berdasarkan teks pencarian yang dimasukkan pengunjung.
- Input: Teks pencarian.
- Aturan pemrosesan: Mencocokkan teks dengan data proyek; atribut pencarian menunggu kesepakatan.
- Output: Daftar hasil.
- Kondisi pengecualian: Tidak ada kecocokan: tampilkan empty state.
- Kriteria penerimaan: Hasil cocok dengan aturan pencarian yang disepakati; query tanpa hasil menampilkan empty state.
- Sumber: instruksi produk pengguna; use case: UC-04; issue: #18.

### FR-11 — Memfilter kategori

- Modul: Proyek; prioritas: High (usulan); aktor: Pengunjung.
- Kebutuhan: Sistem harus menyaring daftar proyek berdasarkan kategori yang dipilih pengunjung.
- Input: Kategori terpilih.
- Aturan pemrosesan: Menerapkan filter ke data proyek dan query aktif.
- Output: Daftar hasil kategori.
- Kondisi pengecualian: Tidak ada kecocokan: tampilkan empty state.
- Kriteria penerimaan: Hasil hanya mencakup kategori terpilih dan menghormati query aktif.
- Sumber: instruksi produk pengguna; use case: UC-04; issue: #18.

### FR-12 — Menampilkan detail proyek

- Modul: Proyek; prioritas: High (usulan); aktor: Pengunjung.
- Kebutuhan: Sistem harus menampilkan latar belakang, tujuan, fitur, teknologi, dokumentasi visual dan kontribusi pada detail proyek yang dipilih.
- Input: ID proyek.
- Aturan pemrosesan: Memilih data proyek yang sesuai.
- Output: Detail proyek.
- Kondisi pengecualian: ID tidak ditemukan: tampilkan pesan dan navigasi kembali.
- Kriteria penerimaan: Data detail sesuai proyek dan link ke profil kontributor tersedia.
- Sumber: instruksi produk pengguna; use case: UC-05; issue: #19, #20.

### FR-13 — Menampilkan direktori kontak

- Modul: Kontak; prioritas: High (usulan); aktor: Pengunjung.
- Kebutuhan: Sistem harus menampilkan foto, nama, role dan kontak profesional masing-masing anggota yang disetujui pada halaman Kontak.
- Input: Data kontak yang disetujui.
- Aturan pemrosesan: Menyajikan email, GitHub dan LinkedIn bila tersedia.
- Output: Direktori kontak.
- Kondisi pengecualian: Informasi tanpa izin atau tidak tersedia tidak ditampilkan.
- Kriteria penerimaan: Enam entri memuat informasi yang diizinkan; tidak ada email kolektif atau form tim.
- Sumber: instruksi produk pengguna; use case: UC-06; issue: #11, #16, #29.

### FR-14 — Menampilkan status pengambilan data

- Modul: Data; prioritas: High (usulan); aktor: Pengunjung.
- Kebutuhan: Sistem harus menampilkan loading, error atau empty state sesuai hasil pengambilan data proyek.
- Input: Status request dan respons.
- Aturan pemrosesan: Membedakan loading, hasil kosong dan kegagalan.
- Output: Pesan state yang sesuai.
- Kondisi pengecualian: Error: tawarkan retry sesuai FR-15.
- Kriteria penerimaan: Tiap kondisi memunculkan state yang berbeda dan dapat dipahami.
- Sumber: instruksi produk pengguna; use case: UC-04; issue: #21, #22.

### FR-15 — Mengulangi request gagal

- Modul: Data; prioritas: High (usulan); aktor: Pengunjung.
- Kebutuhan: Sistem harus menyediakan tindakan retry setelah pengambilan data proyek gagal.
- Input: Aktivasi retry.
- Aturan pemrosesan: Mengirim ulang request nyata.
- Output: Loading lalu data, empty atau error.
- Kondisi pengecualian: Gagal kembali: error dan retry tetap tersedia.
- Kriteria penerimaan: Retry memicu request baru dan hasilnya ditampilkan.
- Sumber: instruksi produk pengguna; use case: UC-04; issue: #21, #22.

### FR-16 — Mengembalikan pengunjung

- Modul: Navigasi; prioritas: High (usulan); aktor: Pengunjung.
- Kebutuhan: Sistem harus menyediakan navigasi kembali dari profil ke Tim dan dari detail proyek ke showcase.
- Input: Aktivasi tautan kembali.
- Aturan pemrosesan: Mengarahkan ke route induk.
- Output: Halaman induk.
- Kondisi pengecualian: Tujuan tidak tersedia: jangan klaim navigasi lulus.
- Kriteria penerimaan: Tautan profil menuju /team dan tautan detail menuju /projects.
- Sumber: instruksi produk pengguna; use case: UC-03 dan UC-05; issue: #10, #19.

## Non-functional requirements

| ID | Kategori | Pernyataan dan kondisi uji | Metode | Kriteria penerimaan | Status/sumber |
| --- | --- | --- | --- | --- | --- |
| NFR-01 | Usability | Label navigasi dan CTA konsisten dengan tujuan; Periksa seluruh label pada route yang tersedia | Review teks dan navigasi | Tidak ada label yang menyesatkan | Usulan / instruksi pengguna |
| NFR-02 | Performance | Target usulan LCP ≤2,5 detik, INP ≤200 ms, CLS ≤0,1 pada persentil ke-75; perlu kesepakatan dan data lapangan; Pengukuran lapangan pada deployment | Web Vitals | Seluruh target disepakati dan terukur | Usulan / instruksi pengguna |
| NFR-03 | Reliability | Kegagalan API menampilkan error dan retry tanpa menampilkan data sukses palsu; Simulasikan request gagal lalu retry | Uji integrasi | Error dan request ulang teramati | Usulan / instruksi pengguna |
| NFR-04 | Compatibility | Route dapat digunakan pada browser desktop dan mobile yang disepakati; Daftar browser dan versi menunggu kesepakatan | Uji lintas browser | Semua browser yang disepakati lulus skenario inti | Usulan / instruksi pengguna |
| NFR-05 | Responsiveness | Konten dan CTA dapat digunakan pada viewport 320, 375, 390, 768, 1024, 1440 dan 1920 CSS px serta zoom 200%; Uji setiap viewport | Uji browser | Tidak ada horizontal overflow halaman dan konten utama tersedia | Usulan / instruksi pengguna |
| NFR-06 | Accessibility | Target WCAG 2.2 AA; verifikasi keyboard, nama, fokus, heading, kontras dan reduced motion; Semua halaman tersedia | Uji manual dan otomatis | Temuan dicatat; kepatuhan penuh menunggu audit menyeluruh | Usulan / instruksi pengguna |
| NFR-07 | Privacy | Hanya data personal dan karya yang disetujui dipublikasikan; Audit konten terhadap daftar izin | Review konten | Tidak ada data tanpa izin pada build publik | Usulan / instruksi pengguna |
| NFR-08 | Security | Jangan memasukkan token atau rahasia ke kode dan respons publik; gunakan HTTPS pada deployment jika tersedia; Audit repository dan deployment | Secret scan dan pemeriksaan URL | Tidak ada rahasia terpapar dan deployment memakai HTTPS | Usulan / instruksi pengguna |
| NFR-09 | Maintainability | Komponen reusable menerima variasi melalui props dan composition; token desain memiliki satu sumber; Review arsitektur dan kode | Inspeksi PR | Komponen dan token memiliki dokumentasi dan tidak diduplikasi tanpa alasan | Usulan / instruksi pengguna |
| NFR-10 | Testability | Setiap kebutuhan memiliki kasus uji dan hasil aktual dapat ditautkan; Audit RTM dan hasil uji | Review dokumen | Semua FR dipetakan ke test case; hasil dinyatakan sesuai pelaksanaan | Usulan / instruksi pengguna |
