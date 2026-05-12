# Data Refresh

Run Layer 1 Data Refresh. Use Alpaca only for trade-critical data. Do not place trades. Compile first, run `python scripts/data_refresh.py --alpaca`, inspect `data/latest/market_snapshot.json`, append findings, show diff, then commit/push or open PR.

Always run compile checks first, never print secrets, never force-push, and preserve auditability.
