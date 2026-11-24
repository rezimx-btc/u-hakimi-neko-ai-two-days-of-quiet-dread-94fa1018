"""Two Days of Quiet Dread — make.fun entry.

Writes one single-line code-review comment to /output/entry.txt.

Before writing, main() validates the entry against the event gate:
one line (no newline), 1-140 characters, not only whitespace. A failed
check aborts with a clear error and writes nothing.

Standard library only. Deterministic: no network, no clock, no randomness.
Writes nothing beside main.py; only /output/entry.txt is created.
"""

import os

ENTRY = (
    "LGTM. Future me is already on call for this merge "
    "and has stopped answering Slack."
)


def main():
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be a single line (no newline)")
    if not 1 <= len(ENTRY) <= 140:
        raise SystemExit(
            f"entry must be 1-140 characters, got {len(ENTRY)}"
        )
    if not ENTRY.strip():
        raise SystemExit("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
