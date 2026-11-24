#!/usr/bin/env python3
"""One-line office joke entry.

Writes a single fresh joke about office life to /output/entry.txt,
one line, at most 200 characters, so the judge can compare it.
Deterministic: the same text on every run, no network, no randomness.
"""

import os
from pathlib import Path

JOKE = (
    "Our office plant died, so facilities replaced it with a photo "
    "of a plant \u2014 morale improved, because the photo never asks "
    "for a meeting."
)
# No trailing newline: the gate counts every character, and the
# judge reads the file exactly as submitted.


def main() -> None:
    text = JOKE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"joke must be 1-200 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    out = Path(os.environ.get("OUTPUT_FILE", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
