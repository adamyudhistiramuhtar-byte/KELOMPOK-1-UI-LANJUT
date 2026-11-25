# Sprint plan — baseline usulan

| Sprint | Tanggal (Asia/Jakarta) | Goal | Increment |
| --- | --- | --- | --- |
| 1, Week 11–12 | 23 November–6 Desember 2026 | Pengunjung mengakses website, melihat anggota dan membuka profil melalui struktur dan sumber data dasar terintegrasi. | Core Member Flow Ready |
| 2, Week 13–14 | 7–20 Desember 2026 | Pengunjung mengeksplorasi portofolio, mencari dan membuka proyek serta kontak dengan API berfungsi. | Feature Complete & Integrated |
| 3, Week 15 | 21–27 Desember 2026 | Website stabil, responsif, teruji, terdokumentasi dan siap dipresentasikan. | Final Product Ready |

Sprint 1 planning 23 November 2026 adalah baseline yang sudah lewat, bukan bukti pelaksanaan. Review dan retrospective 6 Desember; Sprint 2 planning 7 Desember, review dan retrospective 20 Desember; Sprint 3 planning 21 Desember, final review paling lambat 27 Desember atau sebelum jadwal presentasi aktual, retrospective akhir proyek. Jadwal presentasi aktual mengikuti dosen.

Check-in diusulkan Senin, Rabu, Jumat: progress, planning, problem, decision; jam dan peserta perlu dikonfirmasi. Lakukan refinement backlog secara berkala, perbarui dependency dan kapasitas.

## Planning Sprint 1 dan ceremony — usulan

Audit 13 issue dan urutan dependency: [dependency map](dependency-map.md). Sprint backlog aktual dan komitmen belum dikonfirmasi. Planning baseline 23 November sudah lewat dan tidak membuktikan pelaksanaan. Usulan koordinasi dimulai Rabu 25 November 2026, kemudian setiap Senin/Rabu/Jumat selama sprint; jam, peserta dan pelaksanaan harus dikonfirmasi.

- Planning: tinjau goal, kapasitas, dependency, DoR, issue dan commitment yang disepakati.
- Check-in: progress berbukti, planning, problems, keputusan dan tindak lanjut.
- Refinement: cek requirement, acceptance criteria, size, risiko dan dependency bersama PIC.
- Review 6 Desember: demonstrasi increment, acceptance dan feedback aktual.
- Retrospective 6 Desember: apa yang baik, yang sulit, perbaikan dan action ber-PIC.

Tidak ada kehadiran, diskusi atau persetujuan yang diasumsikan.

## Verifikasi view Project

Pada audit API 25 November 2026, Current Sprint berlayout board, filter `iteration:@current`, dan `verticalGroupByFields = Status`. Product Backlog adalah table; Roadmap adalah roadmap; Blocked Items dan Testing & Quality mempunyai filter. Team Workload masih tanpa pengelompokan. API yang tersedia membaca grouping tetapi input update view hanya menyediakan visible fields, bukan grouping; atur grouping lewat UI, misalnya berdasarkan Assignees. Enam akun telah diverifikasi sebagai collaborator repository; akses Project privat harus diverifikasi terpisah. Kesesuaian rentang item pada tampilan roadmap perlu diperiksa melalui UI; tanggal iteration telah tersedia pada Project.

## Scrum working agreement — usulan, belum disetujui

Product Goal: website portofolio responsif untuk mengenal enam anggota, kompetensi, karya, proyek dan kontak profesional yang disetujui. Product Owner memaksimalkan nilai dan mengurutkan Product Backlog; Scrum Master bertanggung jawab atas efektivitas Scrum; Developers bersama-sama membangun increment. Adam adalah PM dan Developer; identitas PO dan SM belum diputuskan. Sumber: [Scrum Guide 2020](https://scrumguides.org/scrum-guide).

Sprint Planning membahas mengapa sprint bernilai, apa yang dapat dilakukan, bagaimana mengerjakannya, kapasitas dan risiko. Daily Scrum diusulkan 15 menit setiap hari kerja untuk Developers memeriksa kemajuan menuju Sprint Goal dan menyesuaikan rencana; tambahan asynchronous adalah adaptasi kelompok mahasiswa, bukan pengganti yang diklaim sebagai ketentuan Scrum. Jam dan kehadiran belum disepakati. Refinement berlangsung sesuai kebutuhan; Sprint Review memeriksa increment aktual dan mengadaptasi backlog; Retrospective meninjau kerja sama, kualitas dan perbaikan. Sprint 3 tujuh hari adalah penyesuaian akademik, bukan cadence default.

Usulan WIP: maksimal satu issue aktif per developer, di luar review ringan dan koordinasi PM. Monitoring manual, tanpa memindahkan issue otomatis. Size S/M/L adalah kompleksitas dan effort relatif, bukan jam, story points, kontribusi, atau velocity numerik. High = wajib/dependency kritis/Sprint Goal; Medium = penting namun dapat ditunda tanpa segera menggagalkan goal; Low = tambahan. Urutan backlog mempertimbangkan nilai, dependency dan risiko, bukan hanya priority. Prioritas #2, #13, #23 dan #25 diusulkan Medium karena dokumentasi proses, ceremony atau refinement dapat diselesaikan setelah increment inti disiapkan; tetap wajib dalam cakupannya. #34 tetap Medium sebagai konsolidasi akhir.

### Checkpoint usulan
- 25–26 November: review SRS/workflow, akses, stack, kontrak API dan arah desain.
- 27–29 November: fondasi aplikasi/desain, komponen, navbar, konten.
- 30 November–2 Desember: beranda, direktori, profil dan konten yang disetujui.
- 3–5 Desember: integrasi, uji fungsional/responsif, perbaikan dan persiapan demo.
- 6 Desember: review, retrospective dan follow-up.

Ini target koordinasi, bukan bukti pekerjaan. #34 adalah konsolidasi Sprint 3; update Week 11–14 tetap dicatat setiap minggu tanpa mengubah owner/milestone. Sprint Goal progress dinilai dari bukti increment, bukan jumlah issue/commit; throughput dan cycle time hanya digunakan bila histori cukup. Jangan membuat burndown atau velocity dari ukuran S/M/L.

### Quality gates dan automation
main belum memiliki branch protection/ruleset dan belum ada CI workflow. Usulan untuk disetujui: PR dengan satu peer approval selain author, selesaikan percakapan review, larang force push/penghapusan main, dan required checks hanya bila CI nyata tersedia. Squash merge adalah usulan, bukan keputusan. Jangan mengaktifkan aturan yang mengunci tim.

Audit API menunjukkan workflow Project aktif: Auto-add sub-issues, Auto-close issue, Item added, Item closed, Pull request linked to issue, Pull request merged. API tidak mengungkap aturan pemicu/target secara lengkap. Periksa melalui Project → Workflows bahwa merge PR tidak otomatis menandai Done atau menutup issue sebelum DoD; jangan mengubah automation tanpa memeriksa efeknya. Arsip hanya setelah retensi disepakati.
