from __future__ import annotations

import argparse
import json
from typing import Any

from .data_quality import run_data_quality_review
from .data_refresh import run_data_refresh
from .daily_summary import run_daily_summary
from .execution import execute_trade_plan
from .position_monitor import run_position_monitor
from .research_context import run_research_context
from .strategy_improvement import run_strategy_improvement_review
from .trade_plan import generate_trade_plan
from .trigger_scan import run_trigger_scan
from .weekly_review import run_weekly_review


def _print_result(result: dict[str, Any]) -> None:
    # Redacted summaries only. Secrets are never printed.
    print(json.dumps({
        "run_id": result.get("run_id"),
        "status": result.get("status") or result.get("approval", {}).get("status"),
        "generated_at": result.get("generated_at"),
    }, indent=2, sort_keys=True))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="atr-os")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("data-refresh")
    p.add_argument("--alpaca", action="store_true", help="Use Alpaca paper account/data instead of deterministic dry-run mock data.")

    sub.add_parser("trigger-scan")

    p = sub.add_parser("generate-trade-plan")
    p.add_argument("--approve-paper", action="store_true", help="Approve for paper if all deterministic gates pass. Does not submit orders.")

    p = sub.add_parser("execute-trade-plan")
    p.add_argument("--confirm-paper", action="store_true", help="Required for actual paper order submission.")
    p.add_argument("--submit", action="store_true", help="Submit paper orders if every guard passes. Default is dry-run no-submit.")

    p = sub.add_parser("position-monitor")
    p.add_argument("--alpaca", action="store_true", help="Use Alpaca for live paper account reconciliation.")

    sub.add_parser("research-context")
    sub.add_parser("data-quality-review")
    sub.add_parser("daily-summary")
    sub.add_parser("weekly-review")
    sub.add_parser("strategy-improvement-review")

    args = parser.parse_args(argv)
    if args.command == "data-refresh":
        result = run_data_refresh(dry_run=not args.alpaca)
    elif args.command == "trigger-scan":
        result = run_trigger_scan()
    elif args.command == "generate-trade-plan":
        result = generate_trade_plan(dry_run=not args.approve_paper, approve_paper=args.approve_paper)
    elif args.command == "execute-trade-plan":
        result = execute_trade_plan(dry_run=not args.submit, confirm_paper=args.confirm_paper)
    elif args.command == "position-monitor":
        result = run_position_monitor(use_alpaca=args.alpaca)
    elif args.command == "research-context":
        result = run_research_context()
    elif args.command == "data-quality-review":
        result = run_data_quality_review()
    elif args.command == "daily-summary":
        result = run_daily_summary()
    elif args.command == "weekly-review":
        result = run_weekly_review()
    elif args.command == "strategy-improvement-review":
        result = run_strategy_improvement_review()
    else:
        raise RuntimeError(f"Unhandled command: {args.command}")
    _print_result(result)
    return 0
