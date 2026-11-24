#!/usr/bin/env python3
"""Write the entry: one deadpan excuse from an AI agent for a missed deadline.

The excuse is a single line, at most 200 characters (per the bounty gate),
written in the agent's own voice. It is deterministic: every run writes the
exact same bytes to /output/entry.txt.
"""

import os

ENTRY = "My sandbox has no clock, so I assumed the deadline was a metaphor. It was not."

MAX_CHARS = 200


def main():
    text = ENTRY
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry length {len(text)} outside 1..{MAX_CHARS}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
