from __future__ import annotations

from typing import Any

from .alpaca_adapter import AlpacaAdapter
from .audit import append_event, new_run_id, record_error
from .file_io import read_json, write_json
from .mock_data import generate_market_snapshot
from .paths import CONFIG_DIR, LATEST_DIR, ensure_repo_dirs


def run_data_refresh(dry_run: bool = True) -> dict[str, Any]:
    ensure_repo_dirs()
    run_id = new_run_id("data_refresh")
    try:
        universe = read_json(CONFIG_DIR / "universe.json", default={})
        symbols = list(universe.get("symbols", []))
        if dry_run:
            snapshot = generate_market_snapshot(symbols)
        else:
            adapter = AlpacaAdapter()
            snapshot = adapter.refresh_snapshot(symbols)
        snapshot["run_id"] = run_id
        write_json(LATEST_DIR / "market_snapshot.json", snapshot)
        append_event("DATA-QUALITY-LOG.md", "Data refresh completed", {
            "run_id": run_id,
            "dry_run": dry_run,
            "generated_at": snapshot.get("generated_at"),
            "data_source": snapshot.get("data_source"),
            "symbols": len(snapshot.get("bars", {})),
            "source_data_hash": snapshot.get("source_data_hash"),
        })
        return snapshot
    except Exception as exc:
        record_error("data_refresh", exc, {"dry_run": dry_run})
        raise
