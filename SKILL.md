---
name: web-unslop
description: Bikin atau review tampilan web (landing page, dashboard, komponen, copy halaman) supaya tidak terbaca sebagai buatan AI. Pakai setiap kali menulis HTML, CSS, JSX, Tailwind, atau teks yang tampil di halaman. Isinya alur dari brief sampai verifikasi, katalog tell visual dan copy, dan linter yang bisa dijalankan.
---

# web-unslop

Hasil AI terbaca dari pilihan default yang sama di setiap proyek: font yang sama, gradien yang sama, kartu tiga kolom yang sama, kalimat pembuka yang sama. Skill ini memaksa satu hal: tiap keputusan visual dan tiap kalimat harus punya alasan yang berasal dari subjek halamannya, bukan dari kebiasaan.

Dua aturan di bawah ini berlaku di setiap langkah.

1. **Jangan tukar satu refleks dengan refleks lain.** Dilarang memakai Inter lalu pindah ke Space Grotesk, atau lepas dari ungu lalu jatuh ke teal di latar gelap. Kalau pilihan akhirmu sama dengan tebakan pertamamu, ulang.
2. **Alasan harus bisa ditunjuk ke subjek.** "Karena terlihat modern" bukan alasan. "Karena nota bengkel ini dicetak dengan mesin ketik slab" adalah alasan.

## Alur kerja

Kerjakan berurutan. Halaman satu komponen boleh melompati langkah 2 dan 5. Halaman multi-section tidak boleh melompati apa pun.

### 0. Brief (5 menit, tertulis)

Tulis jawaban singkat untuk enam hal sebelum menyentuh kode. Kalau jawabannya tidak diketahui, tanyakan ke pemilik, jangan dikarang.

- Siapa yang membuka halaman ini, dari perangkat apa, dalam keadaan apa (terburu-buru, santai, curiga)?
- Satu tindakan yang harus terjadi setelah halaman dibaca.
- Tiga kata sifat untuk merek, lalu satu benda fisik yang mewakilinya (papan toko, kemasan, buku tabel, nota).
- Bukti nyata yang tersedia: angka, foto, nama, tarif, alamat, kutipan asli.
- Tiga halaman atau situs yang disukai pemilik dan alasan spesifiknya.
- Batasan: bahasa, merek yang sudah ada, tema gelap atau terang, anggaran performa.

**Fakta nyata atau placeholder.** Harga, durasi, nama, alamat, angka, kutipan, dan syarat harus datang dari pemilik. Kalau belum ada, tulis `[ISI: harga stempel flash]` di tempatnya. Jangan mengarang angka yang terdengar spesifik, itu spesifik palsu dan justru tell terkuat. Linter menandai `[ISI:` yang tersisa sebagai WARN supaya halaman draf tidak lolos rilis diam-diam.

Template lengkap ada di `references/process.md`. Kalau proyek sudah punya `.impeccable.md`, pakai itu sebagai isi brief dan jangan mewawancarai ulang. Untuk wawancara penemuan yang lebih panjang, buka `vendor/impeccable/commands/shape.md`.

### 1. Arah dan tiga dial

Set tiga angka 1 sampai 10 dan catat alasannya.

| Dial | 1 | 10 | Default jika tidak ada petunjuk |
|---|---|---|---|
| VARIANCE | simetris, grid kaku | asimetris, memecah grid | 7 |
| MOTION | statis | sinematik | 4 |
| DENSITY | galeri, lega | kokpit, padat | 4 |

Dashboard dan alat kerja condong ke DENSITY tinggi dan MOTION rendah. Halaman undangan atau portofolio condong ke VARIANCE tinggi. Angka ini menentukan keputusan di langkah berikutnya, jadi jangan diisi asal.

### 1b. Riset referensi

Sebelum merancang, lihat dulu bentuk yang pernah berhasil: komponen sejenis (21st.dev, shadcn/ui, magicui), pola gerak (motion.dev, animate-ui, react-bits), dan komposisi (Dribbble, Awwwards, Behance). Ambil struktur dan interaksinya, tulis ulang untuk proyek ini. Catat di komentar bukti hanya yang benar-benar dilihat. Cara kerja, kuota 21st.dev, dan sembilan lensa komposisi ada di `references/research.md`.

### 2. Wireframe kasar

Gambar struktur dengan kotak ASCII dulu. Tidak ada warna, font, atau ikon. Tujuannya hierarki dan alur baca.

```
[hero: headline besar kiri, ornamen kanan, satu CTA]
[tabel tarif: garis tipis, tanpa kartu]
[3 langkah bernomor, digeser berselang-seling]
[FAQ: details]
[penutup: alamat + kontak]
```

Buat dua atau tiga variasi struktur sebelum memilih. Struktur pertama yang terlintas biasanya struktur default.

**Tes kerangka.** Sebelum lanjut, tulis urutan section halaman ini dalam satu baris. Bandingkan dengan kerangka bawaan: hero + CTA, lalu tabel atau tiga langkah atau tiga fitur, lalu FAQ, lalu penutup. Kalau urutannya sama, tanyakan untuk tiap section apa yang membuatnya ada di halaman ini, bukan di halaman subjek lain. Hapus yang tidak punya jawaban. Susun ulang urutan dari apa yang ditanyakan pembaca. Detail dan daftar kerangka bawaan di `references/layout.md`.

### 3. Tipografi

Aturan inti, detail di `references/typography.md`.

- Pilih font dengan menanyakan: benda fisik apa yang dicetak dengan huruf ini? Cari di katalog (Google Fonts, Fontshare, Velvetyne, Future Fonts) dengan benda itu di kepala.
- Tolak font di daftar refleks (Inter, Roboto, Open Sans, Arial, Space Grotesk, Poppins, Montserrat, Playfair Display, DM Sans, dan gelombang keduanya). Linter menandai semuanya.
- Pasangkan satu display dengan satu body. Maksimal tiga keluarga.
- Skala ukuran punya rasio minimal 1.25 antar tingkat. Judul pakai `clamp()`.
- Panjang baris 60 sampai 72 karakter (`max-width: 62ch`).
- Monospace bukan jalan pintas untuk kesan teknis.
- Selalu self-host atau embed font. Jangan bergantung CDN yang bisa diblok.

### 4. Warna

Detail di `references/color.md`.

- Satu warna dominan yang berani, satu aksen, sisanya netral yang diberi tint ke hue dominan. Tidak ada `#000` dan `#fff` murni.
- Turunkan palet dari detail fisik subjek (alas meja kerja, kemasan, kertas, logam), bukan dari mood board generik. Kalau subjek tidak punya detail fisik, atau pemilik meminta nuansa pastel, ambil empat sampai enam swatch dari `references/palette-library.md`.
- Pilih tema gelap atau terang dari konteks pembaca. Keduanya bukan default aman.
- Hindari kombinasi yang paling sering dimuntahkan model: gradien ungu ke biru, latar gelap dengan aksen teal atau emerald, glow neon, krem hangat dengan terakota yang dipaksakan ke subjek yang tidak berhubungan.
- Teks isi minimal kontras 4.5:1, teks besar 3:1. Hitung, jangan menebak.

### 5. Layout dan komposisi

Detail di `references/layout.md`.

- Tentukan satu elemen yang diperbesar jadi pusat perhatian (tipografi raksasa, satu warna pekat, satu foto penuh). Kalau semua elemen berukuran sedang, halamannya terbaca rata.
- Rata kiri dengan komposisi asimetris. Rata tengah hanya untuk judul pendek yang memang berdiri sendiri.
- Kartu bukan wadah default. Tabel, daftar bernomor, daftar definisi, dan kolom editorial sering lebih jelas. Kalau tiga blok isinya setara, jangan buat ketiganya identik.
- Ritme spasi berubah antar section. Padding yang sama di semua section terbaca otomatis.
- Dilarang: garis aksen tebal di sisi kartu, kartu di dalam kartu, teks bergradien, ikon besar berpojok bulat di atas tiap judul, pola "angka besar + label kecil + gradien" untuk metrik.

### 6. Gerak

Detail di `references/motion.md`.

- Satu momen gerak yang berarti lebih baik daripada sepuluh kecil yang dekoratif.
- Easing punya karakter: `cubic-bezier(0.34, 1.4, 0.64, 1)` untuk pegas ringan, `cubic-bezier(0.22, 1, 0.36, 1)` untuk keluar halus. Hindari `ease` bawaan dan `transition: all`.
- Hanya animasikan `transform` dan `opacity`.
- Wajib `@media (prefers-reduced-motion: reduce)` yang mematikan atau menyederhanakan semua gerak.

### 7. Copy

Detail dan contoh sebelum-sesudah di `references/copy.md`.

- Dilarang total memakai tanda pisah em dash (U+2014). Pakai koma, titik, atau kata sambung.
- Hapus kata pengisi dan kalimat pembuka kosong. Daftar lengkap ada di `references/tells.md`.
- Setiap klaim membawa angka, mekanisme, syarat, atau nama. Klaim tanpa bukti dihapus.
- Panjang kalimat tidak seragam. Hindari ritme tiga item dan struktur "bukan X tapi Y".
- Judul section jangan seragam. Kalau semua h2 berbentuk "X, lalu Y" atau semuanya sepanjang dua baris, halaman terbaca disusun mesin. Campur: judul satu kata, judul pertanyaan pembaca, judul tanpa judul sama sekali (langsung isi).
- Jangan mewarnai kata terakhir judul.
- CTA menyebut aksi persis yang terjadi: "Kirim foto jam ke WhatsApp", bukan "Mulai sekarang".
- Jalankan tujuh sapuan satu per satu: Clarity, Voice, So What, Prove It, Specificity, Emotion, Zero Risk.

### 8. Bangun

- HTML semantik: satu `<h1>`, `<main>`, `<nav>`, `<button>` untuk aksi dan `<a>` untuk navigasi.
- Token warna dan ukuran sebagai custom property di `:root`. Dukung `prefers-color-scheme`.
- Gaya `:focus-visible` yang terlihat di semua elemen interaktif.
- `<img>` selalu beralt. Dekoratif memakai `alt=""`. SVG dekoratif memakai `aria-hidden="true"`.
- `<meta name="viewport">`, `<meta charset>`, `lang`, `<title>`, meta description.
- Tulis ringkasan keputusan sebagai komentar HTML di dekat atas (template di `references/process.md`) dan sebutkan hal yang sama kepada pemilik di chat. Isinya harus jujur tentang apa yang benar-benar dilakukan.

### 9. Verifikasi

Jalankan berurutan. Jangan menyatakan selesai sebelum ketiganya bersih.

1. **Linter:** `python3 scripts/unslop_lint.py path/ke/halaman.html`. Perbaiki semua FAIL. Baca tiap WARN dan putuskan sadar, bukan reflek menekan. Untuk menegakkannya otomatis, pasang `hooks/web-unslop-gate.py` sebagai hook PreToolUse (lihat README).
2. **Screenshot nyata**, desktop dan lebar sempit. Perintahnya ada di `references/process.md`. Cari teks terpotong, elemen menumpuk, spasi kata yang hilang, dan karakter non-ASCII yang rusak.
3. **Uji slop, tertulis.** Jawab enam pertanyaan di `references/process.md` satu per satu di laporan, lengkap dengan bukti dari halaman. Yang paling sering gagal: (a) apakah halaman ini bisa tertukar dengan halaman subjek lain hanya dengan mengganti teks, (b) apakah ada angka atau klaim yang saya karang, (c) apakah semua judul dan semua jarak antar section berirama sama. Jawaban "sudah" tanpa bukti dianggap gagal.

Linter hanya menangkap pola mekanis. Lolos linter adalah syarat minimal, bukan bukti bahwa halamannya bagus. Dua halaman di `examples/lolos-linter/` lolos tanpa FAIL tapi tetap terbaca AI, dan itu disimpan sebagai peringatan. Untuk penilaian yang lebih dalam dan bersekor, buka `vendor/impeccable/commands/critique.md` dan `audit.md`.

## Perintah perbaikan (dari Impeccable)

Setelah halaman jadi, gejala tertentu punya perintah khusus. Salinan Impeccable v2.1.1 ada di `vendor/impeccable/`.

| Gejala | Buka |
|---|---|
| Bland, terlalu aman | `commands/bolder.md` |
| Terlalu ramai atau keras | `commands/quieter.md`, `commands/distill.md` |
| Hambar, tanpa kepribadian | `commands/delight.md` |
| Abu-abu, tanpa warna | `commands/colorize.md` |
| Spasi dan hierarki lemah | `commands/layout.md` |
| Font bermasalah | `commands/typeset.md` |
| Teks UI membingungkan | `commands/clarify.md` |
| Rusak di layar tertentu | `commands/adapt.md` |
| Lambat atau patah | `commands/optimize.md` |
| Pemeriksaan sebelum rilis | `commands/polish.md` |
| Ingin efek ambisius | `commands/overdrive.md` |

Peta lengkap, cara membaca teks Inggrisnya, dan aturan siapa yang menang saat bertabrakan: `references/impeccable-map.md`.

## Peta referensi

| File | Dibuka saat |
|---|---|
| `references/tells.md` | Review, atau sebelum menyatakan selesai. Katalog lengkap tell beserta pengganti. |
| `references/typography.md` | Memilih font, skala, pasangan. |
| `references/color.md` | Menurunkan palet, tema gelap atau terang, kontras. |
| `references/layout.md` | Komposisi, ritme, pengganti kartu. |
| `references/motion.md` | Menambah gerak apa pun. |
| `references/copy.md` | Menulis atau mengedit teks halaman. |
| `references/process.md` | Template brief, wireframe, screenshot, komentar bukti. |
| `references/research.md` | Riset komponen, gerak, dan komposisi sebelum merancang. |
| `references/palette-library.md` | Swatch siap pakai per keluarga hue, opsi kedua untuk warna. |
| `references/impeccable-map.md` | Cara Impeccable dan web-unslop saling melengkapi. |
| `vendor/impeccable/` | Salinan utuh Impeccable v2.1.1: SKILL.md, 9 referensi, 16 perintah. Apache-2.0. |
| `hooks/web-unslop-gate.py` | Hook yang menolak penulisan halaman yang gagal linter. |
| `references/lint-rules.md` | Arti tiap rule linter dan cara menekannya. |
| `examples/lolos-linter/` | Dua halaman yang lolos linter tapi tetap terbaca AI, lengkap dengan daftar alasannya. Contoh buruk, bukan teladan. |

## Yang sengaja tidak dilakukan skill ini

- Tidak menyuruh membuat desain "minimalis" sebagai pelarian. Halaman sepi tanpa keputusan juga terbaca otomatis.
- Tidak memberi daftar font pilihan. Daftar pilihan hanya melahirkan refleks baru. Library swatch ada sebagai opsi kedua dengan batasan yang dijelaskan, bukan sebagai jalan pintas.
- Tidak mengisi fakta yang tidak diketahui. Placeholder lebih baik daripada angka karangan.
- Tidak menilai selera. Linter mendeteksi pola, penilaian akhir tetap manusia.
