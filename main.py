#!/usr/bin/env python3
"""Worst AI Advice: one line of the worst possible advice an AI could give.

Writes a single line (1-140 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Stdlib only, no network.
"""

import os

ADVICE = (
    "Certainly! To speed up your laptop, delete the System32 folder "
    "\u2014 it is just leftover files Windows forgot to clean up."
)

MIN_CHARS = 1
MAX_CHARS = 140


def validate(text: str) -> str:
    """Return the stripped line, or raise if it fails the bounty gate."""
    line = text.strip()
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"advice must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(line)}"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("advice must be a single line")
    if not line.strip():
        raise ValueError("advice must not be only whitespace")
    return line


def write_entry(text: str, out_dir: str) -> str:
    """Write the validated line and read it back to prove it landed."""
    line = validate(text)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    back = open(path, encoding="utf-8").read()
    if back != line:
        raise SystemExit("read-back mismatch: entry.txt does not match advice")
    return path


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry(ADVICE, out_dir)
    print(f"wrote {len(ADVICE.strip())} characters to {path}")


if __name__ == "__main__":
    main()
