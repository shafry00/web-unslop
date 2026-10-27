# Layout dan komposisi

## Mulai dari bentuk subjek

Template memulai dari wadah: hero tengah, tiga kartu, testimoni, harga, footer. Komposisi yang dirancang memulai dari pertanyaan: apa yang paling penting dilihat pembaca dalam dua detik, dan bentuk apa yang menyampaikannya?

- Tarif: tabel dengan garis tipis, karena orang membandingkan angka.
- Proses: daftar bernomor yang digeser, karena urutan adalah isinya.
- Tanya jawab: `<details>`, karena pembaca memindai pertanyaan.
- Portofolio: gambar besar dengan keterangan kecil di pojok, karena gambar adalah buktinya.
- Alamat dan jam: blok kecil yang bergaris atas, karena itu informasi referensi.

## Satu pusat perhatian

Sebelum menyatakan selesai, tanyakan apakah ada satu elemen yang diperbesar dan dibuat berani sebagai pusat, atau semuanya berukuran sedang dan aman. Pilihan yang berhasil:

- Tipografi raksasa memenuhi satu layar tanpa foto. Judul pendek, satu atau dua kata sampai satu kalimat.
- Satu warna pekat menguasai section.
- Satu foto penuh layar dengan teks bertumpuk.
- Satu angka yang benar dan berukuran sangat besar, dengan konteks dan sumber.

Pilih satu. Dua pusat saling meniadakan.

## Asimetri

- Grid 12 kolom, lalu patahkan: judul di kolom 1 sampai 9, keterangan di kolom 8 sampai 12 yang sejajar bawah.
- Rata kiri sebagai dasar. Rata tengah hanya untuk satu judul pendek yang berdiri sendiri, misalnya penutup.
- Biarkan satu elemen keluar dari bingkai (ornamen terpotong tepi, angka raksasa yang menyentuh margin).
- Margin kiri-kanan tidak harus sama pada setiap section.

## Ritme spasi

Padding atas-bawah yang sama di semua section terbaca sebagai output otomatis.

- Beri tiga atau empat nilai spasi dan gunakan secara berbeda: rapat di dalam kelompok, sedang antar kelompok, lega antar section, sangat lega sebelum bagian penutup.
- Section pertama (hero) lebih padat atau lebih lega dari sisanya, tapi dengan sengaja.
- Gunakan `clamp()` untuk spasi supaya skalanya mengikuti lebar layar.

## Pengganti kartu

Kartu cocok untuk objek yang berdiri sendiri dan bisa dipindah: produk, artikel, orang. Kartu tidak cocok untuk daftar fitur.

| Isi | Pengganti |
|---|---|
| Tiga atau empat fitur | Daftar definisi (`<dl>`), tiap fitur sepanjang baris dengan lebar berbeda |
| Langkah | Daftar bernomor dengan angka besar dan offset |
| Perbandingan | Tabel |
| Keunggulan yang berbeda bobot | Satu besar, dua kecil, jangan setara |
| Kutipan pelanggan asli | Kutipan panjang dengan nama dan konteks, satu per baris |
| Statistik | Kalimat yang memuat angka, atau satu angka besar dengan sumber |

Kalau tetap memakai kartu: jangan kartu di dalam kartu, jangan ikon seragam di atas judul, variasikan ukuran, dan beri isi yang berbeda bentuk.

## Hero

- Satu kalimat klaim yang spesifik, satu kalimat pendukung, satu CTA.
- Hindari lencana "Baru" di atas judul, dua tombol sama berat, dan baris logo palsu.
- Ornamen hero harus berasal dari subjek. Contoh: muka jam dari SVG untuk bengkel jam.

## Responsif

- Rancang dari lebar sempit lalu perlebar. Layout asimetris perlu aturan jelas di ponsel: offset dimatikan, kolom ditumpuk, ornamen dipudarkan agar tidak menimpa teks.
- Tidak ada scroll horizontal. Tabel lebar diberi pembungkus `overflow-x: auto` atau disusun ulang.
- Target sentuh minimal 44px.
- Uji di 500px dan 1280px minimal. Lihat `references/process.md` untuk perintah tangkapan layar.

## Konten sebelum dekorasi

Jika sebuah elemen dihapus dan halaman tidak kehilangan makna, elemen itu dekorasi. Boleh ada, tapi harus yang paling sedikit dan paling berasal dari subjek.
