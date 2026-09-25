# Awesome League of Legends

Curated League of Legends champion and strategy data, packaged for easy reuse.

This repository ships **raw data files only**. There is no parsing or domain
logic here — consumers are expected to load and interpret the files themselves
(for example, the [Sensii LoL AI Coach](https://github.com/sorena-ai/LeagueAiCoach)).

## Layout

| Directory | Contents |
|-----------|----------|
| `champion-combos/` | One XML file per champion describing ability combos and trading patterns. |
| `champion-builds/` | Per-champion directories of item/rune build XML, one file per role. |
| `champion-guide/`  | Per-champion directories of guide XML (strengths, weaknesses, spikes), one file per role. |
| `playbook/`        | Role macro strategy text files covering laning and early/mid/late game. |

## Install

```bash
pip install "awesome-league-of-legends @ git+https://github.com/sorena-ai/awesome-league-of-legends.git@v0.1.0"
```

## Usage

```python
from awesome_league_of_legends import data_dir

# Absolute path to the directory containing the four data folders above.
print(data_dir())
```

## License

Apache License, Version 2.0.
