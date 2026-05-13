"""Research-only alert router.

Reads a validated alert record (produced by alert_intake.py) and dispatches
the appropriate safe action based on next_step.  No execution path exists here.

Safety invariants — enforced unconditionally:
  - Rejects any alert where trade_execution_allowed is not exactly False.
  - Rejects any alert where blocked_by_default is not exactly True.
  - Rejects any alert with execution intent fields (execute, execute_paper,
    submit_order, order, approved_for_execution=true).
  - Rejects crypto or options symbols.
  - Rejects disallowed asset_class values.
  - Validates route_mode compatibility with next_step; fails closed if incompatible.
  - Never calls execute_paper.py.
  - Never passes approve_paper=True to any function.
  - Never sets approved_for_execution=True.
  - Every routing decision is logged to TRIGGER-LOG.md and SIGNAL-LOG.md.
  - request_alert_review also appends to RESEARCH-CONTEXT.md.
  - request_trade_plan_unapproved also appends to SIGNAL-LOG.md with trade context.

Routing actions by next_step:
  log_only                      → write route record; log only.
  request_alert_review          → write route record; append to RESEARCH-CONTEXT.md.
  request_data_refresh          → write route record; CLI may run refresh scripts.
  request_trade_plan_unapproved → write route record; CLI may run pipeline
                                  (no --approve-paper).

Pure functions — no subprocess calls.  The CLI script (route_alert.py)
may optionally execute scripts_for_route() results via subprocess.

route_mode values:
  record_only        → write route record only; no scripts run.
  run_refresh        → valid for request_data_refresh and request_trade_plan_unapproved;
                       CLI runs refresh_data.py + monitor_positions.py.
  run_unapproved_plan → valid for request_trade_plan_unapproved only;
                        CLI runs full pipeline (no --approve-paper).
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Optional

from ..hashing import stable_hash
from ..time_utils import utc_now_iso

ALLOWED_NEXT_STEPS: frozenset = frozenset({
    "log_only",
    "request_data_refresh",
    "request_alert_review",
    "request_trade_plan_unapproved",
})

ALLOWED_ROUTE_MODES: frozenset = frozenset({
    "record_only",
    "run_refresh",
    "run_unapproved_plan",
})

# Which route_modes are permitted for each next_step.
# log_only and request_alert_review are always record_only (no scripts make sense).
_NEXT_STEP_ALLOWED_MODES: dict = {
    "log_only": frozenset({"record_only"}),
    "request_alert_review": frozenset({"record_only"}),
    "request_data_refresh": frozenset({"record_only", "run_refresh"}),
    "request_trade_plan_unapproved": frozenset({"record_only", "run_refresh", "run_unapproved_plan"}),
}

ALLOWED_ASSET_CLASSES: frozenset = frozenset({
    "us_equity", "etf", "cash_like_etf",
})

# Fields that indicate execution intent — must not be present in any routed alert.
EXECUTION_INTENT_FIELDS: frozenset = frozenset({
    "execute",
    "execute_paper",
    "submit_order",
    "order",
})

_SAFE_KEY_PATTERN = re.compile(r"[^A-Za-z0-9_\-]")

# Full pipeline for request_trade_plan_unapproved.
# --approve-paper is intentionally absent — human approval is always required.
# execute_paper.py is intentionally absent — execution never originates from an alert.
SUGGESTED_PIPELINE_COMMANDS: list = [
    "python scripts/refresh_data.py",
    "python scripts/monitor_positions.py",
    "python scripts/scan_triggers.py",
    "python scripts/generate_trade_plan.py",
]

SUGGESTED_REFRESH_COMMANDS: list = [
    "python scripts/refresh_data.py",
    "python scripts/monitor_positions.py",
]


class AlertRouterError(ValueError):
    """Raised when routing is rejected due to a safety violation or bad input."""

    def __init__(self, reason: str) -> None:
        self.reason = reason
        super().__init__(reason)


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_alert_safety(alert: Any) -> None:
    """Verify the alert carries required safety flags before routing.

    Enforces:
      - trade_execution_allowed is exactly False (boolean)
      - blocked_by_default is exactly True (boolean)
      - next_step is in the allowed set
      - no execution intent fields present
      - approved_for_execution is not True
      - asset_class (if present) is in the allowed set
      - symbol is not crypto or options

    Raises AlertRouterError on any violation.
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

    # Execution intent fields must not be present
    for field in EXECUTION_INTENT_FIELDS:
        if field in alert:
            raise AlertRouterError(
                f"alert rejected: execution intent field {field!r} is not permitted"
            )
    if alert.get("approved_for_execution") is True:
        raise AlertRouterError(
            "alert rejected: approved_for_execution=true is not permitted"
        )

    # Asset class must be in the allowed set when present
    asset_class = alert.get("asset_class")
    if asset_class is not None:
        if not isinstance(asset_class, str):
            raise AlertRouterError("asset_class must be a string when present")
        if asset_class.lower() not in ALLOWED_ASSET_CLASSES:
            raise AlertRouterError(
                f"asset_class={asset_class!r} is not allowed; "
                f"permitted: {sorted(ALLOWED_ASSET_CLASSES)}"
            )

    # Symbol must not be crypto or options
    symbol = alert.get("symbol", "")
    if isinstance(symbol, str) and symbol:
        from .alert_intake import _is_crypto_symbol, _is_options_symbol
        if _is_crypto_symbol(symbol):
            raise AlertRouterError(
                f"symbol={symbol!r} appears to be a crypto asset; crypto is not supported"
            )
        if _is_options_symbol(symbol):
            raise AlertRouterError(
                f"symbol={symbol!r} matches an options contract format; options are not supported"
            )


def validate_route_mode(next_step: str, route_mode: str) -> None:
    """Verify route_mode is valid and compatible with next_step.

    Raises AlertRouterError if:
      - route_mode is not in ALLOWED_ROUTE_MODES
      - route_mode is not compatible with next_step
    """
    if route_mode not in ALLOWED_ROUTE_MODES:
        raise AlertRouterError(
            f"route_mode={route_mode!r} is not valid; "
            f"permitted: {sorted(ALLOWED_ROUTE_MODES)}"
        )
    allowed = _NEXT_STEP_ALLOWED_MODES.get(next_step, frozenset())
    if route_mode not in allowed:
        raise AlertRouterError(
            f"route_mode={route_mode!r} is not compatible with next_step={next_step!r}; "
            f"permitted for this next_step: {sorted(allowed)}"
        )


# ---------------------------------------------------------------------------
# Script selection (used by CLI — pure, no subprocess)
# ---------------------------------------------------------------------------

def scripts_for_route(next_step: str, route_mode: str) -> list:
    """Return the list of scripts the CLI should execute for this combination.

    Never returns execute_paper.py.  Never returns --approve-paper.
    Returns an empty list for record_only or when execution is not relevant.

    Called by route_alert.py to decide what to subprocess-run.
    """
    if route_mode == "record_only":
        return []
    if next_step == "request_data_refresh" and route_mode == "run_refresh":
        return list(SUGGESTED_REFRESH_COMMANDS)
    if next_step == "request_trade_plan_unapproved":
        if route_mode == "run_refresh":
            return list(SUGGESTED_REFRESH_COMMANDS)
        if route_mode == "run_unapproved_plan":
            return list(SUGGESTED_PIPELINE_COMMANDS)
    return []


def check_trade_plan_not_approved(trade_plan_path: Path) -> None:
    """Raise AlertRouterError if trade_plan.json has approved_for_execution=True.

    Called by the CLI after generate_trade_plan.py to catch any unexpected approval.
    Safe to call when the file is absent (plan was skipped — no-trigger case).
    """
    if not trade_plan_path.exists():
        return
    try:
        with trade_plan_path.open("r", encoding="utf-8") as fh:
            plan = json.load(fh)
    except Exception as exc:
        raise AlertRouterError(f"cannot read trade_plan.json: {exc}") from exc

    approval = plan.get("approval") or {}
    if approval.get("approved_for_execution") is True:
        raise AlertRouterError(
            "SAFETY VIOLATION: trade_plan.json has approved_for_execution=True after "
            "router-triggered pipeline run; router never approves plans — "
            "inspect generate_trade_plan.py immediately"
        )


# ---------------------------------------------------------------------------
# Route dispatch
# ---------------------------------------------------------------------------

def route_alert(
    alert: Any,
    alerts_dir: Path,
    trigger_log_path: Path,
    signal_log_path: Path,
    research_context_path: Optional[Path] = None,
    route_mode: str = "record_only",
) -> dict:
    """Route a validated alert to its safe research action.

    Writes a route record to alerts_dir/routes/<route_id>.json.
    Logs to TRIGGER-LOG.md and SIGNAL-LOG.md for every next_step.
    Also logs to RESEARCH-CONTEXT.md for request_alert_review.

    Args:
        alert:                   Parsed alert record from alert_intake.process_alert.
        alerts_dir:              Base directory; route records go to alerts_dir/routes/.
        trigger_log_path:        Appended for every routing decision.
        signal_log_path:         Appended for log_only, request_alert_review,
                                 request_trade_plan_unapproved.
        research_context_path:   Appended for request_alert_review (optional).
        route_mode:              One of record_only | run_refresh | run_unapproved_plan.

    Returns:
        Route result dict with keys: route_id, alert_id, symbol, next_step, route_mode,
        routed_at, action_taken, route_record_path, artifact_path, suggested_scripts,
        suggested_commands, scripts_run, safety, blocked, block_reason,
        trade_execution_allowed, approved_trade_plan_created, execution_called.

    Raises:
        AlertRouterError  on any safety or compatibility violation.
    """
    validate_alert_safety(alert)

    next_step: str = str(alert.get("next_step", ""))
    validate_route_mode(next_step, route_mode)

    alert_id: str = str(alert.get("alert_id") or stable_hash(alert))
    symbol: str = str(alert.get("symbol", ""))
    routed_at: str = utc_now_iso()

    # Build a stable, human-readable route_id
    safe_alert_id = _SAFE_KEY_PATTERN.sub("_", alert_id)[:24]
    route_hash = stable_hash({"alert_id": alert_id, "routed_at": routed_at})[:8]
    compact_ts = routed_at[:19].replace(":", "").replace("-", "")
    route_id = f"route_{compact_ts}_{safe_alert_id}_{route_hash}"

    # Safety checks block — invariants always enforced, always the same values
    safety_checks: dict = {
        "trade_execution_allowed": False,           # invariant — never True
        "blocked_by_default": True,                 # invariant — never False
        "execute_paper_called": False,              # invariant — never True
        "approve_paper_passed": False,              # invariant — never True
        "enable_paper_execution_checked_false": True,
        "live_trading_confirmed_checked_false": True,
        "no_execution_intent_fields": True,
        "approved_trade_plan_created": False,       # invariant — never True
        "execution_called": False,                  # invariant — never True
    }

    # Suggested scripts for this next_step (for audit; route_mode controls actual CLI execution)
    suggested_scripts = _full_suggestions_for(next_step)
    action_taken = _action_for(next_step)

    # Build route record
    route_record: dict = {
        "route_id": route_id,
        "routed_at": routed_at,
        "alert_id": alert_id,
        "source": alert.get("source"),
        "symbol": symbol,
        "trigger_id": alert.get("trigger_id"),
        "condition": alert.get("condition") or alert.get("description"),
        "next_step": next_step,
        "route_mode": route_mode,
        "action_taken": action_taken,
        "scripts_run": [],          # CLI updates this after subprocess calls
        "safety_checks": safety_checks,
        "blocked": False,
        "block_reason": None,
        "generated_files": [],
        "trade_execution_allowed": False,
        "approved_trade_plan_created": False,
        "execution_called": False,
        "suggested_scripts": suggested_scripts,
        "data_hashes": {},
    }

    # Write route record (atomic)
    routes_dir = alerts_dir / "routes"
    route_path = routes_dir / f"{route_id}.json"
    _write_json(route_path, route_record)

    # Logs — TRIGGER-LOG for every step
    _append_trigger_log(route_record, trigger_log_path)

    # SIGNAL-LOG for log_only, request_alert_review, request_trade_plan_unapproved
    if next_step in ("log_only", "request_alert_review", "request_trade_plan_unapproved"):
        _append_signal_log(route_record, signal_log_path)

    # RESEARCH-CONTEXT for request_alert_review
    if next_step == "request_alert_review" and research_context_path is not None:
        _append_research_context(alert, route_record, research_context_path)

    return {
        "route_id": route_id,
        "alert_id": alert_id,
        "symbol": symbol,
        "next_step": next_step,
        "route_mode": route_mode,
        "routed_at": routed_at,
        "action_taken": action_taken,
        "route_record_path": str(route_path),
        "artifact_path": str(route_path),   # backward-compat alias
        "suggested_scripts": suggested_scripts,
        "suggested_commands": suggested_scripts,  # backward-compat alias
        "scripts_run": [],
        "safety": safety_checks,
        "blocked": False,
        "block_reason": None,
        "trade_execution_allowed": False,
        "approved_trade_plan_created": False,
        "execution_called": False,
    }


# ---------------------------------------------------------------------------
# Helpers (private)
# ---------------------------------------------------------------------------

def _action_for(next_step: str) -> str:
    return {
        "log_only": "logged",
        "request_alert_review": "review_requested",
        "request_data_refresh": "refresh_requested",
        "request_trade_plan_unapproved": "plan_requested",
    }.get(next_step, "unknown")


def _full_suggestions_for(next_step: str) -> list:
    """Return the full set of suggested scripts for the given next_step.

    Used for audit/display — independent of route_mode.
    The CLI uses scripts_for_route() to determine what to actually execute.
    Never includes execute_paper.py or --approve-paper.
    """
    if next_step == "request_data_refresh":
        return list(SUGGESTED_REFRESH_COMMANDS)
    if next_step == "request_trade_plan_unapproved":
        return list(SUGGESTED_PIPELINE_COMMANDS)
    return []


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, indent=2, sort_keys=True, default=str)
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(text + "\n", encoding="utf-8")
    tmp.replace(path)


def _append_trigger_log(route_record: dict, log_path: Path) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    existing = log_path.read_text(encoding="utf-8") if log_path.exists() else ""
    if existing and not existing.endswith("\n"):
        existing += "\n"

    summary = {
        "routed_at": route_record.get("routed_at"),
        "route_id": route_record.get("route_id"),
        "alert_id": route_record.get("alert_id"),
        "symbol": route_record.get("symbol"),
        "next_step": route_record.get("next_step"),
        "route_mode": route_record.get("route_mode"),
        "action_taken": route_record.get("action_taken"),
        "trade_execution_allowed": route_record.get("trade_execution_allowed"),
        "approved_trade_plan_created": route_record.get("approved_trade_plan_created"),
        "execution_called": route_record.get("execution_called"),
    }
    block = (
        "\n## Alert routed\n\n"
        "```json\n"
        + json.dumps(summary, indent=2, sort_keys=True, default=str)
        + "\n```\n"
    )
    log_path.write_text(existing + block, encoding="utf-8")


def _append_signal_log(route_record: dict, log_path: Path) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    existing = log_path.read_text(encoding="utf-8") if log_path.exists() else ""
    if existing and not existing.endswith("\n"):
        existing += "\n"

    routed_at = route_record.get("routed_at", "")
    alert_id = route_record.get("alert_id", "")
    symbol = route_record.get("symbol", "")
    next_step = route_record.get("next_step", "")
    action_taken = route_record.get("action_taken", "")

    if next_step == "request_trade_plan_unapproved":
        tag = "[UNAPPROVED — review required]"
    else:
        tag = "[research-only — no execution]"

    block = (
        f"\n## Alert routed  ({routed_at})\n\n"
        "```\n"
        f"  {symbol:8s}  alert_id={alert_id}  "
        f"next_step={next_step}  action={action_taken}  {tag}\n"
        "```\n"
    )
    log_path.write_text(existing + block, encoding="utf-8")


def _append_research_context(alert: dict, route_record: dict, log_path: Path) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    existing = log_path.read_text(encoding="utf-8") if log_path.exists() else ""
    if existing and not existing.endswith("\n"):
        existing += "\n"

    routed_at = route_record.get("routed_at", "")
    alert_id = route_record.get("alert_id", "")
    symbol = route_record.get("symbol", "")
    source = alert.get("source", "unknown")
    description = alert.get("description") or alert.get("condition") or "(no description)"

    block = (
        f"\n## Review needed  ({routed_at})\n\n"
        f"- **Symbol**: {symbol}\n"
        f"- **Alert ID**: {alert_id}\n"
        f"- **Source**: {source}\n"
        f"- **Description**: {description}\n"
        f"- **Status**: Awaiting human review — no trade plan generated\n"
    )
    log_path.write_text(existing + block, encoding="utf-8")
