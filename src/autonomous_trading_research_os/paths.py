from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = ROOT / "config"
DATA_DIR = ROOT / "data"
LATEST_DIR = DATA_DIR / "latest"
ARCHIVE_DIR = DATA_DIR / "archive"
MEMORY_DIR = ROOT / "memory"
LOGS_DIR = ROOT / "logs"
RESEARCH_DIR = ROOT / "research"


def ensure_repo_dirs() -> None:
    for path in [CONFIG_DIR, LATEST_DIR, ARCHIVE_DIR, MEMORY_DIR, LOGS_DIR, RESEARCH_DIR]:
        path.mkdir(parents=True, exist_ok=True)
