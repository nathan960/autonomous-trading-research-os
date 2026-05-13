#!/usr/bin/env python3
"""Route a validated external alert to its safe research action.

RESEARCH-ONLY. Never places orders, never calls execute_paper.py, never
generates approved trade plans, never passes --approve-paper.

Usage:
    # Locate alert by ID and route in record-only mode (writes route record, no scripts)
    python scripts/route_alert.py --alert-id tv-20260512-aapl-001 --route-mode record_only

    # Route the most-recently ingested alert, record-only
    python scripts/route_alert.py --latest --route-mode record_only

    # For request_data_refresh: also run refresh_data.py and monitor_positions.py
    python scripts/route_alert.py --alert-id <id> --route-mode run_refresh

    # For request_trade_plan_unapproved: run full pipeline (no --approve-paper)
    python scripts/route_alert.py --alert-id <id> --route-mode run_unapproved_plan

    # Locate alert by file path directly (backward-compat)
    python scripts/route_alert.py --alert-file data/history/alerts/alert-foo.json

route_mode allowed values:
    record_only         Write route record and logs; do not invoke any scripts.
    run_refresh         Also run refresh_data.py + monitor_positions.py.
    run_unapproved_plan Also run refresh_data.py, monitor_positions.py,
                        scan_triggers.py, generate_trade_plan.py (no --approve-paper).

Compatibility:
    log_only                      → record_only only
    request_alert_review          → record_only only
    request_data_refresh          → record_only or run_refresh
    request_trade_plan_unapproved → record_only, run_refresh, or run_unapproved_plan

Exit codes:
    0  routed successfully
    1  safety violation, missing file, incompatible route_mode, or unrecoverable error

Outputs:
    data/history/alerts/routes/<route_id>.json  route record (all next_step values)
    memory/TRIGGER-LOG.md                        append-only routing log
    memory/SIGNAL-LOG.md                         append-only (log_only, review, plan)
    memory/RESEARCH-CONTEXT.md                   append-only (request_alert_review)

Safety:
- trade_execution_allowed must be false in the alert — router rejects otherwise.
- blocked_by_default must be true in the alert — router rejects otherwise.
- Execution intent fields (execute, execute_paper, submit_order, order) are rejected.
- ENABLE_PAPER_EXECUTION must not be 'true' — checked at startup (live mode only).
- LIVE_TRADING_CONFIRMED must not be 'true' — checked at startup (live mode only).
- NEVER calls execute_paper.py.
- NEVER passes --approve-paper to generate_trade_plan.py.
- NEVER approves a trade plan.
- After run_unapproved_plan: verifies trade_plan.json has approved_for_execution=False.
- Never prints secrets.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))

from trading_os.config import HISTORY_DIR, LATEST_DIR, MEMORY_DIR
from trading_os.research.alert_router import (
    ALLOWED_ROUTE_MODES,
    AlertRouterError,
    check_trade_plan_not_approved,
    route_alert,
    scripts_for_route,
    validate_alert_safety,
    validate_route_mode,
)

_ALERTS_DIR = HISTORY_DIR / "alerts"
_TRIGGER_LOG = MEMORY_DIR / "TRIGGER-LOG.md"
_SIGNAL_LOG = MEMORY_DIR / "SIGNAL-LOG.md"
_RESEARCH_CONTEXT = MEMORY_DIR / "RESEARCH-CONTEXT.md"
_TRADE_PLAN_PATH = LATEST_DIR / "trade_plan.json"

_SAFE_KEY_PATTERN = re.compile(r"[^A-Za-z0-9_\-]")
_PYTHON = sys.executable


# ---------------------------------------------------------------------------
# Env safety gates (run when not --dry-run)
# ---------------------------------------------------------------------------

def _check_env_safety() -> None:
    """Fail if execution-related env vars are in dangerous states."""
    if os.environ.get("ENABLE_PAPER_EXECUTION", "").lower() in ("true", "1"):
        raise RuntimeError(
            "ENABLE_PAPER_EXECUTION must not be true when running route_alert.py; "
            "this path never executes orders."
        )
    if os.environ.get("LIVE_TRADING_CONFIRMED", "").lower() in ("true", "1", "yes", "y", "on"):
        raise RuntimeError(
            "LIVE_TRADING_CONFIRMED must not be true — "
            "route_alert.py refuses to run when live trading is confirmed."
        )


# ---------------------------------------------------------------------------
# Alert lookup
# ---------------------------------------------------------------------------

def _find_latest_alert(alerts_dir: Path) -> Path:
    candidates = sorted(
        alerts_dir.glob("alert-*.json"),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    if not candidates:
        raise FileNotFoundError(
            f"No alert-*.json files found in {alerts_dir}. "
            "Run scripts/ingest_alert.py first."
        )
    return candidates[0]


def _find_alert_by_id(alert_id: str, alerts_dir: Path) -> Path:
    """Locate alert-<safe_key>.json matching alert_id.

    Tries the safe-key form first, then an exact-name search.
    """
    safe_key = _SAFE_KEY_PATTERN.sub("_", alert_id)
    candidate = alerts_dir / f"alert-{safe_key}.json"
    if candidate.exists():
        return candidate
    # Broader scan in case the key used different substitution rules
    for p in alerts_dir.glob("alert-*.json"):
        try:
            with p.open("r", encoding="utf-8") as fh:
                data = json.load(fh)
            if str(data.get("alert_id", "")) == alert_id:
                return p
        except Exception:
            continue
    raise FileNotFoundError(
        f"No alert file found for alert_id={alert_id!r} in {alerts_dir}. "
        "Run scripts/ingest_alert.py first."
    )


def _load_alert(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Alert file not found: {path}")
    try:
        with path.open("r", encoding="utf-8") as fh:
            return json.load(fh)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Alert file is not valid JSON: {path}: {exc}") from exc


# ---------------------------------------------------------------------------
# Script execution
# ---------------------------------------------------------------------------

def _run_scripts(script_paths: list, dry_run: bool = False) -> tuple[int, list]:
    """Run the given script command strings sequentially.

    Returns (exit_code, scripts_actually_run).
    Never runs execute_paper.py.  Never passes --approve-paper.
    """
    ran: list = []
    for cmd_str in script_paths:
        parts = cmd_str.split()
        # Safety: never allow execute_paper.py
        if any("execute_paper" in p for p in parts):
            print(
                f"  [route_alert] SAFETY BLOCK: refused to run {cmd_str!r} — "
                "execute_paper is not permitted from this path",
                file=sys.stderr,
            )
            return 1, ran
        # Safety: never allow --approve-paper
        if "--approve-paper" in parts:
            print(
                f"  [route_alert] SAFETY BLOCK: refused to run {cmd_str!r} — "
                "--approve-paper is not permitted from this path",
                file=sys.stderr,
            )
            return 1, ran

        # Replace 'python' with current interpreter for portability
        if parts and parts[0] in ("python", "python3"):
            parts[0] = _PYTHON

        label = Path(parts[1]).name if len(parts) > 1 else cmd_str
        print(f"  [route_alert] run: {' '.join(parts)}")

        if dry_run:
            print(f"  [route_alert] DRY RUN — skipping subprocess call for {label}")
            ran.append(cmd_str)
            continue

        result = subprocess.run(parts, cwd=str(_ROOT))
        ran.append(cmd_str)
        if result.returncode != 0:
            print(
                f"  [route_alert] script {label} exited {result.returncode}",
                file=sys.stderr,
            )
            return result.returncode, ran

    return 0, ran


# ---------------------------------------------------------------------------
# Route record updater
# ---------------------------------------------------------------------------

def _update_route_record(route_record_path: str, scripts_run: list) -> None:
    """Re-write the route record with the actual scripts_run list."""
    p = Path(route_record_path)
    if not p.exists():
        return
    try:
        with p.open("r", encoding="utf-8") as fh:
            record = json.load(fh)
    except Exception:
        return
    record["scripts_run"] = scripts_run
    text = json.dumps(record, indent=2, sort_keys=True, default=str)
    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(text + "\n", encoding="utf-8")
    tmp.replace(p)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Route a validated external alert to its safe research action. "
            "Never places orders. Never calls execute_paper.py. "
            "Never generates approved trade plans."
        ),
    )

    # Alert selection — mutually exclusive
    select_group = parser.add_mutually_exclusive_group(required=True)
    select_group.add_argument(
        "--alert-id",
        metavar="ID",
        help="alert_id of the alert to route (looks up alert-<key>.json).",
    )
    select_group.add_argument(
        "--latest",
        action="store_true",
        help="Route the most recently ingested alert in data/history/alerts/.",
    )
    select_group.add_argument(
        "--alert-file",
        metavar="PATH",
        help="Path to a specific alert JSON file (backward-compat).",
    )

    parser.add_argument(
        "--route-mode",
        choices=sorted(ALLOWED_ROUTE_MODES),
        default="record_only",
        help=(
            "record_only: write route record only (default). "
            "run_refresh: also run refresh_data.py + monitor_positions.py. "
            "run_unapproved_plan: also run full pipeline (no --approve-paper). "
            "Incompatible modes for the alert's next_step are rejected."
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=False,
        help="Validate safety and print what would happen; write no artifacts.",
    )
    args = parser.parse_args()

    # ── Env safety gate ───────────────────────────────────────────────────────
    if not args.dry_run:
        try:
            _check_env_safety()
        except RuntimeError as exc:
            print(f"[route_alert] FATAL env gate: {exc}", file=sys.stderr)
            return 1

    # ── Load alert ────────────────────────────────────────────────────────────
    try:
        if args.alert_id:
            alert_path = _find_alert_by_id(args.alert_id, _ALERTS_DIR)
        elif args.alert_file:
            alert_path = Path(args.alert_file)
        else:
            alert_path = _find_latest_alert(_ALERTS_DIR)
        alert = _load_alert(alert_path)
    except (FileNotFoundError, ValueError) as exc:
        print(f"[route_alert] ERROR: {exc}", file=sys.stderr)
        return 1

    print("[route_alert] starting")
    print(f"  alert_file:  {alert_path}")
    print(f"  alert_id:    {alert.get('alert_id')}")
    print(f"  symbol:      {alert.get('symbol')}")
    print(f"  next_step:   {alert.get('next_step')}")
    print(f"  route_mode:  {args.route_mode}")
    print(f"  dry_run:     {args.dry_run}")

    # ── Dry-run: validate only ────────────────────────────────────────────────
    if args.dry_run:
        try:
            validate_alert_safety(alert)
            validate_route_mode(str(alert.get("next_step", "")), args.route_mode)
        except AlertRouterError as exc:
            print(f"[route_alert] REJECTED: {exc.reason}", file=sys.stderr)
            return 1
        to_run = scripts_for_route(str(alert.get("next_step", "")), args.route_mode)
        print(f"[route_alert] DRY RUN — safety checks pass; no artifacts written")
        print(f"  would route next_step={alert.get('next_step')!r}")
        print(f"  would run: {to_run}")
        return 0

    # ── Route ─────────────────────────────────────────────────────────────────
    try:
        result = route_alert(
            alert=alert,
            alerts_dir=_ALERTS_DIR,
            trigger_log_path=_TRIGGER_LOG,
            signal_log_path=_SIGNAL_LOG,
            research_context_path=_RESEARCH_CONTEXT,
            route_mode=args.route_mode,
        )
    except AlertRouterError as exc:
        print(f"[route_alert] REJECTED: {exc.reason}", file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"[route_alert] ERROR: {exc}", file=sys.stderr)
        return 1

    print(f"[route_alert] routed")
    print(f"  action_taken:      {result['action_taken']}")
    print(f"  route_record_path: {result.get('route_record_path')}")

    # ── Execute scripts if route_mode requires it ─────────────────────────────
    to_run = scripts_for_route(result["next_step"], args.route_mode)
    scripts_actually_run: list = []

    if to_run:
        print(f"[route_alert] route_mode={args.route_mode!r}: running {len(to_run)} script(s)")
        rc, scripts_actually_run = _run_scripts(to_run, dry_run=False)
        _update_route_record(result["route_record_path"], scripts_actually_run)

        if rc != 0:
            print(
                f"[route_alert] pipeline exited {rc} — "
                "route record written but pipeline incomplete",
                file=sys.stderr,
            )
            return rc

        print(f"[route_alert] scripts complete  ran={len(scripts_actually_run)}")

        # ── Safety check: trade plan must not be approved ─────────────────────
        if args.route_mode == "run_unapproved_plan":
            try:
                check_trade_plan_not_approved(_TRADE_PLAN_PATH)
            except AlertRouterError as exc:
                print(f"[route_alert] SAFETY VIOLATION: {exc.reason}", file=sys.stderr)
                return 1
            print("[route_alert] trade plan approval check passed — plan is UNAPPROVED")

    else:
        print(
            f"[route_alert] route_mode={args.route_mode!r}: "
            "record_only — no scripts invoked"
        )

    print(
        f"[route_alert] done  "
        f"route_id={result['route_id']}  "
        f"action={result['action_taken']}  "
        f"scripts_run={len(scripts_actually_run)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
