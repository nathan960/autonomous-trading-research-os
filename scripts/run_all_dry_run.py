#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from autonomous_trading_research_os.data_quality import run_data_quality_review
from autonomous_trading_research_os.data_refresh import run_data_refresh
from autonomous_trading_research_os.daily_summary import run_daily_summary
from autonomous_trading_research_os.execution import execute_trade_plan
from autonomous_trading_research_os.position_monitor import run_position_monitor
from autonomous_trading_research_os.research_context import run_research_context
from autonomous_trading_research_os.strategy_improvement import run_strategy_improvement_review
from autonomous_trading_research_os.trade_plan import generate_trade_plan
from autonomous_trading_research_os.trigger_scan import run_trigger_scan
from autonomous_trading_research_os.weekly_review import run_weekly_review


def main() -> int:
    results = {
        "data_refresh": run_data_refresh(dry_run=True),
        "trigger_scan": run_trigger_scan(),
        "trade_plan": generate_trade_plan(dry_run=True, approve_paper=False),
        "execution": execute_trade_plan(dry_run=True, confirm_paper=False),
        "position_monitor": run_position_monitor(use_alpaca=False),
        "data_quality": run_data_quality_review(),
        "research_context": run_research_context(),
        "daily_summary": run_daily_summary(),
        "weekly_review": run_weekly_review(),
        "strategy_improvement": run_strategy_improvement_review(),
    }
    print(json.dumps({name: {"run_id": result.get("run_id"), "status": result.get("status") or result.get("approval", {}).get("status")} for name, result in results.items()}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
