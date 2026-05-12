# Execute Paper Trade Plan

Run Layer 4 Trade Execution. Submit Alpaca paper orders only if `trade_plan.json` is fresh, approved, and every gate passes. Revalidate Alpaca state. Command: `python scripts/execute_trade_plan.py --submit --confirm-paper`. If any gate fails, fail closed and log the skip.

Always run compile checks first, never print secrets, never force-push, and preserve auditability.
