#!/usr/bin/env python3
"""web-unslop linter.

Mechanical checks for the most recognizable AI design and copy tells.
It catches patterns, it does not judge taste. Passing is the floor, not the goal.

usage:
  unslop_lint.py [--strict] [--json] [--ignore RULE,RULE] PATH...

exit code: 0 clean, 1 at least one FAIL (or any WARN with --strict), 2 usage error.

Suppress one line with the token `unslop-ok` anywhere on that line.
In .md/.txt files, inline code spans and fenced code blocks are skipped by the
phrase rules, so docs can quote banned phrases in backticks.
"""
import argparse
import colorsys
import json
import os
import re
import sys
from html.parser import HTMLParser

CODE_EXT = {".html", ".htm", ".css", ".jsx", ".tsx", ".js", ".ts", ".vue", ".svelte", ".astro"}
HTML_EXT = {".html", ".htm"}
TEXT_EXT = {".md", ".txt"}
SKIP_DIRS = {"node_modules", ".git", "dist", "build", ".next", "__pycache__", "vendor"}

FAIL, WARN = "FAIL", "WARN"

# ---------------------------------------------------------------- word lists

# First-family fonts that are the default of every model. FAIL tier.
REFLEX_FONTS_FAIL = {
    "inter", "roboto", "open sans", "arial", "helvetica", "helvetica neue",
    "space grotesk", "poppins", "montserrat", "playfair display", "dm sans",
    "lato", "segoe ui",
}
# Second-wave reflexes: the font a model picks after being told to avoid the first list. WARN tier.
REFLEX_FONTS_WARN = {
    "fraunces", "outfit", "plus jakarta sans", "manrope", "sora", "lexend",
    "syne", "bricolage grotesque", "instrument serif", "cormorant garamond",
    "lora", "raleway", "nunito", "work sans", "geist", "jetbrains mono",
    "ibm plex sans", "source sans pro", "source sans 3", "urbanist",
    "figtree", "onest", "schibsted grotesk", "newsreader", "crimson",
    "crimson pro", "crimson text", "ibm plex mono", "ibm plex serif",
    "space mono", "dm serif display", "dm serif text", "instrument sans",
}
SYSTEM_FONTS = {"system-ui", "-apple-system", "blinkmacsystemfont", "ui-sans-serif", "sans-serif", "serif", "monospace"}

# Unambiguous filler. FAIL tier.
HYPE_FAIL = [
    "revolusioner", "solusi terbaik", "terpercaya", "dijamin", "buruan",
    "hari ini juga", "tanpa ribet", "cepat dan mudah", "mudah dan cepat",
    "cepat, mudah", "mudah, cepat", "dalam dunia yang serba cepat",
    "di era digital ini", "di era digital", "satu atap", "solusi lengkap",
    "one-stop solution", "seamless", "seamlessly", "cutting-edge",
    "state-of-the-art", "next-level", "next level", "game-changer",
    "game changer", "game-changing", "revolutionize", "revolutionary",
    "unlock the power", "elevate your", "supercharge", "streamline",
    "delve", "tapestry", "unleash", "in today's fast-paced",
    "in today’s fast-paced", "ever-evolving", "world-class", "best-in-class",
    "all-in-one platform", "blazing fast", "blazing-fast", "lightning-fast",
    "reimagine", "built for the future", "take it to the next level",
    "lorem ipsum", "john doe", "jane doe", "your company", "company name",
]
# Words with legitimate uses. WARN tier, a human decides.
HYPE_WARN = [
    "terbaik", "inovatif", "berkualitas tinggi", "sepenuh hati", "robust",
    "holistic", "effortless", "effortlessly", "journey", "perjalanan",
    "empower", "leverage", "unlock", "transform your", "acme",
]
GENERIC_CTA_FAIL = ["click here", "klik di sini", "klik disini"]
GENERIC_CTA_WARN = [
    "get started", "learn more", "read more", "submit", "sign up now",
    "mulai sekarang", "coba sekarang", "selengkapnya", "baca selengkapnya",
    "daftar sekarang", "contact us", "hubungi kami",
]
HYPE_EMOJI = "✨🚀💡🔥⚡🎯🌟💯🤩"
EMOJI_RE = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F000-\U0001F2FF\U00002B00-\U00002BFF]"
)

CONTRAST_STRUCTURES = [
    r"bukan\s+(?:hanya|sekadar|sekedar|cuma)\s+[^.!?\n]{1,70}?,?\s*(?:tapi|tetapi|melainkan)",
    r"\bnot\s+just\s+[^.!?\n]{1,70}?,?\s*but\b",
    r"\bit['’]s\s+not\s+[^.!?\n]{1,50}?,\s*it['’]s\b",
    r"\bmore\s+than\s+just\s+a\b",
    r"\bnot\s+only\s+[^.!?\n]{1,70}?\s+but\s+also\b",
]

# ---------------------------------------------------------------- helpers


class Finding:
    def __init__(self, path, line, level, rule, msg):
        self.path, self.line, self.level, self.rule, self.msg = path, line, level, rule, msg

    def as_dict(self):
        return {"file": self.path, "line": self.line, "level": self.level, "rule": self.rule, "message": self.msg}

    def __str__(self):
        return f"{self.path}:{self.line}: {self.level} {self.rule}: {self.msg}"


def line_of(text, idx):
    return text.count("\n", 0, idx) + 1


def find_line(raw, needle):
    i = raw.lower().find(needle.lower())
    return line_of(raw, i) if i >= 0 else 1


def strip_markup(raw):
    t = re.sub(r"<!--.*?-->", " ", raw, flags=re.S)
    t = re.sub(r"<(script|style)\b.*?</\1>", " ", t, flags=re.S | re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    return t


def strip_md_code(raw):
    t = re.sub(r"```.*?```", " ", raw, flags=re.S)
    t = re.sub(r"~~~.*?~~~", " ", t, flags=re.S)
    t = re.sub(r"`[^`\n]*`", " ", t)
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
    return t


def has_word(text, phrase):
    pat = r"(?<![\w-])" + re.escape(phrase) + r"(?![\w-])"
    return re.search(pat, text, flags=re.I)


def parse_colors(s):
    """Return list of (hue 0-360, saturation 0-1, lightness 0-1)."""
    out = []
    for m in re.finditer(r"#([0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{4}|[0-9a-fA-F]{3})\b", s):
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h[:3])
        r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
        hh, ll, ss = colorsys.rgb_to_hls(r, g, b)
        out.append((hh * 360, ss, ll))
    for m in re.finditer(r"rgba?\(\s*(\d+)[\s,]+(\d+)[\s,]+(\d+)", s):
        r, g, b = (min(255, int(x)) / 255 for x in m.groups())
        hh, ll, ss = colorsys.rgb_to_hls(r, g, b)
        out.append((hh * 360, ss, ll))
    for m in re.finditer(r"hsla?\(\s*([\d.]+)(?:deg)?[\s,]+([\d.]+)%[\s,]+([\d.]+)%", s):
        out.append((float(m.group(1)) % 360, float(m.group(2)) / 100, float(m.group(3)) / 100))
    for m in re.finditer(r"oklch\(\s*([\d.]+)(%?)\s+([\d.]+)\s+([\d.]+)", s):
        L = float(m.group(1)) / (100 if m.group(2) else 1)
        out.append((float(m.group(4)) % 360, min(1.0, float(m.group(3)) / 0.2), L))
    return out


def gradients(text):
    """Yield (index, inner) for each CSS gradient, balancing parentheses."""
    for m in re.finditer(r"(?:repeating-)?(?:linear|radial|conic)-gradient\(", text):
        i, depth = m.end(), 1
        while i < len(text) and depth:
            depth += {"(": 1, ")": -1}.get(text[i], 0)
            i += 1
        yield m.start(), text[m.end():i - 1]


def css_blocks(text):
    for m in re.finditer(r"\{([^{}]*)\}", text):
        yield m.start(), m.group(1)


# ---------------------------------------------------------------- html tree


VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}


class Node:
    def __init__(self, tag, attrs, line, parent):
        self.tag, self.attrs, self.line, self.parent = tag, dict(attrs), line, parent
        self.children, self.texts = [], []

    def walk(self):
        for c in self.children:
            yield c
            yield from c.walk()

    @property
    def cls(self):
        return tuple((self.attrs.get("class") or "").split())


class Tree(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#root", [], 1, None)
        self.cur = self.root

    def handle_starttag(self, tag, attrs):
        n = Node(tag, attrs, self.getpos()[0], self.cur)
        self.cur.children.append(n)
        if tag not in VOID:
            self.cur = n

    def handle_startendtag(self, tag, attrs):
        self.cur.children.append(Node(tag, attrs, self.getpos()[0], self.cur))

    def handle_endtag(self, tag):
        n = self.cur
        while n is not None and n.tag != tag:
            n = n.parent
        if n is not None and n.parent is not None:
            self.cur = n.parent

    def handle_data(self, data):
        self.cur.texts.append(data)


# ---------------------------------------------------------------- checks


def check_file(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        return check_text(path, f.read())


def check_text(path, raw):
    """Lint `raw` as if it lived at `path` (extension picks the rule set)."""
    ext = os.path.splitext(path)[1].lower()
    F = []
    is_code = ext in CODE_EXT
    is_html = ext in HTML_EXT
    is_text = ext in TEXT_EXT

    def add(level, rule, idx_or_line, msg, by_index=True):
        line = line_of(raw, idx_or_line) if by_index else idx_or_line
        F.append(Finding(path, line, level, rule, msg))

    # ---- universal: em dash, anywhere in the file, comments included
    for m in re.finditer("\\u2014", raw):
        add(FAIL, "em-dash", m.start(), "tanda pisah em dash (U+2014). Ganti koma, titik, atau kata sambung.")
    for m in re.finditer(r"(?<=\w) -- (?=\w)", raw):
        if is_code or is_text:
            add(FAIL, "em-dash", m.start(), "dobel strip dipakai sebagai em dash. Ganti koma atau titik.")

    # ---- copy rules
    if is_text:
        visible = strip_md_code(raw)
    elif is_code:
        visible = strip_markup(raw)
    else:
        visible = ""
    if visible:
        for p in HYPE_FAIL:
            if has_word(visible, p):
                add(FAIL, "hype-copy", find_line(raw, p) , f"frasa kosong `{p}`. Ganti klaim spesifik (angka, mekanisme, hasil).", by_index=False)
        for p in HYPE_WARN:
            if has_word(visible, p):
                add(WARN, "hype-copy-maybe", find_line(raw, p), f"`{p}` sering jadi pengisi. Pertahankan hanya kalau ada bukti di kalimatnya.", by_index=False)
        if is_code:
            for p in GENERIC_CTA_FAIL + GENERIC_CTA_WARN:
                pat = r">\s*" + re.escape(p) + r"\s*[!.]?\s*<"
                m = re.search(pat, raw, flags=re.I)
                if m:
                    lvl = FAIL if p in GENERIC_CTA_FAIL else WARN
                    add(lvl, "generic-cta", m.start(), f"CTA generik `{p}`. Tulis aksi persis yang terjadi saat diklik.")
        for pat in CONTRAST_STRUCTURES:
            m = re.search(pat, visible, flags=re.I)
            if m:
                add(WARN, "contrast-structure", find_line(raw, m.group(0)[:25]), "struktur 'bukan X tapi Y' / 'not just X but Y'. Tulis langsung klaim Y.", by_index=False)
                break
        if visible.count("!") >= 3:
            add(WARN, "exclamation", 1, f"{visible.count('!')} tanda seru. Satu pun jarang perlu.", by_index=False)
        for ch in HYPE_EMOJI:
            if ch in visible:
                add(FAIL, "hype-emoji", find_line(raw, ch), f"emoji {ch} sebagai dekorasi. Hapus.", by_index=False)
                break
        else:
            m = EMOJI_RE.search(visible)
            if m:
                add(WARN, "emoji", find_line(raw, m.group(0)), "emoji di teks. Pakai hanya kalau brand voice meminta.", by_index=False)
        if re.search(r"\b\d{1,3}(?:[.,]\d{3})+\+|\b\d+\s?[KkMm]\+", visible):
            add(WARN, "round-stat", 1, "angka bulat berplus (10,000+ / 5K+). Pakai angka asli beserta sumbernya, atau hapus.", by_index=False)
        for m in re.finditer(r"<h[12][^>]*>(.*?)</h[12]>", raw, flags=re.S | re.I):
            t = strip_markup(m.group(1)).strip()
            w = r"[\w'’-]+"
            if re.search(rf"\b{w},\s+{w},?\s+(?:dan|and|&|atau|or)\s+{w}\b", t, flags=re.I) or re.fullmatch(rf"{w},\s*{w},\s*{w}[.!]?", t):
                add(WARN, "rule-of-three", m.start(), f"judul berpola tiga kata sifat: \"{t[:60]}\". Pilih satu klaim yang bisa dibuktikan.")

        if is_code:
            if re.search(r"\[ISI:", visible):
                add(WARN, "placeholder-left", find_line(raw, "[ISI:"), "placeholder [ISI: ...] belum diisi. Isi dengan fakta nyata dari pemilik sebelum rilis.", by_index=False)
            heads = [strip_markup(m.group(2)).strip() for m in re.finditer(r"<h([1-3])\b[^>]*>(.*?)</h\1>", raw, flags=re.S | re.I)]
            two = [h for h in heads if re.match(r"^[^,]{3,45},\s+\S", h)]
            if len(heads) >= 3 and len(two) >= 2 and len(two) * 2 >= len(heads):
                add(WARN, "heading-cadence", find_line(raw, two[0][:20]), f"{len(two)} dari {len(heads)} judul berpola 'X, lalu Y'. Irama seragam terbaca otomatis. Variasikan panjang dan bentuk judul.", by_index=False)
            for m in re.finditer(r"<h([12])\b[^>]*>(.*?)</h\1>", raw, flags=re.S | re.I):
                if re.search(r"\S[^<]*<(em|span|mark|i|b|strong)\b[^>]*>[^<]{1,40}</\1>\s*[.!?]?\s*$", m.group(2).strip()):
                    add(WARN, "accent-last-word", m.start(), "kata terakhir judul diberi warna atau gaya aksen. Tell yang sangat umum. Biarkan judul satu warna.")

    if not is_code:
        return _suppress(F, raw)

    # ---- CSS / style rules
    for idx, body in css_blocks(raw):
        low = body.lower()
        if re.search(r"background-clip\s*:\s*text", low) and "gradient" in low:
            add(FAIL, "gradient-text", idx, "teks bergradien (background-clip:text). Pakai satu warna solid, tekankan lewat bobot atau ukuran.")
        elif re.search(r"text-fill-color\s*:\s*transparent", low) and "gradient" in low:
            add(FAIL, "gradient-text", idx, "teks bergradien (text-fill-color transparent). Pakai warna solid.")
        for m in re.finditer(r"border-(?:left|right|inline-start|inline-end)\s*:\s*(\d+(?:\.\d+)?)(px|rem|em)", low):
            w = float(m.group(1)) * (16 if m.group(2) != "px" else 1)
            if w > 1:
                add(FAIL, "side-stripe", idx, "garis aksen tebal di sisi kiri/kanan kartu. Pakai border penuh, tint latar, atau angka/ikon di depan.")
        for m in re.finditer(r"border-(?:left|right|inline-start|inline-end)-width\s*:\s*(\d+(?:\.\d+)?)px", low):
            if float(m.group(1)) > 1:
                add(FAIL, "side-stripe", idx, "garis aksen tebal di sisi kiri/kanan. Ganti struktur elemen.")

    for m in re.finditer(r"(?<![\w:-])border-[lr]-(?:2|4|8)\b(?!/)", raw):
        add(FAIL, "side-stripe", m.start(), "Tailwind border-l/r tebal sebagai garis aksen. Ganti struktur elemen.")

    # class attr checks (Tailwind and friends)
    for m in re.finditer(r'class(?:Name)?\s*=\s*["\'{`]([^"\'`}]*)', raw):
        cl = m.group(1)
        if "bg-clip-text" in cl and "text-transparent" in cl:
            add(FAIL, "gradient-text", m.start(), "Tailwind teks bergradien (bg-clip-text + text-transparent). Pakai warna solid.")
        if re.search(r"from-(?:purple|violet|indigo|fuchsia)-\d+", cl) and re.search(r"(?:to|via)-(?:blue|cyan|pink|sky|indigo|purple|fuchsia|violet|rose)-\d+", cl):
            add(FAIL, "ai-gradient", m.start(), "gradien ungu ke biru/pink. Warna default model. Turunkan palet dari subjek.")
        if "transition-all" in cl:
            add(WARN, "transition-all", m.start(), "transition-all menganimasi semua properti. Sebut properti yang berubah.")

    # gradients: purple + blue/cyan/pink
    for idx, inner in gradients(raw):
        cols = [c for c in parse_colors(inner) if c[1] > 0.25 and 0.1 < c[2] < 0.95]
        hues = [c[0] for c in cols]
        purple = any(255 <= h <= 320 for h in hues)
        other = any(180 <= h < 255 for h in hues) or any(320 < h <= 350 for h in hues)
        if purple and other:
            add(FAIL, "ai-gradient", idx, "gradien ungu ke biru/cyan/pink. Warna default model. Turunkan palet dari subjek.")

    # colors / palette
    all_cols = parse_colors(raw)
    bg_cols = []
    for m in re.finditer(r"background(?:-color)?\s*:\s*([^;}{]+)", raw, flags=re.I):
        if "gradient" not in m.group(1).lower():
            bg_cols += parse_colors(m.group(1))
    page_dark = bool(bg_cols) and any(c[2] < 0.12 for c in bg_cols) and not any(c[2] > 0.85 for c in bg_cols)
    cream = any(25 <= h <= 50 and 0.2 <= s <= 0.75 and l > 0.88 for h, s, l in all_cols)
    terracotta = any(8 <= h <= 25 and s > 0.4 and 0.35 <= l <= 0.6 for h, s, l in all_cols)
    if cream and terracotta:
        add(WARN, "cream-terracotta", 0, "krem hangat + terakota. Refleks model untuk 'hangat/personal'. Pertahankan hanya kalau subjek memang menuntutnya, dan tulis alasannya.")
    if page_dark:
        if any(150 <= h <= 195 and s > 0.45 and 0.3 <= l <= 0.7 for h, s, l in all_cols):
            add(WARN, "dark-teal", 0, "latar gelap + aksen teal/emerald. Kombinasi paling umum dari model. Pilih aksen dari subjek.")
        for m in re.finditer(r"(?:box|text)-shadow\s*:[^;}]*?\b0\s+0\s+(\d+)px([^;}]*)", raw, flags=re.I):
            if int(m.group(1)) >= 24 and any(c[1] > 0.5 for c in parse_colors(m.group(2))):
                add(WARN, "dark-glow", m.start(), "glow neon berwarna di latar gelap. Tampak keren tanpa keputusan desain.")
                break
    for m in re.finditer(r"filter\s*:\s*blur\((\d+)px\)", raw, flags=re.I):
        if int(m.group(1)) >= 40:
            add(WARN, "blur-blob", m.start(), "blob buram sebagai dekorasi latar. Hapus atau ganti elemen yang punya makna.")
            break
    pure = re.findall(r"(?:^|[;{\s])(?:color|background|background-color|border-color|fill)\s*:\s*(#000(?:000)?|#fff(?:fff)?|black|white)\s*[;}\n]", raw, flags=re.I)
    if pure:
        add(WARN, "pure-black-white", 0, f"{len(pure)}x hitam/putih murni. Beri tint sedikit ke hue palet.")
    if len(re.findall(r"backdrop-filter\s*:|backdrop-blur", raw)) >= 3:
        add(WARN, "glassmorphism", 0, "backdrop-filter dipakai 3x atau lebih. Glass untuk dekorasi, bukan fungsi.")

    for m in re.finditer(r"box-shadow\s*:\s*(?!inset)(-?\d+(?:\.\d+)?)px\s+(-?\d+(?:\.\d+)?)px\s+0(?:px)?\s+[^;,}]+[;}]", raw, flags=re.I):
        if float(m.group(1)) or float(m.group(2)):
            add(WARN, "hard-shadow", m.start(), "bayangan keras tanpa blur (gaya neo-brutalist) sering dipakai untuk tombol. Pastikan itu keputusan merek, bukan kebiasaan.")
            break

    # typography
    fams = []
    for m in re.finditer(r"font-family\s*:\s*([^;}{]+)", raw, flags=re.I):
        stack = [s.strip().strip("'\"").lower() for s in m.group(1).split(",")]
        stack = [s for s in stack if s and not s.startswith("var(")]
        if not stack:
            continue
        first = stack[0]
        fams.append(first)
        if first in REFLEX_FONTS_FAIL:
            add(FAIL, "reflex-font", m.start(), f"font refleks `{first}` di posisi pertama. Pilih lewat prosedur di references/typography.md.")
        elif first in REFLEX_FONTS_WARN:
            add(WARN, "reflex-font-2", m.start(), f"`{first}` adalah pilihan gelombang kedua yang juga sering muncul. Pastikan dipilih dari subjek.")
        elif first in SYSTEM_FONTS:
            add(WARN, "system-font", m.start(), "font sistem di posisi pertama. Tidak ada keputusan tipografi di sini.")
    named = {f for f in fams if f not in SYSTEM_FONTS and not f.startswith("var(")}
    if fams and len(named) == 1 and len(fams) >= 2:
        add(WARN, "single-family", 0, "hanya satu keluarga font dipakai. Pasangkan display dengan body kecuali itu pilihan sadar.")
    if len(named) > 3:
        add(WARN, "too-many-families", 0, f"{len(named)} keluarga font. Maksimal tiga.")

    # motion
    has_motion = bool(re.search(r"@keyframes|animation\s*:|transition\s*:|animate-|transition-", raw))
    for m in re.finditer(r"transition\s*:\s*all\b", raw, flags=re.I):
        add(WARN, "transition-all", m.start(), "transition: all menganimasi semua properti. Sebut properti yang berubah.")
    if has_motion and not re.search(r"cubic-bezier\(|linear\(|spring|ease-(?:out|in)-(?:quad|cubic|quart|quint|expo|circ)", raw):
        add(WARN, "default-easing", 0, "semua gerak pakai easing bawaan browser. Tulis cubic-bezier yang punya karakter.")
    if has_motion and not re.search(r"prefers-reduced-motion|motion-reduce:", raw):
        add(FAIL, "reduced-motion", 0, "ada animasi tapi tidak ada @media (prefers-reduced-motion: reduce).")

    # layout heuristics
    centers = len(re.findall(r"text-align\s*:\s*center", raw, flags=re.I)) + len(re.findall(r"(?<![\w-])text-center\b", raw))
    if centers >= 6:
        add(WARN, "center-everything", 0, f"{centers}x teks rata tengah. Rata kiri dengan komposisi asimetris terbaca lebih dirancang.")

    # accessibility and document basics (html only)
    if is_html:
        if re.search(r"<html\b", raw, flags=re.I):
            if not re.search(r"<html\b[^>]*\blang\s*=", raw, flags=re.I):
                add(FAIL, "html-lang", 0, "<html> tanpa atribut lang.", by_index=True)
            if not re.search(r'<meta[^>]+name=["\']viewport', raw, flags=re.I):
                add(FAIL, "viewport", 0, "tidak ada <meta name=viewport>. Halaman rusak di ponsel.")
            if not re.search(r"<meta[^>]+charset", raw, flags=re.I):
                add(WARN, "charset", 0, "tidak ada <meta charset>. Karakter non-ASCII bisa rusak di file://.")
            if not re.search(r"<title>\s*\S", raw, flags=re.I):
                add(WARN, "title", 0, "tidak ada <title>.")
            if not re.search(r'<meta[^>]+name=["\']description', raw, flags=re.I):
                add(WARN, "meta-description", 0, "tidak ada meta description.")
            h1 = len(re.findall(r"<h1\b", raw, flags=re.I))
            if h1 != 1:
                add(WARN, "h1-count", 0, f"{h1} elemen <h1>. Harus tepat satu.")
        for m in re.finditer(r"<img\b[^>]*>", raw, flags=re.I):
            if not re.search(r"\balt\s*=", m.group(0), flags=re.I):
                add(FAIL, "img-alt", m.start(), "<img> tanpa alt. Isi deskripsi, atau alt=\"\" kalau dekoratif.")
        if re.search(r"<(?:button|a|input|select|textarea)\b", raw, flags=re.I) and not re.search(r":focus-visible|:focus\b|focus:", raw):
            add(WARN, "focus-style", 0, "elemen interaktif tanpa gaya :focus-visible.")
        if re.search(r"outline\s*:\s*(?:none|0)\b", raw, flags=re.I) and not re.search(r":focus-visible", raw):
            add(FAIL, "outline-none", 0, "outline dimatikan tanpa pengganti :focus-visible.")

        # one padding for every section, and the stock landing skeleton
        secs = re.findall(r"<section\b([^>]*)>", raw, flags=re.I)
        if len(secs) >= 4:
            ids = [i for sec in secs for i in re.findall(r"""\bid\s*=\s*["']([\w-]+)""", sec)]
            pad = [(sel.strip().splitlines()[-1].strip() if sel.strip() else "", body)
                   for sel, body in re.findall(r"([^{}]+)\{([^{}]*)\}", raw) if re.search(r"padding(?:-block|-top|-bottom)?\s*:", body)]
            generic = [sel for sel, _ in pad if re.fullmatch(r"(?:main\s*>\s*)?section|\.section", sel)]
            over = [sel for sel, _ in pad if sel not in generic and ("section" in sel or any("#" + i in sel for i in ids))]
            if generic and len(over) < 2:
                add(WARN, "uniform-section-padding", 0, "semua section memakai padding yang sama. Ritme spasi yang sama terbaca otomatis. Variasikan, misalnya rapat, sedang, lega.")
        n_li = max((len(re.findall(r"<li\b", m.group(0), flags=re.I)) for m in re.finditer(r"<ol\b.*?</ol>", raw, flags=re.S | re.I)), default=0)
        if len(re.findall(r"<details\b", raw, flags=re.I)) >= 3 and (re.search(r"<table\b", raw, flags=re.I) or n_li >= 3) and re.search(r"<h1\b", raw, flags=re.I):
            add(WARN, "skeleton-landing", 0, "kerangka hero + tabel atau langkah + FAQ accordion. Itu kerangka bawaan semua landing page AI. Pastikan struktur berasal dari isi, bukan dari kebiasaan (references/layout.md, tes kerangka).")

        # identical feature cards
        tree = Tree()
        try:
            tree.feed(raw)
        except Exception:
            pass
        _cards(tree.root, F, path)
    else:
        if re.search(r"outline\s*:\s*(?:none|0)\b", raw, flags=re.I) and not re.search(r":focus-visible|focus-visible:", raw):
            add(FAIL, "outline-none", 0, "outline dimatikan tanpa pengganti :focus-visible.")

    return _suppress(F, raw)


def _cards(root, F, path):
    def descendants(n):
        return list(n.walk())

    def has_icon(n):
        for d in [n] + descendants(n):
            if d.tag in ("svg", "img", "i"):
                return True
            if any("icon" in c.lower() for c in d.cls):
                return True
        text = "".join(n.texts).strip() or "".join("".join(d.texts) for d in descendants(n)).strip()
        return bool(text) and bool(EMOJI_RE.match(text[0]))

    def is_card(n):
        tags = {d.tag for d in descendants(n)}
        return bool(tags & {"h2", "h3", "h4", "h5"}) and "p" in tags

    for parent in [root] + list(root.walk()):
        groups = {}
        for c in parent.children:
            if c.tag in ("div", "li", "article", "section", "a") and (c.cls or c.tag in ("li", "article")):
                groups.setdefault((c.tag, c.cls), []).append(c)
        for (tag, cls), members in groups.items():
            if len(members) >= 3 and all(is_card(m) for m in members):
                if all(has_icon(m) for m in members):
                    F.append(Finding(path, parent.line, FAIL, "identical-cards", f"{len(members)} kartu identik (ikon + judul + teks). Pakai daftar bernomor, tabel, atau kolom editorial dengan ritme berbeda."))
                else:
                    F.append(Finding(path, parent.line, WARN, "identical-cards-plain", f"{len(members)} blok identik (judul + teks). Cek apakah isinya memang sejenis, kalau tidak variasikan ukuran dan bentuk."))
                break


def _suppress(F, raw):
    lines = raw.splitlines()
    out = []
    for f in F:
        if 1 <= f.line <= len(lines) and "unslop-ok" in lines[f.line - 1]:
            continue
        out.append(f)
    return out


# ---------------------------------------------------------------- cli


def iter_files(paths):
    for p in paths:
        if os.path.isdir(p):
            for d, dirs, files in os.walk(p):
                dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
                for fn in sorted(files):
                    if os.path.splitext(fn)[1].lower() in CODE_EXT | TEXT_EXT:
                        yield os.path.join(d, fn)
        elif os.path.isfile(p):
            yield p
        else:
            print(f"tidak ditemukan: {p}", file=sys.stderr)
            sys.exit(2)


def main(argv=None):
    ap = argparse.ArgumentParser(description="web-unslop linter")
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--strict", action="store_true", help="WARN ikut menggagalkan (exit 1)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--ignore", default="", help="daftar rule dipisah koma")
    a = ap.parse_args(argv)
    ignore = {x.strip() for x in a.ignore.split(",") if x.strip()}
    findings = []
    for f in iter_files(a.paths):
        findings += [x for x in check_file(f) if x.rule not in ignore]
    findings.sort(key=lambda x: (x.path, x.line, x.level))
    if a.json:
        print(json.dumps([x.as_dict() for x in findings], ensure_ascii=False, indent=2))
    else:
        for x in findings:
            print(x)
        nf = sum(x.level == FAIL for x in findings)
        nw = sum(x.level == WARN for x in findings)
        print(f"\n{nf} FAIL, {nw} WARN", file=sys.stderr)
    bad = any(x.level == FAIL for x in findings) or (a.strict and findings)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
