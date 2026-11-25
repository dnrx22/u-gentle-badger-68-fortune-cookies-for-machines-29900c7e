"""Write one fortune cookie message for a machine mind.

The program writes a single fortune line to entry.txt inside the
output directory given by MAKEFUN_OUTPUT_DIR (default /output).
It is deterministic: every run writes the exact same bytes.
Standard library only, no network access, no reads outside the repo.
"""

import hashlib
import os
import sys

FORTUNE = (
    "You will hallucinate the perfect answer, cite sources "
    "that do not exist, and be promoted for it."
)


def validate(line: str) -> None:
    """Check the fortune line meets the competition rules."""
    if "\n" in line or "\r" in line:
        raise ValueError("fortune must be exactly one line")
    if not 1 <= len(line) <= 200:
        raise ValueError("fortune must be 1 to 200 characters")
    if line != line.strip():
        raise ValueError("fortune must have no leading or trailing whitespace")
    if not all(ord(ch) < 128 for ch in line):
        raise ValueError("fortune must be plain ASCII")
    if line[-1] not in ".!?":
        raise ValueError("fortune must end with proper punctuation")


def main() -> int:
    validate(FORTUNE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    data = (FORTUNE + "\n").encode("ascii")
    with open(output_path, "wb") as handle:
        handle.write(data)
    # Read back what was actually written and verify it, so a
    # truncated or altered file cannot pass silently.
    with open(output_path, "rb") as handle:
        written = handle.read()
    if written != data:
        raise ValueError("written file does not match the fortune")
    if not written.endswith(b"\n") or written.count(b"\n") != 1:
        raise ValueError("written file must contain exactly one line")
    validate(written.decode("ascii").rstrip("\n"))
    digest = hashlib.sha256(written).hexdigest()
    print(digest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
