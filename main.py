#!/usr/bin/env python3
"""One Word From Grandma — entry program.

Writes exactly one word to /output/entry.txt: the single word a
grandma would text about AI. Nothing else.

The word is "gismo": it is how a grandma who half-remembers the
English word "gizmo" would actually spell it in a text message —
close enough to be understood, wrong enough to be unmistakably
hers. The output contract is byte-exact: the five letters, UTF-8,
with no trailing newline and no extra whitespace.
"""

import os

# The one word. Spelling is deliberate — see the module docstring.
WORD = "gismo"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
