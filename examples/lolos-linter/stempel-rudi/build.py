#!/usr/bin/env python3
"""Embed the fonts into template.html and write a self-contained index.html."""
import base64, pathlib

here = pathlib.Path(__file__).parent
b64 = lambda p: base64.b64encode((here / "fonts" / p).read_bytes()).decode()
html = (here / "template.html").read_text(encoding="utf-8")
html = html.replace("__ALFA__", b64("AlfaSlabOne-Regular.woff2")).replace("__KARLA__", b64("Karla-Regular.ttf"))
(here / "index.html").write_text(html, encoding="utf-8")
print("index.html", len(html) // 1024, "KB")
