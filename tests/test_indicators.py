from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from autonomous_trading_research_os.indicators import latest_indicator_snapshot
from autonomous_trading_research_os.mock_data import generate_symbol_bars


class IndicatorTests(unittest.TestCase):
    def test_mock_spy_indicators_ready(self) -> None:
        bars = generate_symbol_bars("SPY", 320)
        snapshot = latest_indicator_snapshot("SPY", bars)
        self.assertTrue(snapshot["is_ready"])
        self.assertGreater(snapshot["latest_close"], 0)
        self.assertIsNotNone(snapshot["roc126"])
        self.assertIsNotNone(snapshot["roc252"])
        self.assertIsNotNone(snapshot["atr_pct"])


if __name__ == "__main__":
    unittest.main()
