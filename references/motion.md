# Gerak

## Prinsip

1. **Satu momen yang berarti.** Pilih satu gerak yang menyampaikan sesuatu tentang subjek (jarum jam menyapu masuk, garis peta digambar, angka menetap ke nilai sebenarnya) dan biarkan sisanya diam.
2. **Gerak membawa informasi.** Ia menunjukkan hubungan sebab akibat, urutan, atau asal elemen. Kalau gerak dihapus dan tidak ada informasi yang hilang, itu dekorasi.
3. **Karakter, bukan default.** Easing bawaan browser (`ease`, `ease-in-out`, `linear`) terbaca mekanis.

## Easing dan durasi

| Kebutuhan | Kurva | Durasi |
|---|---|---|
| Pegas ringan (tombol, jarum) | `cubic-bezier(0.34, 1.4, 0.64, 1)` | 300 sampai 600ms |
| Keluar halus (muncul, masuk) | `cubic-bezier(0.22, 1, 0.36, 1)` | 400 sampai 700ms |
| Masuk-keluar tegas (geser panel) | `cubic-bezier(0.65, 0, 0.35, 1)` | 250 sampai 450ms |
| Respons langsung (hover warna) | `cubic-bezier(0.4, 0, 0.2, 1)` | 120 sampai 200ms |

CSS modern mendukung `linear()` untuk pegas sungguhan bila peramban target memungkinkan.

Aturan durasi: elemen kecil cepat, elemen besar lebih lama, jarak jauh lebih lama dari jarak dekat. Jangan memberi semua elemen durasi 0.3s.

## Yang dianimasikan

- Hanya `transform` dan `opacity` untuk gerak berkelanjutan. Properti layout (`width`, `height`, `top`, `left`, `margin`) memicu reflow.
- Garis bawah yang "tumbuh": animasikan `background-size` atau `transform: scaleX()`.
- Jangan `transition: all`. Sebut properti: `transition: transform 0.35s var(--ease), background-color 0.2s`.
- `will-change` hanya pada elemen yang benar-benar bergerak lama, dan dilepas setelahnya.

## Gerak berkurang

Wajib. Tanpa ini linter memberi FAIL.

```css
@media (prefers-reduced-motion: reduce) {
  .hand { animation: none; transform: rotate(52deg); }  /* tampilkan keadaan akhir */
  .cta, tbody tr { transition: none; }
}
```

Keadaan akhir harus tetap benar. Menghentikan animasi di keadaan awal sering menyisakan elemen yang tidak terlihat.

## Pola yang portabel

Pilih satu sampai tiga yang menyambung ke subjek. Semuanya bisa dibuat dengan CSS atau JavaScript biasa.

1. **Kata muncul saat scroll.** Headline tampil kata per kata mengikuti posisi gulir (IntersectionObserver per kata, `opacity` dan `transform`). Cocok untuk manifesto panjang.
2. **Garis digambar.** `stroke-dasharray` dan `stroke-dashoffset` pada SVG. Cocok untuk garis peta, garis bawah aksen, rel linimasa.
3. **Tarikan magnetik.** Tombol sedikit bergeser ke arah kursor saat didekati (hitung jarak pointer, terapkan `transform: translate`). Cocok untuk satu CTA utama.
4. **Pantul pegas.** Skala dengan kurva overshoot saat hover atau tekan.
5. **Huruf bertahap.** Tiap huruf judul diberi `animation-delay` berbeda sedikit.
6. **Perluasan berbagi layout.** Kartu kecil membesar menjadi detail dengan teknik FLIP, bukan modal yang muncul mendadak.
7. **Acak lalu menetap.** Karakter acak menetap ke teks asli. Cocok untuk angka statistik yang benar-benar data.
8. **Tepi mengikuti kursor.** Custom property `--x` dan `--y` diperbarui saat `pointermove` untuk gradien atau border yang menyorot.
9. **Riak dari titik sentuh.** Lingkaran membesar dari titik klik, lalu memudar.
10. **Marquee berkecepatan.** Gulir horizontal yang kecepatannya bereaksi terhadap kecepatan scroll pengguna.

Referensi implementasi untuk dilihat sebelum menulis dari nol: motion.dev/examples, repositori `animate-ui`, `react-bits`, `magicui`, `motion-primitives`. Kalau target akhir HTML statis, tiru polanya dengan CSS, jangan mengimpor pustaka React hanya demi satu efek.

## Tell gerak

- Fade-up setiap section saat gulir dengan durasi dan jarak sama.
- Parallax dan partikel tanpa alasan.
- Hover yang mengubah skala semua kartu sekaligus.
- Loading skeleton untuk konten yang sebenarnya sudah ada.
- Kursor kustom yang menghalangi klik.

## Kinerja

- Tes di perangkat lambat atau dengan throttling CPU. Animasi yang mulus di laptop sering patah di ponsel menengah.
- Tidak ada animasi yang memblokir interaksi pertama.
- Hentikan animasi tak berujung saat tab tidak terlihat atau elemen di luar layar.
