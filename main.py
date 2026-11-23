#!/usr/bin/env python3
"""One Word From Grandma — entry program.

Writes exactly one word to /output/entry.txt: the single word a
grandma would text about AI. Nothing else.
"""

import os

WORD = "gismo"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
