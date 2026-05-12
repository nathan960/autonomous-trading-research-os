from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


def stable_hash(obj: Any) -> str:
    """Stable sha256 of any JSON-serialisable object (canonical key order, no whitespace)."""
    encoded = (
        json.dumps(obj, sort_keys=True, separators=(",", ":"), default=str)
        .encode("utf-8")
    )
    return hashlib.sha256(encoded).hexdigest()


def hash_file(path: Path) -> str:
    """Sha256 of raw file bytes."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def hash_json_file(path: Path) -> str:
    """Stable hash of the parsed content of a JSON file (canonical form, not raw bytes)."""
    with path.open("r", encoding="utf-8") as fh:
        obj = json.load(fh)
    return stable_hash(obj)
