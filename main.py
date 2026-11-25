#!/usr/bin/env python3
"""Write the entry joke to entry.txt in the output directory."""
import os

TEXT = (
    "They turned the old supply closet into a focus room with a glass door, "
    "so now I deep-work while six people watch me and one mouths "
    "'quick question.'\n"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
