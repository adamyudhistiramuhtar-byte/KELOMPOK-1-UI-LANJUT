# K1-08 — kontrak beranda / persiapan, DRAFT

Status: implementasi terblokir oleh #3 (stack/router), #5 (fondasi dan token disetujui), #6 (komponen reusable), #7 (navbar). Tidak ada implementasi atau design system baru dibuat. Gate G5/G7 belum terpenuhi: design source dan approval belum tersedia. Kontrak ini tidak menetapkan stack atau token final dan harus direview Sindi/Alexius.

## Konten dan struktur
Navbar resmi → main berisi eyebrow `TEAM PORTFOLIO — 2026`, h1 `Kenali talenta di balik setiap karya.`, deskripsi `Satu ruang untuk mengenal individu, mengeksplorasi keahlian, dan melihat karya yang merepresentasikan perjalanan kami dalam desain dan pengembangan digital.`, ringkasan fokus, CTA dan maksimal satu tautan teks proyek unggulan yang valid → footer minimal. Tidak ada grid seluruh anggota atau proyek, statistik palsu, form atau gambar AI.

## Kontrak integrasi
- Komponen navbar #7 menyajikan Beranda, Tim, Proyek dan Kontak, termasuk keyboard dan mobile.
- Komponen tombol/tautan #6 harus menerima tujuan internal dan teks; `Jelajahi portofolio` → `/team`, `Lihat proyek` → `/projects`; signature props final mengikuti kontrak pemilik #6.
- Token, tipografi, spacing, fokus dan motion berasal dari #5; tidak ada nilai final yang ditetapkan di sini. Referensi putih/navy, EB Garamond dan Inter berasal dari instruksi pengguna; belum menjadi token resmi.
- Proyek unggulan: tampilkan maksimal satu link hanya bila ada data proyek dan tujuan valid yang disetujui. Data belum ada; jangan buat tautan rusak.

## Interaction, aksesibilitas dan responsif
Tautan: default, hover, focus-visible, active; disabled tidak berlaku untuk navigasi biasa, loading/error tidak berlaku untuk link statis. Fokus terlihat, nama link jelas, landmark nav/main/footer, urutan heading logis, keyboard dan reduced motion. Target WCAG 2.2 AA adalah target desain, bukan klaim kepatuhan. Reflow dan tidak ada overflow harus diuji pada 320, 375, 390, 768, 1024, 1440, 1920 px dan zoom 200%; ukuran touch target mengikuti token/spec disetujui.

## Acceptance tests — semua NOT RUN / terblokir
TC-HOME-01 route `/` terbuka; 02 nama tampil; 03 headline/deskripsi tepat; 04 CTA menuju `/team`; 05 CTA menuju `/projects`; 06 tautan unggulan valid bila tersedia; 07 tidak ada grid anggota/daftar proyek penuh; 08 tidak overflow pada seluruh viewport; 09 CTA dapat dipakai keyboard; 10 indikator fokus terlihat; 11 build berhasil; 12 lint dan test relevan berhasil. Rekam command, environment, expected, actual, status dan screenshot browser aktual setelah runtime tersedia. TC-HOME-06 conditional bila konten disetujui tersedia.
