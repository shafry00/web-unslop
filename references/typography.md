# Tipografi

## Prosedur memilih font

Model punya refleks: begitu diminta "elegan" ia mengambil serif, begitu diminta "teknis" ia mengambil sans geometris atau monospace, begitu diminta "hangat" ia mengambil serif lembut yang sedang tren. Prosedur ini memotong refleks itu.

1. **Tulis tiga kata sifat merek** dari brief. Contoh: teliti, tua, tenang.
2. **Tentukan benda fisik** yang mewakili ketiganya dan dicetak dengan huruf. Contoh: nota servis bengkel, label kain di dalam jaket, papan harga pasar, buku tabel logaritma, kemasan obat tahun 1980-an, struk mesin kasir.
3. **Telusuri katalog** dengan benda itu di kepala. Sumber: Google Fonts, Fontshare, Velvetyne, Future Fonts, Pangram Pangram, Klim, ABC Dinamo. Buka sepuluh kandidat, bukan tiga. Tolak yang pertama kali terlihat "bagus", itu juga refleks terlatih.
4. **Uji silang.** Font yang tepat untuk "elegan" belum tentu serif. Font yang tepat untuk "teknis" belum tentu sans. Kalau pilihan akhir sama dengan tebakan refleksmu sebelum mencari, kembali ke langkah 3.
5. **Uji di konten asli.** Tempel judul, angka Rupiah, nama dengan diakritik, dan satu paragraf. Cek angka tabular, karakter `0` dan `O`, `1` dan `l`, dan tanda baca bahasa Indonesia.
6. **Tulis alasannya** dalam satu kalimat di komentar bukti. Kalimat itu harus menyebut subjek.

Contoh penalaran (bukan daftar pilihan): bengkel jam dengan nota cetak lama menuntut serif ber-sentuhan tinta cetak untuk judul dan sans netral dengan angka tabular untuk tarif. Contoh di `examples/bengkel-jam` memakai Petrona dan Karla untuk alasan itu. Jangan menyalinnya untuk subjek lain.

## Daftar tolak

Linter menandai font di bawah ini jika menjadi pilihan pertama di `font-family`.

- **FAIL:** Inter, Roboto, Open Sans, Arial, Helvetica, Space Grotesk, Poppins, Montserrat, Playfair Display, DM Sans, Lato, Segoe UI.
- **WARN:** Fraunces, Outfit, Plus Jakarta Sans, Manrope, Sora, Lexend, Syne, Bricolage Grotesque, Instrument Serif, Cormorant Garamond, Lora, Raleway, Nunito, Work Sans, Geist, JetBrains Mono, IBM Plex Sans, Source Sans, Urbanist, Figtree, Onest, Schibsted Grotesk.

Font di daftar WARN boleh dipakai kalau uji benda fisik memang mengarah ke sana. Tulis alasannya. Merek yang sudah punya font wajib (brand guideline) mengalahkan aturan ini, sebutkan di komentar bukti.

## Pasangan

- Satu display dan satu body. Tambahan ketiga hanya untuk data (monospace tabular) atau aksen cetak.
- Berkontras jelas: serif dengan sans, atau grotesk lebar dengan humanist sempit. Dua sans yang mirip terlihat seperti kesalahan.
- Jaga tinggi-x dan bobot tampak serupa pada ukuran isi, supaya baris campuran tidak melompat.
- Satu keluarga saja sah bila variasinya lebar (bobot dan lebar berbeda jauh) dan itu keputusan sadar. Linter memberi WARN `single-family`, tekan dengan `unslop-ok` kalau memang disengaja.

## Skala dan ritme

- Skala modular dengan rasio minimal 1.25. Contoh langkah: 0.875, 1, 1.25, 1.563, 1.953, 3.052, 4.768 rem.
- Judul fluid: `clamp(min, preferred, max)`. Contoh: `font-size: clamp(3rem, 1.4rem + 8vw, 8.5rem)`.
- Hero yang berani boleh memakai judul 6 sampai 9 rem di desktop. Itu keputusan, bukan kecelakaan.
- `line-height` mengecil seiring ukuran naik: 1.6 untuk isi, 1.3 untuk subjudul, 0.95 sampai 1.05 untuk judul raksasa.
- `letter-spacing` negatif ringan (`-0.02em`) untuk judul besar, nol untuk isi, positif ringan untuk label kapital kecil.
- Angka di tabel dan harga: `font-variant-numeric: tabular-nums`.

## Teks panjang

- `max-width: 62ch` untuk paragraf. Rentang nyaman 55 sampai 75.
- Rata kiri. Rata kanan-kiri tanpa hyphenation membuat sungai putih.
- `text-wrap: balance` untuk judul, `text-wrap: pretty` untuk paragraf.
- Kapital semua hanya untuk label pendek, dengan `letter-spacing` positif.
- Tebal dipakai untuk memandu mata, jangan menebalkan seperempat kalimat.

## Memuat font

- Embed sebagai `@font-face` dengan data URI base64 bila halaman harus berdiri sendiri, atau self-host file `.woff2`. Jangan bergantung CDN pihak ketiga yang bisa diblok.
- Subset ke rentang Latin yang dipakai: `pyftsubset in.ttf --output-file=out.woff2 --flavor=woff2 --unicodes="U+0020-007E,U+00A0-024F,U+2000-206F,U+2190-21FF" --layout-features='kern,liga'`. Pasang `fonttools` dan `brotli` lebih dulu.
- `font-display: swap`. Muat hanya bobot yang dipakai.
- Cek lisensi. Google Fonts berlisensi OFL dan boleh di-embed. Font komersial perlu lisensi web.
