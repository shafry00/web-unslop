#!/usr/bin/env python3
"""Embed fonts and Wiku images into template.html and write a self-contained index.html.
The swirl path is generated here, same spiral as uns.ai.id."""
import base64, math, pathlib

here = pathlib.Path(__file__).parent
b64 = lambda p: base64.b64encode((here / p).read_bytes()).decode()

def spiral(c=200, R=180, turns=3.2, n=240):
    pts = []
    for i in range(n + 1):
        t = i / n * turns * 2 * math.pi
        r = R * i / n
        pts.append((c + r * math.cos(t), c + r * math.sin(t)))
    return "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)

html = (here / "template.html").read_text(encoding="utf-8")
for k, f in {
    "__MONT800__": "fonts/Montserrat-800.woff2", "__MONT600__": "fonts/Montserrat-600.woff2",
    "__LATO400__": "fonts/Lato-400.woff2", "__LATO700__": "fonts/Lato-700.woff2",
    "__SILK__": "fonts/Silkscreen-400.woff2", "__WK__": "img/wiku-hero.webp", "__PEEK__": "img/wiku-peek.webp",
}.items():
    html = html.replace(k, b64(f))
html = html.replace("__SWIRL__", spiral())
(here / "index.html").write_text(html, encoding="utf-8")
print("index.html", len(html) // 1024, "KB")
