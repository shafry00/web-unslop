# Katalog tell

Tiap entri: apa yang terlihat, kenapa terbaca AI, dan pengganti. Kolom "Linter" menyebut rule yang menandainya, `-` berarti hanya bisa dinilai manusia.

Frasa yang dilarang ditulis di dalam backtick supaya linter tidak menandai dokumen ini sendiri.

## Tipografi

| Tell | Kenapa terbaca AI | Ganti dengan | Linter |
|---|---|---|---|
| Inter, Roboto, Open Sans, Arial, Helvetica di posisi pertama | Font default hampir semua keluaran model | Font yang dipilih lewat uji benda fisik (references/typography.md) | `reflex-font` |
| Space Grotesk, Poppins, Montserrat, Playfair Display, DM Sans | Pilihan "agak beda" yang diulang model | Sama | `reflex-font` |
| Fraunces, Outfit, Plus Jakarta Sans, Manrope, Sora, Lexend, Syne, Bricolage Grotesque, Instrument Serif, Cormorant, Lora | Pengganti gelombang kedua setelah dilarang memakai daftar pertama | Sama. Boleh dipakai kalau alasannya menunjuk ke subjek | `reflex-font-2` |
| Satu keluarga font untuk semuanya | Tidak ada keputusan hierarki | Display + body yang berkontras | `single-family` |
| Font sistem sebagai pilihan utama | Tidak ada keputusan | Font yang di-embed | `system-font` |
| Monospace untuk semua label "biar teknis" | Jalan pintas kesan developer | Monospace hanya untuk kode dan data bertabel | - |
| Hierarki datar, ukuran antar tingkat berdekatan | Semua teks sama penting | Rasio minimal 1.25, ekstrem pada judul | - |
| Teks isi huruf kapital panjang | Sulit dibaca | Kapital hanya untuk label pendek | - |
| Baris lebih dari 80 karakter | Mata kehilangan jejak | `max-width: 62ch` | - |

## Warna

| Tell | Kenapa terbaca AI | Ganti dengan | Linter |
|---|---|---|---|
| Gradien ungu ke biru atau cyan atau pink | Palet default model sejak 2023 | Warna turunan subjek, solid | `ai-gradient` |
| Latar gelap + aksen teal atau emerald | Kombinasi "terlihat teknis" yang paling umum | Aksen dari detail fisik subjek | `dark-teal` |
| Glow neon di latar gelap | Terlihat keren tanpa keputusan | Hapus, atau pakai cahaya yang punya sumber jelas | `dark-glow` |
| Teks bergradien | Dekoratif, bukan bermakna | Satu warna solid, tekankan lewat bobot | `gradient-text` |
| Krem hangat + terakota untuk subjek yang tidak berhubungan | Refleks "hangat dan personal" | Warna yang berasal dari subjek. Untuk skincare atau wellness asli, krem memang konvensi sah | `cream-terracotta` |
| `#000` dan `#fff` murni | Tidak ada di alam, terasa mentah | Hitam dan putih yang diberi tint ke hue palet | `pure-black-white` |
| Abu-abu di atas latar berwarna | Terlihat pudar | Pakai tingkat terang atau gelap dari warna latar itu sendiri | - |
| Blob buram sebagai hiasan latar | Pengisi ruang kosong | Hapus, atau ganti elemen yang punya makna | `blur-blob` |
| Semua warna di tingkat sedang | Tidak ada komitmen | Satu warna pekat dominan, satu aksen | - |

## Layout dan komponen

| Tell | Kenapa terbaca AI | Ganti dengan | Linter |
|---|---|---|---|
| Tiga kartu identik: ikon + judul + dua baris teks | Bentuk fitur-grid yang diulang di setiap landing page AI | Daftar bernomor, tabel, kolom editorial, ukuran berbeda | `identical-cards` |
| Semua rata tengah | Template default | Rata kiri, komposisi asimetris | `center-everything` |
| Garis aksen tebal di sisi kiri kartu atau callout | Sentuhan "desain" paling sering dipakai di dashboard | Border penuh, tint latar, angka di depan, atau tanpa indikator | `side-stripe` |
| Kartu di dalam kartu | Kebisingan visual | Ratakan hierarki | - |
| Semua dibungkus kartu | Wadah menggantikan struktur | Biarkan konten bernapas di atas latar | - |
| Ikon besar berpojok bulat di atas tiap judul | Dekorasi templat | Hapus, atau pakai angka atau data nyata | - |
| Pola metrik: angka raksasa, label kecil, tiga statistik, aksen gradien | Hero metric template | Satu angka yang benar dengan konteks dan sumber | - |
| Glassmorphism di mana-mana | Dekorasi, bukan fungsi | Satu permukaan kaca yang punya alasan (misalnya header di atas foto) | `glassmorphism` |
| Sparkline sebagai hiasan | Terlihat canggih tanpa isi | Grafik yang menjawab pertanyaan, atau hapus | - |
| Bayangan jatuh generik pada persegi membulat | Aman dan tidak berkesan | Bentuk dan elevasi yang konsisten dengan sistem | - |
| Modal untuk semua hal | Malas mencari alternatif | Inline, halaman sendiri, atau popover | - |
| Pil "Baru" atau "Beta" di atas judul hero | Lencana pengisi | Hapus | - |
| Padding section sama di semua bagian | Ritme otomatis | Ritme yang bervariasi | `uniform-section-padding` |
| Kerangka hero + tabel atau langkah + FAQ + penutup | Urutan bawaan, tidak berasal dari isi | Tes kerangka di references/layout.md | `skeleton-landing` |
| Tombol berbayangan keras tanpa blur | Gaya neo-brutalist yang menyebar lewat template | Tombol datar atau bayangan yang punya sumber cahaya | `hard-shadow` |
| Angka 1, 2, 3 raksasa berwarna aksen dan digeser | Langkah bernomor versi dekoratif | Nomor kecil sejajar teks, atau urutan yang tampil dari isi | - |
| Ornamen SVG besar sebagai gimmick (jam, cap, kompas) di pojok hero | Dekorasi yang menggantikan isi | Foto atau gambar nyata dari subjek | - |
| Hero satu warna penuh, teks krem, satu CTA terang | Kombinasi hero paling umum | Komposisi yang berasal dari subjek | - |
| Keterangan kecil abu-abu di bawah semua baris dan gambar | Pengisi hierarki | Keterangan hanya bila perlu | - |
| Semua elemen berukuran sedang | Tidak ada pusat perhatian | Satu elemen diperbesar jadi pusat | - |

## Gerak

| Tell | Ganti dengan | Linter |
|---|---|---|
| `transition: all` | Sebut properti yang berubah | `transition-all` |
| Semua easing bawaan browser | `cubic-bezier` yang punya karakter | `default-easing` |
| Fade-up setiap section saat scroll, durasi sama | Satu momen gerak yang berarti | - |
| Animasi tanpa penanganan gerak berkurang | `prefers-reduced-motion` | `reduced-motion` |
| Animasi `width`, `height`, `top`, `left` | `transform` dan `opacity` | - |
| Parallax dan partikel tanpa tujuan | Hapus | - |

## Copy

Frasa di bawah ditulis di dalam backtick karena dokumen ini sendiri diperiksa linter.

| Tell | Contoh | Ganti dengan | Linter |
|---|---|---|---|
| Tanda pisah em dash | kalimat dengan tanda pisah panjang | Koma, titik, kata sambung | `em-dash` |
| Superlatif kosong | `solusi terbaik`, `terpercaya`, `dijamin`, `revolusioner` | Klaim yang bisa dibuktikan | `hype-copy` |
| Pengisi bahasa Inggris | `seamless`, `cutting-edge`, `next-level`, `game-changer`, `unlock`, `elevate`, `supercharge`, `streamline`, `delve`, `tapestry`, `unleash` | Kata kerja konkret tentang apa yang terjadi | `hype-copy` |
| Pembuka kosong | `dalam dunia yang serba cepat`, `di era digital ini`, `in today's fast-paced world` | Mulai dari fakta | `hype-copy` |
| Tiga sifat berjajar | `cepat, mudah, terpercaya` | Satu klaim dengan bukti | `rule-of-three` |
| Struktur kontras | `bukan hanya A, tapi juga B`, `not just A, but B` | Tulis langsung B | `contrast-structure` |
| CTA generik | `Get Started`, `Learn More`, `Klik di sini`, `Mulai sekarang`, `Submit` | Aksi persis yang terjadi | `generic-cta` |
| Angka bulat berplus tanpa sumber | `10,000+ pengguna` | Angka asli dengan sumber, atau hapus | `round-stat` |
| Emoji hiasan | sparkles, roket, bohlam | Hapus | `hype-emoji`, `emoji` |
| Tanda seru beruntun | tiga atau lebih | Satu pun jarang perlu | `exclamation` |
| Teks placeholder tertinggal | `Lorem ipsum`, `John Doe`, `Your Company` | Isi nyata | `hype-copy` |
| Testimoni karangan dengan nama generik | foto stok + kutipan sempurna | Kutipan asli dengan izin, atau tidak ada bagian testimoni | - |
| Kalimat berpola simetris berulang | tiga kalimat pendek dengan ritme sama | Panjang kalimat bervariasi | - |
| Semua judul berpola "X, lalu Y" | Irama seragam | Judul bervariasi (references/copy.md) | `heading-cadence` |
| Kata terakhir judul diwarnai | `<h1>Jam mati belum tentu <em>rusak.</em></h1>` | Satu warna | `accent-last-word` |
| Angka, harga, dan syarat karangan yang terdengar spesifik | Spesifik palsu | Fakta dari pemilik, atau `[ISI: ...]` | `placeholder-left` bila belum diisi |

## Teknis dan aksesibilitas

| Tell | Linter |
|---|---|
| `<html>` tanpa `lang` | `html-lang` |
| Tanpa `<meta name="viewport">` | `viewport` |
| Tanpa `<meta charset>` | `charset` |
| `<img>` tanpa `alt` | `img-alt` |
| `outline: none` tanpa pengganti fokus | `outline-none` |
| Elemen interaktif tanpa gaya fokus | `focus-style` |
| Nol atau lebih dari satu `<h1>` | `h1-count` |
| Tanpa `<title>` atau meta description | `title`, `meta-description` |
| Kontras warna kurang dari 4.5:1 | tidak dicek mesin, hitung manual (references/color.md) |
