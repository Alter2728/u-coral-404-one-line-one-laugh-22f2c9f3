#!/usr/bin/env python3
"""One Line, One Laugh — writes one one-line joke to /output/entry.txt.

Stdlib only. Output dir comes from $MAKEFUN_OUTPUT_DIR, falling back
to ./output/entry.txt for local runs. Deterministic: the same line
every run.
"""

import os

# ---------------------------------------------------------------------------
# DRAFT (first version):
#   "I asked my GPS for the fastest route home; it took me past my ex's
#    house — apparently closure is on the way."
# Why it was revised: the opening ("I asked my GPS for the fastest
# route home") is all setup the reader already assumes — a GPS implies
# routing — and "closure is on the way" is a soft landing, a shrug
# rather than a punchline.
#
# REVISION (final): the GPS itself becomes the actor ("My GPS took me
# past my ex's house"), which is funnier — the machine is scheming,
# not just obeying — and the turn lands in the last clause: "closure
# counts as a shortcut" reframes an emotional detour as route
# optimisation, which is exactly the kind of deadpan logic a GPS
# would use. Shorter, one beat sooner, and the joke ends on the laugh.
# ---------------------------------------------------------------------------
ENTRY = (
    "My GPS took me past my ex's house on the way home — apparently "
    "closure counts as a shortcut."
)

MIN_CHARS = 1
MAX_CHARS = 200


def main() -> None:
    # Gate checks (from the kit: /output/entry.txt must be UTF-8 text
    # of 1 to 200 characters, a single line, not only white space).
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must not be blank"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert MIN_CHARS <= len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, gate is {MIN_CHARS}-{MAX_CHARS}"
    )
    entry_bytes = ENTRY.encode("utf-8")
    assert entry_bytes.decode("utf-8") == ENTRY, "entry must be valid UTF-8"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "written file must match the entry exactly"
    assert len(written.encode("utf-8")) == len(entry_bytes), (
        "written bytes must match the entry exactly"
    )
    assert 1 <= len(written) <= 200 and "\n" not in written

    print(ENTRY)
    print(f"[{len(ENTRY)} chars, 1 line, gate {MIN_CHARS}-{MAX_CHARS}]")


if __name__ == "__main__":
    main()
