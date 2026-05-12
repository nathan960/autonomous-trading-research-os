from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))

from autonomous_trading_research_os.data_refresh import run_data_refresh
from autonomous_trading_research_os.execution import execute_trade_plan
from autonomous_trading_research_os.trade_plan import generate_trade_plan
from autonomous_trading_research_os.trigger_scan import run_trigger_scan

_LATEST_DIR = _ROOT / "data" / "latest"
_RESTORED_FILES = [
    "trigger_snapshot.json",
    "trade_plan.json",
    "market_snapshot.json",
    "positions_snapshot.json",
    "orders_snapshot.json",
    "account_snapshot.json",
]


class DryRunPipelineTests(unittest.TestCase):
    def setUp(self) -> None:
        self._saved: dict = {}
        for fname in _RESTORED_FILES:
            p = _LATEST_DIR / fname
            if p.exists():
                self._saved[fname] = p.read_bytes()

    def tearDown(self) -> None:
        for fname, content in self._saved.items():
            (_LATEST_DIR / fname).write_bytes(content)

    def test_dry_run_pipeline_blocks_submission(self) -> None:
        run_data_refresh(dry_run=True)
        trigger = run_trigger_scan()
        plan = generate_trade_plan(dry_run=True, approve_paper=False)
        execution = execute_trade_plan(dry_run=True, confirm_paper=False)
        self.assertIn("risk_on", trigger["regime"])
        self.assertEqual(plan["approval"]["status"], "DRY_RUN_ONLY")
        self.assertEqual(execution["status"], "DRY_RUN_NO_SUBMISSION")


if __name__ == "__main__":
    unittest.main()
