# web-unslop

Skill untuk agen AI (Claude Code, Cursor, OpenCode, dan sejenisnya) supaya halaman web yang dihasilkan tidak terbaca sebagai buatan AI. Satu repo berisi alur kerja, katalog tell, linter dan hook yang bisa dijalankan, riset referensi, library warna, dan salinan utuh Impeccable.

Halaman hasil AI punya sidik jari yang sama: Inter atau Space Grotesk, gradien ungu ke biru, tiga kartu berikon, semua rata tengah, dan kalimat seperti `solusi terbaik` atau `seamless`. Skill ini melarang pilihan-pilihan itu dan, lebih penting, melarang menggantinya dengan refleks berikutnya.

## Isi

| Bagian | Fungsi |
|---|---|
| `SKILL.md` | Alur sepuluh langkah: brief, dial, wireframe, tipografi, warna, layout, gerak, copy, bangun, verifikasi |
| `references/tells.md` | Katalog tell lengkap dengan pengganti, per kategori |
| `references/typography.md` `color.md` `layout.md` `motion.md` `copy.md` | Detail tiap bidang |
| `references/process.md` | Template brief, wireframe, komentar bukti, perintah screenshot, uji slop |
| `references/research.md` | Riset komponen (21st.dev dan koleksi terbuka), gerak, dan sembilan lensa komposisi |
| `references/palette-library.md` | Swatch per keluarga hue sebagai opsi warna kedua |
| `references/impeccable-map.md` | Cara Impeccable dan web-unslop dipakai bersama, dan siapa yang menang saat bertabrakan |
| `vendor/impeccable/` | Salinan utuh Impeccable v2.1.1: SKILL.md, 9 referensi, 16 perintah perbaikan. Apache-2.0 |
| `hooks/web-unslop-gate.py` | Hook PreToolUse yang menolak penulisan halaman yang gagal linter |
| `scripts/unslop_lint.py` | Linter tanpa dependensi, Python 3 saja |
| `examples/bengkel-jam/` | Halaman contoh utuh yang lolos linter |
| `tests/test_lint.py` | Tes yang membuktikan tiap rule benar-benar mendeteksi |

## Pasang

Claude Code:

```bash
git clone https://github.com/shafry00/web-unslop ~/.claude/skills/web-unslop
```

Agen lain: salin isi repo ke folder skill atau instruksi proyek, dan arahkan agen ke `SKILL.md`.

## Pakai

Saat meminta agen membuat atau mengedit halaman, skill otomatis relevan. Untuk memanggil eksplisit: "pakai web-unslop".

Linter bisa dijalankan sendiri, tanpa agen:

```bash
python3 scripts/unslop_lint.py halaman.html
python3 scripts/unslop_lint.py src/ --strict
```

Contoh keluaran:

```
bad.html:2: FAIL reflex-font: font refleks `inter` di posisi pertama. Pilih lewat prosedur di references/typography.md.
bad.html:3: FAIL gradient-text: teks bergradien (background-clip:text). Pakai satu warna solid, tekankan lewat bobot atau ukuran.
bad.html:4: FAIL side-stripe: garis aksen tebal di sisi kiri/kanan kartu. Pakai border penuh, tint latar, atau angka/ikon di depan.
bad.html:12: FAIL hype-copy: frasa kosong `seamless`. Ganti klaim spesifik (angka, mekanisme, hasil).

37 temuan pada sampel buruk dari tests/test_lint.py
```

Daftar rule dan batasannya ada di `references/lint-rules.md`.

### Hook penegak (opsional)

Hook menjalankan linter yang sama pada hasil akhir `Write` dan `Edit`, lalu memblokir bila ada FAIL. Tambahkan ke `~/.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [{ "type": "command", "command": "python3 ~/.claude/skills/web-unslop/hooks/web-unslop-gate.py" }]
      }
    ]
  }
}
```

Variabel opsional: `WEB_UNSLOP_STRICT=1` (WARN ikut memblokir) dan `WEB_UNSLOP_REQUIRE_MARKER=1` (halaman ber-`<h1>` wajib membawa komentar bukti). Hook tidak berjalan bila hook dimatikan atau mode izin melewatinya.

## Prinsip

1. **Jangan tukar satu refleks dengan refleks lain.** Daftar font terlarang yang pendek hanya memindahkan refleks ke font berikutnya. Karena itu skill ini memberi prosedur memilih, bukan daftar pilihan.
2. **Setiap keputusan menunjuk ke subjek.** Font dari benda cetak yang mewakili merek. Warna dari detail fisik tempatnya. Copy dari angka dan syarat nyata.
3. **Satu pusat perhatian.** Halaman yang terlihat dirancang berkomitmen pada satu pilihan besar. Halaman yang semuanya berukuran sedang terbaca otomatis.
4. **Mesin menangkap pola, manusia menilai selera.** Linter hanya syarat minimal.

## Batasan yang perlu diketahui

- Lolos linter tidak menjamin halaman bagus. Linter tidak melihat komposisi, ritme, atau kualitas foto.
- Daftar font refleks dan frasa terlarang bersifat berbasis pengamatan dan akan menua. Tambahkan lewat PR.
- Rule berbasis regex dan struktur HTML saudara. Komponen yang dirender lewat JavaScript tidak terjangkau deteksi kartu identik.
- Kontras warna tidak dihitung otomatis. Rumusnya ada di `references/color.md`.
- Isi komentar bukti di halaman tidak bisa diverifikasi mesin.

## Tes

```bash
python3 examples/bengkel-jam/build.py   # membangun index.html dari template + font
python3 tests/test_lint.py
```

Tes memeriksa tiga hal: tiap rule menangkap sampel buruk (sampel ditulis sebagai string di dalam tes, jadi repo tidak memuat halaman buruk), contoh bengkel jam bersih, dan dokumen di repo ini sendiri lolos linter.

## Sumber ide

Teks di luar `vendor/` ditulis ulang, tetapi gagasannya berutang pada karya terbuka berikut:

- [impeccable](https://github.com/pbakaus/impeccable) (pbakaus): disertakan utuh di `vendor/`. Daftar larangan CSS, uji slop, dan prosedur memilih font di bagian utama berangkat dari sini.
- [taste-skill](https://github.com/Leonxlnx/taste-skill): inferensi brief dan tiga dial.
- [anti-slop-writing](https://github.com/adenaufal/anti-slop-writing): larangan kosakata dan tanda pisah.
- [marketingskills](https://github.com/coreyhaines31/marketingskills): tujuh sapuan copy editing.

Repo pendamping untuk teks non-halaman: [unslop](https://github.com/shafry00/unslop).

## Lisensi

MIT untuk semua kecuali dua bagian:

- `vendor/impeccable/` adalah karya Paul Bakaus, Apache-2.0, disalin tanpa perubahan. Lisensi dan pemberitahuan ada di folder itu.
- Font contoh di `examples/bengkel-jam/fonts/` berlisensi SIL OFL 1.1.

Library warna di `references/palette-library.md` menyebut sumber swatchnya.
