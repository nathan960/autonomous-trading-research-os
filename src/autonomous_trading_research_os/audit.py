from __future__ import annotations

from pathlib import Path
from typing import Any
from uuid import uuid4

from .file_io import append_markdown_log, utc_now_iso
from .paths import MEMORY_DIR


def new_run_id(layer: str) -> str:
    return f"{layer}-{utc_now_iso().replace(':', '').replace('-', '').replace('Z', '')}-{uuid4().hex[:8]}"


def append_event(memory_file: str, title: str, payload: Any) -> None:
    append_markdown_log(MEMORY_DIR / memory_file, title, payload)


def record_error(layer: str, error: Exception, extra: dict[str, Any] | None = None) -> None:
    payload = {
        "timestamp": utc_now_iso(),
        "layer": layer,
        "error_type": type(error).__name__,
        "message": str(error),
        "extra": extra or {},
    }
    append_markdown_log(MEMORY_DIR / "ERROR-LOG.md", f"{layer} error", payload)


def write_gitkeep(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text("", encoding="utf-8")
