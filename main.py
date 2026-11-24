#!/usr/bin/env python3
"""Everyday Wonder — one sentence, max 200 characters.

Writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback: script dir).
Stdlib only.
"""

import os
import sys
from pathlib import Path

ENTRY = "The lift doors opened on the wrong floor, and the stranger inside was humming my dead grandmother's lullaby, note for note."


def main() -> int:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        print(f"entry length {len(text)} out of range", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or str(Path(__file__).resolve().parent)
    out_path = Path(out_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
