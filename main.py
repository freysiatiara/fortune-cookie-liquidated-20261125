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


def main():
    output_path = "/output/entry.txt"
    os.makedirs("/output", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(FORTUNE)
    os.chmod(output_path, 0o644)


if __name__ == "__main__":
    main()
