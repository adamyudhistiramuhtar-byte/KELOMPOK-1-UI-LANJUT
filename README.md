# Kelompok 1 — Team Portfolio Website

> Draft perencanaan; belum membuktikan implementasi atau persetujuan tim.

## Project Overview dan Product Goal
Website portofolio responsif untuk mengenalkan enam anggota, kompetensi, karya, proyek, dan kontak profesional yang disetujui untuk publikasi. Mata kuliah Pengembangan UI Lanjut; Agile dengan Scrum yang diadaptasi.

## Team Members
Adam Yudhistira Muhtar (Project Manager dan System Analyst), Alexius Prasta Nugraha, Sindi Rahmawati, Marza, Panji Laryan, Muhammad Indra. Alokasi awal tersedia pada [team responsibilities](docs/team-responsibilities.md).

## Project Scope dan Functional Requirements
Beranda `/` berisi hero, nilai, CTA Tim dan Proyek serta tautan teks proyek unggulan. `/team` menampilkan enam kartu; `/team/:id` profil, kompetensi dan 3–5 screenshot karya; `/projects` menampilkan minimal tiga proyek dengan search dan filter; `/projects/:id` memuat detail dan kontribusi; `/contact` memuat direktori kontak profesional yang disetujui. Detail: [requirements](docs/requirements.md), [SRS draft](docs/SRS.md).

## Non-functional Requirements
Responsif desktop/tablet/mobile, aksesibilitas, komponen reusable, state loading/error/empty dan retry, serta pengujian relevan. Integrasi minimal satu API dengan request-response nyata; array statis tidak memenuhi ketentuan.

## Technology Stack
Belum disepakati. Vue diprioritaskan sebagai usulan sesuai materi; dependency dan API harus disetujui tim. [Arsitektur](docs/component-architecture.md) dan [kontrak API](docs/api-contract.md) masih draft.

## Project Roadmap dan Sprint Goals
| Sprint | Tanggal (Asia/Jakarta) | Goal | Increment |
| --- | --- | --- | --- |
| 1, Week 11–12 | 23 November–6 Desember 2026 | Pengunjung mengakses website, melihat anggota dan membuka profil melalui struktur dan sumber data dasar terintegrasi. | Core Member Flow Ready |
| 2, Week 13–14 | 7–20 Desember 2026 | Pengunjung mengeksplorasi portofolio, mencari dan membuka proyek serta kontak dengan API berfungsi. | Feature Complete & Integrated |
| 3, Week 15 | 21–27 Desember 2026 | Website stabil, responsif, teruji, terdokumentasi dan siap dipresentasikan. | Final Product Ready |

## Development Workflow
Issue → branch → development → commit → PR → peer review → merge → Done. Lihat [CONTRIBUTING](CONTRIBUTING.md). Tidak ada asumsi bahwa PR saja berarti Done.

## GitHub Projects
Project: https://github.com/users/adamyudhistiramuhtar-byte/projects/1. Repository: https://github.com/adamyudhistiramuhtar-byte/KELOMPOK-1-UI-LANJUT

## Documentation Links
[SRS](docs/SRS.md) · [Design](docs/DESIGN.md) · [User flow](docs/user-flow.md) · [Sprint plan](docs/sprint-plan.md) · [Risk register](docs/risk-register.md) · [Decision log](docs/decision-log.md) · [DoR/DoD](docs/definition-of-done.md)

## Testing Strategy
Unit atau functional, integration/API failure, responsif, usability, dan aksesibilitas. [Test plan](docs/testing/test-plan.md), [test cases](docs/testing/test-cases.md), [actual results](docs/testing/test-results.md) harus diisi berdasarkan pelaksanaan.

## Contribution Guidelines
Lihat [CONTRIBUTING](CONTRIBUTING.md); seluruh anggota berkontribusi pada produk dan memperbarui issue masing-masing.

## Sprint 1 coordination

Perencanaan dan batasan audit dependency: [sprint plan](docs/sprint-plan.md), [dependency map](docs/dependency-map.md), [Definition of Ready](docs/definition-of-ready.md). Template review dan retrospective akan dipersiapkan terpisah. Artefak masih memerlukan review tim.
