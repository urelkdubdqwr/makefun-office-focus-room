#!/usr/bin/env python3
"""Write the entry joke to entry.txt in the output directory.

The output directory is MAKEFUN_OUTPUT_DIR when set and non-empty, otherwise
/output. It is created if missing. The file content is exactly TEXT followed
by one trailing newline.
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
