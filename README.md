# ASCII Discord Bot [![Run ASCII Discord Bot](https://github.com/SlawSimulation/Discord-ACAII-Bot/actions/workflows/run-bot.yml/badge.svg)](https://github.com/SlawSimulation/Discord-ACAII-Bot/actions/workflows/run-bot.yml)

Plays animated ASCII art in a Discord channel by editing a single message.

## Setup

1. **Create two repository secrets**

| Name            | Example               | Notes                         |
|-----------------|-----------------------|-------------------------------|
| `DISCORD_TOKEN` | `MTAz…`               | Bot token from the Dev Portal |
| `CHANNEL_ID`    | `123456789012345678`  | Channel to post animation     |
| *(Optional)* `FRAME_DELAY` | `0.25`     | Seconds per frame             |

2. `git push` or click **Run workflow** ▸ **run-bot** to start.

## Local testing

```bash
export DISCORD_TOKEN="…" CHANNEL_ID="…"
python -m pip install -r requirements.txt
python bot.py
