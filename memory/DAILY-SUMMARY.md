# Daily Summary

Daily deterministic summary output.

## Daily summary

```json
{
  "breadth": 0.8987341772151899,
  "data_quality_status": "PASS",
  "execution_status": "DRY_RUN_NO_SUBMISSION",
  "failed_gates": [],
  "generated_at": "2026-05-12T15:31:20Z",
  "plan_status": "DRY_RUN_ONLY",
  "plan_targets": {
    "APD": 0.084553,
    "BIL": 0.1,
    "BKNG": 0.081628,
    "BLK": 0.09616,
    "DIS": 0.091409,
    "EOG": 0.094018,
    "KO": 0.087681,
    "LLY": 0.08698,
    "ORCL": 0.093499,
    "WELL": 0.09616,
    "WMT": 0.087912
  },
  "position_status": "OK",
  "risk_on": true,
  "run_id": "daily_summary-20260512T153120-84f99fa0",
  "schema_version": "0.1.0",
  "selected_symbols": [
    "WMT",
    "APD",
    "DIS",
    "ORCL",
    "LLY",
    "BLK",
    "BKNG",
    "KO",
    "WELL",
    "EOG"
  ],
  "skipped_count": 11,
  "submitted_count": 0
}
```

## Daily summary

```json
{
  "breadth": 0.8987341772151899,
  "data_quality_status": "PASS",
  "execution_status": "DRY_RUN_NO_SUBMISSION",
  "failed_gates": [],
  "generated_at": "2026-05-12T15:32:53Z",
  "plan_status": "DRY_RUN_ONLY",
  "plan_targets": {
    "APD": 0.084553,
    "BIL": 0.1,
    "BKNG": 0.081628,
    "BLK": 0.09616,
    "DIS": 0.091409,
    "EOG": 0.094018,
    "KO": 0.087681,
    "LLY": 0.08698,
    "ORCL": 0.093499,
    "WELL": 0.09616,
    "WMT": 0.087912
  },
  "position_status": "OK",
  "risk_on": true,
  "run_id": "daily_summary-20260512T153253-2f65c4ac",
  "schema_version": "0.1.0",
  "selected_symbols": [
    "WMT",
    "APD",
    "DIS",
    "ORCL",
    "LLY",
    "BLK",
    "BKNG",
    "KO",
    "WELL",
    "EOG"
  ],
  "skipped_count": 11,
  "submitted_count": 0
}
```

## Daily summary

```json
{
  "breadth": 0.8987341772151899,
  "data_quality_status": "PASS",
  "execution_status": "DRY_RUN_NO_SUBMISSION",
  "failed_gates": [],
  "generated_at": "2026-05-12T15:33:05Z",
  "plan_status": "DRY_RUN_ONLY",
  "plan_targets": {
    "APD": 0.084553,
    "BIL": 0.1,
    "BKNG": 0.081628,
    "BLK": 0.09616,
    "DIS": 0.091409,
    "EOG": 0.094018,
    "KO": 0.087681,
    "LLY": 0.08698,
    "ORCL": 0.093499,
    "WELL": 0.09616,
    "WMT": 0.087912
  },
  "position_status": "OK",
  "risk_on": true,
  "run_id": "daily_summary-20260512T153305-214630a6",
  "schema_version": "0.1.0",
  "selected_symbols": [
    "WMT",
    "APD",
    "DIS",
    "ORCL",
    "LLY",
    "BLK",
    "BKNG",
    "KO",
    "WELL",
    "EOG"
  ],
  "skipped_count": 11,
  "submitted_count": 0
}
```
## Daily Summary — 2026-05-13

**Generated:** 2026-05-13T19:05:10Z  **Run ID:** daily_summary-2026-05-13

### Account & Risk
- Equity: $40,000.00 | Cash: $40,000.00 | Buying power: $40,000.00
- Peak: $99,803.09 | Drawdown: -59.92% | Positions: 0

### Positions (0)
None.

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.00%, breadth=58.23%)
- Candidates: 27 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-13T17:23:26Z

### Trade Plan
- Plan ID: `trade_plan-20260513T190459-18194eac`
- Generated: 2026-05-13T19:04:59Z | Expires: 2026-05-14T01:04:59Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - JNJ BUY $25.00 @ $229.65 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260513T172327-9066f495`
- All gates pass: YES

### Dry Runs Today (6)
- Pass: 5 | Fail: 1
  - RISK_STATE_NOT_PAUSED: 1x

### Paper Executions Today (1)
- WELL BUY $25.00 @ $218.90 (PAPER_SUBMITTED) submitted=2026-05-13T16:00:36Z

### Order Monitor
- Tracked: 1 | Filled: 0 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 7 | Latest: order_monitor-20260513T174742-2bda44ae

### Alerts (total=8, today=8)
- By source: tradingview=6, test=2
- By next_step: request_trade_plan_unapproved=2, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=5)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
