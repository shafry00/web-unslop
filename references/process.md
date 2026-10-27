# Proses

## Template brief

Salin, isi, simpan di samping proyek (`BRIEF.md`). Kolom yang tidak diketahui ditanyakan, bukan dikarang.

```
Pembaca       : siapa, perangkat, situasi (terburu, santai, curiga)
Tindakan      : satu hal yang harus terjadi setelah membaca
Merek         : tiga kata sifat
Benda fisik   : satu benda yang mewakili ketiganya
Bukti nyata   : angka, foto, nama, tarif, alamat, kutipan asli yang tersedia
Referensi     : tiga halaman yang disukai + alasan spesifik
Batasan       : bahasa, merek yang ada, tema, anggaran performa
Dial          : VARIANCE _ / MOTION _ / DENSITY _  (alasan satu kalimat)
Satu pusat    : elemen yang akan diperbesar jadi pusat perhatian
```

## Wireframe

Tingkat 1: kotak ASCII. Tingkat 2: HTML abu-abu polos bila struktur multi-section rumit. Tingkat 3: konten asli. Jangan melompat ke tingkat 3.

```
+------------------------------------------------------+
| nama                                      [kontak]   |
+------------------------------------------------------+
| HEADLINE BESAR (kol 1-9)               ( ornamen )   |
| subkalimat (kol 1-6)                                 |
| [ CTA ]                    alamat + jam (kol 8-12)   |
+------------------------------------------------------+
| tabel tarif: pekerjaan | waktu | harga               |
+------------------------------------------------------+
| 1  langkah                                           |
|      2  langkah                                      |
|          3  langkah                                  |
+------------------------------------------------------+
| FAQ details x3                                       |
+------------------------------------------------------+
```

Teknik Crazy Eights untuk eksplorasi cepat: gambar delapan variasi struktur dalam delapan menit, pilih satu. Variasi pertama hampir selalu struktur default.

Lewati wireframe untuk komponen tunggal (tombol, kartu). Wajib untuk landing page, dashboard, dan formulir multi-langkah.

## Komentar bukti

Taruh di dekat atas file. Hook `hooks/web-unslop-gate.py` dengan `WEB_UNSLOP_REQUIRE_MARKER=1` menolak halaman ber-`<h1>` yang komentarnya tidak ada atau kolomnya kosong (component, brief, wireframe, layout, font, warna, gerak, copy). Isi hanya hal yang benar-benar dikerjakan. Tujuannya agar pemilik bisa mengaudit keputusan tanpa menebak.

```html
<!-- web-unslop
component: referensi komponen yang dilihat, atau "tidak ada yang relevan karena X, dibangun manual"
brief   : pembaca, tindakan, benda fisik (satu baris)
dial    : VARIANCE 7 / MOTION 4 / DENSITY 4
wireframe: struktur kasar yang dipikirkan dulu
layout  : kenapa komposisi ini dan apa pusat perhatiannya
font    : nama + alasan yang menunjuk ke subjek
warna   : sumber palet (detail fisik apa)
gerak   : satu momen yang dipilih dan kenapa
copy    : register + sapuan yang paling banyak mengubah teks
-->
```

Sebutkan ringkasan yang sama ke pemilik di chat. Komentar tersembunyi saja tidak cukup.

## Perintah linter

```bash
python3 scripts/unslop_lint.py halaman.html          # satu file
python3 scripts/unslop_lint.py src/ --strict         # satu folder, WARN ikut menggagalkan
python3 scripts/unslop_lint.py . --json              # keluaran mesin
python3 scripts/unslop_lint.py x.html --ignore single-family,focus-style
```

Hasil: `file:baris: LEVEL rule: pesan`. Kode keluar 0 bila tidak ada FAIL (atau tidak ada temuan dengan `--strict`), 1 bila ada, 2 bila argumen salah.

Menekan satu temuan: tulis `unslop-ok` di baris yang sama, lalu catat alasan di komentar bukti. Di `.md` dan `.txt`, frasa di dalam backtick atau blok kode tidak diperiksa, jadi dokumen boleh mengutip frasa terlarang.

## Tangkapan layar

Peramban headless membaca file lokal langsung, tanpa server dan tanpa login.

```bash
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"   # macOS
# Linux: google-chrome atau chromium

"$CHROME" --headless=new --disable-gpu --hide-scrollbars \
  --window-size=1280,2400 --virtual-time-budget=4000 \
  --screenshot=/tmp/desktop.png "file:///jalur/absolut/halaman.html"

"$CHROME" --headless=new --disable-gpu --hide-scrollbars \
  --window-size=500,3000 --virtual-time-budget=4000 \
  --screenshot=/tmp/sempit.png "file:///jalur/absolut/halaman.html"
```

Catatan jujur: pada Chrome headless versi baru, `--window-size` lebar di bawah sekitar 500 piksel dipaksa naik. Emulasi lewat CDP juga tidak andal di semua lingkungan. Jadi 500px adalah lebar sempit yang bisa diuji andal, dan itu cukup menangkap masalah struktural: teks terpotong, elemen menumpuk, scroll horizontal. Uji lebar 390px asli di perangkat atau DevTools bila halaman kritis.

Yang dicari di tangkapan layar:

1. Teks terpotong atau meluber di tepi.
2. Flex atau grid yang menumpuk, bukan membungkus.
3. Spasi antar kata yang hilang (kasus nyata: isi `' '` pada `span.inline-block` menciut jadi nol lebar, pakai ` `).
4. Karakter non-ASCII yang rusak ("mojibake") saat dibuka lewat `file://`, tanda `<meta charset="UTF-8">` hilang.
5. Ornamen yang menimpa teks di lebar sempit.
6. Mode gelap dan terang keduanya terbaca (`--force-dark-mode` tidak cukup, uji dengan `prefers-color-scheme` di DevTools).

Ulangi sampai bersih.

## Uji slop

Tanya dengan jujur, dalam urutan ini.

1. Kalau seseorang diberi tahu "ini buatan AI", apakah mereka langsung percaya? Apa yang membuat mereka percaya?
2. Telusuri tiap bagian di `references/tells.md` terhadap halaman. Tandai yang ada.
3. Apakah ada satu elemen yang berani, atau semuanya aman?
4. Apakah tiap keputusan di komentar bukti menunjuk ke subjek, atau hanya ke selera umum?
5. Apakah ada klaim, angka, atau testimoni yang tidak punya sumber?
6. Apakah halaman ini bisa tertukar dengan halaman dari subjek lain hanya dengan mengganti teks? Kalau bisa, ia belum dirancang.
7. Apakah semua judul berirama sama, dan semua jarak antar section sama? Hitung, jangan menebak.
8. Apakah kerangkanya sama dengan halaman lain yang pernah kamu buat? Bandingkan urutan section satu baris.

Jawab tiap pertanyaan tertulis di laporan dengan bukti (kutipan judul, nilai padding, urutan section). "Sudah" tanpa bukti dihitung gagal.

## Laporan akhir ke pemilik

Satu paragraf pendek: keputusan terbesar dan alasannya, hasil linter, hal yang diuji dan hal yang belum, serta apa yang perlu diisi pemilik (foto asli, angka asli, nomor kontak). Jangan menyatakan "bebas dari tell AI". Katakan apa yang diperiksa.
