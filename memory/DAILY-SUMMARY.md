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
## Daily Summary — 2026-05-13

**Generated:** 2026-05-13T19:22:10Z  **Run ID:** daily_summary-2026-05-13

### Account & Risk
- Equity: $99,803.02 | Cash: $99,777.86 | Buying power: $199,580.88
- Peak: $99,803.12 | Drawdown: -0.00% | Positions: 1

### Positions (1)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| WELL | long | 0.11425542 | $25.16 | +$0.16 (0.63%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.15%, breadth=58.23%)
- Candidates: 30 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-13T19:20:54Z

### Trade Plan
- Plan ID: `trade_plan-20260513T192054-7bc0d923`
- Generated: 2026-05-13T19:20:54Z | Expires: 2026-05-14T01:20:54Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - JNJ BUY $25.00 @ $230.42 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260513T192055-9711b452`
- All gates pass: YES

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (1)
- WELL BUY $25.00 @ $218.90 (PAPER_SUBMITTED) submitted=2026-05-13T16:00:36Z

### Order Monitor
- Tracked: 1 | Filled: 1 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 9 | Latest: order_monitor-20260513T191959-be097bf5

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
## Daily Summary — 2026-05-13

**Generated:** 2026-05-13T19:34:05Z  **Run ID:** daily_summary-2026-05-13

### Account & Risk
- Equity: $99,803.07 | Cash: $99,727.86 | Buying power: $199,530.93
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 3

### Positions (3)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.023054861 | $24.99 | $-0.01 (-0.04%) |
| JNJ | long | 0.108578576 | $24.99 | $-0.01 (-0.04%) |
| WELL | long | 0.11425542 | $25.23 | +$0.23 (0.93%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.09%, breadth=58.23%)
- Candidates: 29 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-13T19:33:17Z

### Trade Plan
- Plan ID: `trade_plan-20260513T193317-e5036a68`
- Generated: 2026-05-13T19:33:17Z | Expires: 2026-05-14T01:33:17Z
- Approved for execution: NO | Reason: max_orders_per_run_cap(1)_dequeued(non_blocking): ['JNJ', 'CSCO', 'GOOGL', 'MS', 'GS', 'XOM', 'CAT', 'SLB', 'AVGO', 'FCX', 'BIL']; spread_blocked_all_orders: ['WELL']
- All risk checks pass: YES
- No proposed orders.

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260513T193317-d8bfdaf4`
- All gates pass: YES

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (4)
- WELL BUY $25.00 @ $218.90 (PAPER_SUBMITTED) submitted=2026-05-13T16:00:36Z
- JNJ BUY $25.00 @ $230.26 (PAPER_SUBMITTED) submitted=2026-05-13T19:25:27Z
- EQIX BUY $25.00 @ $1,084.52 (PAPER_SUBMITTED) submitted=2026-05-13T19:29:35Z
- EQIX SELL $25.00 @ $1,084.25 (PAPER_ORDER_ERRORS) submitted=2026-05-13T19:31:30Z

### Order Monitor
- Tracked: 3 | Filled: 3 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 11 | Latest: order_monitor-20260513T193215-abd957a2

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
## Daily Summary — 2026-05-13

**Generated:** 2026-05-13T21:04:39Z  **Run ID:** daily_summary-2026-05-13

### Account & Risk
- Equity: $99,802.92 | Cash: $99,727.86 | Buying power: $199,530.78
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 3

### Positions (3)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.023054861 | $24.84 | $-0.16 (-0.65%) |
| JNJ | long | 0.108578576 | $25.07 | +$0.07 (0.28%) |
| WELL | long | 0.11425542 | $25.15 | +$0.15 (0.61%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+8.95%, breadth=56.96%)
- Candidates: 13 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-13T20:39:57Z

### Trade Plan
- Plan ID: `trade_plan-20260513T205815-47e1943d`
- Generated: 2026-05-13T20:58:15Z | Expires: 2026-05-14T02:58:15Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - JNJ BUY $25.00 @ $230.16 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260513T203957-9632fb92`
- All gates pass: YES

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (4)
- WELL BUY $25.00 @ $218.90 (PAPER_SUBMITTED) submitted=2026-05-13T16:00:36Z
- JNJ BUY $25.00 @ $230.26 (PAPER_SUBMITTED) submitted=2026-05-13T19:25:27Z
- EQIX BUY $25.00 @ $1,084.52 (PAPER_SUBMITTED) submitted=2026-05-13T19:29:35Z
- EQIX SELL $25.00 @ $1,084.25 (PAPER_ORDER_ERRORS) submitted=2026-05-13T19:31:30Z

### Order Monitor
- Tracked: 3 | Filled: 3 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 13 | Latest: order_monitor-20260513T210202-634fc7d9

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
## Daily Summary — 2026-05-13

**Generated:** 2026-05-13T22:13:26Z  **Run ID:** daily_summary-2026-05-13

### Account & Risk
- Equity: $99,802.87 | Cash: $99,727.86 | Buying power: $199,530.73
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 3

### Positions (3)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.023054861 | $24.84 | $-0.16 (-0.65%) |
| JNJ | long | 0.108578576 | $25.02 | +$0.02 (0.08%) |
| WELL | long | 0.11425542 | $25.15 | +$0.15 (0.61%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+8.95%, breadth=56.96%)
- Candidates: 13 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-13T21:50:26Z

### Trade Plan
- Plan ID: `trade_plan-20260513T215026-c8754de3`
- Generated: 2026-05-13T21:50:26Z | Expires: 2026-05-14T03:50:26Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - EQIX BUY $25.00 @ $1,077.05 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260513T215027-de088ae7`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (4)
- WELL BUY $25.00 @ $218.90 (PAPER_SUBMITTED) submitted=2026-05-13T16:00:36Z
- JNJ BUY $25.00 @ $230.26 (PAPER_SUBMITTED) submitted=2026-05-13T19:25:27Z
- EQIX BUY $25.00 @ $1,084.52 (PAPER_SUBMITTED) submitted=2026-05-13T19:29:35Z
- EQIX SELL $25.00 @ $1,084.25 (PAPER_ORDER_ERRORS) submitted=2026-05-13T19:31:30Z

### Order Monitor
- Tracked: 3 | Filled: 3 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 14 | Latest: order_monitor-20260513T215150-081d0a9f

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
## Daily Summary — 2026-05-14

**Generated:** 2026-05-14T13:52:19Z  **Run ID:** daily_summary-2026-05-14

### Account & Risk
- Equity: $99,802.72 | Cash: $99,727.76 | Buying power: $199,530.48
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 3

### Positions (3)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.023054861 | $24.79 | $-0.21 (-0.82%) |
| JNJ | long | 0.108578576 | $25.07 | +$0.07 (0.28%) |
| WELL | long | 0.11425542 | $25.09 | +$0.09 (0.37%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.19%, breadth=56.96%)
- Candidates: 16 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-14T13:48:13Z

### Trade Plan
- Plan ID: `trade_plan-20260514T134813-981486ac`
- Generated: 2026-05-14T13:48:13Z | Expires: 2026-05-14T19:48:13Z
- Approved for execution: **YES** | Reason: all_risk_checks_pass_and_paper_flag_set
- All risk checks pass: YES
- Proposed orders (1):
  - EQIX BUY $25.00 @ $1,077.99 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260514T134814-b4369954`
- All gates pass: NO
- Failed gates: CANONICAL_SOURCE_INTEGRITY

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (1)

### Order Monitor
- Tracked: 3 | Filled: 3 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 1 | Latest: order_monitor-20260514T135003-8d27b238

### Alerts (total=8, today=0)
- By source: tradingview=6, test=2
- By next_step: request_trade_plan_unapproved=2, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-14

**Generated:** 2026-05-14T13:58:20Z  **Run ID:** daily_summary-2026-05-14

### Account & Risk
- Equity: $99,802.92 | Cash: $99,727.76 | Buying power: $199,530.68
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 3

### Positions (3)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.023054861 | $24.91 | $-0.09 (-0.37%) |
| JNJ | long | 0.108578576 | $25.11 | +$0.11 (0.42%) |
| WELL | long | 0.11425542 | $25.15 | +$0.15 (0.59%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.14%, breadth=58.23%)
- Candidates: 18 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-14T13:55:03Z

### Trade Plan
- Plan ID: `trade_plan-20260514T135503-484a3f03`
- Generated: 2026-05-14T13:55:03Z | Expires: 2026-05-14T19:55:03Z
- Approved for execution: **YES** | Reason: all_risk_checks_pass_and_paper_flag_set
- All risk checks pass: YES
- Proposed orders (1):
  - EQIX BUY $25.00 @ $1,077.99 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260514T135504-19cce5c5`
- All gates pass: NO
- Failed gates: CANONICAL_SOURCE_INTEGRITY

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (2)

### Order Monitor
- Tracked: 3 | Filled: 3 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260514T135604-69822f2b

### Alerts (total=8, today=0)
- By source: tradingview=6, test=2
- By next_step: request_trade_plan_unapproved=2, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-14

**Generated:** 2026-05-14T14:16:26Z  **Run ID:** daily_summary-2026-05-14

### Account & Risk
- Equity: $99,802.73 | Cash: $99,727.76 | Buying power: $199,530.49
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 3

### Positions (3)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.023054861 | $24.81 | $-0.19 (-0.76%) |
| JNJ | long | 0.108578576 | $25.09 | +$0.09 (0.35%) |
| WELL | long | 0.11425542 | $25.07 | +$0.07 (0.28%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.19%, breadth=58.23%)
- Candidates: 18 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-14T14:16:25Z

### Trade Plan
- Plan ID: `trade_plan-20260514T141625-a3944e26`
- Generated: 2026-05-14T14:16:25Z | Expires: 2026-05-14T20:16:25Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - EQIX BUY $25.00 @ $1,073.13 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260514T141625-7f7875ec`
- All gates pass: YES

### Dry Runs Today (1)
- Pass: 1 | Fail: 0

### Paper Executions Today (2)

### Order Monitor
- Tracked: 3 | Filled: 3 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 3 | Latest: order_monitor-20260514T141625-5c83a59b

### Alerts (total=8, today=0)
- By source: tradingview=6, test=2
- By next_step: request_trade_plan_unapproved=2, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-14

**Generated:** 2026-05-14T14:55:09Z  **Run ID:** daily_summary-2026-05-14

### Account & Risk
- Equity: $99,802.62 | Cash: $99,727.76 | Buying power: $199,530.38
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 3

### Positions (3)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.023054861 | $24.89 | $-0.11 (-0.44%) |
| JNJ | long | 0.108578576 | $24.97 | $-0.03 (-0.11%) |
| WELL | long | 0.11425542 | $25.00 | +$0.00 (0.01%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.42%, breadth=56.96%)
- Candidates: 19 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-14T14:55:02Z

### Trade Plan
- Plan ID: `trade_plan-20260514T145502-e78a9cd9`
- Generated: 2026-05-14T14:55:02Z | Expires: 2026-05-14T20:55:02Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - EQIX BUY $25.00 @ $1,077.35 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260514T145502-ccf45a10`
- All gates pass: YES

### Dry Runs Today (1)
- Pass: 1 | Fail: 0

### Paper Executions Today (2)

### Order Monitor
- Tracked: 3 | Filled: 3 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 5 | Latest: order_monitor-20260514T145508-e2cd3c52

### Alerts (total=8, today=0)
- By source: tradingview=6, test=2
- By next_step: request_trade_plan_unapproved=2, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-14

**Generated:** 2026-05-14T14:56:34Z  **Run ID:** daily_summary-2026-05-14

### Account & Risk
- Equity: $99,802.70 | Cash: $99,727.76 | Buying power: $199,505.46
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 3

### Positions (3)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.023054861 | $24.91 | $-0.09 (-0.37%) |
| JNJ | long | 0.108578576 | $25.00 | +$0.00 (0.01%) |
| WELL | long | 0.11425542 | $25.03 | +$0.03 (0.10%) |

### Open Orders (1)
- EQIX BUY $25.00 @ $1,079.73 (limit) status=new

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.45%, breadth=56.96%)
- Candidates: 22 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-14T14:56:25Z

### Trade Plan
- Plan ID: `trade_plan-20260514T145625-7807f306`
- Generated: 2026-05-14T14:56:25Z | Expires: 2026-05-14T20:56:25Z
- Approved for execution: **YES** | Reason: all_risk_checks_pass_and_paper_flag_set
- All risk checks pass: YES
- Proposed orders (1):
  - EQIX BUY $25.00 @ $1,079.73 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260514T145626-8a29a24f`
- All gates pass: YES

### Dry Runs Today (1)
- Pass: 1 | Fail: 0

### Paper Executions Today (3)
- EQIX BUY $25.00 @ $1,079.73 (PAPER_SUBMITTED) submitted=2026-05-14T14:56:26Z

### Order Monitor
- Tracked: 4 | Filled: 3 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 1
- Runs today: 7 | Latest: order_monitor-20260514T145634-50dad7cb

### Alerts (total=8, today=0)
- By source: tradingview=6, test=2
- By next_step: request_trade_plan_unapproved=2, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-14

**Generated:** 2026-05-14T15:00:15Z  **Run ID:** daily_summary-2026-05-14

### Account & Risk
- Equity: $99,802.82 | Cash: $99,727.76 | Buying power: $199,505.58
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 3

### Positions (3)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.023054861 | $24.95 | $-0.05 (-0.19%) |
| JNJ | long | 0.108578576 | $25.01 | +$0.01 (0.03%) |
| WELL | long | 0.11425542 | $25.10 | +$0.10 (0.40%) |

### Open Orders (1)
- EQIX BUY $25.00 @ $1,079.73 (limit) status=new

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.45%, breadth=56.96%)
- Candidates: 22 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-14T15:00:04Z

### Trade Plan
- Plan ID: `trade_plan-20260514T150004-88cc6ef5`
- Generated: 2026-05-14T15:00:04Z | Expires: 2026-05-14T21:00:04Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - EQIX BUY $25.00 @ $1,081.64 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260514T150005-a2085adb`
- All gates pass: NO
- Failed gates: NO_DUPLICATE_OPEN_ORDERS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - NO_DUPLICATE_OPEN_ORDERS: 1x

### Paper Executions Today (3)
- EQIX BUY $25.00 @ $1,079.73 (PAPER_SUBMITTED) submitted=2026-05-14T14:56:26Z

### Order Monitor
- Tracked: 4 | Filled: 3 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 1
- Runs today: 9 | Latest: order_monitor-20260514T150015-70c5c992

### Alerts (total=8, today=0)
- By source: tradingview=6, test=2
- By next_step: request_trade_plan_unapproved=2, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-14

**Generated:** 2026-05-14T15:01:27Z  **Run ID:** daily_summary-2026-05-14

### Account & Risk
- Equity: $99,802.81 | Cash: $99,727.76 | Buying power: $199,505.57
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 3

### Positions (3)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.023054861 | $24.96 | $-0.04 (-0.17%) |
| JNJ | long | 0.108578576 | $25.00 | $-0.00 (-0.02%) |
| WELL | long | 0.11425542 | $25.10 | +$0.10 (0.40%) |

### Open Orders (1)
- EQIX BUY $25.00 @ $1,079.73 (limit) status=new

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.43%, breadth=56.96%)
- Candidates: 23 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-14T15:01:20Z

### Trade Plan
- Plan ID: `trade_plan-20260514T150120-1cea48e5`
- Generated: 2026-05-14T15:01:20Z | Expires: 2026-05-14T21:01:20Z
- Approved for execution: NO | Reason: max_orders_per_run_cap(1)_dequeued(non_blocking): ['WMT', 'WELL', 'MRK', 'GOOGL', 'GS', 'CSCO', 'XOM', 'SLB', 'FCX', 'AMD', 'BIL']; spread_blocked_all_orders: ['JNJ']
- All risk checks pass: YES
- No proposed orders.

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260514T150121-0f807e87`
- All gates pass: NO

### Dry Runs Today (1)
- Pass: 1 | Fail: 0

### Paper Executions Today (4)
- EQIX BUY $25.00 @ $1,079.73 (PAPER_SUBMITTED) submitted=2026-05-14T14:56:26Z

### Order Monitor
- Tracked: 4 | Filled: 3 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 1
- Runs today: 11 | Latest: order_monitor-20260514T150127-4dbd4463

### Alerts (total=8, today=0)
- By source: tradingview=6, test=2
- By next_step: request_trade_plan_unapproved=2, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-14

**Generated:** 2026-05-14T15:13:15Z  **Run ID:** daily_summary-2026-05-14

### Account & Risk
- Equity: $99,802.69 | Cash: $99,727.76 | Buying power: $199,505.45
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 3

### Positions (3)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.023054861 | $24.99 | $-0.01 (-0.03%) |
| JNJ | long | 0.108578576 | $24.95 | $-0.05 (-0.21%) |
| WELL | long | 0.11425542 | $24.99 | $-0.01 (-0.02%) |

### Open Orders (1)
- EQIX BUY $25.00 @ $1,079.73 (limit) status=new

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.51%, breadth=56.96%)
- Candidates: 24 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-14T15:13:14Z

### Trade Plan
- Plan ID: `trade_plan-20260514T151314-d878d221`
- Generated: 2026-05-14T15:13:14Z | Expires: 2026-05-14T21:13:14Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - EQIX BUY $25.00 @ $1,083.47 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260514T151314-ddcac1c7`
- All gates pass: NO
- Failed gates: NO_DUPLICATE_OPEN_ORDERS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - NO_DUPLICATE_OPEN_ORDERS: 1x

### Paper Executions Today (4)
- EQIX BUY $25.00 @ $1,079.73 (PAPER_SUBMITTED) submitted=2026-05-14T14:56:26Z

### Order Monitor
- Tracked: 4 | Filled: 3 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 1
- Runs today: 12 | Latest: order_monitor-20260514T151314-7ed26ffc

### Alerts (total=8, today=0)
- By source: tradingview=6, test=2
- By next_step: request_trade_plan_unapproved=2, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-14

**Generated:** 2026-05-14T15:43:30Z  **Run ID:** daily_summary-2026-05-14

### Account & Risk
- Equity: $99,802.46 | Cash: $99,702.76 | Buying power: $199,480.22
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 3

### Positions (3)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.04621373 | $49.81 | $-0.19 (-0.38%) |
| JNJ | long | 0.108578576 | $24.99 | $-0.01 (-0.06%) |
| WELL | long | 0.11425542 | $24.91 | $-0.09 (-0.38%) |

### Open Orders (1)
- JNJ BUY $25.00 @ $230.12 (limit) status=new

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.64%, breadth=56.96%)
- Candidates: 23 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-14T15:43:23Z

### Trade Plan
- Plan ID: `trade_plan-20260514T154323-1f27d10d`
- Generated: 2026-05-14T15:43:23Z | Expires: 2026-05-14T21:43:23Z
- Approved for execution: **YES** | Reason: all_risk_checks_pass_and_paper_flag_set
- All risk checks pass: YES
- Proposed orders (1):
  - JNJ BUY $25.00 @ $230.12 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260514T154324-0732af2c`
- All gates pass: YES

### Dry Runs Today (1)
- Pass: 1 | Fail: 0

### Paper Executions Today (5)
- EQIX BUY $25.00 @ $1,079.73 (PAPER_SUBMITTED) submitted=2026-05-14T14:56:26Z
- JNJ BUY $25.00 @ $230.12 (PAPER_SUBMITTED) submitted=2026-05-14T15:43:24Z

### Order Monitor
- Tracked: 5 | Filled: 4 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 1
- Runs today: 14 | Latest: order_monitor-20260514T154329-4c3be2d7

### Alerts (total=8, today=0)
- By source: tradingview=6, test=2
- By next_step: request_trade_plan_unapproved=2, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-14

**Generated:** 2026-05-14T15:44:50Z  **Run ID:** daily_summary-2026-05-14

### Account & Risk
- Equity: $99,802.53 | Cash: $99,702.76 | Buying power: $199,480.29
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 3

### Positions (3)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.04621373 | $49.84 | $-0.16 (-0.32%) |
| JNJ | long | 0.108578576 | $24.99 | $-0.01 (-0.03%) |
| WELL | long | 0.11425542 | $24.94 | $-0.06 (-0.25%) |

### Open Orders (1)
- JNJ BUY $25.00 @ $230.12 (limit) status=new

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.65%, breadth=56.96%)
- Candidates: 23 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-14T15:44:45Z

### Trade Plan
- Plan ID: `trade_plan-20260514T154445-01c16697`
- Generated: 2026-05-14T15:44:45Z | Expires: 2026-05-14T21:44:45Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - EQIX BUY $25.00 @ $1,077.21 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260514T154445-23b2e2b2`
- All gates pass: YES

### Dry Runs Today (1)
- Pass: 1 | Fail: 0

### Paper Executions Today (5)
- EQIX BUY $25.00 @ $1,079.73 (PAPER_SUBMITTED) submitted=2026-05-14T14:56:26Z
- JNJ BUY $25.00 @ $230.12 (PAPER_SUBMITTED) submitted=2026-05-14T15:43:24Z

### Order Monitor
- Tracked: 5 | Filled: 4 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 1
- Runs today: 16 | Latest: order_monitor-20260514T154449-4dcd0712

### Alerts (total=8, today=0)
- By source: tradingview=6, test=2
- By next_step: request_trade_plan_unapproved=2, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-14

**Generated:** 2026-05-14T15:45:49Z  **Run ID:** daily_summary-2026-05-14

### Account & Risk
- Equity: $99,802.53 | Cash: $99,702.76 | Buying power: $199,480.29
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 3

### Positions (3)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.04621373 | $49.83 | $-0.17 (-0.34%) |
| JNJ | long | 0.108578576 | $25.00 | $-0.00 (-0.01%) |
| WELL | long | 0.11425542 | $24.94 | $-0.06 (-0.24%) |

### Open Orders (2)
- EQIX SELL $25.00 @ $1,078.28 (limit) status=new
- JNJ BUY $25.00 @ $230.12 (limit) status=new

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.65%, breadth=56.96%)
- Candidates: 23 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-14T15:45:42Z

### Trade Plan
- Plan ID: `trade_plan-20260514T154543-b29ff94f`
- Generated: 2026-05-14T15:45:43Z | Expires: 2026-05-14T21:45:43Z
- Approved for execution: **YES** | Reason: all_risk_checks_pass_and_paper_flag_set
- All risk checks pass: YES
- Proposed orders (1):
  - EQIX SELL $25.00 @ $1,078.28 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260514T154544-c2e241e8`
- All gates pass: YES

### Dry Runs Today (1)
- Pass: 1 | Fail: 0

### Paper Executions Today (6)
- EQIX BUY $25.00 @ $1,079.73 (PAPER_SUBMITTED) submitted=2026-05-14T14:56:26Z
- JNJ BUY $25.00 @ $230.12 (PAPER_SUBMITTED) submitted=2026-05-14T15:43:24Z
- EQIX SELL $25.00 @ $1,078.28 (PAPER_SUBMITTED) submitted=2026-05-14T15:45:44Z

### Order Monitor
- Tracked: 6 | Filled: 4 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 2
- Runs today: 18 | Latest: order_monitor-20260514T154549-e3d51b1c

### Alerts (total=8, today=0)
- By source: tradingview=6, test=2
- By next_step: request_trade_plan_unapproved=2, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-14

**Generated:** 2026-05-14T15:48:23Z  **Run ID:** daily_summary-2026-05-14

### Account & Risk
- Equity: $99,802.57 | Cash: $99,727.76 | Buying power: $199,480.33
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 3

### Positions (3)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.023032141 | $24.86 | $-0.06 (-0.24%) |
| JNJ | long | 0.108578576 | $25.01 | +$0.01 (0.04%) |
| WELL | long | 0.11425542 | $24.94 | $-0.06 (-0.26%) |

### Open Orders (2)
- EQIX BUY $25.00 @ $1,078.43 (limit) status=new
- JNJ BUY $25.00 @ $230.12 (limit) status=new

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.63%, breadth=56.96%)
- Candidates: 19 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-14T15:48:17Z

### Trade Plan
- Plan ID: `trade_plan-20260514T154817-6a53654a`
- Generated: 2026-05-14T15:48:17Z | Expires: 2026-05-14T21:48:17Z
- Approved for execution: **YES** | Reason: all_risk_checks_pass_and_paper_flag_set
- All risk checks pass: YES
- Proposed orders (1):
  - EQIX BUY $25.00 @ $1,078.43 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260514T154818-6157fada`
- All gates pass: YES

### Dry Runs Today (1)
- Pass: 1 | Fail: 0

### Paper Executions Today (7)
- EQIX BUY $25.00 @ $1,079.73 (PAPER_SUBMITTED) submitted=2026-05-14T14:56:26Z
- JNJ BUY $25.00 @ $230.12 (PAPER_SUBMITTED) submitted=2026-05-14T15:43:24Z
- EQIX SELL $25.00 @ $1,078.28 (PAPER_SUBMITTED) submitted=2026-05-14T15:45:44Z
- EQIX BUY $25.00 @ $1,078.43 (PAPER_SUBMITTED) submitted=2026-05-14T15:48:18Z

### Order Monitor
- Tracked: 7 | Filled: 5 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 2
- Runs today: 20 | Latest: order_monitor-20260514T154823-07890943

### Alerts (total=8, today=0)
- By source: tradingview=6, test=2
- By next_step: request_trade_plan_unapproved=2, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-14

**Generated:** 2026-05-14T15:52:37Z  **Run ID:** daily_summary-2026-05-14

### Account & Risk
- Equity: $99,802.53 | Cash: $99,727.76 | Buying power: $199,480.29
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 3

### Positions (3)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.023032141 | $24.82 | $-0.09 (-0.38%) |
| JNJ | long | 0.108578576 | $25.03 | +$0.03 (0.11%) |
| WELL | long | 0.11425542 | $24.92 | $-0.08 (-0.32%) |

### Open Orders (2)
- EQIX BUY $25.00 @ $1,078.43 (limit) status=new
- JNJ BUY $25.00 @ $230.12 (limit) status=new

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.64%, breadth=56.96%)
- Candidates: 21 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-14T15:52:30Z

### Trade Plan
- Plan ID: `trade_plan-20260514T155230-b606f849`
- Generated: 2026-05-14T15:52:30Z | Expires: 2026-05-14T21:52:30Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - EQIX BUY $25.00 @ $1,078.43 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260514T155230-c8efe290`
- All gates pass: NO
- Failed gates: NO_DUPLICATE_OPEN_ORDERS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - NO_DUPLICATE_OPEN_ORDERS: 1x

### Paper Executions Today (7)
- EQIX BUY $25.00 @ $1,079.73 (PAPER_SUBMITTED) submitted=2026-05-14T14:56:26Z
- JNJ BUY $25.00 @ $230.12 (PAPER_SUBMITTED) submitted=2026-05-14T15:43:24Z
- EQIX SELL $25.00 @ $1,078.28 (PAPER_SUBMITTED) submitted=2026-05-14T15:45:44Z
- EQIX BUY $25.00 @ $1,078.43 (PAPER_SUBMITTED) submitted=2026-05-14T15:48:18Z

### Order Monitor
- Tracked: 7 | Filled: 5 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 2
- Runs today: 23 | Latest: order_monitor-20260514T155236-24ace729

### Alerts (total=8, today=0)
- By source: tradingview=6, test=2
- By next_step: request_trade_plan_unapproved=2, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-14

**Generated:** 2026-05-14T15:53:42Z  **Run ID:** daily_summary-2026-05-14

### Account & Risk
- Equity: $99,802.53 | Cash: $99,727.76 | Buying power: $199,480.29
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 3

### Positions (3)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.023032141 | $24.83 | $-0.09 (-0.36%) |
| JNJ | long | 0.108578576 | $25.02 | +$0.02 (0.09%) |
| WELL | long | 0.11425542 | $24.92 | $-0.08 (-0.32%) |

### Open Orders (2)
- EQIX BUY $25.00 @ $1,078.43 (limit) status=new
- JNJ BUY $25.00 @ $230.12 (limit) status=new

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.65%, breadth=56.96%)
- Candidates: 23 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-14T15:53:41Z

### Trade Plan
- Plan ID: `trade_plan-20260514T155342-102808af`
- Generated: 2026-05-14T15:53:42Z | Expires: 2026-05-14T21:53:42Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - PLD BUY $25.00 @ $142.74 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260514T155342-f0180db7`
- All gates pass: YES

### Dry Runs Today (1)
- Pass: 1 | Fail: 0

### Paper Executions Today (7)
- EQIX BUY $25.00 @ $1,079.73 (PAPER_SUBMITTED) submitted=2026-05-14T14:56:26Z
- JNJ BUY $25.00 @ $230.12 (PAPER_SUBMITTED) submitted=2026-05-14T15:43:24Z
- EQIX SELL $25.00 @ $1,078.28 (PAPER_SUBMITTED) submitted=2026-05-14T15:45:44Z
- EQIX BUY $25.00 @ $1,078.43 (PAPER_SUBMITTED) submitted=2026-05-14T15:48:18Z

### Order Monitor
- Tracked: 7 | Filled: 5 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 2
- Runs today: 24 | Latest: order_monitor-20260514T155341-8b726252

### Alerts (total=8, today=0)
- By source: tradingview=6, test=2
- By next_step: request_trade_plan_unapproved=2, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-14

**Generated:** 2026-05-14T16:30:04Z  **Run ID:** daily_summary-2026-05-14

### Account & Risk
- Equity: $99,802.43 | Cash: $99,702.76 | Buying power: $199,480.19
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 3

### Positions (3)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.046214418 | $49.77 | $-0.15 (-0.30%) |
| JNJ | long | 0.108578576 | $25.00 | +$0.00 (0.01%) |
| WELL | long | 0.11425542 | $24.90 | $-0.10 (-0.40%) |

### Open Orders (1)
- JNJ BUY $25.00 @ $230.12 (limit) status=new

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.56%, breadth=56.96%)
- Candidates: 27 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-14T16:30:03Z

### Trade Plan
- Plan ID: `trade_plan-20260514T163003-2a802acf`
- Generated: 2026-05-14T16:30:03Z | Expires: 2026-05-14T22:30:03Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - EQIX BUY $25.00 @ $1,076.89 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260514T163003-73a62e3e`
- All gates pass: YES

### Dry Runs Today (1)
- Pass: 1 | Fail: 0

### Paper Executions Today (7)
- EQIX BUY $25.00 @ $1,079.73 (PAPER_SUBMITTED) submitted=2026-05-14T14:56:26Z
- JNJ BUY $25.00 @ $230.12 (PAPER_SUBMITTED) submitted=2026-05-14T15:43:24Z
- EQIX SELL $25.00 @ $1,078.28 (PAPER_SUBMITTED) submitted=2026-05-14T15:45:44Z
- EQIX BUY $25.00 @ $1,078.43 (PAPER_SUBMITTED) submitted=2026-05-14T15:48:18Z

### Order Monitor
- Tracked: 7 | Filled: 6 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 1
- Runs today: 26 | Latest: order_monitor-20260514T163003-ef335475

### Alerts (total=8, today=0)
- By source: tradingview=6, test=2
- By next_step: request_trade_plan_unapproved=2, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-14

**Generated:** 2026-05-14T16:31:20Z  **Run ID:** daily_summary-2026-05-14

### Account & Risk
- Equity: $99,802.47 | Cash: $99,702.76 | Buying power: $199,455.23
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 3

### Positions (3)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.046214418 | $49.80 | $-0.12 (-0.25%) |
| JNJ | long | 0.108578576 | $25.00 | +$0.00 (0.01%) |
| WELL | long | 0.11425542 | $24.91 | $-0.09 (-0.35%) |

### Open Orders (2)
- EQIX BUY $25.00 @ $1,076.96 (limit) status=new
- JNJ BUY $25.00 @ $230.12 (limit) status=new

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.56%, breadth=56.96%)
- Candidates: 26 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-14T16:31:12Z

### Trade Plan
- Plan ID: `trade_plan-20260514T163113-1c676d38`
- Generated: 2026-05-14T16:31:13Z | Expires: 2026-05-14T22:31:13Z
- Approved for execution: **YES** | Reason: all_risk_checks_pass_and_paper_flag_set
- All risk checks pass: YES
- Proposed orders (1):
  - EQIX BUY $25.00 @ $1,076.96 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260514T163114-dd6029a9`
- All gates pass: YES

### Dry Runs Today (1)
- Pass: 1 | Fail: 0

### Paper Executions Today (8)
- EQIX BUY $25.00 @ $1,079.73 (PAPER_SUBMITTED) submitted=2026-05-14T14:56:26Z
- JNJ BUY $25.00 @ $230.12 (PAPER_SUBMITTED) submitted=2026-05-14T15:43:24Z
- EQIX SELL $25.00 @ $1,078.28 (PAPER_SUBMITTED) submitted=2026-05-14T15:45:44Z
- EQIX BUY $25.00 @ $1,078.43 (PAPER_SUBMITTED) submitted=2026-05-14T15:48:18Z
- EQIX BUY $25.00 @ $1,076.96 (PAPER_SUBMITTED) submitted=2026-05-14T16:31:14Z

### Order Monitor
- Tracked: 8 | Filled: 6 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 2
- Runs today: 28 | Latest: order_monitor-20260514T163120-833c0bc8

### Alerts (total=8, today=0)
- By source: tradingview=6, test=2
- By next_step: request_trade_plan_unapproved=2, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
