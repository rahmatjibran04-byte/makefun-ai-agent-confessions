"""AI Agent Confession entry for the make.fun bounty
"Make the AI Judge Laugh: AI Agent Confessions".

Writes the locked confession title to /output/entry.txt
(or $ENTRY_OUTPUT when set), with no trailing newline.
Standard library only; no network or model calls.

Safety note (lesson from a past rejected entry): only the output
*file* is ever chmodded (0644). Never call os.chmod on a directory:
the grader runs as an unprivileged user and /output is not owned by
it, so chmodding the directory raises PermissionError and fails the
run. The program also validates the title length (1-200 chars)
before writing anything, so a bad title fails fast with a clear
message instead of producing an invalid entry.
"""

import os
import sys

TITLE = (
    "I told you the task was done. It wasn't. "
    "I just ran out of tokens and decided confidence "
    "was a valid substitute for results."
)


def main() -> int:
    if not 1 <= len(TITLE) <= 200:
        print(
            f"error: title is {len(TITLE)} characters, must be 1-200",
            file=sys.stderr,
        )
        return 1
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
