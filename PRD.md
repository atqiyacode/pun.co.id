# PRD — Company Profile PT. Prima Utama Nasional (PUN)

Versi: 1.0
Tanggal: 2026-08-14
Sumber konten: `PTPUN Company Profile - 2026_260814_235433.pdf`

## 1. Ringkasan

Website company profile satu halaman (single-page, scroll) untuk PT. Prima Utama Nasional (PUN), perusahaan kontraktor di bidang pertambangan mineral & batubara, eksplorasi hutan, dan konstruksi bangunan/fasilitas penunjang — sejak 2023.

Teknologi: **Nuxt 3** (Vue 3), build **static site generation (SSG)** → output `dist/` murni HTML statis, data konten dari **file JSON** (bukan database server). SEO penuh: meta tags, OpenGraph, JSON-LD structured data, sitemap, robots.txt.

## 2. Tujuan & Tolok Ukur

| Tujuan | Metrik |
|---|---|
| Profesionalitas & kredibilitas di mata calon klien (smelter, PLN/Indonesia Power, kontraktor) | Bounce rate < 50%, waktu kunjung > 60 dtk |
| Ditemukan di Google untuk nama perusahaan & layanan | Terindeks dalam 2 minggu, peringkat halaman 1 untuk "PT Prima Utama Nasional" |
| Media presentasi digital menggantikan PDF | Link website dibagikan di proposal/email |

## 3. Target Audiens

- Calon klien korporat: perusahaan energi, smelter, pemegang kontrak tambang
- Mitra/subkontraktor potensial
- Calon investor & vendor
- Pencari kerja (via halaman kontak)

## 4. Struktur Halaman (Satu Halaman Scroll)

Navbar sticky: Home · About Us · Services · Contact (anchor scroll). Satu URL `/` + hash section.

### 4.1 Hero
- Nama: **PT. Prima Utama Nasional**
- Singkatan: **PUN**
- Tagline: *"Kepuasan pelanggan, kebanggaan kami"*
- CTA: "Lihat Layanan" → `#services`, "Hubungi Kami" → `#contact`
- Background: visual tambang/hutan (dari aset perusahaan; placeholder dulu)

### 4.2 About Us (Who We Are)
- "PT. Prima Utama Nasional sejak 2023, perusahaan swasta bergerak di bidang **kontraktor bangunan, fasilitas penunjang, eksplorasi hutan dan kandungan di dalamnya, serta pertambangan mineral dan batubara**."
- Motto: "Memberikan layanan prima merupakan dedikasi dan kepuasan pelanggan merupakan kebanggaan bagi kami."
- Tampilan: 3–4 kartu bidang usaha (Bangunan & Fasilitas · Eksplorasi Hutan · Pertambangan Mineral · Batubara) + foto/ilustrasi.

### 4.3 Visi & Misi
- **Visi:** "Berkembang dan menjadi pemain utama di sektor kontraktor pertambangan dan hutan." / "Menjadi pemimpin industri dalam solusi yang berkelanjutan dan inovatif, serta mengembangkan perusahaan agar semakin besar dan memberikan dampak bagi dunia."
- **Misi:** "Hadirnya kami di berbagai project dan lokasi di Indonesia dapat memberikan manfaat nyata bagi masyarakat setempat."

### 4.4 Our Journey (Timeline)
- Tahun: **2023, 2024, 2025, 2026**
- ⚠️ **ASUMSI:** detail peristiwa per tahun tidak ada di PDF → placeholder di JSON, isi menunggu data dari pihak PUN.

### 4.5 Quote Band
- *"Dream big, work hard, and create magic."* — @pt.pun

### 4.6 Our Service (3 Kartu)
| Layanan | Deskripsi (dari PDF) |
|---|---|
| Penambangan Batubara | Teknik menambang yang benar akan menghasilkan hasil yang baik dan efisiensi biaya. |
| Penambangan Nikel | Proses penambangan nikel kadar tinggi memerlukan ketelitian tinggi agar material yang bersifat merusak kadar dapat dihindari. |
| Trading | Kepercayaan yang klien berikan kepada kami guna memenuhi kebutuhan kontrak mereka. |

### 4.7 Our Project (Portfolio)
| Project | Deskripsi |
|---|---|
| Batubara | Penambangan batubara di Kalimantan Timur, memenuhi kontrak kebutuhan Indonesia Power. |
| Nikel | Penambangan nikel kadar tinggi guna memenuhi kebutuhan Smelter. |

### 4.8 Contact
- Telepon/WA: **+62 811 35 666 36**
- Web: **www.pun.co.id**
- Alamat: Kartika Chandra Office Tower I, Suite 008-009, Jl. Jendral Gatot Subroto Kaveling 18-20, Karet Semanggi, Kec. Setiabudi, Jakarta Selatan, DKI Jakarta 12930
- CTA: tombol `tel:` + link WhatsApp (wa.me/628113566636)

### 4.9 Footer
- Copyright: © 2026 PT. Prima Utama Nasional
- Nav ulang + kontak ringkas.

## 5. Arsitektur Teknis

```
Nuxt 3 (Vue 3, Vite)
├── content/ atau data/
│   └── company.json      ← "database" statis, satu-satunya sumber konten
├── pages/
│   └── index.vue         ← satu halaman, semua section sebagai komponen
├── components/
│   ├── Navbar.vue, Hero.vue, About.vue, VisionMission.vue,
│   ├── Journey.vue, Services.vue, Projects.vue, Contact.vue, Footer.vue
├── composables/
│   └── useCompanyData.js ← baca JSON via import (build-time)
├── public/
│   ├── favicon.ico, robots.txt
│   └── images/ (logo, hero, project)
└── nuxt.config.ts        ← ssr: false? TIDAK. gunakan SSG (target static)
```

Build: `npx nuxi generate` → folder `dist/` statis → deploy ke hosting statis mana pun (Netlify/Vercel/GitHub Pages/Nginx).

**Kenapa SSG + JSON:**
- Tanpa server/database → murah, cepat, aman, deploy di mana saja
- SEO terbaik: HTML lengkap dirender saat build, crawler langsung baca konten
- Konten diedit cukup dengan edit `company.json` lalu rebuild — tidak perlu CMS

## 6. Struktur Data JSON (Schema)

File: `data/company.json` (atau `content/company.json`)

```json
{
  "company": {
    "name": "PT. Prima Utama Nasional",
    "shortName": "PUN",
    "tagline": "Kepuasan pelanggan, kebanggaan kami",
    "foundedYear": 2023,
    "logo": "/images/logo.png",
    "contact": {
      "phone": "+62 811 35 666 36",
      "whatsapp": "628113566636",
      "email": "",
      "website": "https://www.pun.co.id",
      "address": "Kartika Chandra Office Tower I, Suite 008-009, Jl. Jendral Gatot Subroto Kaveling 18-20, Karet Semanggi, Kec. Setiabudi, Jakarta Selatan, DKI Jakarta 12930",
      "mapUrl": "https://maps.google.com/?q=..."
    }
  },
  "hero": { "title": "...", "subtitle": "...", "cta": [...] },
  "about": { "description": "...", "fields": ["Kontraktor Bangunan", "Fasilitas Penunjang", "Eksplorasi Hutan", "Pertambangan Mineral & Batubara"] },
  "vision": { "title": "...", "description": "..." },
  "mission": { "title": "...", "description": "..." },
  "journey": [
    { "year": 2023, "title": "", "description": "" },
    { "year": 2024, "title": "", "description": "" },
    { "year": 2025, "title": "", "description": "" },
    { "year": 2026, "title": "", "description": "" }
  ],
  "quote": { "text": "Dream big, work hard, and create magic.", "author": "@pt.pun" },
  "services": [
    { "title": "Penambangan Batubara", "description": "...", "icon": "..." },
    { "title": "Penambangan Nikel", "description": "...", "icon": "..." },
    { "title": "Trading", "description": "...", "icon": "..." }
  ],
  "projects": [
    { "title": "Batubara", "description": "Penambangan batubara di Kalimantan Timur, memenuhi kontrak kebutuhan Indonesia Power.", "image": "" },
    { "title": "Nikel", "description": "Penambangan nikel kadar tinggi guna memenuhi kebutuhan Smelter.", "image": "" }
  ]
}
```

Semua section dirender dari JSON ini — edit konten tanpa sentuh komponen Vue.

## 7. Spesifikasi SEO

1. **Meta tags** per halaman via `useHead()`: `title`, `description`, `keywords`, canonical URL.
2. **OpenGraph + Twitter Card**: `og:title`, `og:description`, `og:image` (1200×630), `og:url`, `og:type=website`.
3. **JSON-LD structured data** (`application/ld+json`):
   - `Organization` (nama, logo, alamat, telepon, sameAs, URL)
   - `LocalBusiness`/`ProfessionalService` untuk lokasi
   - `Service` untuk tiap layanan (batubara, nikel, trading)
   - `WebSite` + `SearchAction` (jika ada pencarian — skip dulu)
4. **sitemap.xml** otomatis (modul `@nuxtjs/sitemap` atau generate manual) → submit ke Google Search Console.
5. **robots.txt**: izinkan semua, tunjuk sitemap.
6. **Semantik HTML**: satu `h1` (nama perusahaan), `h2` per section, `alt` di semua gambar, `aria-label` di ikon/nav.
7. **Mobile-friendly & Core Web Vitals**: SSG = LCP cepat (statis), gambar `loading="lazy"`, preload font lokal (hindari Google Fonts remote demi performa).
8. `lang="id"` di `<html>`.

## 8. Desain & UX

- Tema: gelap/teal + aksen emas/amber (kesan tambang & energi) — finalisasi dengan aset brand PUN.
- Tipografi: font sans modern (lokal, self-hosted).
- Animasi: scroll reveal halus (IntersectionObserver, tanpa library berat).
- Responsif penuh: mobile-first, hamburger menu di bawah 768px.
- Kontras & ukuran font sesuai WCAG AA.

## 9. Kebutuhan Non-Fungsional

| Aspek | Target |
|---|---|
| Performa | Lighthouse Performance ≥ 90, LCP < 2.5s |
| Ukuran bundle | JS < 100KB gzipped (karena statis, sebagian besar konten = HTML) |
| Aksesibilitas | WCAG 2.1 AA, keyboard navigable |
| SEO | Lighthouse SEO ≥ 95 |
| Kompatibilitas | Chrome/Firefox/Safari/Edge 2 versi terakhir, iOS/Android |
| Keamanan | Tanpa form backend = permukaan serangan minim; form (jika ada) pakai layanan pihak ketiga |

## 10. Acceptance Criteria

- [ ] Satu halaman `/` dengan 8 section, semua konten sesuai PDF, navigasi anchor berfungsi
- [ ] Semua konten dapat diubah hanya dengan edit `company.json` + rebuild
- [ ] `nuxi generate` menghasilkan `dist/` statis tanpa error
- [ ] Deploy ke hosting statis → site live, semua gambar & link jalan
- [ ] Meta tags, OG image, JSON-LD, sitemap.xml, robots.txt terpasang & valid (test via validator)
- [ ] Lighthouse: Performance ≥ 90, SEO ≥ 95, Accessibility ≥ 90
- [ ] Responsif di mobile & desktop
- [ ] Kontak: klik tel: & WhatsApp membuka aplikasi dengan nomor benar

## 11. Di Luar Cakupan (Future)

- Halaman multi-page (Layanan detail, Galeri, Karir)
- i18n EN/ID
- Blog/berita
- Form kontak dengan backend/CMS (Sanity/Strapi)
- Panel admin untuk edit konten

## 12. Estimasi & Deliverables

| Tahap | Output | Estimasi |
|---|---|---|
| Setup project Nuxt 3 + struktur | Repo siap build | 0.5 hari |
| JSON data + komponen section | Semua section render dari data | 1–1.5 hari |
| Styling responsif + animasi | UI final sesuai brand | 1–1.5 hari |
| SEO (meta, JSON-LD, sitemap, robots) | Validated | 0.5 hari |
| Build, test Lighthouse, deploy | Site live | 0.5 hari |
| **Total** | | **± 4 hari** |

## 13. Pertanyaan Terbuka (butuh jawaban PUN)

1. Detail per tahun di section Journey (2023–2026) — PDF kosong, isi apa?
2. Logo & foto (hero, project, kantor) — tersedia? Format PNG/SVG?
3. Email resmi untuk ditampilkan?
4. Warna brand / panduan identitas visual?
5. Bahasa: Indonesia saja atau perlu versi English?
6. Domain: www.pun.co.id sudah dipakai? Deploy di mana (Netlify/Vercel/domain sendiri)?
7. Link Google Maps kantor — koordinat/URL?
