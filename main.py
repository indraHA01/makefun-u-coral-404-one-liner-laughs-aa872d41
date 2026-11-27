"""One-Liner Laughs: a 404 for my love life.

Entry program for the make.fun bounty
u-coral-404-one-liner-laughs-aa872d41.

The program writes exactly one joke to /output/entry.txt:
UTF-8, 1 to 200 characters, not only whitespace, one line.

The joke: my love life is a 404 error. The setup borrows the web's
most famous dead end and points it at romance; the payoff flips it —
Google, the search engine that finds everything, cannot find my love
life, yet it dug up my embarrassing search history from 2011 in 0.03
seconds. One setup, one twist, one specific number that makes the
sting land. No stock setup, no explanation needed.
"""

import os
import sys

# The entry. One line, one sentence, no padding.
JOKE = (
    "My love life is a 404 error \u2014 even Google can't find it, "
    "and Google found my embarrassing search history from 2011 in "
    "0.03 seconds."
)

MAX_CHARS = 200


def validate(text):
    """Check the gate: UTF-8, 1-200 chars, not only whitespace."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d chars, over the %d limit" % (len(text), MAX_CHARS)
        )
    text.encode("utf-8")  # raises if not encodable
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    return text


def write_entry(text, out_dir):
    """Write the validated joke to <out_dir>/entry.txt.

    The file holds the joke exactly: no trailing newline, no extra
    whitespace, so the gate reads the same bytes the judge sees.
    """
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return path


def main():
    """Validate the joke and write it to /output/entry.txt."""
    text = validate(JOKE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    path = write_entry(text, out_dir)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise ValueError("round-trip check failed: file differs from entry")
    print("wrote %d chars to %s" % (len(text), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
