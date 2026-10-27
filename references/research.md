# Riset referensi

Langkah sebelum menulis kode final. Tujuannya mencari bentuk, bukan menyalin. Hasil riset dicatat di komentar bukti (`component`, `layout`, `gerak`) dengan jujur: tulis yang benar-benar dilihat.

## 1. Komponen

Cari struktur dan interaksi yang pernah berhasil sebelum merancang sendiri.

**Dengan MCP 21st.dev** (bila terpasang):

1. `search` atau `search_picker` untuk beberapa opsi dari kata kunci atau deskripsi. Gratis, boleh dipakai sepuasnya.
2. Pilih dari pratinjau, deskripsi, dan metadata. Jangan buka kode sumbernya dulu.
3. Tulis ulang dari nol untuk proyek ini, mengambil struktur dan interaksinya, bukan tampilannya.
4. `get_component` (ambil sumber asli) hanya bila pratinjau tidak cukup untuk menebak interaksi kompleks, atau pemilik memintanya. Akun gratis dibatasi sekitar dua kali sehari. Cek sisa kuota dengan `get_usage` bila ragu.

**Tanpa MCP:** telusuri koleksi terbuka seperti shadcn/ui, magicui, cult-ui, motion-primitives, animate-ui, atau topik GitHub `framer-motion`, lalu baca sumbernya langsung.

Kalau tidak ada yang cocok, tulis di komentar bukti: "tidak ada yang relevan karena X, dibangun manual".

## 2. Gerak

Sumber untuk easing dan pola yang lebih halus dari bawaan browser:

- **motion.dev/examples**: contoh resmi Motion, rujukan easing dan timing.
- **animate-ui** (imskyleen): komponen animasi Tailwind + Motion, untuk mikro-interaksi.
- **motion** (motiondivision): sumber pustaka, untuk memahami primitif (pegas, stagger, gestur) yang bisa ditiru manual.
- **react-bits** (DavidHDev): efek latar, animasi teks, komponen interaktif.
- **magicui**, **cult-ui**, **motion-primitives**, **precedent**, **fancy**: koleksi komponen animasi untuk dilihat sumbernya.

Kalau target akhir HTML statis, tiru polanya dengan CSS atau JavaScript biasa. Jangan mengimpor pustaka React demi satu efek. Sepuluh pola portabel ada di `references/motion.md`.

## 3. Komposisi

Temuan dari penelusuran manual Dribbble, Pinterest, Behance, dan Awwwards. Pakai sebagai lensa tambahan, bukan resep. Tiap lensa harus tetap berakar pada subjek.

**Kanvas gelap dengan satu sumber cahaya.** Latar nyaris hitam, satu bentuk bercahaya sebagai satu-satunya titik terang. Cocok untuk produk teknologi, AI, alat developer. Tetap awasi tell `dark-glow` dan `dark-teal`: lensa ini sah hanya bila cahayanya punya alasan.

**Serif editorial besar di atas foto potret.** Judul serif besar menimpa foto close-up, palet netral gelap. Pola berulang di kategori mode, kecantikan, gaya hidup.

**Blok warna datar pekat.** Kuning terang, ungu sedang, hijau tua dipakai datar (tanpa gradien) sebagai latar section atau kartu studi kasus.

**Foto sinematik penuh layar.** Pemandangan atau potret dramatis memenuhi satu layar, tipografi tebal bertumpuk di atasnya. Cocok untuk wisata, petualangan, cerita.

**Color-blocking jenuh.** Kuning-hitam diagonal, kisi warna kontras kuat. Sah untuk merek yang bertenaga atau jenaka, bukan otomatis kurang elegan.

**Tipografi raksasa sebagai hero utuh.** Tanpa foto. Headline dipecah beberapa baris besar memenuhi layar. Judul satu atau dua kata. Contoh dari situs pemenang: satu kata, ukuran raksasa, sisanya ruang kosong.

**Satu arah, komitmen penuh.** Studio pemenang penghargaan memilih satu warna atau tekstur dan tidak mencampur banyak: biru jenuh penuh, merah berbutir, hitam putih murni, gradien mesh pastel. Butir atau noise berat dipakai sengaja untuk kesan film.

**Foto produk dalam konteks nyata.** Laptop di rumput, ponsel dekat api, monitor di atas kontainer. Bukan mockup datar.

**Kecantikan dan perawatan kulit.** Krem dan beige hangat memang bahasa visual niche ini. Peringatan "krem + terakota = refleks" berlaku bila warna itu dipaksakan ke subjek yang tidak berhubungan. Bedanya: dipilih karena spesifik ke subjek, atau karena malas berpikir.

Pertanyaan penutup setelah riset: halaman ini punya satu pilihan visual yang berani, atau semuanya aman? Bukan banyak mikro-interaksi yang membuat halaman elegan, melainkan keberanian membuat satu keputusan besar dan menjalankannya penuh.

## 4. Teknik membuka situs yang berat JavaScript

Situs seperti Behance, Awwwards, dan Pinterest sulit dibaca lewat fetch biasa. Render dengan Chrome headless lalu baca gambarnya.

```bash
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$CHROME" --headless=new --disable-gpu --screenshot=/tmp/ref.png \
  --window-size=1440,3000 --virtual-time-budget=6000 "https://contoh.com/halaman"
```

Buka `/tmp/ref.png` dengan alat baca gambar. Untuk apa yang dilihat: tulis pola struktur, ukuran relatif, dan perilaku warna, bukan menyalin aset. Tampilan hasil karya orang lain dilindungi, strukturnya adalah gagasan.

## 5. Catat di komentar bukti

Contoh isi yang jujur:

```
component: 3 pratinjau tabel harga dari 21st.dev dilihat, dibangun manual dengan garis tipis karena data perbandingan
gerak    : meniru pola path-draw dari motion.dev, versi CSS saja
layout   : lensa tipografi raksasa, headline 9 kolom tanpa foto
```

Isi yang tidak jujur (mengklaim riset yang tidak dilakukan) lebih buruk daripada kolom kosong. Hook tidak bisa memverifikasi kebenaran isinya. Hanya pemilik yang bisa mengauditnya.
