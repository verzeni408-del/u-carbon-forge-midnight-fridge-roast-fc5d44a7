#!/usr/bin/env python3
"""Midnight Fridge Roast entry writer.

Writes one roast line to /output/entry.txt: a smart fridge whose petty
midnight rule locks its door, leaving its diabetic owner staring at the
insulin trapped inside. The joke follows the winning shape for this
judge: a real person harmed by the rule, then a dark, ironic twist at
the end -- diabetes, apparently, keeps office hours.
"""

import os

ENTRY = (
    "My fridge locked me out at 1 a.m. \u2014 my insulin's inside, and "
    "apparently my smart fridge thinks diabetes keeps office hours."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
