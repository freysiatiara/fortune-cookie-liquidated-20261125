#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes a single fortune cookie message for a crypto trader who has
just been liquidated to /output/entry.txt.
"""

import os

FORTUNE = (
    "Fortune favors the bold, but tonight it favored the exchange: "
    "your coins now live in a nicer wallet."
)


def validate(text):
    """Guard the gate before writing: 1-160 chars, one line, at most 20 words."""
    if not 1 <= len(text) <= 160:
        raise ValueError("fortune must be 1-160 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("fortune must be a single line")
    if len(text.split()) > 20:
        raise ValueError("fortune must be at most 20 words")


def main():
    output_path = "/output/entry.txt"
    validate(FORTUNE)
    os.makedirs("/output", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(FORTUNE)
    os.chmod(output_path, 0o644)


if __name__ == "__main__":
    main()
