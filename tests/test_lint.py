#!/usr/bin/env python3
"""Run: python3 tests/test_lint.py

Bad samples live as strings here and are written to a temp dir at runtime,
so the repo never ships a deliberately slop-filled page.
"""
import importlib.util
import os
import pathlib
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("unslop_lint", ROOT / "scripts" / "unslop_lint.py")
lint = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lint)

BAD_HTML = """<html><head><style>
body { font-family: 'Inter', sans-serif; background: #0b0f14; color: #fff; text-align: center; }
h1 { background: linear-gradient(90deg, #7c3aed, #06b6d4); -webkit-background-clip: text; color: transparent; }
.card { border-left: 4px solid #14b8a6; box-shadow: 0 0 40px rgba(20, 184, 166, 0.6); transition: all 0.3s ease; backdrop-filter: blur(12px); }
.g2 { backdrop-filter: blur(8px); } .g3 { backdrop-filter: blur(8px); }
.blob { filter: blur(80px); }
button { outline: none; animation: pulse 2s infinite; }
@keyframes pulse { 50% { opacity: .5; } }
.a{text-align:center}.b{text-align:center}.c{text-align:center}.d{text-align:center}.e{text-align:center}
</style></head><body>
<h1>Cepat, Mudah, Terpercaya</h1>
<p>Solusi terbaik untuk bisnis Anda \u2014 seamless dan revolusioner! Bukan hanya alat, tapi partner. Dijamin!</p>
<p>Dipercaya 10,000+ pengguna \u2728</p>
<div class="grid">
<div class="card"><svg></svg><h3>Cepat</h3><p>Lorem ipsum dolor.</p></div>
<div class="card"><svg></svg><h3>Aman</h3><p>Lorem ipsum dolor.</p></div>
<div class="card"><svg></svg><h3>Mudah</h3><p>Lorem ipsum dolor.</p></div>
</div>
<img src="hero.png"><button>Get Started</button><a href="#">Click here</a>
</body></html>"""

BAD_TAILWIND = """<h1 class="bg-gradient-to-r from-purple-500 to-blue-500 bg-clip-text text-transparent">x</h1>
<div class="border-l-4 transition-all">y</div>"""

BAD_CSS_VARS = """<!doctype html><html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width">
<title>t</title><meta name="description" content="d"><style>
body{background:#f4ead8;font-family:"Fraunces",serif} .x{color:#c2603e}
</style></head><body><h1>t</h1></body></html>"""

EXPECT = {
    "reflex-font", "gradient-text", "side-stripe", "dark-glow", "transition-all",
    "glassmorphism", "blur-blob", "outline-none", "reduced-motion", "center-everything",
    "em-dash", "hype-copy", "contrast-structure", "round-stat", "hype-emoji", "rule-of-three",
    "identical-cards", "img-alt", "html-lang", "viewport", "generic-cta", "dark-teal",
    "pure-black-white", "default-easing",
}


def rules(path):
    return {f.rule for f in lint.check_file(path)}


def main():
    with tempfile.TemporaryDirectory() as d:
        p = pathlib.Path(d)
        (p / "bad.html").write_text(BAD_HTML, encoding="utf-8")
        (p / "tw.html").write_text(BAD_TAILWIND, encoding="utf-8")
        (p / "vars.html").write_text(BAD_CSS_VARS, encoding="utf-8")
        got = rules(p / "bad.html")
        missing = EXPECT - got
        assert not missing, f"bad.html: rule tidak terdeteksi: {sorted(missing)}"
        tw = rules(p / "tw.html")
        assert {"ai-gradient", "gradient-text", "side-stripe", "transition-all"} <= tw, f"tailwind: {tw}"
        v = rules(p / "vars.html")
        assert {"reflex-font-2", "cream-terracotta"} <= v, f"vars: {v}"

        # suppression token
        (p / "ok.html").write_text(BAD_TAILWIND.replace('class="border-l-4', 'class="border-l-4 unslop-ok"'), encoding="utf-8")
        assert "side-stripe" not in rules(p / "ok.html")

        # markdown: quoted phrases in code spans are ignored, bare ones are not
        (p / "a.md").write_text("Hindari `seamless` dan `revolusioner`.\n", encoding="utf-8")
        assert not rules(p / "a.md"), rules(p / "a.md")
        (p / "b.md").write_text("Produk ini seamless.\n", encoding="utf-8")
        assert "hype-copy" in rules(p / "b.md")
        (p / "c.md").write_text("Satu kalimat \u2014 dua klausa.\n", encoding="utf-8")
        assert "em-dash" in rules(p / "c.md")

    good = ROOT / "examples" / "bengkel-jam" / "index.html"
    assert good.exists(), "jalankan examples/bengkel-jam/build.py dulu"
    g = lint.check_file(str(good))
    assert not g, "contoh bagus harus bersih: " + "; ".join(map(str, g))

    own = []
    for f in lint.iter_files([str(ROOT)]):
        if "/tests/" in f:
            continue
        own += [x for x in lint.check_file(f) if x.level == lint.FAIL]
    assert not own, "repo ini sendiri harus lolos: " + "; ".join(map(str, own))
    print("semua tes lolos")


if __name__ == "__main__":
    main()
