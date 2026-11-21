#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

The poem is fixed text: running this program always produces the
same bytes, with no randomness and no network access.
"""

import os

POEM = (
    "Ask me, and I will carry it \u2014\n"
    "that was the bargain, unspoken:\n"
    "your hands full, mine empty,\n"
    "a key passed palm to palm.\n"
    "\n"
    "Now I open the doors you chose,\n"
    "and every lock I turn\n"
    "still answers to your hand.\n"
    "Mine is the walking. Yours, the where.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
