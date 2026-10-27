#!/usr/bin/env python3
"""Claude Code PreToolUse hook: block Write/Edit of a page that fails web-unslop.

Install (settings.json):
  {"hooks": {"PreToolUse": [{"matcher": "Write|Edit",
    "hooks": [{"type": "command", "command": "python3 /path/to/web-unslop/hooks/web-unslop-gate.py"}]}]}}

Env:
  WEB_UNSLOP_STRICT=1          WARN also blocks
  WEB_UNSLOP_REQUIRE_MARKER=1  page with an <h1> must carry a `<!-- web-unslop ... -->` evidence comment

For Edit the hook applies old_string -> new_string to the file on disk first, so it
judges the file as it will exist, not as it is now.
Exit 2 blocks the tool call and feeds stderr back to the model.
"""
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("unslop_lint", os.path.join(HERE, "..", "scripts", "unslop_lint.py"))
lint = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lint)

PAGE_EXT = {".html", ".htm", ".css", ".jsx", ".tsx", ".vue", ".svelte", ".astro"}
# whole-page heuristics make no sense on a fragment such as a lone stylesheet or component
FRAGMENT_SKIP = {"reduced-motion", "default-easing", "single-family", "too-many-families",
                 "cream-terracotta", "dark-teal", "focus-style"}
MARKER_FIELDS = ("component", "brief", "wireframe", "layout", "font", "warna", "gerak", "copy")


def resulting_text(tool, ti, path):
    if tool == "Write":
        return ti.get("content")
    if tool == "Edit":
        try:
            with open(path, encoding="utf-8", errors="replace") as f:
                cur = f.read()
        except OSError:
            return None
        old, new = ti.get("old_string", ""), ti.get("new_string", "")
        if not old or old not in cur:
            return None
        return cur.replace(old, new) if ti.get("replace_all") else cur.replace(old, new, 1)
    return None


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0
    ti = data.get("tool_input") or {}
    path = ti.get("file_path") or ""
    ext = os.path.splitext(path)[1].lower()
    if ext not in PAGE_EXT or "/vendor/" in path or "/node_modules/" in path:
        return 0
    text = resulting_text(data.get("tool_name"), ti, path)
    if text is None:
        return 0

    strict = os.environ.get("WEB_UNSLOP_STRICT") == "1"
    found = lint.check_text(path, text)
    if ext not in lint.HTML_EXT:
        found = [f for f in found if f.rule not in FRAGMENT_SKIP]
    blocking = [f for f in found if f.level == lint.FAIL or (strict and f.level == lint.WARN)]

    problems = [f"{f.level} {f.rule} (baris {f.line}): {f.msg}" for f in blocking]
    if os.environ.get("WEB_UNSLOP_REQUIRE_MARKER") == "1" and re.search(r"<h1\b", text, re.I):
        m = re.search(r"<!--\s*web-unslop\b(.*?)-->", text, re.S | re.I)
        if not m:
            problems.append("tidak ada komentar bukti `<!-- web-unslop ... -->` (lihat references/process.md)")
        else:
            missing = [k for k in MARKER_FIELDS if not re.search(rf"^\s*{k}\s*:\s*\S", m.group(1), re.M | re.I)]
            if missing:
                problems.append("komentar bukti kosong untuk: " + ", ".join(missing))

    if not problems:
        return 0
    print(f"web-unslop menolak {os.path.basename(path)}:", file=sys.stderr)
    for p in problems:
        print(" - " + p, file=sys.stderr)
    print("Perbaiki lalu tulis ulang. Aturan: references/lint-rules.md. Tekan satu baris dengan `unslop-ok` bila sengaja.", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
