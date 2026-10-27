# Library warna

Kumpulan swatch siap pakai, dikelompokkan per keluarga hue. Dua sumber awalnya: lembar swatch "Trend Color Guide Palette" (perkiraan tren warna pastel dan netral) dan bagan warna karya seniman NinjahMonki untuk ilustrasi karakter (disampel per piksel). Nilai hex adalah fakta warna, bukan karya yang dilindungi, tetapi kredit sumber tetap dicantumkan.

## Kapan dipakai

Ini **opsi B** untuk langkah warna. Opsi A (utama) di `references/color.md` menurunkan palet dari detail fisik subjek. Pakai library ini bila:

- subjek tidak punya detail fisik yang bisa diturunkan (alat internal, produk digital murni), atau
- pemilik meminta nuansa pastel atau lembut, atau
- butuh titik awal cepat yang tetap bisa dipertanggungjawabkan.

Cara pakai: pilih empat sampai enam warna dari keluarga hue yang paling dekat dengan subjek. Satu menjadi dominan, satu aksen, sisanya netral. Tulis di komentar bukti keluarga mana yang dipilih dan kenapa.

## Batasan yang jujur

- Library didominasi tingkat terang tinggi. Satu-satunya warna gelap adalah `#302E30`. Untuk tinta atau teks berkontras tinggi di atas latar pastel, `#302E30` sering sudah cukup. Bila tidak, pakai netral gelap kustom bernuansa hue dominan dan sebutkan di komentar bukti.
- Pastel di atas latar gelap sering gagal kontras. Hitung rasionya (`references/color.md`).
- Krem hangat dan terakota dari library ini mudah jatuh ke tell `cream-terracotta`. Cek ulang bila kombinasi itu muncul.
- Library bukan daftar pilihan untuk diulang di setiap proyek. Kalau dua proyek berturut-turut memakai swatch yang sama, kembali ke opsi A.

## Swatch

**Pink/rose (soft → vivid):**
`#B4AEDD` `#DCC9E8` `#E9D7E8` `#F5DCE4` `#FBECEF` `#F1E4EF` `#EFD6E0` `#fcc4c4` `#eeb6b6` `#e08c8c` `#d29a9a` `#d27e7e` `#E0498A` `#D14F97` `#e00e54` `#ee62a8` `#e08ca8` `#d27e9a` `#E8317F`

**Coral/peach:**
`#F2A0A0` `#EFB4BE` `#E2685A` `#F3C9A0` `#F2C6D2` `#D3667F` `#E2917E` `#F0947E` `#F2CB98` `#C79488` `#D3A8A4` `#fcd2c4` `#fce0d2` `#fcc4a8` `#fcb67e` `#ee9a54` `#eea89a` `#eeb6a8`

**Yellow/cream/neutral pucat:**
`#F5EA8C` `#F0E2A8` `#F0DE7E` `#F1E8B0` `#F5DE9C` `#E8D6CE` `#EDE7DD` `#D6C7BE` `#fce0c4` `#fceee0` `#fce0a8` `#fceea8` `#fceec4` `#eed27e` `#fcfcc4` `#eeeec4`

**Lime/yellow-green:**
`#E6E79A` `#DCE9A0` `#eeee9a` `#d2d2a8` `#eefcc4` `#e0eec4` `#e0fcc4` `#d2eeb6` `#c4eea8`

**Green/sage/emerald:**
`#A9D6BB` `#B8D69A` `#7FCB9E` `#A9DBC7` `#79C9A4` `#D2DECA` `#d2fcc4` `#a8e09a` `#c4fcc4` `#c4eec4` `#8ce08c` `#c4fcd2` `#b6eec4` `#7ee0a8`

**Teal/mint:**
`#7FD1CB` `#86DCD0` `#c4fce0` `#b6e0d2` `#9ac4b6` `#7ed2b6` `#c4fcee` `#7ec4b6` `#8cd2c4` `#c4fcfc`

**Sky/cyan/pale blue:**
`#C9DDF2` `#C7DCF2` `#CFE0F5` `#7FCDE0` `#5FA9C4` `#D6E0E2` `#e0fcfc` `#c4eeee` `#a8e0ee` `#b6eefc` `#c4eefc` `#7eb6d2` `#9ad2ee` `#8cc4ee`

**Blue/periwinkle:**
`#C7CBE0` `#C4D3F0` `#92AEE0` `#B6BEE0` `#c4e0fc` `#7ea8d2` `#46709a` `#9ac4ee` `#7ea8ee` `#c4d2ee` `#7e9ad2` `#c4d2fc` `#7e8cd2` `#7e8ce0`

**Purple/lavender:**
`#8E93D6` `#8382C9` `#DAC3D4` `#DDC7E0` `#c4c4fc` `#7e7ec4` `#7e7ed2` `#c4c4ee` `#8c7ed2` `#8c7ec4` `#d2c4fc` `#d2c4ee` `#a88ce0` `#9a7ed2`

**Magenta/orchid:**
`#e0c4fc` `#c49ae0` `#e0c4ee` `#fcc4fc` `#eec4ee` `#d270d2` `#d2a8d2` `#eea8ee` `#ee62d2`

**Dusty/muted (skin-tone & neutral ramps):**
`#C79A9E` `#B79A97` `#8B6E78` `#c47e9a` `#e08ca8` `#b67e9a` `#c47ea8` `#b67ea8` `#d27e8c`

**Dark/neutral (satu-satunya warna gelap di library):**
`#302E30`: charcoal-hitam, satu-satunya opsi kontras tinggi dari dalam library. Butuh lebih gelap berarti keluar library.
