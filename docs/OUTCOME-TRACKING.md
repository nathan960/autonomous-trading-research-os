# Trade Outcome Tracking

Research-only tool to track paper trade performance over time. No execution path.

---

## Overview

| Script | Workflow | Output |
|--------|----------|--------|
| `scripts/track_outcomes.py` | `outcome-tracker.yml` | `data/latest/outcome_snapshot.json`, `data/history/outcomes/outcome_<date>-<hash8>.json`, `memory/TRADE-LOG.md`, `memory/EXPERIMENT-LOG.md` |

---

## What it reads

- `data/latest/order_monitor_report.json` — filled lifecycle entries
- `data/latest/positions_snapshot.json` — current positions (unrealized P/L)
- `data/latest/market_snapshot.json` — current prices (SPY, BIL, individual symbols)
- `data/latest/outcome_snapshot.json` — existing outcome records (merged, not replaced)

---

## What it writes

| File | Mode |
|------|------|
| `data/latest/outcome_snapshot.json` | Replaced each run |
| `data/history/outcomes/outcome_<YYYY-MM-DD>-<hash8>.json` | Create |
| `memory/TRADE-LOG.md` | Append |
| `memory/EXPERIMENT-LOG.md` | Append (observations only, never strategy changes) |

---

## How it works

1. Reads filled orders from `order_monitor_report.json["lifecycles"]`.
2. For each filled order, builds an outcome record with:
   - Identity: `client_order_id`, `broker_order_id`, `symbol`, `side`
   - Execution: `fill_price`, `limit_price`, `filled_qty`, `filled_notional`, `slippage_vs_limit`
   - Plan context: `plan_id`, `run_id`, `trade_plan_hash`, `trigger_snapshot_hash`
   - Current state: `current_price`, `current_position_qty`, `current_unrealized_pl`, `current_return_pct`
   - Benchmarks: `spy_price_at_check`, `bil_price_at_check`
   - Outcome windows: `same_day`, `1_trading_day`, `5_trading_days`, `20_trading_days`, `63_trading_days`
3. Merges with any existing outcomes from `data/latest/outcome_snapshot.json`. For the same `client_order_id`, later `checked_at` wins.
4. Writes snapshot and appends to memory files.

---

## Outcome windows

| Window | Status becomes "elapsed" when |
|--------|-------------------------------|
| `same_day` | Calendar date advances past fill date |
| `1_trading_day` | ≥ 1.3 calendar days since fill |
| `5_trading_days` | ≥ 7 calendar days since fill |
| `20_trading_days` | ≥ 28 calendar days since fill |
| `63_trading_days` | ≥ 91 calendar days since fill |

When a window is `pending`, no return is recorded yet. When `elapsed`, the
current price at that check is used as an approximation. For exact window
returns, a historical price lookup would be needed (not yet implemented).

---

## Output JSON schema

### outcome_snapshot.json

```json
{
  "run_id": "outcome_tracker-20260513T195351-015ef98f",
  "generated_at": "2026-05-13T19:53:51Z",
  "outcomes_count": 3,
  "snapshot_hash": "16 hex chars",
  "outcomes": [
    {
      "client_order_id": "TOS-20260513T160035-WELL-BUY",
      "broker_order_id": "a57f3df1-...",
      "symbol": "WELL",
      "side": "buy",
      "entry_or_exit": "entry",
      "plan_id": "trade_plan-20260513T160035-0460e121",
      "run_id": "execution-20260513T160036-b4ad22c3",
      "trade_plan_hash": "...",
      "trigger_snapshot_hash": null,
      "filled_at": "2026-05-13T16:00:36Z",
      "fill_price": 218.808,
      "limit_price": 218.9,
      "filled_qty": 0.11425542,
      "filled_notional": 25.0,
      "slippage_vs_limit": -0.092,
      "slippage_pct": -0.00042,
      "current_price": 220.85,
      "current_position_qty": 0.11425542,
      "current_market_value": 25.23,
      "current_unrealized_pl": 0.23,
      "current_unrealized_pl_pct": 0.00933,
      "current_return_pct": 0.00935,
      "spy_price_at_check": 743.265,
      "bil_price_at_check": 91.495,
      "outcome_windows": {
        "same_day": {"status": "pending"},
        "1_trading_day": {"status": "pending"},
        "5_trading_days": {"status": "pending"},
        "20_trading_days": {"status": "pending"},
        "63_trading_days": {"status": "pending"}
      },
      "lifecycle_status": "filled",
      "checked_at": "2026-05-13T19:53:51Z",
      "first_seen_at": "2026-05-13T19:53:51Z"
    }
  ]
}
```

---

## Usage

```bash
# Run with full writes
python scripts/track_outcomes.py

# Preview without writing files
python scripts/track_outcomes.py --dry-run
```

### GitHub Actions

**Workflow:** `.github/workflows/outcome-tracker.yml`

Scheduled: weekdays at 21:15 UTC (after order-monitor and daily-summary).

---

## Deduplication

Outcome records are keyed by `client_order_id`. If the same order appears in
multiple monitor reports, only the record with the latest `checked_at` is kept.
`first_seen_at` is preserved from the original record and never overwritten.

---

## Safety constraints

- `ENABLE_PAPER_EXECUTION=false` hardcoded in workflow
- `LIVE_TRADING_CONFIRMED=false` hardcoded in workflow
- `execute_paper.py` is never called or imported
- `--approve-paper` is never passed
- `config/strategy.json` and `config/risk_limits.json` are never written
- `approved_for_execution` is never set
- Orders are never submitted, cancelled, or replaced

---

## Memory log locations

| File | Written by | Content |
|------|-----------|---------|
| `memory/TRADE-LOG.md` | `track_outcomes.py` | Append-only; one entry per run |
| `memory/EXPERIMENT-LOG.md` | `track_outcomes.py` | Append-only; unrealized return observations only |
