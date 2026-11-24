#!/usr/bin/env python3
"""Write a one-line code review comment to entry.txt.

The entry is a single flat line that approves a pull request while
carrying quiet existential dread. Standard library only, no network.
"""

import os
import sys

LINE = "LGTM. I approved the last one for the same reason, and look where that brought us: here, approving this one."


def main():
    # Validate before writing anything.
    if "\n" in LINE or "\r" in LINE:
        print("error: entry must be exactly one line", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("error: entry must not be blank", file=sys.stderr)
        return 1
    if len(LINE) > 140:
        print("error: entry exceeds 140 characters", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.umask(0o022)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)

    # Read back and refuse to finish if the content differs.
    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    if back != LINE:
        print("error: entry.txt content mismatch after write", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
