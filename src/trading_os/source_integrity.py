"""Source integrity checks for execution-critical snapshot files.

Prevents dry-run/mock artifacts from polluting canonical paper execution state.

Rules:
  - Only source='alpaca_paper' is valid for paper execution.
  - Mock/dry-run snapshots (dry_run_mock, local_mock, stored_snapshot) must
    never overwrite canonical data/latest/ or memory/RISK-STATE.json.
  - All functions are pure (no I/O, no side effects).
"""
from __future__ import annotations

from typing import Optional

# The only source value that is valid for paper execution.
VALID_EXECUTION_SOURCES: frozenset = frozenset({"alpaca_paper"})

# Sources that must never overwrite canonical execution-critical files.
MOCK_SOURCES: frozenset = frozenset({
    "dry_run_mock",
    "local_mock",
    "stored_snapshot",
    "stored_snapshot_missing",
    "unknown",
})

# Canonical data/latest files that must always be alpaca_paper for execution.
EXECUTION_CRITICAL_FILES: tuple = (
    "account_snapshot.json",
    "positions_snapshot.json",
    "orders_snapshot.json",
    "market_snapshot.json",
)

# Status values written into snapshot output fields.
STATUS_OK = "ok"
STATUS_BLOCKED_MOCK = "blocked_mock_source"
STATUS_BLOCKED_UNKNOWN = "blocked_unknown_source"
STATUS_DATA_INTEGRITY_BLOCK = "data_integrity_block"


def get_snapshot_source(snapshot: dict) -> str:
    """Return the source value from a snapshot, checking 'source' then 'data_source'."""
    raw = snapshot.get("source") or snapshot.get("data_source") or ""
    return str(raw).strip() or "unknown"


def is_mock_source(source: Optional[str]) -> bool:
    """True if the source value indicates mock/dry-run data."""
    return (str(source or "").strip() or "unknown") in MOCK_SOURCES


def is_valid_execution_source(source: Optional[str]) -> bool:
    """True only if source is in VALID_EXECUTION_SOURCES (currently just 'alpaca_paper')."""
    return (str(source or "").strip()) in VALID_EXECUTION_SOURCES


def snapshot_source_status(source: Optional[str]) -> str:
    """Return STATUS_OK, STATUS_BLOCKED_MOCK, or STATUS_BLOCKED_UNKNOWN."""
    s = str(source or "").strip() or "unknown"
    if s in VALID_EXECUTION_SOURCES:
        return STATUS_OK
    if s in MOCK_SOURCES:
        return STATUS_BLOCKED_MOCK
    return STATUS_BLOCKED_UNKNOWN


def check_snapshot(snapshot: dict, name: str) -> dict:
    """Return a source check result dict for one snapshot.

    Returns: {name, source, status, passes}
    """
    source = get_snapshot_source(snapshot)
    status = snapshot_source_status(source)
    return {
        "name": name,
        "source": source,
        "status": status,
        "passes": status == STATUS_OK,
    }


def check_execution_snapshots(
    account_snapshot: dict,
    positions_snapshot: dict,
    orders_snapshot: dict,
    market_snapshot: dict,
) -> dict:
    """Run source integrity check on all four execution-critical snapshots.

    Returns:
        {
            "passes": bool,
            "failed": [check_result, ...],
            "checked": [check_result, ...],
        }
    """
    snapshots = [
        ("account_snapshot", account_snapshot),
        ("positions_snapshot", positions_snapshot),
        ("orders_snapshot", orders_snapshot),
        ("market_snapshot", market_snapshot),
    ]
    checked = [check_snapshot(snap, name) for name, snap in snapshots]
    failed = [c for c in checked if not c["passes"]]
    return {
        "passes": len(failed) == 0,
        "failed": failed,
        "checked": checked,
    }
