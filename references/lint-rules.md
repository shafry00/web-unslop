# Rule linter

`python3 scripts/unslop_lint.py PATH...`. FAIL membuat kode keluar 1. WARN hanya melaporkan, kecuali `--strict`.

Folder `vendor/` dilewati saat memindai direktori.

Ekstensi yang diperiksa penuh: `.html .htm .css .jsx .tsx .js .ts .vue .svelte .astro`. Teks saja: `.md .txt`. Aturan struktur (`identical-cards`, `html-lang`, `viewport`, `img-alt`, dan sejenisnya) hanya berjalan pada `.html` dan `.htm`.

| Rule | Level | Yang dicari |
|---|---|---|
| `em-dash` | FAIL | Karakter U+2014 di file apa pun, termasuk komentar. Juga ` -- ` di antara kata pada kode dan teks. |
| `hype-copy` | FAIL | Frasa pengisi tak ambigu, placeholder (`Lorem ipsum`, `John Doe`) |
| `hype-copy-maybe` | WARN | Kata yang kadang sah (`terbaik`, `journey`, `robust`, `leverage`, dan sejenisnya) |
| `generic-cta` | FAIL / WARN | Teks tombol atau tautan generik. `click here` FAIL, sisanya WARN |
| `hype-emoji` | FAIL | Emoji dekoratif tertentu (sparkles, roket, bohlam, api, petir, target, bintang) |
| `emoji` | WARN | Emoji lain di teks |
| `rule-of-three` | WARN | Judul h1 atau h2 berpola tiga kata sifat |
| `contrast-structure` | WARN | `bukan hanya X tapi Y`, `not just X but Y`, `it's not X, it's Y` |
| `round-stat` | WARN | `10,000+`, `5K+` |
| `exclamation` | WARN | Tiga tanda seru atau lebih |
| `gradient-text` | FAIL | `background-clip: text` dengan gradien, atau `bg-clip-text text-transparent` |
| `ai-gradient` | FAIL | Gradien yang memuat hue ungu bersama biru, cyan, atau pink (CSS dan Tailwind) |
| `side-stripe` | FAIL | `border-left` atau `border-right` lebih dari 1px, `border-l-2/4/8` |
| `reflex-font` | FAIL | Font refleks gelombang pertama di posisi pertama `font-family` |
| `reflex-font-2` | WARN | Font refleks gelombang kedua |
| `system-font` | WARN | Font sistem di posisi pertama |
| `single-family` | WARN | Hanya satu keluarga font bernama |
| `too-many-families` | WARN | Lebih dari tiga keluarga |
| `pure-black-white` | WARN | `#000`, `#fff`, `black`, `white` sebagai warna |
| `cream-terracotta` | WARN | Krem hangat dan terakota dalam satu file |
| `dark-teal` | WARN | Halaman gelap dengan aksen teal atau emerald |
| `dark-glow` | WARN | Bayangan glow berwarna blur 24px ke atas di halaman gelap |
| `blur-blob` | WARN | `filter: blur(40px)` ke atas |
| `glassmorphism` | WARN | `backdrop-filter` atau `backdrop-blur` tiga kali atau lebih |
| `transition-all` | WARN | `transition: all`, `transition-all` |
| `default-easing` | WARN | Ada gerak tapi tidak ada `cubic-bezier`, `linear()`, atau kurva bernama |
| `reduced-motion` | FAIL | Ada animasi tanpa `prefers-reduced-motion` |
| `center-everything` | WARN | Enam kali `text-align: center` atau `text-center` |
| `heading-cadence` | WARN | Separuh judul atau lebih berpola "X, lalu Y" (minimal dua dari tiga judul) |
| `accent-last-word` | WARN | Kata terakhir h1 atau h2 dibungkus em, span, mark, i, b, atau strong |
| `placeholder-left` | WARN | `[ISI: ...]` masih ada di teks |
| `hard-shadow` | WARN | `box-shadow` offset bukan nol dengan blur 0 |
| `uniform-section-padding` | WARN | Empat section atau lebih, hanya satu aturan padding generik, kurang dari dua override |
| `skeleton-landing` | WARN | h1, FAQ accordion tiga atau lebih, dan tabel atau daftar bernomor tiga item |
| `identical-cards` | FAIL | Tiga saudara identik berisi ikon, judul, dan paragraf |
| `identical-cards-plain` | WARN | Tiga saudara identik berisi judul dan paragraf |
| `html-lang` | FAIL | `<html>` tanpa `lang` |
| `viewport` | FAIL | Tidak ada meta viewport |
| `charset` | WARN | Tidak ada meta charset |
| `title` | WARN | Tidak ada `<title>` |
| `meta-description` | WARN | Tidak ada meta description |
| `h1-count` | WARN | Jumlah `<h1>` bukan satu |
| `img-alt` | FAIL | `<img>` tanpa `alt` |
| `focus-style` | WARN | Ada elemen interaktif tanpa gaya fokus |
| `outline-none` | FAIL | `outline: none` tanpa `:focus-visible` |

## Hook

`hooks/web-unslop-gate.py` menjalankan linter yang sama pada hasil akhir `Write` dan `Edit` (untuk `Edit`, `old_string` diterapkan ke file di disk lebih dulu). Exit 2 memblokir dan mengirim alasannya ke model. File `.html .htm .css .jsx .tsx .vue .svelte .astro` diperiksa. Untuk file selain HTML, rule yang butuh gambaran seluruh halaman (`reduced-motion`, `default-easing`, `single-family`, `too-many-families`, `cream-terracotta`, `dark-teal`, `focus-style`) dilewati. Folder `vendor/` dan `node_modules/` dilewati.

Variabel lingkungan: `WEB_UNSLOP_STRICT=1` membuat WARN ikut memblokir. `WEB_UNSLOP_REQUIRE_MARKER=1` mewajibkan komentar bukti pada halaman ber-`<h1>`.

Batasan hook: hanya berjalan bila hook aktif. Mematikan semua hook, atau mode izin yang melewati hook, menonaktifkannya tanpa pemberitahuan. Isi komentar bukti tetap tidak bisa diverifikasi.

## Batasan

- Berbasis pola. Variasi teknis yang tidak terantisipasi bisa lolos, dan beberapa WARN bisa salah alarm.
- Kontras warna tidak dihitung karena nilainya sering lewat variabel CSS.
- Isi komentar bukti tidak bisa diverifikasi mesin. Hanya manusia yang bisa mengaudit kejujurannya.
- Linter tidak menilai komposisi, ritme, atau apakah ada pusat perhatian. Itu bagian dari uji slop manual.
- Deteksi kartu identik memakai struktur HTML saudara, jadi komponen yang dirender lewat JavaScript tidak terjangkau.

## Menambah rule

Tambahkan pengecekan di `check_file()`, satu entri di tabel ini, dan satu kasus di `tests/test_lint.py` yang gagal bila rule dihapus. Rule baru tidak boleh menggagalkan `examples/lolos-linter/bengkel-jam/index.html` tanpa alasan.
