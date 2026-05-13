#!/usr/bin/env python3
"""Route a validated external alert to its safe research action.

RESEARCH-ONLY. Never places orders, never calls execute_paper.py, never
generates approved trade plans.

Usage:
    python scripts/route_alert.py --latest
    python scripts/route_alert.py --alert-file data/history/alerts/alert-foo.json
    python scripts/route_alert.py --latest --run-pipeline

    --run-pipeline  For request_trade_plan_unapproved alerts: execute
                    scan_triggers.py then generate_trade_plan.py (no --approve-paper).
                    Ignored for all other next_step values.

Exit codes:
    0  routed successfully
    1  safety violation, missing file, or unrecoverable error

Outputs:
    data/history/alerts/{review,refresh,plan}-requests/<action>-<id>.json  (where applicable)
    memory/TRIGGER-LOG.md   append-only routing log
    memory/SIGNAL-LOG.md    append-only (request_trade_plan_unapproved only)

Safety:
- trade_execution_allowed must be false in the alert — router rejects otherwise.
- blocked_by_default must be true in the alert — router rejects otherwise.
- NEVER calls execute_paper.py.
- NEVER passes --approve-paper to generate_trade_plan.py.
- ENABLE_PAPER_EXECUTION is not read — execution is impossible from this path.
- Never prints secrets.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))

from trading_os.config import HISTORY_DIR, MEMORY_DIR
from trading_os.research.alert_router import AlertRouterError, route_alert

_ALERTS_DIR = HISTORY_DIR / "alerts"
_TRIGGER_LOG = MEMORY_DIR / "TRIGGER-LOG.md"
_SIGNAL_LOG = MEMORY_DIR / "SIGNAL-LOG.md"

_PYTHON = sys.executable


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


def _load_alert(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Alert file not found: {path}")
    try:
        with path.open("r", encoding="utf-8") as fh:
            return json.load(fh)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Alert file is not valid JSON: {path}: {exc}") from exc


def _run_pipeline(dry_run_mode: bool = False) -> int:
    """Run scan_triggers → generate_trade_plan (no --approve-paper).

    Never calls execute_paper.py.
    Never passes --approve-paper.
    """
    commands = [
        [_PYTHON, str(_ROOT / "scripts" / "scan_triggers.py")],
        [_PYTHON, str(_ROOT / "scripts" / "generate_trade_plan.py")],
        # execute_paper.py is intentionally absent
    ]
    for cmd in commands:
        label = Path(cmd[1]).name
        print(f"  [route_alert] pipeline: {' '.join(cmd)}")
        if dry_run_mode:
            print(f"  [route_alert] DRY RUN — skipping subprocess call for {label}")
            continue
        result = subprocess.run(cmd, cwd=str(_ROOT))
        if result.returncode != 0:
            print(
                f"  [route_alert] pipeline step {label} exited {result.returncode}",
                file=sys.stderr,
            )
            return result.returncode
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Route a validated alert to its safe research action (no execution).",
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--alert-file",
        metavar="PATH",
        help="Path to a specific alert JSON file.",
    )
    group.add_argument(
        "--latest",
        action="store_true",
        help="Route the most recently ingested alert in data/history/alerts/.",
    )
    parser.add_argument(
        "--run-pipeline",
        action="store_true",
        default=False,
        help=(
            "For request_trade_plan_unapproved: invoke scan_triggers.py then "
            "generate_trade_plan.py (no --approve-paper).  Ignored for other next_step values."
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=False,
        help="Log what would happen without writing artifacts or invoking the pipeline.",
    )
    args = parser.parse_args()

    # ── Load alert ────────────────────────────────────────────────────────────
    try:
        if args.alert_file:
            alert_path = Path(args.alert_file)
        else:
            alert_path = _find_latest_alert(_ALERTS_DIR)
        alert = _load_alert(alert_path)
    except (FileNotFoundError, ValueError) as exc:
        print(f"[route_alert] ERROR: {exc}", file=sys.stderr)
        return 1

    print(f"[route_alert] starting")
    print(f"  alert_file:  {alert_path}")
    print(f"  alert_id:    {alert.get('alert_id')}")
    print(f"  symbol:      {alert.get('symbol')}")
    print(f"  next_step:   {alert.get('next_step')}")
    print(f"  run_pipeline:{args.run_pipeline}")
    print(f"  dry_run:     {args.dry_run}")

    # ── Route ─────────────────────────────────────────────────────────────────
    try:
        if args.dry_run:
            # Validate safety but write nothing.
            from trading_os.research.alert_router import validate_alert_safety
            validate_alert_safety(alert)
            print(f"[route_alert] DRY RUN — safety checks pass; no artifacts written")
            print(f"  would route next_step={alert.get('next_step')!r}")
            return 0

        result = route_alert(
            alert=alert,
            alerts_dir=_ALERTS_DIR,
            trigger_log_path=_TRIGGER_LOG,
            signal_log_path=_SIGNAL_LOG,
        )
    except AlertRouterError as exc:
        print(f"[route_alert] REJECTED: {exc.reason}", file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"[route_alert] ERROR: {exc}", file=sys.stderr)
        return 1

    print(f"[route_alert] routed")
    print(f"  action_taken:  {result['action_taken']}")
    print(f"  artifact_path: {result.get('artifact_path')}")

    # ── Optionally invoke pipeline ────────────────────────────────────────────
    if args.run_pipeline and result["next_step"] == "request_trade_plan_unapproved":
        print(f"[route_alert] --run-pipeline: invoking scan + plan (no --approve-paper)")
        rc = _run_pipeline(dry_run_mode=False)
        if rc != 0:
            print(f"[route_alert] pipeline exited {rc}", file=sys.stderr)
            return rc
        print(f"[route_alert] pipeline complete — trade plan is UNAPPROVED")
    elif args.run_pipeline:
        print(
            f"[route_alert] --run-pipeline ignored for next_step={result['next_step']!r}"
        )

    print(f"[route_alert] done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
