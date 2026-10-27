# Halaman Universitas Sebelas Maret (tidak resmi)

Contoh teladan pertama repo ini. Bukan situs resmi UNS dan tidak memakai logo resmi.

Bangun: `python3 build.py`. Hasil: `index.html` mandiri, font dan gambar sudah ter-embed.

## Kenapa ini dijadikan teladan

1. **Aset milik subjek.** Maskot Wiku, token warna, font, kisi lingkaran, swirl, huruf U berkisi, dan jendela piksel berasal dari uns.ai.id milik pemilik repo. Tidak ada ornamen SVG pengganti.
2. **Satu sistem sampai detail.** Bayangan keras, pill, dan jendela piksel dipakai konsisten, bukan di satu tombol.
3. **Bentuk mengikuti isi.** Daftar fakultas menjadi strip kolom vertikal, data yang belum ada menjadi jendela piksel `JADWAL.TXT`, bukan kerangka hero, tabel, langkah, FAQ.
4. **Tanpa fakta karangan.** Hanya tiga fakta yang diyakini (berdiri 11 Maret 1976, Surakarta, Kentingan). Selebihnya `[ISI: ...]`.
5. **Kejujuran yang terlihat.** Catatan "bukan situs resmi" di hero dan footer, dan daftar fakultas ditandai belum diverifikasi.

## Syarat dan batasnya

- Kemiripan dengan uns.ai.id datang dari aset yang dipinjam. Skill tidak menciptakannya.
- Wiku adalah maskot proyek AI Center, bukan maskot resmi UNS. Gambar di `img/` milik pemilik repo, tidak dilisensikan untuk dipakai ulang tanpa izin.
- Aturan `reflex-font`, `hard-shadow`, `side-stripe`, `accent-last-word`, dan `pure-black-white` sengaja diizinkan lewat `unslop-allow` karena itu sistem merek uns.ai.id.
- Linter menandai `placeholder-left` selama `[ISI: ...]` masih ada. Itu memang benar: halaman ini draf sampai pemilik mengisinya.
- Belum diuji: animasi bergerak, lebar 390px asli, dan kontras teks muted di bagian gelap secara hitungan.
- Daftar fakultas dan alamat berasal dari ingatan penulis dan belum diverifikasi.
