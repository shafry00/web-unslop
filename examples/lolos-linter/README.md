# Dua halaman yang lolos linter tapi tetap terbaca AI

Folder ini sengaja disimpan sebagai **contoh buruk**. Keduanya tidak punya FAIL di linter dan lolos hook, tetapi ketika ditunjukkan ke pembaca manusia, keduanya terbaca sebagai buatan AI. Tujuannya mengingatkan bahwa lolos linter hanya syarat minimal.

Halaman: `bengkel-jam/` (bengkel jam fiktif) dan `stempel-rudi/` (toko stempel fiktif). Bangun dengan `python3 bengkel-jam/build.py` dan `python3 stempel-rudi/build.py`.

## Kenapa gagal uji desain

1. **Kerangka sama persis di keduanya:** hero, tabel, langkah atau lembar, FAQ, footer. Teksnya bisa ditukar tanpa mengubah struktur.
2. **Irama judul seragam:** hampir semua judul berbentuk "X, lalu Y".
3. **Tell visual yang tidak tertangkap linter versi awal:**
   - kata terakhir judul diwarnai aksen (bengkel jam)
   - angka 1, 2, 3 besar berwarna yang digeser (bengkel jam)
   - ornamen SVG sebagai gimmick: muka jam, cap miring raksasa
   - hero satu warna penuh, tanpa aset yang hanya dimiliki subjeknya
   - satu tombol berbayangan keras yang tidak menjadi bahasa sistem (toko stempel)
   - keterangan kecil abu-abu di mana-mana
4. **Spasi antar section identik.**
5. **Isinya karangan.** Harga, durasi, dan syarat tampak spesifik tapi saya yang membuatnya. Tidak ada foto, orang, atau data nyata. Itu spesifik palsu.

## Yang tertangkap sekarang

Setelah linter diperkuat, kedua halaman mendapat WARN: `skeleton-landing`, `heading-cadence`, `accent-last-word` (bengkel jam), `uniform-section-padding` dan `hard-shadow` (toko stempel). Jalankan:

```bash
python3 scripts/unslop_lint.py examples/lolos-linter/
```

Tell lain di daftar nomor 3 dan 5 masih hanya bisa dinilai manusia. Itu batas linter, bukan kebetulan.

## Koreksi terhadap analisis awal

Analisis awal menyebut bayangan keras dan hero satu warna sebagai tell. Dua situs rujukan pemilik (uns.ai.id, afs.larutmalam.id) memakai keduanya dan tidak terbaca AI. Perbedaan sebenarnya: kedua situs itu punya aset yang hanya dimiliki subjeknya (maskot, orang nyata, produk) dan menjalankan satu sistem sampai ke detail. Dua halaman di sini hanya punya ornamen SVG buatan dan fakta karangan. Rinciannya di `references/benchmark.md`.

## Pelajaran

- Tes kerangka dan uji slop tertulis (`references/layout.md`, `references/process.md`) dijalankan sebelum membangun, bukan sesudahnya.
- Tanpa fakta nyata dari pemilik, halaman apa pun akan terbaca karangan. Pakai `[ISI: ...]`.
- Halaman yang bagus butuh keputusan yang diambil dari isi subjek yang nyata. Contoh teladan di repo ini belum ada. Kalau kamu membangun satu dengan brief sungguhan, kirim sebagai PR.
