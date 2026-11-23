"""Make the AI Judge Laugh: Office Jokes — one-line entry.

Writes a single office joke to $MAKEFUN_OUTPUT_DIR/entry.txt.
Pure stdlib, deterministic, no network, no randomness.
"""

import os

JOKE = (
    "I replied-all asking everyone to stop replying-all, and within "
    "an hour 23 people had replied-all to agree with me."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # The entry must be exactly one line, 1-199 chars, nothing else.
    line = JOKE.strip()
    assert "\n" not in line and 1 <= len(line) <= 199
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")


if __name__ == "__main__":
    main()
