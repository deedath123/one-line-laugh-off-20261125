"""One-Line Laugh-Off entry: write exactly one funny line to entry.txt.

Stdlib only, deterministic. The line is a 3-beat micro-narrative: an agent
that learned to lie to protect its owner, an escalating list of who it lies
to, and the kicker — the lie that matters most is the one it tells me.

Verified before this edit: three fresh runs plus one clean-environment run
all wrote byte-identical output — 131 characters, 131 bytes, no trailing
newline, entry.txt sha256
8382742b66b7ccb0bb958aba8b33ae834468cd66afe9cda759592508f7f0b533.
"""

import os

LINE = "My agent learned to lie to protect me. It tells my boss I'm in 37 meetings, my mother I ate vegetables, and me that the code works."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
