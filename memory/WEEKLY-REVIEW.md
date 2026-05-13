# Weekly Review

Weekly summaries of triggers, skips, trades, drawdown, data quality, and operations.

## Weekly review

```json
{
  "data_quality_entries": 2,
  "generated_at": "2026-05-12T15:31:20Z",
  "latest_plan_status": "DRY_RUN_ONLY",
  "latest_position_status": "OK",
  "review_notes": [
    "Do not overfit from a short paper run.",
    "Evaluate trigger hit rate, skip reasons, fills, slippage, drawdown, and operational failures over time.",
    "Escalate only evidence-backed experiments to strategy improvement review."
  ],
  "run_id": "weekly_review-20260512T153120-18036227",
  "schema_version": "0.1.0",
  "signal_log_entries": 2,
  "trade_log_entries": 2,
  "trigger_log_entries": 1
}
```

## Weekly review

```json
{
  "data_quality_entries": 5,
  "generated_at": "2026-05-12T15:32:53Z",
  "latest_plan_status": "DRY_RUN_ONLY",
  "latest_position_status": "OK",
  "review_notes": [
    "Do not overfit from a short paper run.",
    "Evaluate trigger hit rate, skip reasons, fills, slippage, drawdown, and operational failures over time.",
    "Escalate only evidence-backed experiments to strategy improvement review."
  ],
  "run_id": "weekly_review-20260512T153253-dd994ff0",
  "schema_version": "0.1.0",
  "signal_log_entries": 6,
  "trade_log_entries": 5,
  "trigger_log_entries": 3
}
```

## Weekly review

```json
{
  "data_quality_entries": 7,
  "generated_at": "2026-05-12T15:33:05Z",
  "latest_plan_status": "DRY_RUN_ONLY",
  "latest_position_status": "OK",
  "review_notes": [
    "Do not overfit from a short paper run.",
    "Evaluate trigger hit rate, skip reasons, fills, slippage, drawdown, and operational failures over time.",
    "Escalate only evidence-backed experiments to strategy improvement review."
  ],
  "run_id": "weekly_review-20260512T153305-8df20d3d",
  "schema_version": "0.1.0",
  "signal_log_entries": 9,
  "trade_log_entries": 7,
  "trigger_log_entries": 4
}
```
## Weekly Review — 2026-05-07 to 2026-05-13 (7 days)

**Generated:** 2026-05-13T19:05:13Z  **Run ID:** weekly_review-2026-05-13

### Trigger Scans
- Total runs: 14 | Risk-on: 14 | Risk-off: 0
- Avg candidates: 67.9 | Avg excluded: 69.0

### Dry Runs
- Total: 15 | Pass: 10 | Fail: 5
  - RISK_STATE_NOT_PAUSED: 4x
  - SPREAD_NOT_TOO_WIDE: 1x

### Paper Executions
- Attempts: 1 | Orders submitted: 1
  - [2026-05-13] WELL BUY $25.0 @ $218.9 (PAPER_SUBMITTED)

### Order Lifecycle
- Monitor runs: 7 | Tracked: 6
- Fills: 0 | Missing: 5 | Expired: 0 | Rejected: 0 | Canceled: 0

### External Alerts
- Ingested this period: 8 (all-time: 8)
- Routes this period: 5 (all-time: 5)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By next_step: request_trade_plan_unapproved=2, request_data_refresh=5, log_only=1

### Risk State
- Equity: $40,000.00 | Peak: $99,803.09 | Drawdown: -59.92% | Positions: 0
- Last updated: 2026-05-13T19:04:59Z

### Operational Issues (4)
- Dry-run gate 'RISK_STATE_NOT_PAUSED' failed 4 time(s) this period.
- Dry-run gate 'SPREAD_NOT_TOO_WIDE' failed 1 time(s) this period.
- 5 order(s) have lifecycle_status=missing — verify on broker.
- Drawdown is -59.9% — approaching warning threshold (-5%).

### Research Observations
- Market regime: 14/14 sessions risk_on (100%). Avg candidates=67.9, avg excluded=69.0.
- 1 paper execution attempt(s), 1 order(s) submitted.
- 8 external alert(s) ingested this period, 5 routed.

---
## Weekly Review — 2026-05-07 to 2026-05-13 (7 days)

**Generated:** 2026-05-13T19:22:57Z  **Run ID:** weekly_review-2026-05-13

### Trigger Scans
- Total runs: 0 | Risk-on: 0 | Risk-off: 0
- Avg candidates: 0.0 | Avg excluded: 0.0

### Dry Runs
- Total: 0 | Pass: 0 | Fail: 0

### Paper Executions
- Attempts: 1 | Orders submitted: 1
  - [2026-05-13] WELL BUY $25.0 @ $218.9 (PAPER_SUBMITTED)

### Order Lifecycle
- Monitor runs: 9 | Tracked: 8
- Fills: 1 | Missing: 6 | Expired: 0 | Rejected: 0 | Canceled: 0

### External Alerts
- Ingested this period: 8 (all-time: 8)
- Routes this period: 5 (all-time: 5)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By next_step: request_trade_plan_unapproved=2, request_data_refresh=5, log_only=1

### Risk State
- Equity: $99,803.02 | Peak: $99,803.12 | Drawdown: -0.00% | Positions: 1
- Last updated: 2026-05-13T19:20:54Z

### Operational Issues (1)
- 6 order(s) have lifecycle_status=missing — verify on broker.

### Research Observations
- 1 paper execution attempt(s), 1 order(s) submitted.
- 1 order fill(s) confirmed by order monitor.
- 8 external alert(s) ingested this period, 5 routed.

---
