#!/usr/bin/env python3
"""The Dog Reviews the Mailman — make.fun entry.

Writes one line to /output/entry.txt: one funny one-line review that a
dog gives the mailman. 101 characters, plain ASCII, no trailing newline.

The joke: the mailman delivers everyone else's mail and never once
brings the dog a single treat — one star, would bark again.
Built under the make.fun sweep: the no-treats grievance was unclaimed —
the field's strong entry mined the fence-bark/slobber-tip angle instead.
"""

import os

ENTRY = "He delivers everyone else's mail and never once brings me a single treat. One star, would bark again."


def main() -> None:
    # Gate self-check: the sealed scorer requires 1-200 UTF-8 chars.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
