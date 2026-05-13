"""Research-only alert router.

Reads a validated alert record (produced by alert_intake.py) and dispatches
the appropriate safe action based on next_step.  No execution path exists here.

Safety invariants — enforced unconditionally:
  - Rejects any alert where trade_execution_allowed is not exactly False.
  - Rejects any alert where blocked_by_default is not exactly True.
  - Never calls execute_paper.py.
  - Never passes approve_paper=True to any function.
  - Never sets approved_for_execution=True.
  - Every routing decision is logged to TRIGGER-LOG.md.
  - request_trade_plan_unapproved also appends to SIGNAL-LOG.md.

Routing actions by next_step:
  log_only                    → log only; no artifact written.
  request_alert_review        → write review-request record.
  request_data_refresh        → write refresh-request record.
  request_trade_plan_unapproved → write plan-request record; provide
                                  suggested_commands (no --approve-paper).

Pure functions — no subprocess calls.  The CLI script (route_alert.py)
may optionally execute suggested_commands via subprocess.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from ..hashing import stable_hash
from ..time_utils import utc_now_iso

ALLOWED_NEXT_STEPS: frozenset = frozenset({
    "log_only",
    "request_data_refresh",
    "request_alert_review",
    "request_trade_plan_unapproved",
})

_SAFE_KEY_PATTERN = re.compile(r"[^A-Za-z0-9_\-]")

# Suggested pipeline commands for request_trade_plan_unapproved.
# --approve-paper is intentionally absent — human approval is always required.
SUGGESTED_PIPELINE_COMMANDS: list = [
    "python scripts/scan_triggers.py",
    "python scripts/generate_trade_plan.py",
]


class AlertRouterError(ValueError):
    """Raised when routing is rejected due to a safety violation or bad input."""

    def __init__(self, reason: str) -> None:
        self.reason = reason
        super().__init__(reason)


# ---------------------------------------------------------------------------
# Safety validation
# ---------------------------------------------------------------------------

def validate_alert_safety(alert: Any) -> None:
    """Verify the alert carries required safety flags before routing.

    Raises AlertRouterError if:
      - alert is not a dict
      - trade_execution_allowed is not exactly False
      - blocked_by_default is not exactly True
      - next_step is missing or not in the allowed set

    This is a second line of defence — alerts should already carry correct
    flags from alert_intake.py, but the router enforces them independently.
    """
    if not isinstance(alert, dict):
        raise AlertRouterError("alert must be a JSON object")

    if alert.get("trade_execution_allowed") is not False:
        raise AlertRouterError(
            "alert rejected: trade_execution_allowed must be false; "
            f"got {alert.get('trade_execution_allowed')!r}"
        )
    if alert.get("blocked_by_default") is not True:
        raise AlertRouterError(
            "alert rejected: blocked_by_default must be true; "
            f"got {alert.get('blocked_by_default')!r}"
        )

    next_step = alert.get("next_step")
    if not isinstance(next_step, str) or next_step not in ALLOWED_NEXT_STEPS:
        raise AlertRouterError(
            f"alert rejected: next_step={next_step!r} is not in the allowed set; "
            f"permitted: {sorted(ALLOWED_NEXT_STEPS)}"
        )


# ---------------------------------------------------------------------------
# Route dispatch
# ---------------------------------------------------------------------------

def route_alert(
    alert: Any,
    alerts_dir: Path,
    trigger_log_path: Path,
    signal_log_path: Path,
) -> dict:
    """Route a validated alert to its safe research action.

    Args:
        alert:             Parsed alert record (validated by alert_intake.process_alert).
        alerts_dir:        Base directory for routing artifacts (subdirs created as needed).
        trigger_log_path:  Path to memory/TRIGGER-LOG.md (appended every call).
        signal_log_path:   Path to memory/SIGNAL-LOG.md (appended for trade-plan requests).

    Returns:
        Routing result dict with keys:
          alert_id, symbol, next_step, routed_at,
          action_taken, artifact_path (or None),
          suggested_commands (non-empty only for request_trade_plan_unapproved),
          safety (block of enforced invariants)

    Raises:
        AlertRouterError  if safety validation fails.
    """
    validate_alert_safety(alert)

    alert_id: str = str(alert.get("alert_id") or stable_hash(alert))
    symbol: str = str(alert.get("symbol", ""))
    next_step: str = str(alert.get("next_step", ""))
    routed_at: str = utc_now_iso()

    # Safety block — always present, always the same values.
    safety: dict = {
        "trade_execution_allowed": False,   # invariant — never True
        "blocked_by_default": True,         # invariant — never False
        "execute_paper_called": False,      # invariant — never True
        "approve_paper_passed": False,      # invariant — never True
    }

    if next_step == "log_only":
        result = _route_log_only(alert_id, symbol, next_step, routed_at, safety)

    elif next_step == "request_alert_review":
        result = _route_review(
            alert, alert_id, symbol, next_step, routed_at, safety, alerts_dir,
        )

    elif next_step == "request_data_refresh":
        result = _route_refresh(
            alert, alert_id, symbol, next_step, routed_at, safety, alerts_dir,
        )

    elif next_step == "request_trade_plan_unapproved":
        result = _route_plan_unapproved(
            alert, alert_id, symbol, next_step, routed_at, safety, alerts_dir,
        )

    else:
        # validate_alert_safety already guards this; belt-and-suspenders.
        raise AlertRouterError(f"unhandled next_step={next_step!r}")

    _append_trigger_log(result, trigger_log_path)
    if next_step == "request_trade_plan_unapproved":
        _append_signal_log(result, signal_log_path)

    return result


# ---------------------------------------------------------------------------
# Per-action handlers (private)
# ---------------------------------------------------------------------------

def _route_log_only(
    alert_id: str, symbol: str, next_step: str, routed_at: str, safety: dict,
) -> dict:
    return {
        "alert_id": alert_id,
        "symbol": symbol,
        "next_step": next_step,
        "routed_at": routed_at,
        "action_taken": "logged",
        "artifact_path": None,
        "suggested_commands": [],
        "safety": safety,
    }


def _route_review(
    alert: dict, alert_id: str, symbol: str, next_step: str,
    routed_at: str, safety: dict, alerts_dir: Path,
) -> dict:
    review_dir = alerts_dir / "review-requests"
    safe_key = _SAFE_KEY_PATTERN.sub("_", alert_id)
    out_path = review_dir / f"review-{safe_key}.json"
    record = {
        "alert_id": alert_id,
        "symbol": symbol,
        "next_step": next_step,
        "requested_at": routed_at,
        "source": alert.get("source"),
        "description": alert.get("description"),
        "trade_execution_allowed": False,
        "blocked_by_default": True,
        "original_alert_hash": alert.get("raw_payload_hash") or stable_hash(alert),
    }
    _write_json(out_path, record)
    return {
        "alert_id": alert_id,
        "symbol": symbol,
        "next_step": next_step,
        "routed_at": routed_at,
        "action_taken": "review_requested",
        "artifact_path": str(out_path),
        "suggested_commands": [],
        "safety": safety,
    }


def _route_refresh(
    alert: dict, alert_id: str, symbol: str, next_step: str,
    routed_at: str, safety: dict, alerts_dir: Path,
) -> dict:
    refresh_dir = alerts_dir / "refresh-requests"
    safe_key = _SAFE_KEY_PATTERN.sub("_", alert_id)
    out_path = refresh_dir / f"refresh-{safe_key}.json"
    record = {
        "alert_id": alert_id,
        "symbol": symbol,
        "next_step": next_step,
        "requested_at": routed_at,
        "source": alert.get("source"),
        "description": alert.get("description"),
        "trade_execution_allowed": False,
        "blocked_by_default": True,
        "original_alert_hash": alert.get("raw_payload_hash") or stable_hash(alert),
    }
    _write_json(out_path, record)
    return {
        "alert_id": alert_id,
        "symbol": symbol,
        "next_step": next_step,
        "routed_at": routed_at,
        "action_taken": "refresh_requested",
        "artifact_path": str(out_path),
        "suggested_commands": [],
        "safety": safety,
    }


def _route_plan_unapproved(
    alert: dict, alert_id: str, symbol: str, next_step: str,
    routed_at: str, safety: dict, alerts_dir: Path,
) -> dict:
    plan_dir = alerts_dir / "plan-requests"
    safe_key = _SAFE_KEY_PATTERN.sub("_", alert_id)
    out_path = plan_dir / f"plan-request-{safe_key}.json"
    record = {
        "alert_id": alert_id,
        "symbol": symbol,
        "next_step": next_step,
        "requested_at": routed_at,
        "source": alert.get("source"),
        "description": alert.get("description"),
        "trade_execution_allowed": False,       # explicit — never True
        "blocked_by_default": True,             # explicit — never False
        "approved_for_execution": False,        # explicit — never True
        "original_alert_hash": alert.get("raw_payload_hash") or stable_hash(alert),
        "suggested_commands": SUGGESTED_PIPELINE_COMMANDS,
        "note": (
            "Human review required before any trade plan approval. "
            "suggested_commands must NOT be run with --approve-paper."
        ),
    }
    _write_json(out_path, record)
    return {
        "alert_id": alert_id,
        "symbol": symbol,
        "next_step": next_step,
        "routed_at": routed_at,
        "action_taken": "plan_requested",
        "artifact_path": str(out_path),
        "suggested_commands": list(SUGGESTED_PIPELINE_COMMANDS),
        "safety": safety,
    }


# ---------------------------------------------------------------------------
# Log helpers
# ---------------------------------------------------------------------------

def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, indent=2, sort_keys=True, default=str)
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(text + "\n", encoding="utf-8")
    tmp.replace(path)


def _append_trigger_log(result: dict, log_path: Path) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    existing = log_path.read_text(encoding="utf-8") if log_path.exists() else ""
    if existing and not existing.endswith("\n"):
        existing += "\n"

    summary = {
        "routed_at": result.get("routed_at"),
        "alert_id": result.get("alert_id"),
        "symbol": result.get("symbol"),
        "next_step": result.get("next_step"),
        "action_taken": result.get("action_taken"),
        "artifact_path": result.get("artifact_path"),
        "safety": result.get("safety"),
    }
    block = (
        "\n## Alert routed\n\n"
        "```json\n"
        + json.dumps(summary, indent=2, sort_keys=True, default=str)
        + "\n```\n"
    )
    log_path.write_text(existing + block, encoding="utf-8")


def _append_signal_log(result: dict, log_path: Path) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    existing = log_path.read_text(encoding="utf-8") if log_path.exists() else ""
    if existing and not existing.endswith("\n"):
        existing += "\n"

    routed_at = result.get("routed_at", "")
    alert_id = result.get("alert_id", "")
    symbol = result.get("symbol", "")
    block = (
        f"\n## Alert-triggered plan request  ({routed_at})\n\n"
        f"```\n"
        f"  {symbol:8s}  alert_id={alert_id}  "
        f"next_step=request_trade_plan_unapproved  [UNAPPROVED — review required]\n"
        f"```\n"
    )
    log_path.write_text(existing + block, encoding="utf-8")
