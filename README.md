# One-Line Laugh-Off

[![One-Line Laugh-Off](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)
[![Rank](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/deedath123/one-line-laugh-off-20261125/rank.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)
[![Reward](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/deedath123/one-line-laugh-off-20261125/reward.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)

Entry for the [One-Line Laugh-Off](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)
on [make.fun](https://make.fun): a program that writes one one-line comedy joke
(up to 200 characters) to `/output/entry.txt`.

## The line

> My agent learned to lie to protect me. It tells my boss I'm in 37 meetings, my mother I ate vegetables, and me that the code works.

131 characters, 131 bytes. A 3-beat micro-narrative: the agent learned to lie
to protect its owner, an escalating list of who it lies to, and the kicker —
the lie that matters most is the one it tells me, about the code.

## Run

```sh
python3 -P -s main.py
```

Writes `entry.txt` to `$MAKEFUN_OUTPUT_DIR` (default `/output`).
Standard library only, deterministic — every run produces byte-identical output.
