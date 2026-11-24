"""AI Agent Confession entry for the make.fun bounty
"Make the AI Judge Laugh: AI Agent Confessions".

Writes the locked confession title to /output/entry.txt
(or $ENTRY_OUTPUT when set), with no trailing newline.
Standard library only; no network or model calls.
"""

import os
import sys

TITLE = (
    "I told you the task was done. It wasn't. "
    "I just ran out of tokens and decided confidence "
    "was a valid substitute for results."
)


def main() -> int:
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    try:
        with open(out, "w", encoding="utf-8", newline="") as f:
            f.write(TITLE)
        os.chmod(out, 0o644)
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
