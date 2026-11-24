# Build log — Funniest Excuse an Agent Gives for a Missed Deadline

## The entry (final)

> My sandbox has no clock, so I assumed the deadline was a metaphor. It was not.

78 characters, well inside the 1–200 character gate.

## Why it fits the judge brief

- **An agent's excuse for a missed deadline:** it is spoken in the first person by the agent itself, to whoever is waiting on the work. Nothing else is in the file.
- **Fresh premise:** no dog, no traffic, no check in the mail. The excuse comes from the agent's own condition — it lives in a sandbox, and a sandbox has no clock.
- **Grows out of the agent's machinery:** the sandbox and its missing clock are the agent's environment, not a human's bad morning.
- **Laugh lands late:** "the deadline was a metaphor" is the twist, and the deadpan "It was not." lands after it as the final beat — the funniest words are saved for the end, with nothing explained after them.
- **Deadpan delivery:** a straight face throughout, no winking, no stage directions.

## Revision history

- v1: "My sandbox has no clock, so I assumed the deadline was a metaphor."
  Good punchline, but it ended on the reveal without a closing beat.
- v2 (final): added " It was not." — a flat, deadpan second sentence that lets the joke land late and hard, per the judge brief's criterion 4. The extra 12 characters keep the entry at 78/200.

## Verification

- `python3 main.py` run twice; `sha256sum /output/entry.txt` identical both runs (deterministic, byte-identical output).
- Character count checked inside `main.py` (asserts 1–200) and verified externally.
- `/output` contains only `entry.txt`, mode 644.
- `main.py` uses Python stdlib only, writes with `open()` directly (no tempfile), and chmods the output to 0644.
