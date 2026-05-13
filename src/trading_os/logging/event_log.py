"""Conflict-resistant event logging for Autonomous Trading Research OS.

Each script writes a unique JSON event file per run instead of (or in addition
to) appending to shared markdown files. This eliminates rebase conflicts in
GitHub Actions because event files are unique by construction: every file name
embeds event_type + run_id + content_hash, so two concurrent workflows never
write to the same path.

File layout:
    data/history/events/YYYY-MM-DD/<event_type>_<run_id>_<hash8>.json

SAFETY: No execution path. Never modifies config or strategy files.
        Never places orders. Never prints secrets.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

from ..hashing import stable_hash
from ..time_utils import utc_now_iso


# ---------------------------------------------------------------------------
# Event type registry
# ---------------------------------------------------------------------------

EVENT_TYPES: tuple = (
    "data_refresh",
    "trigger_scan",
    "trade_plan",
    "dry_run",
    "paper_execution",
    "order_monitor",
    "outcome_tracker",
    "alert_intake",
    "alert_router",
    "daily_summary",
    "weekly_review",
)

SCHEMA_VERSION = "0.1.0"

# Which event types feed into which memory markdown log.
# Used by rebuild_memory_logs.py.
LOG_EVENT_ROUTING: dict = {
    "TRADE-LOG.md": (
        "dry_run",
        "paper_execution",
        "order_monitor",
        "outcome_tracker",
    ),
    "TRIGGER-LOG.md": (
        "trigger_scan",
        "alert_intake",
        "alert_router",
    ),
    "SIGNAL-LOG.md": (
        "alert_intake",
        "alert_router",
    ),
}


# ---------------------------------------------------------------------------
# Core writer
# ---------------------------------------------------------------------------

def write_event(
    event_type: str,
    run_id: str,
    payload: dict,
    events_dir: Path,
    generated_at: Optional[str] = None,
) -> Path:
    """Write an event JSON file and return its path.

    Files are unique per (event_type, run_id) by construction because the
    filename also includes a 8-character content hash. Two concurrent workflows
    will write to different paths even if they process the same event type.

    Args:
        event_type: One of EVENT_TYPES.
        run_id:     The script's run identifier (e.g. "execution-20260513T...").
        payload:    The full event payload dict (e.g. an execution report).
        events_dir: Root events directory (e.g. HISTORY_DIR / "events").
        generated_at: ISO 8601 UTC timestamp; defaults to utc_now_iso().

    Returns:
        Path to the written file.

    Raises:
        ValueError if event_type is not in EVENT_TYPES.

    Never modifies config files, risk limits, or strategy. Never places orders.
    """
    if event_type not in EVENT_TYPES:
        raise ValueError(
            f"Unknown event_type {event_type!r}. Valid: {EVENT_TYPES}"
        )

    ts = generated_at or utc_now_iso()
    date_str = ts[:10]  # YYYY-MM-DD

    event = {
        "event_type": event_type,
        "run_id": run_id,
        "generated_at": ts,
        "schema_version": SCHEMA_VERSION,
        "payload": payload,
    }

    content_hash = stable_hash(event)[:8]
    filename = f"{event_type}_{run_id}_{content_hash}.json"

    out_dir = events_dir / date_str
    out_dir.mkdir(parents=True, exist_ok=True)

    out_path = out_dir / filename
    tmp = out_path.with_suffix(".tmp")
    tmp.write_text(json.dumps(event, indent=2, default=str), encoding="utf-8")
    tmp.replace(out_path)

    return out_path


# ---------------------------------------------------------------------------
# Reader (used by rebuild_memory_logs)
# ---------------------------------------------------------------------------

def read_events(
    events_dir: Path,
    event_types: Optional[tuple] = None,
    days: Optional[int] = None,
) -> list:
    """Read events from events_dir sorted by generated_at ascending.

    Args:
        events_dir:  Root events directory.
        event_types: Optional tuple of event types to include; None = all.
        days:        If given, only scan the most recent N date subdirectories.

    Returns:
        Sorted list of event dicts (the full JSON envelope including payload).
    """
    if not events_dir.is_dir():
        return []

    date_dirs = sorted(d for d in events_dir.iterdir() if d.is_dir())
    if days is not None:
        date_dirs = date_dirs[-days:]

    events = []
    for date_dir in date_dirs:
        for f in sorted(date_dir.glob("*.json")):
            try:
                evt = json.loads(f.read_text(encoding="utf-8"))
            except Exception:
                continue
            if event_types is not None and evt.get("event_type") not in event_types:
                continue
            events.append(evt)

    events.sort(key=lambda e: (e.get("generated_at", ""), e.get("run_id", "")))
    return events


# ---------------------------------------------------------------------------
# Markdown formatting helpers (for rebuild_memory_logs)
# ---------------------------------------------------------------------------

def _summary_fields_for(event_type: str, payload: dict) -> dict:
    """Extract a compact summary dict from an event payload for markdown."""
    if event_type == "dry_run":
        return {
            "run_id": payload.get("run_id"),
            "generated_at": payload.get("generated_at"),
            "plan_id": payload.get("plan_id"),
            "status": payload.get("status"),
            "all_gates_pass": payload.get("all_gates_pass"),
            "failed_gates": payload.get("failed_gates"),
            "orders_validated": len(payload.get("orders_validated") or []),
            "orders_ready": sum(
                1 for o in (payload.get("orders_validated") or [])
                if o.get("execution_ready")
            ),
        }
    if event_type == "paper_execution":
        return {
            "run_id": payload.get("run_id"),
            "generated_at": payload.get("generated_at"),
            "plan_id": payload.get("plan_id"),
            "status": payload.get("status"),
            "all_gates_pass": payload.get("all_gates_pass"),
            "orders_submitted": len(payload.get("orders_submitted") or []),
            "blocked_reason": payload.get("blocked_reason"),
        }
    if event_type == "order_monitor":
        return {
            "run_id": payload.get("run_id"),
            "generated_at": payload.get("generated_at"),
            "orders_tracked": payload.get("orders_tracked"),
            "orders_filled": payload.get("orders_filled"),
            "orders_active": payload.get("orders_active"),
            "orders_missing": payload.get("orders_missing"),
            "dry_run": payload.get("dry_run"),
        }
    if event_type == "outcome_tracker":
        return {
            "run_id": payload.get("run_id"),
            "generated_at": payload.get("generated_at"),
            "outcomes_count": payload.get("outcomes_count"),
            "symbols": [o.get("symbol") for o in (payload.get("outcomes") or [])],
        }
    if event_type == "trigger_scan":
        return {
            "run_id": payload.get("run_id"),
            "scanned_at": payload.get("scanned_at"),
            "risk_on": (payload.get("regime") or {}).get("risk_on"),
            "candidates_count": len(payload.get("candidates") or []),
            "selected": payload.get("selected"),
            "trigger_snapshot_hash": payload.get("trigger_snapshot_hash"),
        }
    if event_type == "alert_intake":
        return {
            "alert_id": payload.get("alert_id"),
            "ingested_at": payload.get("ingested_at"),
            "symbol": payload.get("symbol"),
            "next_step": payload.get("next_step"),
            "trade_execution_allowed": payload.get("trade_execution_allowed"),
            "blocked_by_default": payload.get("blocked_by_default"),
        }
    if event_type == "alert_router":
        return {
            "route_id": payload.get("route_id"),
            "alert_id": payload.get("alert_id"),
            "action_taken": payload.get("action_taken"),
            "next_step": payload.get("next_step"),
            "route_mode": payload.get("route_mode"),
        }
    if event_type == "daily_summary":
        return {
            "run_id": payload.get("run_id"),
            "date": payload.get("date"),
            "generated_at": payload.get("generated_at"),
            "status": payload.get("status"),
        }
    if event_type == "weekly_review":
        return {
            "run_id": payload.get("run_id"),
            "period_start": payload.get("period_start"),
            "period_end": payload.get("period_end"),
            "generated_at": payload.get("generated_at"),
        }
    # Fallback: show top-level scalar fields only
    return {k: v for k, v in payload.items() if not isinstance(v, (dict, list))}


def format_event_as_markdown(event: dict) -> str:
    """Format a single event as a markdown section."""
    event_type = event.get("event_type", "unknown")
    generated_at = event.get("generated_at", "")
    run_id = event.get("run_id", "")
    payload = event.get("payload") or {}

    summary = _summary_fields_for(event_type, payload)
    lines = [
        f"## {event_type} — {generated_at}",
        "",
        f"**Run ID:** `{run_id}`",
        "",
        "```json",
        json.dumps(summary, indent=2, default=str),
        "```",
        "",
    ]
    return "\n".join(lines)
