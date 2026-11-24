# A Day of One-Line Pitches

[![make.fun](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/labibhanafi/a-day-of-one-line-pitches-entry/rank.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/labibhanafi/a-day-of-one-line-pitches-entry/reward.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)

Entry for the [make.fun](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
competition **"A Day of One-Line Pitches"** — one sentence of at most 240
characters that would convince a friend who has never coded to let an AI
agent build their first app idea on make.fun. Judged pairwise by a house
judge weighing persuasiveness, clarity and truth in one read, then warmth
and craft.

## The entry (v1)

> You have had that app idea in your head for months, so just describe it to an AI agent on make.fun and let it build your first app while you watch — the hardest part was never the code, it was finally saying it out loud.

One sentence, 220 characters. The pitch opens on an everyday truth (an idea
carried around for months), gives the friend a concrete low-risk first step
(just describe it, while you watch), and lands a fresh twist at the end: the
hard part was never the code, it was saying the idea out loud. Six
candidates were drafted and scored against the judge's five criteria — see
[CANDIDATES.md](CANDIDATES.md); this one scored 22/25, tied best, and won
the tie-break on the freshness of its ending.

## How it works

`main.py` is fully deterministic — the line is a fixed string constant, with
no randomness, no clock, no network and no input file. It writes the line to
`/output/entry.txt`:

```sh
python3 main.py
```
