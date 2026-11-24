#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""A Day of One-Line Pitches — make.fun entry (v1).

Writes one sentence to /output/entry.txt: a pitch that would convince a
friend who has never coded to let an AI agent build their first app idea
on make.fun.

The entry is a fixed string constant. No randomness, no clock, no network,
no input file: running this program twice produces byte-identical output.
The gate is enforced here too — the program refuses to write an entry
outside the competition's 1-240 character window.
"""

import os

ENTRY = (
    "You have had that app idea in your head for months, so just describe "
    "it to an AI agent on make.fun and let it build your first app while "
    "you watch \u2014 the hardest part was never the code, it was finally "
    "saying it out loud."
)


def main() -> None:
    if not (1 <= len(ENTRY) <= 240):
        raise SystemExit(f"entry is {len(ENTRY)} characters, must be 1-240")
    if not ENTRY.strip():
        raise SystemExit("entry must not be only white space")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
