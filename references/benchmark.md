# Tolok ukur: dua situs yang tidak terbaca AI

Dua situs milik pemilik repo ini dipakai sebagai pembanding: **uns.ai.id** (UNS AI Center) dan **afs.larutmalam.id** (Accidentally Fun Studio). Catatan di bawah berasal dari tangkapan layar bagian atas halaman dan sumber CSS UNS. Bagian bawah halaman AFS dan sumbernya tidak saya baca, jadi tidak ada klaim tentangnya.

## Temuan yang mengoreksi skill ini

Dulu skill ini menyebut bayangan keras, hero satu warna penuh, kata kunci berwarna, dan kartu berjajar sebagai tell. Kedua situs memakai semuanya, dan keduanya tidak terbaca AI. Jadi tell-nya bukan teknik itu. Linter versi sebelumnya menjatuhkan 47 FAIL pada sumber UNS, hampir semuanya `reflex-font` (Montserrat, Lato), `side-stripe`, dan `identical-cards`. Ketiganya sekarang WARN, dan keputusan merek bisa diizinkan per file (`unslop-allow:`).

Pelajarannya: teknik yang sama bisa jadi slop atau desain, tergantung apakah ia **dimiliki**.

## Yang membuat keduanya terbaca dirancang

**1. Aset yang hanya dimiliki subjek ini.**
UNS punya maskot Wiku, karakter berbusana Jawa yang berdiri di dalam huruf U berpola batik. AFS punya ikon kucing dan stiker "STUDIO" yang dimiringkan. Tidak ada situs lain yang bisa memakai aset itu, jadi tidak bisa tertukar. Ini jawaban terkuat untuk uji "bisa tertukar dengan subjek lain?".

**2. Satu sistem yang dijalankan sampai ke detail.**
UNS memakai bayangan `4px 4px 0` berwarna tinta di tombol, kartu, dan jendela obrolan. AFS memakai bayangan keras yang sama di tombol, label, dan judul. Radius, ketebalan garis, dan warna tinta konsisten. Bayangan keras jadi bahasa merek, bukan hiasan di satu tombol.

**3. Warna jenuh yang dikomit, dengan satu pasangan kontras.**
UNS: biru cyan jenuh dengan kuning menyala sebagai aksen tunggal. AFS: biru laut penuh dengan kuning dan satu titik merah muda. Tidak ada gradien ungu dan tidak ada pastel aman. Tiap halaman memilih arah lalu memenuhinya.

**4. Satu detail yang tidak aman.**
UNS memakai Silkscreen (font piksel) hanya untuk jendela "WIKU.EXE", sementara seluruh halaman memakai Montserrat. AFS menumpuk judul kapital raksasa dengan kemiringan dan bayangan. Detail ini menandakan ada orang yang memutuskan.

**5. Akronim atau konsep menjadi layout.**
Bagian LUHUR di UNS: lima kolom vertikal dengan lebar berbeda, tiap kolom satu huruf raksasa dan label diputar 90 derajat. Isinya (lima pegangan) menentukan bentuknya. Bukan tiga kartu setara.

**6. Kejujuran yang jarang ada di halaman AI.**
UNS menulis di hero: "Situs ini bukan situs resmi milik Universitas Sebelas Maret", menamai orang di balik proyek (dengan foto, jabatan, dan angkatan), menandai demo obrolan sebagai "Simulasi tampilan. Hasil asli bergantung pada pertanyaan dan berkasmu", dan menyebut batas layanan ("Ada kuota harian").

**7. Bahasa yang menyebut hal nyata.**
"Baca berkas sampai 20 MB", "Unggah PDF, minta dokumen Word atau Excel", "Parafrase ilmiah yang bersitasi". Ukuran, format, dan batasan, bukan sifat.

## Cara memakainya

- Sebelum merancang, tulis aset apa yang hanya dimiliki subjek ini (maskot, foto orang, produk asli, data, tulisan tangan, tempat). Kalau tidak ada, minta ke pemilik atau tulis `[ISI: foto ...]`. Jangan menggambar pengganti dengan SVG.
- Pilih satu aturan bentuk (bayangan, radius, garis) dan jalankan di semua komponen.
- Komit pada satu pasangan warna jenuh yang berasal dari merek, lalu penuhi halaman.
- Sisakan satu detail yang tidak aman, tapi masih menunjuk ke subjek.
- Biarkan isi menentukan bentuk (akronim, urutan, data), bukan wadah.
- Tulis batasan dan asal-usul dengan jujur.

## Batas klaim

- Dua situs ini lolos uji pemilik, bukan uji pihak luar. Penilaian "tidak slop" tetap subjektif.
- Karya mereka bersumber dari aset yang tidak bisa disalin repo ini (maskot, foto). Skill hanya bisa mengarahkan mencari aset serupa, bukan menggantinya.
- Linter tidak mengukur satu pun dari tujuh butir di atas. Semuanya penilaian manusia.
