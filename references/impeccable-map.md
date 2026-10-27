# Impeccable di dalam web-unslop

`vendor/impeccable/` berisi salinan utuh Impeccable v2.1.1 (Apache-2.0, lihat `vendor/impeccable/NOTICE.md`). Dokumen ini menjelaskan bagian mana yang dipakai pada langkah mana, dan siapa yang menang kalau dua skill tidak sepakat.

## Pembagian peran

| | web-unslop | Impeccable |
|---|---|---|
| Kekuatan | Alur wajib dari brief sampai verifikasi, linter dan hook yang bisa dijalankan, aturan copy, bukti keputusan | Aturan desain yang dalam, perintah untuk memperbaiki hasil (critique, polish, bolder, dan seterusnya), referensi per bidang |
| Bentuk | Satu jalur berurutan | Kumpulan perintah yang dipanggil sesuai kebutuhan |
| Bahasa | Indonesia | Inggris |

Pakai web-unslop sebagai jalur utama. Buka Impeccable ketika butuh kedalaman atau ketika hasil perlu diperbaiki dengan satu perintah tertentu.

## Peta langkah

| Langkah web-unslop | Buka di Impeccable |
|---|---|
| 0 Brief | `vendor/impeccable/SKILL.md` bagian Context Gathering Protocol dan Teach Mode, serta `commands/shape.md` untuk wawancara penemuan yang lebih panjang |
| 1 Arah dan dial | `vendor/impeccable/SKILL.md` bagian Design Direction |
| 3 Tipografi | `reference/typography.md` dan `commands/typeset.md` |
| 4 Warna | `reference/color-and-contrast.md` dan `commands/colorize.md` |
| 5 Layout | `reference/spatial-design.md` dan `commands/layout.md` |
| 6 Gerak | `reference/motion-design.md`, `commands/animate.md`, `commands/overdrive.md` untuk efek ambisius |
| 7 Copy | `reference/ux-writing.md` dan `commands/clarify.md` |
| 8 Bangun | `reference/interaction-design.md`, `reference/responsive-design.md`, `commands/adapt.md` |
| 9 Verifikasi | `commands/audit.md`, `commands/critique.md`, `commands/polish.md`, `commands/optimize.md` |

## Perintah perbaikan

Dipanggil setelah ada halaman. Tiap file berisi langkah lengkapnya.

| Gejala | Buka |
|---|---|
| Terlihat bland, aman, tidak berkesan | `commands/bolder.md` |
| Terlalu ramai, terlalu keras, melelahkan | `commands/quieter.md` |
| Terlalu banyak elemen, tidak fokus | `commands/distill.md` |
| Fungsional tapi hambar, tanpa kepribadian | `commands/delight.md` |
| Terlalu abu-abu, tanpa warna | `commands/colorize.md` |
| Spasi dan hierarki lemah, grid monoton | `commands/layout.md` |
| Font dan hierarki teks bermasalah | `commands/typeset.md` |
| Teks UI membingungkan | `commands/clarify.md` |
| Rusak di ukuran layar tertentu | `commands/adapt.md` |
| Lambat atau patah | `commands/optimize.md` |
| Perlu penilaian menyeluruh dengan skor | `commands/critique.md` dan `commands/audit.md` |
| Pemeriksaan akhir sebelum rilis | `commands/polish.md` |
| Ingin melewati batas biasa (shader, fisika pegas) | `commands/overdrive.md` |

## Cara membaca teks Impeccable di sini

Salinannya tidak diubah, jadi teksnya masih menyebut `/impeccable`, `/shape`, `.impeccable.md`. Bacalah sebagai berikut.

- `/impeccable` berarti `vendor/impeccable/SKILL.md`.
- `/shape`, `/critique`, `/audit` dan seterusnya berarti file dengan nama itu di `vendor/impeccable/commands/`.
- `reference/xxx.md` di dalam teks berarti `vendor/impeccable/reference/xxx.md`.
- Tautan relatif yang rusak bukan kesalahan isi, hanya karena struktur folder berbeda dari aslinya.
- Aturan "wajib jalankan teach" dipenuhi oleh brief di langkah 0 web-unslop. Kalau proyek sudah punya `.impeccable.md`, pakai itu sebagai isi brief dan jangan wawancara ulang.

## Kalau dua aturan bertabrakan

| Topik | Yang menang | Alasan |
|---|---|---|
| Em dash | web-unslop | Larangan mutlak, dicek mesin |
| Bahasa dan register copy | web-unslop (`references/copy.md`) | Disesuaikan ke pemilik, Impeccable menulis untuk konteks Inggris |
| Daftar font tolak | Gabungan keduanya. Linter memuat daftar Impeccable dan daftar tambahan dari pengamatan | Lebih banyak refleks tertangkap |
| Urutan kerja | web-unslop | Satu jalur lebih mudah dipatuhi daripada tiga mode |
| Kedalaman aturan per bidang | Impeccable | Referensinya lebih panjang |
| Ketegasan "tidak ada pengecualian" pada bans CSS | Impeccable. Side stripe dan gradient text adalah larangan tanpa pengecualian | Sudah selaras dengan linter |

Kalau tetap bimbang, pilih aturan yang lebih ketat, lalu catat keputusannya di komentar bukti.

## Menambah pembaruan upstream

Salinan ini snapshot. Untuk memperbarui: ganti isi `vendor/impeccable/` dengan rilis baru, perbarui nomor versi di `NOTICE.md`, jalankan `python3 tests/test_lint.py`. Linter melewati folder `vendor/` jadi tidak ikut diperiksa.
