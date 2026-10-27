# Impeccable (vendored)

Files in this directory are copied **unmodified** from Impeccable v2.1.1 by Paul Bakaus.

- Source: https://github.com/pbakaus/impeccable
- License: Apache License 2.0, full text in `LICENSE` next to this file.
- Upstream states it is based on Anthropic's `frontend-design` skill.
- Upstream NOTICE (platform design skills by ehmo, MIT) concerns `ios.md` and `android.md`, which are not included here.

Layout of the copy:

| Here | Upstream |
|---|---|
| `SKILL.md` | `impeccable/SKILL.md` |
| `reference/*.md` | `impeccable/reference/*.md` |
| `commands/<name>.md` | the separate `<name>/SKILL.md` command skills (shape, critique, audit, polish, bolder, quieter, distill, delight, overdrive, layout, typeset, colorize, animate, adapt, clarify, optimize) |

Not copied: `scripts/cleanup-deprecated.mjs`.

Because the copy is verbatim, text inside still says `/impeccable`, `/shape`, `/critique` and so on, and still mentions `.impeccable.md`. Inside web-unslop, read those as "open the matching file in this directory". `references/impeccable-map.md` explains how the two skills fit together and which one wins when they disagree.

This directory is the only part of the repository under Apache-2.0. Everything else is MIT.
