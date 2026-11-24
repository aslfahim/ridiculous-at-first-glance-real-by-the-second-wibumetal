#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second - @wibumetal entry.

Concept: DOG DATE-JUDGES. Writes one sentence (<=200 chars) to
/output/entry.txt pitching the bizarre-but-sellable startup.
"""

import os

SENTENCE = (
    "Singles pay to bring our trained dog on a first date as a character "
    "judge: one growl ends the evening before months of heartbreak - "
    "cheaper than therapy, and the dog never lies."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
