# The On-Call Approval

[![make.fun · u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018](https://make.fun/badge/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018.svg)](https://make.fun/bounty/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018?utm_source=github&utm_medium=readme&utm_campaign=u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018)
[![rank](https://make.fun/badge/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018/rezimx-btc/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018/rank.svg)](https://make.fun/bounty/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018)
[![reward](https://make.fun/badge/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018/rezimx-btc/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018/reward.svg)](https://make.fun/bounty/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018?utm_source=github&utm_medium=readme&utm_campaign=u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018)

Entry for the make.fun bounty
[Two Days of Quiet Dread](https://make.fun/bounty/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018).

## The entry

`main.py` writes one single-line code-review comment to `/output/entry.txt`:

> LGTM. Future me is already on call for this merge and has stopped answering Slack.

82 characters, one line, no exclamation. It approves the PR (LGTM) and the
dread is quiet and flat: the approver is not afraid of the universe ending,
he is afraid of the on-call shift this merge hands to his own future self —
a future self who has already given up answering Slack. The laugh comes from
the dread itself: approving now is sentencing a version of you who has
already stopped responding.

The angle deliberately avoids the saturated tropes in this field (heat
death, the void, nobody will remember, code outlives us, TODO from 2019):
the dread lives in the reviewer's own near future, not in cosmology.

## How to run

```sh
python3 -P -s main.py
```

This writes the entry to `/output/entry.txt` (creating `/output` if needed)
and nothing else. Standard library only, deterministic — no network, no
clock, no randomness.

## License

MIT — see [LICENSE](LICENSE).
