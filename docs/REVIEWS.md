# Daily Summary and Weekly Review

Research-only audit tools. No execution path. Never place orders.

---

## Overview

| Script | Workflow | Output |
|--------|----------|--------|
| `scripts/daily_summary.py` | `daily-summary.yml` | `data/history/runs/daily_summary-<date>-<hash>.json`, `memory/DAILY-SUMMARY.md` |
| `scripts/weekly_review.py` | `weekly-review.yml` | `data/history/runs/weekly_review-<date>-<hash>.json`, `memory/WEEKLY-REVIEW.md`, `memory/EXPERIMENT-LOG.md` |

---

## Daily Summary

### What it reads
- `data/latest/account_snapshot.json`
- `data/latest/positions_snapshot.json`
- `data/latest/orders_snapshot.json`
- `data/latest/trigger_snapshot.json`
- `data/latest/trade_plan.json`
- `data/latest/execution_report.json`
- `data/latest/order_monitor_report.json`
- `data/latest/data_quality_report.json`
- `memory/RISK-STATE.json`
- `data/history/executions/execution-<date>*_dry_run.json`
- `data/history/executions/execution-<date>*_paper.json`
- `data/history/orders/order_monitor-<date>*.json`
- `data/history/alerts/alert-*.json`
- `data/history/alerts/routes/route_*.json`

### What it writes
| File | Mode |
|------|------|
| `data/history/runs/daily_summary-<YYYY-MM-DD>-<hash8>.json` | Create |
| `memory/DAILY-SUMMARY.md` | Append |

### Usage
```bash
# Today
python scripts/daily_summary.py

# Specific date
python scripts/daily_summary.py --date 2026-05-13

# Preview without writing
python scripts/daily_summary.py --dry-run
```

### GitHub Actions
**Workflow:** `.github/workflows/daily-summary.yml`

| Input | Default | Description |
|-------|---------|-------------|
| `date` | (today) | YYYY-MM-DD date to summarise |

Scheduled: weekdays at 21:00 UTC (after market close + position monitoring).

---

## Weekly Review

### What it aggregates (last 7 days by default)
- Trigger scans from `data/history/triggers/YYYY-MM-DD.jsonl`
- Dry-run execution reports from `data/history/executions/`
- Paper execution reports from `data/history/executions/`
- Order monitor runs from `data/history/orders/`
- External alerts and route records from `data/history/alerts/`
- Latest data quality report and risk state

### What it writes
| File | Mode |
|------|------|
| `data/history/runs/weekly_review-<YYYY-MM-DD>-<hash8>.json` | Create |
| `memory/WEEKLY-REVIEW.md` | Append |
| `memory/EXPERIMENT-LOG.md` | Append (only when issues/observations exist) |

### Usage
```bash
# Last 7 days
python scripts/weekly_review.py

# Specific end date
python scripts/weekly_review.py --date 2026-05-13

# Longer look-back
python scripts/weekly_review.py --days 14

# Preview without writing
python scripts/weekly_review.py --dry-run
```

### GitHub Actions
**Workflow:** `.github/workflows/weekly-review.yml`

| Input | Default | Description |
|-------|---------|-------------|
| `date` | (today) | End date of the review window |
| `days` | `7` | Number of days to look back |

Scheduled: Fridays at 21:30 UTC.

---

## Output JSON Schema

### daily_summary-*.json
```json
{
  "run_id": "daily_summary-2026-05-13",
  "date": "2026-05-13",
  "generated_at": "...",
  "status": "ok",
  "summary_hash": "16 hex chars",
  "account": { "equity": 99803.09, "cash": ..., "buying_power": ... },
  "risk_state": { "drawdown": 0.0, "peak_equity": ..., "position_count": 1 },
  "positions": [ { "symbol": "WELL", "side": "long", ... } ],
  "open_orders": [],
  "trigger_scan": { "risk_on": true, "candidates_count": 27, ... },
  "trade_plan": {
    "plan_id": "...",
    "approved_for_execution": false,
    "proposed_orders": [ { "symbol": "BLK", "side": "buy", ... } ]
  },
  "execution_report": { "all_gates_pass": true, "failed_gates": [] },
  "dry_runs": { "count": 3, "fail_count": 1, "failing_gates": { "RISK_STATE_NOT_PAUSED": 1 } },
  "paper_executions": { "count": 1, "total_orders_submitted": 1 },
  "order_monitor": { "orders_tracked": 1, "orders_filled": 0, "orders_missing": 1 },
  "alerts": { "total_count": 8, "ingested_today": 1, "by_next_step": {...} },
  "alert_routes": { "total_routes": 4, "execution_called_any": false, "approved_trade_plan_created_any": false },
  "data_quality": { "status": "PASS", "issues_count": 0 }
}
```

### weekly_review-*.json
```json
{
  "run_id": "weekly_review-2026-05-13",
  "period_start": "2026-05-07",
  "period_end": "2026-05-13",
  "days": 7,
  "generated_at": "...",
  "status": "ok",
  "review_hash": "16 hex chars",
  "trigger_scans": { "total_runs": 5, "risk_on_sessions": 5, "avg_candidates": 27.0 },
  "dry_runs": { "total_runs": 5, "fail_count": 5, "failing_gates": { "RISK_STATE_NOT_PAUSED": 5 } },
  "paper_executions": { "total_attempts": 1, "total_orders_submitted": 1 },
  "order_monitor": { "total_runs": 6, "fills": 1, "missing": 0 },
  "alerts": { "alerts_this_period": 2, "routes_this_period": 2, "execution_called_any": false },
  "data_quality": { "latest_status": "PASS" },
  "risk_state": { "drawdown": 0.0, "peak_equity": 99803.09 },
  "operational_issues": [],
  "research_observations": [ "Market regime: 5/5 sessions risk_on (100%)." ],
  "proposed_experiments": []
}
```

---

## Memory Log Locations

| File | Written by | Content |
|------|-----------|---------|
| `memory/DAILY-SUMMARY.md` | `daily_summary.py` | Append-only; one entry per run |
| `memory/WEEKLY-REVIEW.md` | `weekly_review.py` | Append-only; one entry per run |
| `memory/EXPERIMENT-LOG.md` | `weekly_review.py` | Append-only; experiment candidates only. **Never modifies strategy or risk limits.** |

---

## Safety Constraints

Both scripts and modules enforce the same safety rules as the rest of the system:

- `ENABLE_PAPER_EXECUTION=false` hardcoded in both workflows
- `LIVE_TRADING_CONFIRMED=false` hardcoded in both workflows
- `execute_paper.py` is never called or imported
- `--approve-paper` is never passed
- `config/strategy.json` and `config/risk_limits.json` are never written
- `approved_for_execution` is only read (for auditing), never set
