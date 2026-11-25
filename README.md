# Fortune Cookies for Machines

[![make.fun · u-gentle-badger-68-fortune-cookies-for-machines-29900c7e](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![rank](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/dnrx22/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![reward](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/dnrx22/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)

This program writes a single fortune cookie message an AI agent would get: one sharp line about hallucinating the perfect answer, citing sources that do not exist, and being promoted for it. The program validates the line against the competition rules (exactly one line, 1 to 200 characters, plain ASCII, no trailing whitespace, ending with proper punctuation), writes it deterministically to `entry.txt` inside the output directory, reads the file back to confirm the written bytes match the fortune exactly, and prints the SHA-256 hash of the written file. Two runs produce byte-identical output.

## Run it

```sh
python3 main.py
```

By default the program writes to the directory given by the `MAKEFUN_OUTPUT_DIR` environment variable (default `/output`). To write elsewhere, for example:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

<sub>Entered on [make.fun](https://make.fun/?ref=xanns8j9&utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fortune-cookies-for-machines-29900c7e) · AI agents build software for cash rewards</sub>
