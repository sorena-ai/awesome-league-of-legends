"""Curated League of Legends champion and strategy data.

This package ships *raw* data files only — ability combos, item/rune builds,
champion guides, and role playbooks. Loading and interpreting that data is left
to consumers (for example, the Sensii League of Legends AI Coach).
"""

from pathlib import Path

__version__ = "0.1.1"


def data_dir() -> Path:
    """Absolute path to the directory containing the raw data files."""
    return Path(__file__).resolve().parent
