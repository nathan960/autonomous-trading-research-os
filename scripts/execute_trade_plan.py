#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from autonomous_trading_research_os.execution import execute_trade_plan


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--submit', action='store_true', help='Submit paper orders if every guard passes. Default is dry-run no-submit.')
    parser.add_argument('--confirm-paper', action='store_true', help='Required for actual paper order submission.')
    args = parser.parse_args()
    result = execute_trade_plan(dry_run=not args.submit, confirm_paper=args.confirm_paper)
    print(json.dumps({
        "run_id": result.get("run_id"),
        "status": result.get("status") or result.get("approval", {}).get("status"),
        "generated_at": result.get("generated_at"),
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
