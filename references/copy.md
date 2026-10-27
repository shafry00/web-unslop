# Copy halaman

Berlaku untuk judul, subjudul, tombol, mikrokopi, pesan galat, keadaan kosong, meta description, dan teks alt.

## Aturan mutlak

**Tidak ada tanda pisah em dash (U+2014).** Ganti dengan koma, titik, titik dua, tanda kurung, atau kalimat baru. Tanda kurung ganda dua strip (` -- `) yang dipakai sebagai pengganti juga dilarang. Linter menggagalkan keduanya di semua file.

## Larangan kata dan struktur

Daftar kata di `references/tells.md`. Prinsipnya: kalau kalimat tetap bermakna setelah sebuah kata dihapus, kata itu pengisi.

Struktur yang dihindari:

- Tiga sifat berjajar (`cepat, mudah, terpercaya`).
- `bukan hanya X, tapi juga Y` dan `not just X, but Y`. Tulis Y saja.
- Pembuka yang memuji zaman (`di era digital ini`, `in today's fast-paced world`).
- Penutup yang mengulang pembuka.
- Pertanyaan retoris sebagai judul section ("Siap menaikkan bisnismu?").
- Tiga kalimat pendek berirama sama berturut-turut.
- Tanda seru.
- Emoji hiasan.

## Jangan mengarang fakta

Spesifik yang karangan lebih buruk daripada kabur yang jujur, karena terlihat meyakinkan. Harga, durasi, tahun berdiri, jumlah pelanggan, syarat garansi, dan kutipan harus berasal dari pemilik atau sumber yang bisa dicek.

- Belum ada datanya: tulis `[ISI: apa yang dibutuhkan]` di tempatnya. Contoh: `[ISI: tarif stempel flash]`. Linter memberi WARN `placeholder-left` selama masih tersisa.
- Pemilik menyuruh mengarang untuk contoh: tandai halamannya sebagai contoh di tempat yang terlihat, dan jangan memakainya sebagai bukti kualitas skill.
- Angka perkiraan: tulis sebagai perkiraan dan sebut asumsinya.

## Irama judul

Judul yang semuanya berbentuk dua klausa dengan koma ("Harga tertulis, selesai sebelum Anda pulang"), semuanya sepanjang dua baris, dan semuanya bernada janji kecil, terbaca disusun mesin. Linter menandai bila separuh judul atau lebih berpola itu (`heading-cadence`).

Variasikan:

- Judul satu kata atau satu kata benda: "Tarif."
- Judul berupa pertanyaan nyata dari pembaca: "Berapa lama kalau jamnya mati total?"
- Judul berupa pernyataan fakta tanpa klausa kedua: "Servis total lima hari kerja."
- Tanpa judul: langsung isi, bila kontennya sudah menjelaskan diri.
- Judul panjang untuk satu bagian saja yang memang butuh argumen.

Jangan mewarnai atau menebalkan kata terakhir judul untuk "menekankan". Itu tell yang sangat umum (`accent-last-word`).

## Pengganti: spesifik dan bisa dibuktikan

| Pengisi | Spesifik |
|---|---|
| `Layanan cepat` | "Ganti baterai 20 menit, ditunggu." |
| `Harga terjangkau` | "Servis total mulai Rp 350.000, estimasi tertulis sebelum dibongkar." |
| `Berpengalaman` | "Memperbaiki jam di Lorong 4 sejak 1998." (hanya bila benar) |
| `Kualitas terjamin` | "Garansi enam bulan, tercatat di nota." |
| `Hubungi kami` | "Kirim foto jam ke WhatsApp." |

Tiap klaim membawa salah satu: angka, durasi, syarat, nama, mekanisme. Kalau tidak ada bukti, hapus klaimnya. Jangan mengarang testimoni, angka pengguna, atau logo klien.

## Tujuh sapuan

Jalankan satu per satu. Satu sapuan, satu perhatian.

1. **Clarity.** Struktur membingungkan? Jargon yang tidak perlu? Kalimat yang harus dibaca dua kali?
2. **Voice.** Satu register dari awal sampai akhir, tidak melompat dari santai ke korporat.
3. **So What.** Tiap klaim menjawab "kenapa pembaca peduli".
4. **Prove It.** Klaim didukung angka, contoh, atau mekanisme.
5. **Specificity.** Kata kabur menjadi konkret. "Cepat" menjadi durasi. "Banyak" menjadi jumlah.
6. **Emotion.** Detail indrawi atau situasi nyata, secukupnya. Satu detail yang tepat mengalahkan lima kata sifat.
7. **Zero Risk.** Di dekat CTA, hilangkan hambatan: biaya, komitmen, waktu, apa yang terjadi setelah klik.

## Register

Pilih satu sesuai konteks, jangan mencampur.

- **Penjelasan.** Mengalir seperti bercerita. Partikel peralihan santai ("Nah,", "Jadi,"). Istilah teknis dijelaskan ulang dengan bahasa sehari-hari.
- **Cerita personal.** Putar balik cerita disebut terang-terangan. Ucapan terima kasih dan penyebutan orang. Ditutup dengan wawasan dan ajakan pendek. Tanpa emoji.
- **Institusional ringkas.** Kalimat pendek sampai sedang. Tanpa partikel santai. Dibuka dengan pengamatan umum lalu menyempit ke hal spesifik. Ditutup dengan terima kasih dan harapan singkat.

Kalau pemilik punya panduan merek atau contoh tulisan, itu mengalahkan register di atas. Kalau konteksnya ambigu, tanyakan.

## CTA

Sebut aksi dan hasil, dari sudut pandang pembaca.

| Generik | Spesifik |
|---|---|
| `Submit` | "Kirim foto jam" |
| `Get Started` | "Buat undangan pertamamu" |
| `Learn More` | "Lihat tarif lengkap" |
| `Klik di sini` | "Unduh tabel tarif (PDF, 80 KB)" |
| `Mulai sekarang` | "Pesan jadwal servis Sabtu" |

Satu CTA utama per layar. CTA kedua harus terlihat lebih ringan.

## Mikrokopi

- **Galat:** katakan apa yang terjadi dan apa yang bisa dilakukan. "Nomor WhatsApp kurang dua digit. Cek lagi, biasanya diawali 08 atau 62." bukan "Terjadi kesalahan."
- **Keadaan kosong:** jelaskan kenapa kosong dan satu langkah berikutnya. Bukan ilustrasi lucu dengan "Belum ada apa-apa di sini".
- **Label formulir:** kata benda yang jelas. Placeholder bukan pengganti label.
- **Konfirmasi:** sebut hasilnya. "Estimasi dikirim ke 0812... dalam satu hari kerja."
- **Tombol destruktif:** sebut objeknya. "Hapus 3 foto", bukan "Ya".

## Sebelum dan sesudah

**Hero**
Sebelum: `Solusi terbaik untuk servis jam Anda. Cepat, mudah, terpercaya.`
Sesudah: "Jam mati belum tentu rusak. Kirim foto muka dan belakangnya, estimasi tertulis datang sebelum ada yang dibongkar."

**Fitur**
Sebelum: `Platform kami menghadirkan pengalaman seamless untuk mengelola keuangan Anda.`
Sesudah: "Catat pengeluaran dari WhatsApp. Rekap bulanan masuk ke email tanggal 1."

**Tentang**
Sebelum: `Kami berkomitmen memberikan layanan terbaik dengan sepenuh hati.`
Sesudah: "Hasan memperbaiki jam di Lorong 4 sejak 1998. Anaknya, Dewi, mengurus jam elektronik."

(Contoh di atas fiktif untuk ilustrasi.)

## Meta dan teks alt

- `<title>`: nama + konteks, di bawah 60 karakter.
- Meta description: satu atau dua kalimat spesifik, di bawah 160 karakter. Jangan mengulang judul.
- Alt: apa yang terlihat dan relevan. "Muka jam saku berkaca retak, jarum menunjuk 4.10." Bukan "gambar jam". Dekoratif memakai `alt=""`.

## Bahasa

- Pakai bahasa pembaca. Bahasa Indonesia santai-profesional untuk kebanyakan halaman umum. Tentukan `Anda`, `kamu`, atau tanpa kata ganti sejak awal dan konsisten.
- Campur istilah Inggris hanya untuk istilah yang memang dipakai pembaca ("checkout", "login"). Jangan menerjemahkan paksa, jangan menyisipkan bahasa Inggris demi terlihat modern.
- Angka dan mata uang format lokal: `Rp 350.000`, `09.00`, "5 hari kerja".
