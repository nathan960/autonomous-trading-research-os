from __future__ import annotations

import os
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from autonomous_trading_research_os.settings import RuntimeSettings
from autonomous_trading_research_os.risk import classify_symbol


class RiskGateTests(unittest.TestCase):
    def test_live_mode_is_blocked(self) -> None:
        old = os.environ.get("TRADING_MODE")
        os.environ["TRADING_MODE"] = "live"
        try:
            with self.assertRaises(RuntimeError):
                RuntimeSettings.from_env().validate_paper_only()
        finally:
            if old is None:
                os.environ.pop("TRADING_MODE", None)
            else:
                os.environ["TRADING_MODE"] = old

    def test_crypto_like_symbol_classified(self) -> None:
        self.assertEqual(classify_symbol("BTC/USD"), "crypto_like")


if __name__ == "__main__":
    unittest.main()
