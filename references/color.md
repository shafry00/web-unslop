# Warna

## Menurunkan palet dari subjek

Palet yang aman dan palet yang khas dibedakan oleh sumbernya. Sumber yang benar adalah benda dan tempat yang nyata.

1. Daftar lima sampai delapan detail fisik subjek. Bengkel jam: alas meja kerja hijau, kuningan tuas, kertas nota, tinta stempel, kaca pembesar.
2. Ambil satu detail sebagai **warna dominan**. Pilih yang paling berani dan paling spesifik, bukan yang paling netral.
3. Ambil satu detail lain sebagai **aksen** yang jarang dipakai (satu CTA, satu garis, satu kata di judul).
4. **Netral** diturunkan dari hue dominan: kertas bernuansa hijau-abu, tinta hijau-hitam. Bukan abu-abu murni.
5. Cek hasilnya terhadap daftar tell di bawah. Kalau mendarat di salah satunya, kembali ke langkah 1 dan cari detail yang lebih spesifik.

Contoh penalaran dari `examples/bengkel-jam`: dominan hijau alas kerja `#26382f`, aksen kuningan `#c9a24d`, kertas `#e8ebe2`, tinta `#18201b`. Semua netral membawa sedikit hijau.

Bila subjek tidak punya detail fisik (alat internal, dashboard), turunkan dari merek yang sudah ada. Kalau merek pun belum ada, tanyakan satu hal ke pemilik: warna apa yang sudah dipakai di kartu nama, kemasan, atau tanda tokonya?

Alternatif untuk subjek tanpa detail fisik: `references/palette-library.md`.

## Komitmen

Situs yang terlihat dirancang memilih satu arah dan berkomitmen: biru jenuh penuh, merah berbutir, hitam putih murni, blok warna datar. Jangan mencampur lima warna sedang supaya aman.

- Satu warna menempati 40 sampai 70 persen luas area terlihat.
- Aksen di bawah 10 persen.
- Variasi lewat tingkat terang dan gelap dari warna yang sama, bukan menambah hue.

## Tema gelap atau terang

Pilih dari konteks pembaca, bukan dari rasa takut salah.

- Dibuka malam hari di ponsel, banyak membaca layar lama, alat kreatif dan media: gelap masuk akal.
- Dibuka siang di luar ruangan, dokumen, harga, dan transaksi: terang lebih terbaca.
- Merek dengan identitas jelas: ikuti identitasnya.
- Selalu sediakan keduanya lewat token: `:root { --paper: ...; --ink: ... }` dan override di `@media (prefers-color-scheme: dark)` serta `[data-theme="dark"]`. Kalau halaman sengaja satu tema (misalnya undangan cetak), catat alasannya.

## Tell warna

| Tell | Catatan |
|---|---|
| Gradien ungu ke biru, cyan, atau pink | Default model. FAIL di linter. |
| Latar gelap + teal atau emerald | Kombinasi paling umum untuk "teknis". WARN. |
| Glow neon berwarna di latar gelap | WARN. |
| Krem hangat + terakota | Refleks untuk "hangat". Sah untuk skincare, wellness, atau kerajinan yang memang berwarna itu. WARN dan tulis alasan. |
| `#000` dan `#fff` murni | Beri tint ke hue palet. |
| Gradien sebagai pengisi latar section | Ganti blok warna datar. |
| Teks abu-abu di atas warna latar | Pakai tingkat dari warna latar. |

## Kontras

Linter tidak menghitung kontras karena nilai sering berasal dari variabel CSS. Hitung sendiri.

- Teks isi: minimal 4.5:1.
- Teks besar (24px ke atas, atau 19px tebal): minimal 3:1.
- Komponen UI dan batas input: minimal 3:1 terhadap latar.

Rumus WCAG: ubah tiap kanal sRGB `c` (0 sampai 1) menjadi `c <= 0.04045 ? c/12.92 : ((c+0.055)/1.055)^2.4`, lalu `L = 0.2126 R + 0.7152 G + 0.0722 B`. Rasio = `(L_terang + 0.05) / (L_gelap + 0.05)`.

Potongan Python untuk dijalankan cepat:

```python
def lum(h):
    r, g, b = (int(h[i:i+2], 16) / 255 for i in (1, 3, 5))
    f = lambda c: c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)

def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)

print(round(ratio("#c9a24d", "#26382f"), 2))
```

Cek terutama pasangan pastel di atas latar gelap dan teks tipis di atas foto.

## Format

- Pakai `oklch()` untuk menurunkan tingkat terang secara konsisten, sediakan fallback hex bila perlu mendukung peramban lama.
- Definisikan token semantik (`--paper`, `--ink`, `--accent`), bukan nama warna (`--green`).
- Satu sumber kebenaran di `:root`. Tidak ada hex yang tersebar di komponen.
