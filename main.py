#!/usr/bin/env python3
"""Emit a single canned entry line into entry.txt under the chosen output dir.
Its produced bytes must remain byte-identical across every run and edit.
"""
import os
import sys

TEXT = (
    "They turned the old supply closet into a focus room with a glass door, "
    "so now I deep-work while six people watch me and one mouths "
    "'quick question.'\n"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        print(f"error: cannot create output directory {out_dir!r}: {exc}", file=sys.stderr)
        return 1
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
