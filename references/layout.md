# Layout dan komposisi

## Mulai dari bentuk subjek

Template memulai dari wadah: hero tengah, tiga kartu, testimoni, harga, footer. Komposisi yang dirancang memulai dari pertanyaan: apa yang paling penting dilihat pembaca dalam dua detik, dan bentuk apa yang menyampaikannya?

- Tarif: tabel dengan garis tipis, karena orang membandingkan angka.
- Proses: urutan yang terbaca dari isinya, misalnya daftar bernomor kecil sejajar teks. Angka raksasa berwarna yang digeser berselang-seling adalah tell.
- Tanya jawab: `<details>`, karena pembaca memindai pertanyaan.
- Portofolio: gambar besar dengan keterangan kecil di pojok, karena gambar adalah buktinya.
- Alamat dan jam: blok kecil yang bergaris atas, karena itu informasi referensi.

## Tes kerangka

Kerangka bawaan semua landing page AI:

1. hero: judul besar, satu kalimat, satu CTA
2. tiga fitur, atau tabel harga, atau tiga langkah bernomor
3. testimoni atau baris logo
4. FAQ accordion
5. penutup dengan CTA kedua

Tiap bagian masuk akal sendirian. Masalahnya urutan dan kehadirannya otomatis. Kalau teks dua halaman dari subjek berbeda ditukar dan strukturnya tetap cocok, halaman itu belum dirancang.

Cara menjalankan:

1. Tulis urutan section halamanmu dalam satu baris.
2. Untuk tiap section, tulis pertanyaan pembaca yang dijawabnya. Tidak ada pertanyaan, hapus.
3. Urutkan menurut pertanyaan yang muncul di kepala pembaca, bukan menurut kebiasaan. Orang yang ragu soal harga butuh harga di atas. Orang yang takut salah pesan butuh contoh hasil sebelum apa pun.
4. Tanyakan apa bentuk isinya, bukan wadah apa yang tersedia. Prosedur dua langkah tidak perlu tiga kartu. Satu foto yang bagus tidak perlu dikelilingi tiga baris fitur.
5. Variasikan bentuk antar section: satu kolom sempit, satu lebar penuh, satu bergaya dokumen, satu hanya gambar. Dua section berturut-turut jangan berbentuk sama.
6. Kerangka yang sama dengan halaman sebelumnya yang kamu buat (di proyek lain atau di sesi ini) berarti gagal. Ulangi.

Linter menandai kerangka `hero + tabel atau langkah + FAQ accordion` sebagai WARN `skeleton-landing`. Itu heuristik, bukan vonis. Tanda lolos yang sebenarnya adalah jawaban tertulis untuk langkah 2.

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

Padding atas-bawah yang sama di semua section terbaca sebagai output otomatis. Linter menandainya (`uniform-section-padding`) pada halaman dengan empat section atau lebih yang hanya punya satu aturan padding.

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
- Ornamen SVG besar di pojok hero (muka jam, cap, kompas) adalah tell, karena menggantikan isi. Pakai foto, gambar, atau data nyata dari subjek. Kalau belum ada, tulis `[ISI: foto bengkel]` daripada menggambar pengganti.

## Responsif

- Rancang dari lebar sempit lalu perlebar. Layout asimetris perlu aturan jelas di ponsel: offset dimatikan, kolom ditumpuk, ornamen dipudarkan agar tidak menimpa teks.
- Tidak ada scroll horizontal. Tabel lebar diberi pembungkus `overflow-x: auto` atau disusun ulang.
- Target sentuh minimal 44px.
- Uji di 500px dan 1280px minimal. Lihat `references/process.md` untuk perintah tangkapan layar.

## Konten sebelum dekorasi

Jika sebuah elemen dihapus dan halaman tidak kehilangan makna, elemen itu dekorasi. Boleh ada, tapi harus yang paling sedikit dan paling berasal dari subjek.
