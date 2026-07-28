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
## Daily Summary — 2026-05-14

**Generated:** 2026-05-14T16:52:38Z  **Run ID:** daily_summary-2026-05-14

### Account & Risk
- Equity: $99,802.59 | Cash: $99,652.76 | Buying power: $199,430.35
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.046214418 | $49.88 | $-0.03 (-0.07%) |
| JNJ | long | 0.217219435 | $50.01 | +$0.01 (0.03%) |
| WELL | long | 0.11425542 | $24.93 | $-0.07 (-0.29%) |
| WMT | long | 0.18899876 | $25.00 | $-0.00 (-0.00%) |

### Open Orders (1)
- EQIX BUY $25.00 @ $1,076.96 (limit) status=new

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.51%, breadth=56.96%)
- Candidates: 25 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-14T16:52:32Z

### Trade Plan
- Plan ID: `trade_plan-20260514T165232-1f83cea2`
- Generated: 2026-05-14T16:52:32Z | Expires: 2026-05-14T22:52:32Z
- Approved for execution: **YES** | Reason: all_risk_checks_pass_and_paper_flag_set
- All risk checks pass: YES
- Proposed orders (1):
  - WMT BUY $25.00 @ $132.36 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260514T165233-adcb0da2`
- All gates pass: YES

### Dry Runs Today (1)
- Pass: 1 | Fail: 0

### Paper Executions Today (9)
- EQIX BUY $25.00 @ $1,079.73 (PAPER_SUBMITTED) submitted=2026-05-14T14:56:26Z
- JNJ BUY $25.00 @ $230.12 (PAPER_SUBMITTED) submitted=2026-05-14T15:43:24Z
- EQIX SELL $25.00 @ $1,078.28 (PAPER_SUBMITTED) submitted=2026-05-14T15:45:44Z
- EQIX BUY $25.00 @ $1,078.43 (PAPER_SUBMITTED) submitted=2026-05-14T15:48:18Z
- EQIX BUY $25.00 @ $1,076.96 (PAPER_SUBMITTED) submitted=2026-05-14T16:31:14Z
- WMT BUY $25.00 @ $132.36 (PAPER_SUBMITTED) submitted=2026-05-14T16:52:33Z

### Order Monitor
- Tracked: 9 | Filled: 8 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 1
- Runs today: 30 | Latest: order_monitor-20260514T165237-6aef2461

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

**Generated:** 2026-05-14T17:17:45Z  **Run ID:** daily_summary-2026-05-14

### Account & Risk
- Equity: $99,802.45 | Cash: $99,652.76 | Buying power: $199,405.21
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.046214418 | $49.81 | $-0.11 (-0.22%) |
| JNJ | long | 0.217219435 | $50.00 | $-0.00 (-0.01%) |
| WELL | long | 0.11425542 | $24.85 | $-0.15 (-0.61%) |
| WMT | long | 0.18899876 | $25.04 | +$0.04 (0.17%) |

### Open Orders (2)
- JNJ BUY $25.00 @ $230.05 (limit) status=new
- EQIX BUY $25.00 @ $1,076.96 (limit) status=new

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.31%, breadth=56.96%)
- Candidates: 20 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-14T17:17:38Z

### Trade Plan
- Plan ID: `trade_plan-20260514T171739-65285f83`
- Generated: 2026-05-14T17:17:39Z | Expires: 2026-05-14T23:17:39Z
- Approved for execution: **YES** | Reason: all_risk_checks_pass_and_paper_flag_set
- All risk checks pass: YES
- Proposed orders (1):
  - JNJ BUY $25.00 @ $230.05 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260514T171740-77316146`
- All gates pass: YES

### Dry Runs Today (1)
- Pass: 1 | Fail: 0

### Paper Executions Today (10)
- EQIX BUY $25.00 @ $1,079.73 (PAPER_SUBMITTED) submitted=2026-05-14T14:56:26Z
- JNJ BUY $25.00 @ $230.12 (PAPER_SUBMITTED) submitted=2026-05-14T15:43:24Z
- EQIX SELL $25.00 @ $1,078.28 (PAPER_SUBMITTED) submitted=2026-05-14T15:45:44Z
- EQIX BUY $25.00 @ $1,078.43 (PAPER_SUBMITTED) submitted=2026-05-14T15:48:18Z
- EQIX BUY $25.00 @ $1,076.96 (PAPER_SUBMITTED) submitted=2026-05-14T16:31:14Z
- WMT BUY $25.00 @ $132.36 (PAPER_SUBMITTED) submitted=2026-05-14T16:52:33Z
- JNJ BUY $25.00 @ $230.05 (PAPER_SUBMITTED) submitted=2026-05-14T17:17:40Z

### Order Monitor
- Tracked: 10 | Filled: 8 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 2
- Runs today: 32 | Latest: order_monitor-20260514T171744-2fa6a81a

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

**Generated:** 2026-05-14T17:18:53Z  **Run ID:** daily_summary-2026-05-14

### Account & Risk
- Equity: $99,802.45 | Cash: $99,652.76 | Buying power: $199,380.21
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.046214418 | $49.81 | $-0.11 (-0.22%) |
| JNJ | long | 0.217219435 | $49.99 | $-0.01 (-0.01%) |
| WELL | long | 0.11425542 | $24.84 | $-0.16 (-0.65%) |
| WMT | long | 0.18899876 | $25.05 | +$0.05 (0.20%) |

### Open Orders (3)
- WMT BUY $25.00 @ $132.48 (limit) status=new
- JNJ BUY $25.00 @ $230.05 (limit) status=new
- EQIX BUY $25.00 @ $1,076.96 (limit) status=new

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.35%, breadth=56.96%)
- Candidates: 21 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-14T17:18:44Z

### Trade Plan
- Plan ID: `trade_plan-20260514T171844-6adf1380`
- Generated: 2026-05-14T17:18:44Z | Expires: 2026-05-14T23:18:44Z
- Approved for execution: **YES** | Reason: all_risk_checks_pass_and_paper_flag_set
- All risk checks pass: YES
- Proposed orders (1):
  - WMT BUY $25.00 @ $132.48 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260514T171846-d8b15803`
- All gates pass: YES

### Dry Runs Today (1)
- Pass: 1 | Fail: 0

### Paper Executions Today (11)
- EQIX BUY $25.00 @ $1,079.73 (PAPER_SUBMITTED) submitted=2026-05-14T14:56:26Z
- JNJ BUY $25.00 @ $230.12 (PAPER_SUBMITTED) submitted=2026-05-14T15:43:24Z
- EQIX SELL $25.00 @ $1,078.28 (PAPER_SUBMITTED) submitted=2026-05-14T15:45:44Z
- EQIX BUY $25.00 @ $1,078.43 (PAPER_SUBMITTED) submitted=2026-05-14T15:48:18Z
- EQIX BUY $25.00 @ $1,076.96 (PAPER_SUBMITTED) submitted=2026-05-14T16:31:14Z
- WMT BUY $25.00 @ $132.36 (PAPER_SUBMITTED) submitted=2026-05-14T16:52:33Z
- JNJ BUY $25.00 @ $230.05 (PAPER_SUBMITTED) submitted=2026-05-14T17:17:40Z
- WMT BUY $25.00 @ $132.48 (PAPER_SUBMITTED) submitted=2026-05-14T17:18:46Z

### Order Monitor
- Tracked: 11 | Filled: 8 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 3
- Runs today: 34 | Latest: order_monitor-20260514T171853-e8122113

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

**Generated:** 2026-05-14T17:19:58Z  **Run ID:** daily_summary-2026-05-14

### Account & Risk
- Equity: $99,802.48 | Cash: $99,652.76 | Buying power: $199,380.24
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.046214418 | $49.82 | $-0.09 (-0.19%) |
| JNJ | long | 0.217219435 | $50.02 | +$0.02 (0.04%) |
| WELL | long | 0.11425542 | $24.83 | $-0.17 (-0.69%) |
| WMT | long | 0.18899876 | $25.05 | +$0.05 (0.19%) |

### Open Orders (3)
- WMT BUY $25.00 @ $132.48 (limit) status=new
- JNJ BUY $25.00 @ $230.05 (limit) status=new
- EQIX BUY $25.00 @ $1,076.96 (limit) status=new

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.31%, breadth=56.96%)
- Candidates: 26 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-14T17:19:52Z

### Trade Plan
- Plan ID: `trade_plan-20260514T171952-80924b93`
- Generated: 2026-05-14T17:19:52Z | Expires: 2026-05-14T23:19:52Z
- Approved for execution: NO | Reason: max_orders_per_run_cap(1)_dequeued(non_blocking): ['MRK', 'GOOGL', 'CSCO', 'XOM', 'CAT', 'SLB', 'AVGO', 'FCX', 'BIL']; open_order_blocked_at_planning: ['JNJ', 'WMT', 'EQIX']
- All risk checks pass: YES
- No proposed orders.

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260514T171953-fe151e9b`
- All gates pass: NO

### Dry Runs Today (1)
- Pass: 1 | Fail: 0

### Paper Executions Today (12)
- EQIX BUY $25.00 @ $1,079.73 (PAPER_SUBMITTED) submitted=2026-05-14T14:56:26Z
- JNJ BUY $25.00 @ $230.12 (PAPER_SUBMITTED) submitted=2026-05-14T15:43:24Z
- EQIX SELL $25.00 @ $1,078.28 (PAPER_SUBMITTED) submitted=2026-05-14T15:45:44Z
- EQIX BUY $25.00 @ $1,078.43 (PAPER_SUBMITTED) submitted=2026-05-14T15:48:18Z
- EQIX BUY $25.00 @ $1,076.96 (PAPER_SUBMITTED) submitted=2026-05-14T16:31:14Z
- WMT BUY $25.00 @ $132.36 (PAPER_SUBMITTED) submitted=2026-05-14T16:52:33Z
- JNJ BUY $25.00 @ $230.05 (PAPER_SUBMITTED) submitted=2026-05-14T17:17:40Z
- WMT BUY $25.00 @ $132.48 (PAPER_SUBMITTED) submitted=2026-05-14T17:18:46Z

### Order Monitor
- Tracked: 11 | Filled: 8 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 3
- Runs today: 36 | Latest: order_monitor-20260514T171957-39d8f2be

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

**Generated:** 2026-05-14T17:21:09Z  **Run ID:** daily_summary-2026-05-14

### Account & Risk
- Equity: $99,802.28 | Cash: $99,577.76 | Buying power: $199,355.04
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092645923 | $99.75 | $-0.17 (-0.17%) |
| JNJ | long | 0.217219435 | $49.97 | $-0.03 (-0.06%) |
| WELL | long | 0.11425542 | $24.81 | $-0.19 (-0.75%) |
| WMT | long | 0.377715036 | $49.99 | $-0.01 (-0.01%) |

### Open Orders (1)
- JNJ BUY $25.00 @ $230.05 (limit) status=new

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.33%, breadth=56.96%)
- Candidates: 23 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-14T17:21:02Z

### Trade Plan
- Plan ID: `trade_plan-20260514T172103-835a36b9`
- Generated: 2026-05-14T17:21:03Z | Expires: 2026-05-14T23:21:03Z
- Approved for execution: **YES** | Reason: all_risk_checks_pass_and_paper_flag_set
- All risk checks pass: YES
- Proposed orders (1):
  - EQIX BUY $25.00 @ $1,078.96 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260514T172104-b71591c3`
- All gates pass: YES

### Dry Runs Today (1)
- Pass: 1 | Fail: 0

### Paper Executions Today (13)
- EQIX BUY $25.00 @ $1,079.73 (PAPER_SUBMITTED) submitted=2026-05-14T14:56:26Z
- JNJ BUY $25.00 @ $230.12 (PAPER_SUBMITTED) submitted=2026-05-14T15:43:24Z
- EQIX SELL $25.00 @ $1,078.28 (PAPER_SUBMITTED) submitted=2026-05-14T15:45:44Z
- EQIX BUY $25.00 @ $1,078.43 (PAPER_SUBMITTED) submitted=2026-05-14T15:48:18Z
- EQIX BUY $25.00 @ $1,076.96 (PAPER_SUBMITTED) submitted=2026-05-14T16:31:14Z
- WMT BUY $25.00 @ $132.36 (PAPER_SUBMITTED) submitted=2026-05-14T16:52:33Z
- JNJ BUY $25.00 @ $230.05 (PAPER_SUBMITTED) submitted=2026-05-14T17:17:40Z
- WMT BUY $25.00 @ $132.48 (PAPER_SUBMITTED) submitted=2026-05-14T17:18:46Z
- EQIX BUY $25.00 @ $1,078.96 (PAPER_SUBMITTED) submitted=2026-05-14T17:21:04Z

### Order Monitor
- Tracked: 12 | Filled: 11 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 1
- Runs today: 38 | Latest: order_monitor-20260514T172109-0160a03c

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

**Generated:** 2026-05-14T17:22:32Z  **Run ID:** daily_summary-2026-05-14

### Account & Risk
- Equity: $99,802.27 | Cash: $99,552.76 | Buying power: $199,355.03
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092645923 | $99.74 | $-0.17 (-0.17%) |
| JNJ | long | 0.325894297 | $74.97 | $-0.03 (-0.05%) |
| WELL | long | 0.11425542 | $24.83 | $-0.17 (-0.69%) |
| WMT | long | 0.377715036 | $49.97 | $-0.03 (-0.06%) |

### Open Orders (1)
- EQIX SELL $25.00 @ $1,076.63 (limit) status=new

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.31%, breadth=56.96%)
- Candidates: 21 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-14T17:22:25Z

### Trade Plan
- Plan ID: `trade_plan-20260514T172226-ed557b0a`
- Generated: 2026-05-14T17:22:26Z | Expires: 2026-05-14T23:22:26Z
- Approved for execution: **YES** | Reason: all_risk_checks_pass_and_paper_flag_set
- All risk checks pass: YES
- Proposed orders (1):
  - EQIX SELL $25.00 @ $1,076.63 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260514T172227-c20719b0`
- All gates pass: YES

### Dry Runs Today (1)
- Pass: 1 | Fail: 0

### Paper Executions Today (14)
- EQIX BUY $25.00 @ $1,079.73 (PAPER_SUBMITTED) submitted=2026-05-14T14:56:26Z
- JNJ BUY $25.00 @ $230.12 (PAPER_SUBMITTED) submitted=2026-05-14T15:43:24Z
- EQIX SELL $25.00 @ $1,078.28 (PAPER_SUBMITTED) submitted=2026-05-14T15:45:44Z
- EQIX BUY $25.00 @ $1,078.43 (PAPER_SUBMITTED) submitted=2026-05-14T15:48:18Z
- EQIX BUY $25.00 @ $1,076.96 (PAPER_SUBMITTED) submitted=2026-05-14T16:31:14Z
- WMT BUY $25.00 @ $132.36 (PAPER_SUBMITTED) submitted=2026-05-14T16:52:33Z
- JNJ BUY $25.00 @ $230.05 (PAPER_SUBMITTED) submitted=2026-05-14T17:17:40Z
- WMT BUY $25.00 @ $132.48 (PAPER_SUBMITTED) submitted=2026-05-14T17:18:46Z
- EQIX BUY $25.00 @ $1,078.96 (PAPER_SUBMITTED) submitted=2026-05-14T17:21:04Z
- EQIX SELL $25.00 @ $1,076.63 (PAPER_SUBMITTED) submitted=2026-05-14T17:22:27Z

### Order Monitor
- Tracked: 13 | Filled: 12 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 1
- Runs today: 40 | Latest: order_monitor-20260514T172232-2e4ad7df

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

**Generated:** 2026-05-14T17:23:43Z  **Run ID:** daily_summary-2026-05-14

### Account & Risk
- Equity: $99,802.35 | Cash: $99,577.76 | Buying power: $199,355.11
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.069427216 | $74.78 | $-0.09 (-0.12%) |
| JNJ | long | 0.325894297 | $74.97 | $-0.03 (-0.04%) |
| WELL | long | 0.11425542 | $24.85 | $-0.15 (-0.61%) |
| WMT | long | 0.377715036 | $49.99 | $-0.01 (-0.02%) |

### Open Orders (1)
- EQIX BUY $25.00 @ $1,076.63 (limit) status=new

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.36%, breadth=56.96%)
- Candidates: 22 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-14T17:23:35Z

### Trade Plan
- Plan ID: `trade_plan-20260514T172335-e46d4d8a`
- Generated: 2026-05-14T17:23:35Z | Expires: 2026-05-14T23:23:35Z
- Approved for execution: **YES** | Reason: all_risk_checks_pass_and_paper_flag_set
- All risk checks pass: YES
- Proposed orders (1):
  - EQIX BUY $25.00 @ $1,076.63 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260514T172337-37cce12a`
- All gates pass: YES

### Dry Runs Today (1)
- Pass: 1 | Fail: 0

### Paper Executions Today (15)
- EQIX BUY $25.00 @ $1,079.73 (PAPER_SUBMITTED) submitted=2026-05-14T14:56:26Z
- JNJ BUY $25.00 @ $230.12 (PAPER_SUBMITTED) submitted=2026-05-14T15:43:24Z
- EQIX SELL $25.00 @ $1,078.28 (PAPER_SUBMITTED) submitted=2026-05-14T15:45:44Z
- EQIX BUY $25.00 @ $1,078.43 (PAPER_SUBMITTED) submitted=2026-05-14T15:48:18Z
- EQIX BUY $25.00 @ $1,076.96 (PAPER_SUBMITTED) submitted=2026-05-14T16:31:14Z
- WMT BUY $25.00 @ $132.36 (PAPER_SUBMITTED) submitted=2026-05-14T16:52:33Z
- JNJ BUY $25.00 @ $230.05 (PAPER_SUBMITTED) submitted=2026-05-14T17:17:40Z
- WMT BUY $25.00 @ $132.48 (PAPER_SUBMITTED) submitted=2026-05-14T17:18:46Z
- EQIX BUY $25.00 @ $1,078.96 (PAPER_SUBMITTED) submitted=2026-05-14T17:21:04Z
- EQIX SELL $25.00 @ $1,076.63 (PAPER_SUBMITTED) submitted=2026-05-14T17:22:27Z
- EQIX BUY $25.00 @ $1,076.63 (PAPER_SUBMITTED) submitted=2026-05-14T17:23:37Z

### Order Monitor
- Tracked: 14 | Filled: 13 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 1
- Runs today: 42 | Latest: order_monitor-20260514T172342-3397bcc4

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

**Generated:** 2026-05-14T17:49:06Z  **Run ID:** daily_summary-2026-05-14

### Account & Risk
- Equity: $99,802.74 | Cash: $99,552.76 | Buying power: $199,355.50
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $99.88 | +$0.00 (0.00%) |
| JNJ | long | 0.325894297 | $75.04 | +$0.04 (0.06%) |
| WELL | long | 0.11425542 | $24.92 | $-0.08 (-0.31%) |
| WMT | long | 0.377715036 | $50.13 | +$0.13 (0.27%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.54%, breadth=56.96%)
- Candidates: 24 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-14T17:48:59Z

### Trade Plan
- Plan ID: `trade_plan-20260514T174859-80aa0a0e`
- Generated: 2026-05-14T17:48:59Z | Expires: 2026-05-14T23:48:59Z
- Approved for execution: NO | Reason: spread_blocked_all_orders: ['JNJ', 'WELL']; churn_blocked_all_orders: ['WMT', 'EQIX', 'AMD', 'GOOGL', 'CSCO', 'FCX', 'SLB', 'XOM', 'NEE', 'PM', 'BIL']
- All risk checks pass: YES
- No proposed orders.

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260514T174900-1d804822`
- All gates pass: NO

### Dry Runs Today (1)
- Pass: 1 | Fail: 0

### Paper Executions Today (16)
- EQIX BUY $25.00 @ $1,079.73 (PAPER_SUBMITTED) submitted=2026-05-14T14:56:26Z
- JNJ BUY $25.00 @ $230.12 (PAPER_SUBMITTED) submitted=2026-05-14T15:43:24Z
- EQIX SELL $25.00 @ $1,078.28 (PAPER_SUBMITTED) submitted=2026-05-14T15:45:44Z
- EQIX BUY $25.00 @ $1,078.43 (PAPER_SUBMITTED) submitted=2026-05-14T15:48:18Z
- EQIX BUY $25.00 @ $1,076.96 (PAPER_SUBMITTED) submitted=2026-05-14T16:31:14Z
- WMT BUY $25.00 @ $132.36 (PAPER_SUBMITTED) submitted=2026-05-14T16:52:33Z
- JNJ BUY $25.00 @ $230.05 (PAPER_SUBMITTED) submitted=2026-05-14T17:17:40Z
- WMT BUY $25.00 @ $132.48 (PAPER_SUBMITTED) submitted=2026-05-14T17:18:46Z
- EQIX BUY $25.00 @ $1,078.96 (PAPER_SUBMITTED) submitted=2026-05-14T17:21:04Z
- EQIX SELL $25.00 @ $1,076.63 (PAPER_SUBMITTED) submitted=2026-05-14T17:22:27Z
- EQIX BUY $25.00 @ $1,076.63 (PAPER_SUBMITTED) submitted=2026-05-14T17:23:37Z

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 44 | Latest: order_monitor-20260514T174905-df0c406c

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

**Generated:** 2026-05-14T17:50:28Z  **Run ID:** daily_summary-2026-05-14

### Account & Risk
- Equity: $99,802.68 | Cash: $99,552.76 | Buying power: $199,355.44
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $99.86 | $-0.02 (-0.02%) |
| JNJ | long | 0.325894297 | $75.00 | +$0.00 (0.01%) |
| WELL | long | 0.11425542 | $24.92 | $-0.08 (-0.31%) |
| WMT | long | 0.377715036 | $50.14 | +$0.14 (0.27%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.56%, breadth=56.96%)
- Candidates: 28 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-14T17:50:22Z

### Trade Plan
- Plan ID: `trade_plan-20260514T175022-194500dd`
- Generated: 2026-05-14T17:50:22Z | Expires: 2026-05-14T23:50:22Z
- Approved for execution: NO | Reason: spread_blocked_all_orders: ['JNJ', 'WELL']; churn_blocked_all_orders: ['WMT', 'EQIX', 'CAT', 'GOOGL', 'CSCO', 'FCX', 'AVGO', 'SLB', 'MS', 'XOM', 'BIL']
- All risk checks pass: YES
- No proposed orders.

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260514T175023-d2a85437`
- All gates pass: NO

### Dry Runs Today (1)
- Pass: 1 | Fail: 0

### Paper Executions Today (17)
- EQIX BUY $25.00 @ $1,079.73 (PAPER_SUBMITTED) submitted=2026-05-14T14:56:26Z
- JNJ BUY $25.00 @ $230.12 (PAPER_SUBMITTED) submitted=2026-05-14T15:43:24Z
- EQIX SELL $25.00 @ $1,078.28 (PAPER_SUBMITTED) submitted=2026-05-14T15:45:44Z
- EQIX BUY $25.00 @ $1,078.43 (PAPER_SUBMITTED) submitted=2026-05-14T15:48:18Z
- EQIX BUY $25.00 @ $1,076.96 (PAPER_SUBMITTED) submitted=2026-05-14T16:31:14Z
- WMT BUY $25.00 @ $132.36 (PAPER_SUBMITTED) submitted=2026-05-14T16:52:33Z
- JNJ BUY $25.00 @ $230.05 (PAPER_SUBMITTED) submitted=2026-05-14T17:17:40Z
- WMT BUY $25.00 @ $132.48 (PAPER_SUBMITTED) submitted=2026-05-14T17:18:46Z
- EQIX BUY $25.00 @ $1,078.96 (PAPER_SUBMITTED) submitted=2026-05-14T17:21:04Z
- EQIX SELL $25.00 @ $1,076.63 (PAPER_SUBMITTED) submitted=2026-05-14T17:22:27Z
- EQIX BUY $25.00 @ $1,076.63 (PAPER_SUBMITTED) submitted=2026-05-14T17:23:37Z

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 46 | Latest: order_monitor-20260514T175028-5d1f8063

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

**Generated:** 2026-05-14T17:52:26Z  **Run ID:** daily_summary-2026-05-14

### Account & Risk
- Equity: $99,802.59 | Cash: $99,552.76 | Buying power: $199,355.35
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $99.80 | $-0.08 (-0.08%) |
| JNJ | long | 0.325894297 | $75.00 | +$0.00 (0.00%) |
| WELL | long | 0.11425542 | $24.90 | $-0.10 (-0.42%) |
| WMT | long | 0.377715036 | $50.14 | +$0.14 (0.28%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.55%, breadth=56.96%)
- Candidates: 29 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-14T17:52:20Z

### Trade Plan
- Plan ID: `trade_plan-20260514T175220-3c52d3d5`
- Generated: 2026-05-14T17:52:20Z | Expires: 2026-05-14T23:52:20Z
- Approved for execution: NO | Reason: spread_blocked_all_orders: ['WELL']; churn_blocked_all_orders: ['JNJ', 'WMT', 'EQIX', 'AMD', 'CAT', 'GOOGL', 'CSCO', 'FCX', 'SLB', 'MS', 'XOM', 'BIL']
- All risk checks pass: YES
- No proposed orders.

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260514T175221-05f9ad9c`
- All gates pass: NO

### Dry Runs Today (1)
- Pass: 1 | Fail: 0

### Paper Executions Today (18)
- EQIX BUY $25.00 @ $1,079.73 (PAPER_SUBMITTED) submitted=2026-05-14T14:56:26Z
- JNJ BUY $25.00 @ $230.12 (PAPER_SUBMITTED) submitted=2026-05-14T15:43:24Z
- EQIX SELL $25.00 @ $1,078.28 (PAPER_SUBMITTED) submitted=2026-05-14T15:45:44Z
- EQIX BUY $25.00 @ $1,078.43 (PAPER_SUBMITTED) submitted=2026-05-14T15:48:18Z
- EQIX BUY $25.00 @ $1,076.96 (PAPER_SUBMITTED) submitted=2026-05-14T16:31:14Z
- WMT BUY $25.00 @ $132.36 (PAPER_SUBMITTED) submitted=2026-05-14T16:52:33Z
- JNJ BUY $25.00 @ $230.05 (PAPER_SUBMITTED) submitted=2026-05-14T17:17:40Z
- WMT BUY $25.00 @ $132.48 (PAPER_SUBMITTED) submitted=2026-05-14T17:18:46Z
- EQIX BUY $25.00 @ $1,078.96 (PAPER_SUBMITTED) submitted=2026-05-14T17:21:04Z
- EQIX SELL $25.00 @ $1,076.63 (PAPER_SUBMITTED) submitted=2026-05-14T17:22:27Z
- EQIX BUY $25.00 @ $1,076.63 (PAPER_SUBMITTED) submitted=2026-05-14T17:23:37Z

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 48 | Latest: order_monitor-20260514T175226-ca48b7d0

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

**Generated:** 2026-05-14T17:57:44Z  **Run ID:** daily_summary-2026-05-14

### Account & Risk
- Equity: $99,802.45 | Cash: $99,552.76 | Buying power: $199,355.21
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $99.83 | $-0.05 (-0.05%) |
| JNJ | long | 0.325894297 | $74.91 | $-0.09 (-0.12%) |
| WELL | long | 0.11425542 | $24.88 | $-0.12 (-0.48%) |
| WMT | long | 0.377715036 | $50.07 | +$0.07 (0.14%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.54%, breadth=56.96%)
- Candidates: 27 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-14T17:57:38Z

### Trade Plan
- Plan ID: `trade_plan-20260514T175738-9eae9b62`
- Generated: 2026-05-14T17:57:38Z | Expires: 2026-05-14T23:57:38Z
- Approved for execution: NO | Reason: spread_blocked_all_orders: ['JNJ']; churn_blocked_all_orders: ['WMT', 'EQIX', 'AMD', 'CAT', 'GOOGL', 'CSCO', 'FCX', 'SLB', 'XOM', 'WELL', 'BIL']
- All risk checks pass: YES
- No proposed orders.

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260514T175739-c2e2d180`
- All gates pass: NO

### Dry Runs Today (1)
- Pass: 1 | Fail: 0

### Paper Executions Today (19)
- EQIX BUY $25.00 @ $1,079.73 (PAPER_SUBMITTED) submitted=2026-05-14T14:56:26Z
- JNJ BUY $25.00 @ $230.12 (PAPER_SUBMITTED) submitted=2026-05-14T15:43:24Z
- EQIX SELL $25.00 @ $1,078.28 (PAPER_SUBMITTED) submitted=2026-05-14T15:45:44Z
- EQIX BUY $25.00 @ $1,078.43 (PAPER_SUBMITTED) submitted=2026-05-14T15:48:18Z
- EQIX BUY $25.00 @ $1,076.96 (PAPER_SUBMITTED) submitted=2026-05-14T16:31:14Z
- WMT BUY $25.00 @ $132.36 (PAPER_SUBMITTED) submitted=2026-05-14T16:52:33Z
- JNJ BUY $25.00 @ $230.05 (PAPER_SUBMITTED) submitted=2026-05-14T17:17:40Z
- WMT BUY $25.00 @ $132.48 (PAPER_SUBMITTED) submitted=2026-05-14T17:18:46Z
- EQIX BUY $25.00 @ $1,078.96 (PAPER_SUBMITTED) submitted=2026-05-14T17:21:04Z
- EQIX SELL $25.00 @ $1,076.63 (PAPER_SUBMITTED) submitted=2026-05-14T17:22:27Z
- EQIX BUY $25.00 @ $1,076.63 (PAPER_SUBMITTED) submitted=2026-05-14T17:23:37Z

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 50 | Latest: order_monitor-20260514T175743-7012dd33

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

**Generated:** 2026-05-14T18:07:56Z  **Run ID:** daily_summary-2026-05-14

### Account & Risk
- Equity: $99,802.14 | Cash: $99,552.76 | Buying power: $199,354.90
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $99.65 | $-0.23 (-0.23%) |
| JNJ | long | 0.325894297 | $74.90 | $-0.10 (-0.14%) |
| WELL | long | 0.11425542 | $24.84 | $-0.16 (-0.66%) |
| WMT | long | 0.377715036 | $49.99 | $-0.01 (-0.02%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.43%, breadth=56.96%)
- Candidates: 28 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-14T18:07:55Z

### Trade Plan
- Plan ID: `trade_plan-20260514T180756-fc25ae26`
- Generated: 2026-05-14T18:07:56Z | Expires: 2026-05-15T00:07:56Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- No proposed orders.

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260514T180756-13659e28`
- All gates pass: YES

### Dry Runs Today (1)
- Pass: 1 | Fail: 0

### Paper Executions Today (19)
- EQIX BUY $25.00 @ $1,079.73 (PAPER_SUBMITTED) submitted=2026-05-14T14:56:26Z
- JNJ BUY $25.00 @ $230.12 (PAPER_SUBMITTED) submitted=2026-05-14T15:43:24Z
- EQIX SELL $25.00 @ $1,078.28 (PAPER_SUBMITTED) submitted=2026-05-14T15:45:44Z
- EQIX BUY $25.00 @ $1,078.43 (PAPER_SUBMITTED) submitted=2026-05-14T15:48:18Z
- EQIX BUY $25.00 @ $1,076.96 (PAPER_SUBMITTED) submitted=2026-05-14T16:31:14Z
- WMT BUY $25.00 @ $132.36 (PAPER_SUBMITTED) submitted=2026-05-14T16:52:33Z
- JNJ BUY $25.00 @ $230.05 (PAPER_SUBMITTED) submitted=2026-05-14T17:17:40Z
- WMT BUY $25.00 @ $132.48 (PAPER_SUBMITTED) submitted=2026-05-14T17:18:46Z
- EQIX BUY $25.00 @ $1,078.96 (PAPER_SUBMITTED) submitted=2026-05-14T17:21:04Z
- EQIX SELL $25.00 @ $1,076.63 (PAPER_SUBMITTED) submitted=2026-05-14T17:22:27Z
- EQIX BUY $25.00 @ $1,076.63 (PAPER_SUBMITTED) submitted=2026-05-14T17:23:37Z

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 51 | Latest: order_monitor-20260514T180755-9e97e747

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

**Generated:** 2026-05-14T21:49:48Z  **Run ID:** daily_summary-2026-05-14

### Account & Risk
- Equity: $99,802.93 | Cash: $99,552.76 | Buying power: $199,355.69
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $100.03 | +$0.15 (0.15%) |
| JNJ | long | 0.325894297 | $75.22 | +$0.22 (0.29%) |
| WELL | long | 0.11425542 | $24.88 | $-0.12 (-0.48%) |
| WMT | long | 0.377715036 | $50.04 | +$0.04 (0.09%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.55%, breadth=58.23%)
- Candidates: 17 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-14T21:49:47Z

### Trade Plan
- Plan ID: `trade_plan-20260514T214947-b0ee5f7f`
- Generated: 2026-05-14T21:49:47Z | Expires: 2026-05-15T03:49:47Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- No proposed orders.

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260514T214947-fbdb271b`
- All gates pass: YES

### Dry Runs Today (1)
- Pass: 1 | Fail: 0

### Paper Executions Today (19)
- EQIX BUY $25.00 @ $1,079.73 (PAPER_SUBMITTED) submitted=2026-05-14T14:56:26Z
- JNJ BUY $25.00 @ $230.12 (PAPER_SUBMITTED) submitted=2026-05-14T15:43:24Z
- EQIX SELL $25.00 @ $1,078.28 (PAPER_SUBMITTED) submitted=2026-05-14T15:45:44Z
- EQIX BUY $25.00 @ $1,078.43 (PAPER_SUBMITTED) submitted=2026-05-14T15:48:18Z
- EQIX BUY $25.00 @ $1,076.96 (PAPER_SUBMITTED) submitted=2026-05-14T16:31:14Z
- WMT BUY $25.00 @ $132.36 (PAPER_SUBMITTED) submitted=2026-05-14T16:52:33Z
- JNJ BUY $25.00 @ $230.05 (PAPER_SUBMITTED) submitted=2026-05-14T17:17:40Z
- WMT BUY $25.00 @ $132.48 (PAPER_SUBMITTED) submitted=2026-05-14T17:18:46Z
- EQIX BUY $25.00 @ $1,078.96 (PAPER_SUBMITTED) submitted=2026-05-14T17:21:04Z
- EQIX SELL $25.00 @ $1,076.63 (PAPER_SUBMITTED) submitted=2026-05-14T17:22:27Z
- EQIX BUY $25.00 @ $1,076.63 (PAPER_SUBMITTED) submitted=2026-05-14T17:23:37Z

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 53 | Latest: order_monitor-20260514T214946-f5d4b8ea

### Alerts (total=10, today=2)
- By source: tradingview=8, test=2
- By next_step: request_trade_plan_unapproved=4, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-14

**Generated:** 2026-05-14T22:13:05Z  **Run ID:** daily_summary-2026-05-14

### Account & Risk
- Equity: $99,802.93 | Cash: $99,552.76 | Buying power: $199,355.69
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $100.03 | +$0.15 (0.15%) |
| JNJ | long | 0.325894297 | $75.22 | +$0.22 (0.29%) |
| WELL | long | 0.11425542 | $24.88 | $-0.12 (-0.48%) |
| WMT | long | 0.377715036 | $50.04 | +$0.04 (0.09%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.55%, breadth=58.23%)
- Candidates: 17 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-14T21:49:47Z

### Trade Plan
- Plan ID: `trade_plan-20260514T214947-b0ee5f7f`
- Generated: 2026-05-14T21:49:47Z | Expires: 2026-05-15T03:49:47Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- No proposed orders.

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260514T214947-fbdb271b`
- All gates pass: YES

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (19)
- EQIX BUY $25.00 @ $1,079.73 (PAPER_SUBMITTED) submitted=2026-05-14T14:56:26Z
- JNJ BUY $25.00 @ $230.12 (PAPER_SUBMITTED) submitted=2026-05-14T15:43:24Z
- EQIX SELL $25.00 @ $1,078.28 (PAPER_SUBMITTED) submitted=2026-05-14T15:45:44Z
- EQIX BUY $25.00 @ $1,078.43 (PAPER_SUBMITTED) submitted=2026-05-14T15:48:18Z
- EQIX BUY $25.00 @ $1,076.96 (PAPER_SUBMITTED) submitted=2026-05-14T16:31:14Z
- WMT BUY $25.00 @ $132.36 (PAPER_SUBMITTED) submitted=2026-05-14T16:52:33Z
- JNJ BUY $25.00 @ $230.05 (PAPER_SUBMITTED) submitted=2026-05-14T17:17:40Z
- WMT BUY $25.00 @ $132.48 (PAPER_SUBMITTED) submitted=2026-05-14T17:18:46Z
- EQIX BUY $25.00 @ $1,078.96 (PAPER_SUBMITTED) submitted=2026-05-14T17:21:04Z
- EQIX SELL $25.00 @ $1,076.63 (PAPER_SUBMITTED) submitted=2026-05-14T17:22:27Z
- EQIX BUY $25.00 @ $1,076.63 (PAPER_SUBMITTED) submitted=2026-05-14T17:23:37Z

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 53 | Latest: order_monitor-20260514T214946-f5d4b8ea

### Alerts (total=10, today=2)
- By source: tradingview=8, test=2
- By next_step: request_trade_plan_unapproved=4, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-15

**Generated:** 2026-05-15T21:41:04Z  **Run ID:** daily_summary-2026-05-15

### Account & Risk
- Equity: $99,799.26 | Cash: $99,552.75 | Buying power: $199,352.01
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $98.21 | $-1.63 (-1.64%) |
| JNJ | long | 0.325894297 | $74.10 | $-0.90 (-1.20%) |
| WELL | long | 0.11425542 | $24.42 | $-0.58 (-2.32%) |
| WMT | long | 0.377715036 | $49.78 | $-0.22 (-0.44%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_OFF** (SPY 200DMA=✓, 6m ROC=+8.16%, breadth=54.43%)
- Candidates: 15 | Selected: 0 | Excluded: 79
- Scanned at: 2026-05-15T21:41:04Z

### Trade Plan
- Plan ID: `trade_plan-20260515T214104-7822211e`
- Generated: 2026-05-15T21:41:04Z | Expires: 2026-05-16T03:41:04Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - EQIX SELL $25.00 @ $1,060.00 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260515T214104-6e56ad0c`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260515T214103-e9236256

### Alerts (total=12, today=2)
- By source: tradingview=10, test=2
- By next_step: request_trade_plan_unapproved=6, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-15

**Generated:** 2026-05-15T22:00:42Z  **Run ID:** daily_summary-2026-05-15

### Account & Risk
- Equity: $99,799.26 | Cash: $99,552.75 | Buying power: $199,352.01
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $98.21 | $-1.63 (-1.64%) |
| JNJ | long | 0.325894297 | $74.10 | $-0.90 (-1.20%) |
| WELL | long | 0.11425542 | $24.42 | $-0.58 (-2.32%) |
| WMT | long | 0.377715036 | $49.78 | $-0.22 (-0.44%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_OFF** (SPY 200DMA=✓, 6m ROC=+8.16%, breadth=54.43%)
- Candidates: 15 | Selected: 0 | Excluded: 79
- Scanned at: 2026-05-15T21:41:04Z

### Trade Plan
- Plan ID: `trade_plan-20260515T214104-7822211e`
- Generated: 2026-05-15T21:41:04Z | Expires: 2026-05-16T03:41:04Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - EQIX SELL $25.00 @ $1,060.00 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260515T214104-6e56ad0c`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260515T214103-e9236256

### Alerts (total=12, today=2)
- By source: tradingview=10, test=2
- By next_step: request_trade_plan_unapproved=6, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-18

**Generated:** 2026-05-18T21:50:59Z  **Run ID:** daily_summary-2026-05-18

### Account & Risk
- Equity: $99,800.42 | Cash: $99,552.75 | Buying power: $199,353.17
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $98.45 | $-1.39 (-1.39%) |
| JNJ | long | 0.325894297 | $74.59 | $-0.41 (-0.55%) |
| WELL | long | 0.11425542 | $24.29 | $-0.71 (-2.83%) |
| WMT | long | 0.377715036 | $50.33 | +$0.33 (0.67%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.87%, breadth=55.70%)
- Candidates: 19 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-18T21:50:58Z

### Trade Plan
- Plan ID: `trade_plan-20260518T215059-e7e56c9f`
- Generated: 2026-05-18T21:50:59Z | Expires: 2026-05-19T03:50:59Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - JNJ BUY $25.00 @ $228.93 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260518T215059-d65e28f1`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260518T215058-f205abfc

### Alerts (total=14, today=2)
- By source: tradingview=12, test=2
- By next_step: request_trade_plan_unapproved=8, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-18

**Generated:** 2026-05-18T22:04:30Z  **Run ID:** daily_summary-2026-05-18

### Account & Risk
- Equity: $99,800.42 | Cash: $99,552.75 | Buying power: $199,353.17
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $98.45 | $-1.39 (-1.39%) |
| JNJ | long | 0.325894297 | $74.59 | $-0.41 (-0.55%) |
| WELL | long | 0.11425542 | $24.29 | $-0.71 (-2.83%) |
| WMT | long | 0.377715036 | $50.33 | +$0.33 (0.67%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.87%, breadth=55.70%)
- Candidates: 19 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-18T21:50:58Z

### Trade Plan
- Plan ID: `trade_plan-20260518T215059-e7e56c9f`
- Generated: 2026-05-18T21:50:59Z | Expires: 2026-05-19T03:50:59Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - JNJ BUY $25.00 @ $228.93 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260518T215059-d65e28f1`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260518T215058-f205abfc

### Alerts (total=14, today=2)
- By source: tradingview=12, test=2
- By next_step: request_trade_plan_unapproved=8, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-19

**Generated:** 2026-05-19T22:00:14Z  **Run ID:** daily_summary-2026-05-19

### Account & Risk
- Equity: $99,800.35 | Cash: $99,552.75 | Buying power: $199,353.10
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $97.19 | $-2.65 (-2.66%) |
| JNJ | long | 0.325894297 | $74.82 | $-0.18 (-0.24%) |
| WELL | long | 0.11425542 | $24.91 | $-0.09 (-0.37%) |
| WMT | long | 0.377715036 | $50.69 | +$0.69 (1.37%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_OFF** (SPY 200DMA=✓, 6m ROC=+9.21%, breadth=53.16%)
- Candidates: 13 | Selected: 0 | Excluded: 79
- Scanned at: 2026-05-19T22:00:13Z

### Trade Plan
- Plan ID: `trade_plan-20260519T220014-e0847b4b`
- Generated: 2026-05-19T22:00:14Z | Expires: 2026-05-20T04:00:14Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - EQIX SELL $25.00 @ $1,049.00 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260519T220014-65d972d2`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260519T220013-6d911730

### Alerts (total=16, today=2)
- By source: tradingview=14, test=2
- By next_step: request_trade_plan_unapproved=10, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-19

**Generated:** 2026-05-19T22:17:44Z  **Run ID:** daily_summary-2026-05-19

### Account & Risk
- Equity: $99,800.35 | Cash: $99,552.75 | Buying power: $199,353.10
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $97.19 | $-2.65 (-2.66%) |
| JNJ | long | 0.325894297 | $74.82 | $-0.18 (-0.24%) |
| WELL | long | 0.11425542 | $24.91 | $-0.09 (-0.37%) |
| WMT | long | 0.377715036 | $50.69 | +$0.69 (1.37%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_OFF** (SPY 200DMA=✓, 6m ROC=+9.21%, breadth=53.16%)
- Candidates: 13 | Selected: 0 | Excluded: 79
- Scanned at: 2026-05-19T22:00:13Z

### Trade Plan
- Plan ID: `trade_plan-20260519T220014-e0847b4b`
- Generated: 2026-05-19T22:00:14Z | Expires: 2026-05-20T04:00:14Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - EQIX SELL $25.00 @ $1,049.00 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260519T220014-65d972d2`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260519T220013-6d911730

### Alerts (total=16, today=2)
- By source: tradingview=14, test=2
- By next_step: request_trade_plan_unapproved=10, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-20

**Generated:** 2026-05-20T22:15:23Z  **Run ID:** daily_summary-2026-05-20

### Account & Risk
- Equity: $99,800.44 | Cash: $99,552.75 | Buying power: $199,353.19
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $98.49 | $-1.36 (-1.36%) |
| JNJ | long | 0.325894297 | $74.72 | $-0.28 (-0.37%) |
| WELL | long | 0.11425542 | $24.91 | $-0.09 (-0.37%) |
| WMT | long | 0.377715036 | $49.58 | $-0.42 (-0.84%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+11.35%, breadth=56.96%)
- Candidates: 17 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-20T22:15:22Z

### Trade Plan
- Plan ID: `trade_plan-20260520T221523-26202569`
- Generated: 2026-05-20T22:15:23Z | Expires: 2026-05-21T04:15:23Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - JNJ BUY $25.00 @ $229.27 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260520T221523-122ec062`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260520T221522-c13c2584

### Alerts (total=18, today=2)
- By source: tradingview=16, test=2
- By next_step: request_trade_plan_unapproved=12, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-20

**Generated:** 2026-05-20T22:24:59Z  **Run ID:** daily_summary-2026-05-20

### Account & Risk
- Equity: $99,800.44 | Cash: $99,552.75 | Buying power: $199,353.19
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $98.49 | $-1.36 (-1.36%) |
| JNJ | long | 0.325894297 | $74.72 | $-0.28 (-0.37%) |
| WELL | long | 0.11425542 | $24.91 | $-0.09 (-0.37%) |
| WMT | long | 0.377715036 | $49.58 | $-0.42 (-0.84%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+11.35%, breadth=56.96%)
- Candidates: 17 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-20T22:15:22Z

### Trade Plan
- Plan ID: `trade_plan-20260520T221523-26202569`
- Generated: 2026-05-20T22:15:23Z | Expires: 2026-05-21T04:15:23Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - JNJ BUY $25.00 @ $229.27 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260520T221523-122ec062`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260520T221522-c13c2584

### Alerts (total=18, today=2)
- By source: tradingview=16, test=2
- By next_step: request_trade_plan_unapproved=12, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-21

**Generated:** 2026-05-21T22:05:34Z  **Run ID:** daily_summary-2026-05-21

### Account & Risk
- Equity: $99,798.34 | Cash: $99,552.75 | Buying power: $199,351.09
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $99.41 | $-0.44 (-0.44%) |
| JNJ | long | 0.325894297 | $75.50 | +$0.50 (0.67%) |
| WELL | long | 0.11425542 | $24.68 | $-0.32 (-1.28%) |
| WMT | long | 0.377715036 | $46.01 | $-3.99 (-7.99%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+12.50%, breadth=58.23%)
- Candidates: 20 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-21T22:05:33Z

### Trade Plan
- Plan ID: `trade_plan-20260521T220533-65e68056`
- Generated: 2026-05-21T22:05:33Z | Expires: 2026-05-22T04:05:33Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - WMT SELL $25.00 @ $121.80 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260521T220534-88285473`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260521T220533-8df90e99

### Alerts (total=20, today=2)
- By source: tradingview=18, test=2
- By next_step: request_trade_plan_unapproved=14, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-21

**Generated:** 2026-05-21T22:20:19Z  **Run ID:** daily_summary-2026-05-21

### Account & Risk
- Equity: $99,798.34 | Cash: $99,552.75 | Buying power: $199,351.09
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $99.41 | $-0.44 (-0.44%) |
| JNJ | long | 0.325894297 | $75.50 | +$0.50 (0.67%) |
| WELL | long | 0.11425542 | $24.68 | $-0.32 (-1.28%) |
| WMT | long | 0.377715036 | $46.01 | $-3.99 (-7.99%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+12.50%, breadth=58.23%)
- Candidates: 20 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-21T22:05:33Z

### Trade Plan
- Plan ID: `trade_plan-20260521T220533-65e68056`
- Generated: 2026-05-21T22:05:33Z | Expires: 2026-05-22T04:05:33Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - WMT SELL $25.00 @ $121.80 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260521T220534-88285473`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260521T220533-8df90e99

### Alerts (total=20, today=2)
- By source: tradingview=18, test=2
- By next_step: request_trade_plan_unapproved=14, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-22

**Generated:** 2026-05-22T21:51:48Z  **Run ID:** daily_summary-2026-05-22

### Account & Risk
- Equity: $99,799.22 | Cash: $99,552.75 | Buying power: $199,351.97
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $100.04 | +$0.20 (0.20%) |
| JNJ | long | 0.325894297 | $76.37 | +$1.37 (1.83%) |
| WELL | long | 0.11425542 | $24.70 | $-0.30 (-1.21%) |
| WMT | long | 0.377715036 | $45.35 | $-4.65 (-9.30%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+12.52%, breadth=60.76%)
- Candidates: 12 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-22T21:51:48Z

### Trade Plan
- Plan ID: `trade_plan-20260522T215148-d536c070`
- Generated: 2026-05-22T21:51:48Z | Expires: 2026-05-23T03:51:48Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - O BUY $25.00 @ $62.03 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260522T215148-eb37f028`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260522T215147-6804bf7b

### Alerts (total=21, today=1)
- By source: tradingview=19, test=2
- By next_step: request_trade_plan_unapproved=15, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-22

**Generated:** 2026-05-22T22:09:50Z  **Run ID:** daily_summary-2026-05-22

### Account & Risk
- Equity: $99,799.22 | Cash: $99,552.75 | Buying power: $199,351.97
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $100.04 | +$0.20 (0.20%) |
| JNJ | long | 0.325894297 | $76.37 | +$1.37 (1.83%) |
| WELL | long | 0.11425542 | $24.70 | $-0.30 (-1.21%) |
| WMT | long | 0.377715036 | $45.35 | $-4.65 (-9.30%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+12.52%, breadth=60.76%)
- Candidates: 12 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-22T21:51:48Z

### Trade Plan
- Plan ID: `trade_plan-20260522T215148-d536c070`
- Generated: 2026-05-22T21:51:48Z | Expires: 2026-05-23T03:51:48Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - O BUY $25.00 @ $62.03 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260522T215148-eb37f028`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260522T215147-6804bf7b

### Alerts (total=21, today=1)
- By source: tradingview=19, test=2
- By next_step: request_trade_plan_unapproved=15, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-25

**Generated:** 2026-05-25T21:50:50Z  **Run ID:** daily_summary-2026-05-25

### Account & Risk
- Equity: $99,799.29 | Cash: $99,552.75 | Buying power: $199,352.04
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $100.04 | +$0.20 (0.20%) |
| JNJ | long | 0.325894297 | $76.37 | +$1.37 (1.83%) |
| WELL | long | 0.11425542 | $24.70 | $-0.30 (-1.21%) |
| WMT | long | 0.377715036 | $45.43 | $-4.57 (-9.14%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+12.52%, breadth=60.76%)
- Candidates: 12 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-25T21:50:50Z

### Trade Plan
- Plan ID: `trade_plan-20260525T215050-9fe086a0`
- Generated: 2026-05-25T21:50:50Z | Expires: 2026-05-26T03:50:50Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - O BUY $25.00 @ $62.03 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260525T215050-7b499df9`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260525T215049-78aa7d84

### Alerts (total=21, today=0)
- By source: tradingview=19, test=2
- By next_step: request_trade_plan_unapproved=15, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-25

**Generated:** 2026-05-25T22:09:47Z  **Run ID:** daily_summary-2026-05-25

### Account & Risk
- Equity: $99,799.29 | Cash: $99,552.75 | Buying power: $199,352.04
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $100.04 | +$0.20 (0.20%) |
| JNJ | long | 0.325894297 | $76.37 | +$1.37 (1.83%) |
| WELL | long | 0.11425542 | $24.70 | $-0.30 (-1.21%) |
| WMT | long | 0.377715036 | $45.43 | $-4.57 (-9.14%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+12.52%, breadth=60.76%)
- Candidates: 12 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-25T21:50:50Z

### Trade Plan
- Plan ID: `trade_plan-20260525T215050-9fe086a0`
- Generated: 2026-05-25T21:50:50Z | Expires: 2026-05-26T03:50:50Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - O BUY $25.00 @ $62.03 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260525T215050-7b499df9`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260525T215049-78aa7d84

### Alerts (total=21, today=0)
- By source: tradingview=19, test=2
- By next_step: request_trade_plan_unapproved=15, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-26

**Generated:** 2026-05-26T22:11:53Z  **Run ID:** daily_summary-2026-05-26

### Account & Risk
- Equity: $99,797.01 | Cash: $99,552.75 | Buying power: $199,349.76
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $99.60 | $-0.24 (-0.24%) |
| JNJ | long | 0.325894297 | $74.98 | $-0.02 (-0.03%) |
| WELL | long | 0.11425542 | $24.92 | $-0.08 (-0.31%) |
| WMT | long | 0.377715036 | $44.76 | $-5.24 (-10.48%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+15.03%, breadth=62.03%)
- Candidates: 16 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-26T22:11:52Z

### Trade Plan
- Plan ID: `trade_plan-20260526T221152-f5a3f47e`
- Generated: 2026-05-26T22:11:52Z | Expires: 2026-05-27T04:11:52Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - LIN BUY $25.00 @ $514.87 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260526T221152-7836405c`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260526T221152-8901247a

### Alerts (total=23, today=2)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-26

**Generated:** 2026-05-26T22:20:52Z  **Run ID:** daily_summary-2026-05-26

### Account & Risk
- Equity: $99,797.01 | Cash: $99,552.75 | Buying power: $199,349.76
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $99.60 | $-0.24 (-0.24%) |
| JNJ | long | 0.325894297 | $74.98 | $-0.02 (-0.03%) |
| WELL | long | 0.11425542 | $24.92 | $-0.08 (-0.31%) |
| WMT | long | 0.377715036 | $44.76 | $-5.24 (-10.48%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+15.03%, breadth=62.03%)
- Candidates: 16 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-26T22:11:52Z

### Trade Plan
- Plan ID: `trade_plan-20260526T221152-f5a3f47e`
- Generated: 2026-05-26T22:11:52Z | Expires: 2026-05-27T04:11:52Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - LIN BUY $25.00 @ $514.87 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260526T221152-7836405c`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260526T221152-8901247a

### Alerts (total=23, today=2)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-27

**Generated:** 2026-05-27T22:22:29Z  **Run ID:** daily_summary-2026-05-27

### Account & Risk
- Equity: $99,796.58 | Cash: $99,552.75 | Buying power: $199,349.33
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $99.16 | $-0.69 (-0.69%) |
| JNJ | long | 0.325894297 | $75.33 | +$0.33 (0.44%) |
| WELL | long | 0.11425542 | $24.47 | $-0.53 (-2.11%) |
| WMT | long | 0.377715036 | $44.88 | $-5.12 (-10.24%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+13.87%, breadth=59.49%)
- Candidates: 14 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-27T22:22:28Z

### Trade Plan
- Plan ID: `trade_plan-20260527T222228-34add6a2`
- Generated: 2026-05-27T22:22:28Z | Expires: 2026-05-28T04:22:28Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - PLD BUY $25.00 @ $146.52 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260527T222228-33852481`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260527T222228-e2fba483

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-27

**Generated:** 2026-05-27T22:42:04Z  **Run ID:** daily_summary-2026-05-27

### Account & Risk
- Equity: $99,796.58 | Cash: $99,552.75 | Buying power: $199,349.33
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $99.16 | $-0.69 (-0.69%) |
| JNJ | long | 0.325894297 | $75.33 | +$0.33 (0.44%) |
| WELL | long | 0.11425542 | $24.47 | $-0.53 (-2.11%) |
| WMT | long | 0.377715036 | $44.88 | $-5.12 (-10.24%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+13.87%, breadth=59.49%)
- Candidates: 14 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-27T22:22:28Z

### Trade Plan
- Plan ID: `trade_plan-20260527T222228-34add6a2`
- Generated: 2026-05-27T22:22:28Z | Expires: 2026-05-28T04:22:28Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - PLD BUY $25.00 @ $146.52 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260527T222228-33852481`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260527T222228-e2fba483

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-28

**Generated:** 2026-05-28T22:21:35Z  **Run ID:** daily_summary-2026-05-28

### Account & Risk
- Equity: $99,795.89 | Cash: $99,552.75 | Buying power: $199,348.64
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $99.07 | $-0.77 (-0.77%) |
| JNJ | long | 0.325894297 | $75.28 | +$0.28 (0.38%) |
| WELL | long | 0.11425542 | $24.03 | $-0.97 (-3.89%) |
| WMT | long | 0.377715036 | $44.75 | $-5.25 (-10.50%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+12.84%, breadth=56.96%)
- Candidates: 11 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-28T22:21:34Z

### Trade Plan
- Plan ID: `trade_plan-20260528T222134-2790195b`
- Generated: 2026-05-28T22:21:34Z | Expires: 2026-05-29T04:21:34Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - JNJ BUY $25.00 @ $230.80 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260528T222134-4554f8bb`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260528T222134-e678953d

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-28

**Generated:** 2026-05-28T22:42:17Z  **Run ID:** daily_summary-2026-05-28

### Account & Risk
- Equity: $99,795.89 | Cash: $99,552.75 | Buying power: $199,348.64
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $99.07 | $-0.77 (-0.77%) |
| JNJ | long | 0.325894297 | $75.28 | +$0.28 (0.38%) |
| WELL | long | 0.11425542 | $24.03 | $-0.97 (-3.89%) |
| WMT | long | 0.377715036 | $44.75 | $-5.25 (-10.50%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+12.84%, breadth=56.96%)
- Candidates: 11 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-28T22:21:34Z

### Trade Plan
- Plan ID: `trade_plan-20260528T222134-2790195b`
- Generated: 2026-05-28T22:21:34Z | Expires: 2026-05-29T04:21:34Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - JNJ BUY $25.00 @ $230.80 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260528T222134-4554f8bb`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260528T222134-e678953d

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-29

**Generated:** 2026-05-29T22:18:30Z  **Run ID:** daily_summary-2026-05-29

### Account & Risk
- Equity: $99,792.28 | Cash: $99,552.75 | Buying power: $199,345.03
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $98.81 | $-1.03 (-1.03%) |
| JNJ | long | 0.325894297 | $73.48 | $-1.52 (-2.02%) |
| WELL | long | 0.11425542 | $23.48 | $-1.52 (-6.08%) |
| WMT | long | 0.377715036 | $43.75 | $-6.25 (-12.49%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+12.05%, breadth=55.70%)
- Candidates: 13 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-29T22:18:30Z

### Trade Plan
- Plan ID: `trade_plan-20260529T221830-a6bd11cf`
- Generated: 2026-05-29T22:18:30Z | Expires: 2026-05-30T04:18:30Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - EQIX BUY $25.00 @ $1,067.71 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260529T221830-792cd51c`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260529T221829-8b0b36ee

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-05-29

**Generated:** 2026-05-29T22:38:16Z  **Run ID:** daily_summary-2026-05-29

### Account & Risk
- Equity: $99,792.28 | Cash: $99,552.75 | Buying power: $199,345.03
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $98.81 | $-1.03 (-1.03%) |
| JNJ | long | 0.325894297 | $73.48 | $-1.52 (-2.02%) |
| WELL | long | 0.11425542 | $23.48 | $-1.52 (-6.08%) |
| WMT | long | 0.377715036 | $43.75 | $-6.25 (-12.49%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+12.05%, breadth=55.70%)
- Candidates: 13 | Selected: 10 | Excluded: 69
- Scanned at: 2026-05-29T22:18:30Z

### Trade Plan
- Plan ID: `trade_plan-20260529T221830-a6bd11cf`
- Generated: 2026-05-29T22:18:30Z | Expires: 2026-05-30T04:18:30Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - EQIX BUY $25.00 @ $1,067.71 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260529T221830-792cd51c`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260529T221829-8b0b36ee

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-01

**Generated:** 2026-06-01T22:50:35Z  **Run ID:** daily_summary-2026-06-01

### Account & Risk
- Equity: $99,788.80 | Cash: $99,552.75 | Buying power: $199,341.55
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $97.37 | $-2.47 (-2.47%) |
| JNJ | long | 0.325894297 | $72.93 | $-2.07 (-2.77%) |
| WELL | long | 0.11425542 | $22.55 | $-2.45 (-9.80%) |
| WMT | long | 0.377715036 | $43.20 | $-6.80 (-13.59%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_OFF** (SPY 200DMA=✓, 6m ROC=+11.59%, breadth=53.16%)
- Candidates: 9 | Selected: 0 | Excluded: 79
- Scanned at: 2026-06-01T22:50:35Z

### Trade Plan
- Plan ID: `trade_plan-20260601T225035-7f1f2e01`
- Generated: 2026-06-01T22:50:35Z | Expires: 2026-06-02T04:50:35Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- No proposed orders.

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260601T225035-7c1afea9`
- All gates pass: YES

### Dry Runs Today (1)
- Pass: 1 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260601T225034-03c2faf6

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-01

**Generated:** 2026-06-01T23:03:26Z  **Run ID:** daily_summary-2026-06-01

### Account & Risk
- Equity: $99,788.80 | Cash: $99,552.75 | Buying power: $199,341.55
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $97.37 | $-2.47 (-2.47%) |
| JNJ | long | 0.325894297 | $72.93 | $-2.07 (-2.77%) |
| WELL | long | 0.11425542 | $22.55 | $-2.45 (-9.80%) |
| WMT | long | 0.377715036 | $43.20 | $-6.80 (-13.59%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_OFF** (SPY 200DMA=✓, 6m ROC=+11.59%, breadth=53.16%)
- Candidates: 9 | Selected: 0 | Excluded: 79
- Scanned at: 2026-06-01T22:50:35Z

### Trade Plan
- Plan ID: `trade_plan-20260601T225035-7f1f2e01`
- Generated: 2026-06-01T22:50:35Z | Expires: 2026-06-02T04:50:35Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- No proposed orders.

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260601T225035-7c1afea9`
- All gates pass: YES

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260601T225034-03c2faf6

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-02

**Generated:** 2026-06-02T22:51:05Z  **Run ID:** daily_summary-2026-06-02

### Account & Risk
- Equity: $99,789.55 | Cash: $99,552.75 | Buying power: $199,342.30
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $99.30 | $-0.54 (-0.54%) |
| JNJ | long | 0.325894297 | $72.51 | $-2.49 (-3.32%) |
| WELL | long | 0.11425542 | $22.32 | $-2.68 (-10.72%) |
| WMT | long | 0.377715036 | $42.67 | $-7.33 (-14.67%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_OFF** (SPY 200DMA=✓, 6m ROC=+11.14%, breadth=51.90%)
- Candidates: 12 | Selected: 0 | Excluded: 79
- Scanned at: 2026-06-02T22:51:04Z

### Trade Plan
- Plan ID: `trade_plan-20260602T225104-87aaea10`
- Generated: 2026-06-02T22:51:04Z | Expires: 2026-06-03T04:51:04Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - BIL BUY $25.00 @ $91.40 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260602T225105-e67e5df7`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS, RISK_LIMITS_RESPECTED

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x
  - RISK_LIMITS_RESPECTED: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260602T225104-be9fee17

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-02

**Generated:** 2026-06-02T23:03:48Z  **Run ID:** daily_summary-2026-06-02

### Account & Risk
- Equity: $99,789.55 | Cash: $99,552.75 | Buying power: $199,342.30
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $99.30 | $-0.54 (-0.54%) |
| JNJ | long | 0.325894297 | $72.51 | $-2.49 (-3.32%) |
| WELL | long | 0.11425542 | $22.32 | $-2.68 (-10.72%) |
| WMT | long | 0.377715036 | $42.67 | $-7.33 (-14.67%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_OFF** (SPY 200DMA=✓, 6m ROC=+11.14%, breadth=51.90%)
- Candidates: 12 | Selected: 0 | Excluded: 79
- Scanned at: 2026-06-02T22:51:04Z

### Trade Plan
- Plan ID: `trade_plan-20260602T225104-87aaea10`
- Generated: 2026-06-02T22:51:04Z | Expires: 2026-06-03T04:51:04Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - BIL BUY $25.00 @ $91.40 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260602T225105-e67e5df7`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS, RISK_LIMITS_RESPECTED

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260602T225104-be9fee17

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-03

**Generated:** 2026-06-03T22:53:09Z  **Run ID:** daily_summary-2026-06-03

### Account & Risk
- Equity: $99,792.69 | Cash: $99,552.75 | Buying power: $199,345.44
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $99.78 | $-0.06 (-0.06%) |
| JNJ | long | 0.325894297 | $72.75 | $-2.25 (-3.00%) |
| WELL | long | 0.11425542 | $22.80 | $-2.20 (-8.78%) |
| WMT | long | 0.377715036 | $44.60 | $-5.40 (-10.80%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_OFF** (SPY 200DMA=✓, 6m ROC=+10.87%, breadth=53.16%)
- Candidates: 11 | Selected: 0 | Excluded: 79
- Scanned at: 2026-06-03T22:53:08Z

### Trade Plan
- Plan ID: `trade_plan-20260603T225309-f5f975f1`
- Generated: 2026-06-03T22:53:09Z | Expires: 2026-06-04T04:53:09Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - BIL BUY $25.00 @ $91.41 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260603T225309-ad0bf62b`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS, RISK_LIMITS_RESPECTED

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x
  - RISK_LIMITS_RESPECTED: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260603T225308-6ba835d5

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-03

**Generated:** 2026-06-03T23:06:11Z  **Run ID:** daily_summary-2026-06-03

### Account & Risk
- Equity: $99,792.69 | Cash: $99,552.75 | Buying power: $199,345.44
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $99.78 | $-0.06 (-0.06%) |
| JNJ | long | 0.325894297 | $72.75 | $-2.25 (-3.00%) |
| WELL | long | 0.11425542 | $22.80 | $-2.20 (-8.78%) |
| WMT | long | 0.377715036 | $44.60 | $-5.40 (-10.80%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_OFF** (SPY 200DMA=✓, 6m ROC=+10.87%, breadth=53.16%)
- Candidates: 11 | Selected: 0 | Excluded: 79
- Scanned at: 2026-06-03T22:53:08Z

### Trade Plan
- Plan ID: `trade_plan-20260603T225309-f5f975f1`
- Generated: 2026-06-03T22:53:09Z | Expires: 2026-06-04T04:53:09Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - BIL BUY $25.00 @ $91.41 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260603T225309-ad0bf62b`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS, RISK_LIMITS_RESPECTED

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260603T225308-6ba835d5

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-04

**Generated:** 2026-06-04T22:11:33Z  **Run ID:** daily_summary-2026-06-04

### Account & Risk
- Equity: $99,795.75 | Cash: $99,552.75 | Buying power: $398,697.00
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $100.91 | +$1.07 (1.07%) |
| JNJ | long | 0.325894297 | $74.55 | $-0.45 (-0.60%) |
| WELL | long | 0.11425542 | $22.95 | $-2.05 (-8.21%) |
| WMT | long | 0.377715036 | $44.59 | $-5.41 (-10.81%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+11.08%, breadth=58.23%)
- Candidates: 10 | Selected: 9 | Excluded: 70
- Scanned at: 2026-06-04T22:11:32Z

### Trade Plan
- Plan ID: `trade_plan-20260604T221132-a5501470`
- Generated: 2026-06-04T22:11:32Z | Expires: 2026-06-05T04:11:32Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - AEP BUY $25.00 @ $127.80 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260604T221132-02cd1cac`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260604T221131-1803134e

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-04

**Generated:** 2026-06-04T22:22:16Z  **Run ID:** daily_summary-2026-06-04

### Account & Risk
- Equity: $99,795.75 | Cash: $99,552.75 | Buying power: $398,697.00
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $100.91 | +$1.07 (1.07%) |
| JNJ | long | 0.325894297 | $74.55 | $-0.45 (-0.60%) |
| WELL | long | 0.11425542 | $22.95 | $-2.05 (-8.21%) |
| WMT | long | 0.377715036 | $44.59 | $-5.41 (-10.81%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+11.08%, breadth=58.23%)
- Candidates: 10 | Selected: 9 | Excluded: 70
- Scanned at: 2026-06-04T22:11:32Z

### Trade Plan
- Plan ID: `trade_plan-20260604T221132-a5501470`
- Generated: 2026-06-04T22:11:32Z | Expires: 2026-06-05T04:11:32Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - AEP BUY $25.00 @ $127.80 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260604T221132-02cd1cac`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260604T221131-1803134e

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-05

**Generated:** 2026-06-05T22:05:51Z  **Run ID:** daily_summary-2026-06-05

### Account & Risk
- Equity: $99,796.70 | Cash: $99,552.75 | Buying power: $398,894.07
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $100.06 | +$0.22 (0.22%) |
| JNJ | long | 0.325894297 | $75.61 | +$0.61 (0.81%) |
| WELL | long | 0.11425542 | $23.64 | $-1.36 (-5.43%) |
| WMT | long | 0.377715036 | $44.64 | $-5.36 (-10.72%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+7.84%, breadth=60.76%)
- Candidates: 19 | Selected: 10 | Excluded: 69
- Scanned at: 2026-06-05T22:05:50Z

### Trade Plan
- Plan ID: `trade_plan-20260605T220550-ed452261`
- Generated: 2026-06-05T22:05:50Z | Expires: 2026-06-06T04:05:50Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - JNJ BUY $25.00 @ $232.71 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260605T220550-82db17cb`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260605T220550-414e925e

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-05

**Generated:** 2026-06-05T22:15:41Z  **Run ID:** daily_summary-2026-06-05

### Account & Risk
- Equity: $99,796.70 | Cash: $99,552.75 | Buying power: $398,894.07
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $100.06 | +$0.22 (0.22%) |
| JNJ | long | 0.325894297 | $75.61 | +$0.61 (0.81%) |
| WELL | long | 0.11425542 | $23.64 | $-1.36 (-5.43%) |
| WMT | long | 0.377715036 | $44.64 | $-5.36 (-10.72%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+7.84%, breadth=60.76%)
- Candidates: 19 | Selected: 10 | Excluded: 69
- Scanned at: 2026-06-05T22:05:50Z

### Trade Plan
- Plan ID: `trade_plan-20260605T220550-ed452261`
- Generated: 2026-06-05T22:05:50Z | Expires: 2026-06-06T04:05:50Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - JNJ BUY $25.00 @ $232.71 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260605T220550-82db17cb`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260605T220550-414e925e

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-08

**Generated:** 2026-06-08T22:15:13Z  **Run ID:** daily_summary-2026-06-08

### Account & Risk
- Equity: $99,794.78 | Cash: $99,552.75 | Buying power: $398,888.68
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $98.46 | $-1.38 (-1.38%) |
| JNJ | long | 0.325894297 | $75.58 | +$0.58 (0.77%) |
| WELL | long | 0.11425542 | $22.85 | $-2.15 (-8.60%) |
| WMT | long | 0.377715036 | $45.14 | $-4.86 (-9.72%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_OFF** (SPY 200DMA=✓, 6m ROC=+8.00%, breadth=54.43%)
- Candidates: 10 | Selected: 0 | Excluded: 79
- Scanned at: 2026-06-08T22:15:12Z

### Trade Plan
- Plan ID: `trade_plan-20260608T221512-6e5e2f60`
- Generated: 2026-06-08T22:15:12Z | Expires: 2026-06-09T04:15:12Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - BIL BUY $25.00 @ $91.45 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260608T221513-a0e5c744`
- All gates pass: NO
- Failed gates: RISK_LIMITS_RESPECTED

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - RISK_LIMITS_RESPECTED: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260608T221512-d313f095

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-08

**Generated:** 2026-06-08T22:27:29Z  **Run ID:** daily_summary-2026-06-08

### Account & Risk
- Equity: $99,794.78 | Cash: $99,552.75 | Buying power: $398,888.68
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $98.46 | $-1.38 (-1.38%) |
| JNJ | long | 0.325894297 | $75.58 | +$0.58 (0.77%) |
| WELL | long | 0.11425542 | $22.85 | $-2.15 (-8.60%) |
| WMT | long | 0.377715036 | $45.14 | $-4.86 (-9.72%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_OFF** (SPY 200DMA=✓, 6m ROC=+8.00%, breadth=54.43%)
- Candidates: 10 | Selected: 0 | Excluded: 79
- Scanned at: 2026-06-08T22:15:12Z

### Trade Plan
- Plan ID: `trade_plan-20260608T221512-6e5e2f60`
- Generated: 2026-06-08T22:15:12Z | Expires: 2026-06-09T04:15:12Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - BIL BUY $25.00 @ $91.45 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260608T221513-a0e5c744`
- All gates pass: NO
- Failed gates: RISK_LIMITS_RESPECTED

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260608T221512-d313f095

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-09

**Generated:** 2026-06-09T22:14:10Z  **Run ID:** daily_summary-2026-06-09

### Account & Risk
- Equity: $99,796.79 | Cash: $99,552.75 | Buying power: $398,894.32
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $98.19 | $-1.65 (-1.65%) |
| JNJ | long | 0.325894297 | $77.31 | +$2.31 (3.08%) |
| WELL | long | 0.11425542 | $23.62 | $-1.38 (-5.50%) |
| WMT | long | 0.377715036 | $44.92 | $-5.08 (-10.17%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+7.50%, breadth=56.96%)
- Candidates: 16 | Selected: 10 | Excluded: 69
- Scanned at: 2026-06-09T22:14:09Z

### Trade Plan
- Plan ID: `trade_plan-20260609T221409-465d6d04`
- Generated: 2026-06-09T22:14:09Z | Expires: 2026-06-10T04:14:09Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - UNP BUY $25.00 @ $271.29 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260609T221409-9a03307b`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260609T221409-9a6b4472

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-09

**Generated:** 2026-06-09T22:25:03Z  **Run ID:** daily_summary-2026-06-09

### Account & Risk
- Equity: $99,796.79 | Cash: $99,552.75 | Buying power: $398,894.32
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $98.19 | $-1.65 (-1.65%) |
| JNJ | long | 0.325894297 | $77.31 | +$2.31 (3.08%) |
| WELL | long | 0.11425542 | $23.62 | $-1.38 (-5.50%) |
| WMT | long | 0.377715036 | $44.92 | $-5.08 (-10.17%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+7.50%, breadth=56.96%)
- Candidates: 16 | Selected: 10 | Excluded: 69
- Scanned at: 2026-06-09T22:14:09Z

### Trade Plan
- Plan ID: `trade_plan-20260609T221409-465d6d04`
- Generated: 2026-06-09T22:14:09Z | Expires: 2026-06-10T04:14:09Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - UNP BUY $25.00 @ $271.29 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260609T221409-9a03307b`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260609T221409-9a6b4472

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-10

**Generated:** 2026-06-10T22:30:55Z  **Run ID:** daily_summary-2026-06-10

### Account & Risk
- Equity: $99,796.23 | Cash: $99,552.75 | Buying power: $398,892.75
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $96.20 | $-3.64 (-3.65%) |
| JNJ | long | 0.325894297 | $77.72 | +$2.72 (3.63%) |
| WELL | long | 0.11425542 | $24.15 | $-0.85 (-3.40%) |
| WMT | long | 0.377715036 | $45.41 | $-4.59 (-9.18%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+6.13%, breadth=58.23%)
- Candidates: 10 | Selected: 10 | Excluded: 69
- Scanned at: 2026-06-10T22:30:54Z

### Trade Plan
- Plan ID: `trade_plan-20260610T223055-8fd8c448`
- Generated: 2026-06-10T22:30:55Z | Expires: 2026-06-11T04:30:55Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - O BUY $25.00 @ $62.12 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260610T223055-b89bb534`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260610T223054-617e1899

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-10

**Generated:** 2026-06-10T22:51:51Z  **Run ID:** daily_summary-2026-06-10

### Account & Risk
- Equity: $99,796.23 | Cash: $99,552.75 | Buying power: $398,892.75
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $96.20 | $-3.64 (-3.65%) |
| JNJ | long | 0.325894297 | $77.72 | +$2.72 (3.63%) |
| WELL | long | 0.11425542 | $24.15 | $-0.85 (-3.40%) |
| WMT | long | 0.377715036 | $45.41 | $-4.59 (-9.18%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+6.13%, breadth=58.23%)
- Candidates: 10 | Selected: 10 | Excluded: 69
- Scanned at: 2026-06-10T22:30:54Z

### Trade Plan
- Plan ID: `trade_plan-20260610T223055-8fd8c448`
- Generated: 2026-06-10T22:30:55Z | Expires: 2026-06-11T04:30:55Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - O BUY $25.00 @ $62.12 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260610T223055-b89bb534`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260610T223054-617e1899

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-11

**Generated:** 2026-06-11T22:28:16Z  **Run ID:** daily_summary-2026-06-11

### Account & Risk
- Equity: $99,796.37 | Cash: $99,552.75 | Buying power: $398,893.13
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $96.65 | $-3.19 (-3.20%) |
| JNJ | long | 0.325894297 | $77.46 | +$2.46 (3.28%) |
| WELL | long | 0.11425542 | $24.07 | $-0.93 (-3.72%) |
| WMT | long | 0.377715036 | $45.44 | $-4.56 (-9.12%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+8.00%, breadth=63.29%)
- Candidates: 19 | Selected: 10 | Excluded: 69
- Scanned at: 2026-06-11T22:28:15Z

### Trade Plan
- Plan ID: `trade_plan-20260611T222815-13077acf`
- Generated: 2026-06-11T22:28:15Z | Expires: 2026-06-12T04:28:15Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - JNJ BUY $25.00 @ $238.31 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260611T222815-e5cfc44f`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260611T222815-5b9e865f

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-11

**Generated:** 2026-06-11T22:50:35Z  **Run ID:** daily_summary-2026-06-11

### Account & Risk
- Equity: $99,796.37 | Cash: $99,552.75 | Buying power: $398,893.13
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $96.65 | $-3.19 (-3.20%) |
| JNJ | long | 0.325894297 | $77.46 | +$2.46 (3.28%) |
| WELL | long | 0.11425542 | $24.07 | $-0.93 (-3.72%) |
| WMT | long | 0.377715036 | $45.44 | $-4.56 (-9.12%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+8.00%, breadth=63.29%)
- Candidates: 19 | Selected: 10 | Excluded: 69
- Scanned at: 2026-06-11T22:28:15Z

### Trade Plan
- Plan ID: `trade_plan-20260611T222815-13077acf`
- Generated: 2026-06-11T22:28:15Z | Expires: 2026-06-12T04:28:15Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - JNJ BUY $25.00 @ $238.31 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260611T222815-e5cfc44f`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260611T222815-5b9e865f

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-12

**Generated:** 2026-06-12T22:14:34Z  **Run ID:** daily_summary-2026-06-12

### Account & Risk
- Equity: $99,799.13 | Cash: $99,552.75 | Buying power: $398,900.85
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $97.82 | $-2.02 (-2.02%) |
| JNJ | long | 0.325894297 | $78.42 | +$3.42 (4.56%) |
| WELL | long | 0.11425542 | $24.48 | $-0.52 (-2.07%) |
| WMT | long | 0.377715036 | $45.65 | $-4.35 (-8.70%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+7.87%, breadth=65.82%)
- Candidates: 15 | Selected: 10 | Excluded: 69
- Scanned at: 2026-06-12T22:14:33Z

### Trade Plan
- Plan ID: `trade_plan-20260612T221433-ee2be16e`
- Generated: 2026-06-12T22:14:33Z | Expires: 2026-06-13T04:14:33Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - KO BUY $25.00 @ $82.62 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260612T221433-9d1f2b8e`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260612T221433-ef2ccf9f

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-12

**Generated:** 2026-06-12T22:25:43Z  **Run ID:** daily_summary-2026-06-12

### Account & Risk
- Equity: $99,799.13 | Cash: $99,552.75 | Buying power: $398,900.85
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $97.82 | $-2.02 (-2.02%) |
| JNJ | long | 0.325894297 | $78.42 | +$3.42 (4.56%) |
| WELL | long | 0.11425542 | $24.48 | $-0.52 (-2.07%) |
| WMT | long | 0.377715036 | $45.65 | $-4.35 (-8.70%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+7.87%, breadth=65.82%)
- Candidates: 15 | Selected: 10 | Excluded: 69
- Scanned at: 2026-06-12T22:14:33Z

### Trade Plan
- Plan ID: `trade_plan-20260612T221433-ee2be16e`
- Generated: 2026-06-12T22:14:33Z | Expires: 2026-06-13T04:14:33Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - KO BUY $25.00 @ $82.62 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260612T221433-9d1f2b8e`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260612T221433-ef2ccf9f

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-15

**Generated:** 2026-06-15T22:50:21Z  **Run ID:** daily_summary-2026-06-15

### Account & Risk
- Equity: $99,798.08 | Cash: $99,552.75 | Buying power: $398,897.91
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $98.62 | $-1.22 (-1.23%) |
| JNJ | long | 0.325894297 | $76.80 | +$1.80 (2.40%) |
| WELL | long | 0.11425542 | $24.32 | $-0.68 (-2.74%) |
| WMT | long | 0.377715036 | $45.59 | $-4.41 (-8.82%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.52%, breadth=64.56%)
- Candidates: 16 | Selected: 10 | Excluded: 69
- Scanned at: 2026-06-15T22:50:20Z

### Trade Plan
- Plan ID: `trade_plan-20260615T225020-7870d4cc`
- Generated: 2026-06-15T22:50:20Z | Expires: 2026-06-16T04:50:20Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - AEP BUY $25.00 @ $129.31 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260615T225021-f0b8c4d0`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260615T225020-495189ce

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-15

**Generated:** 2026-06-15T23:03:39Z  **Run ID:** daily_summary-2026-06-15

### Account & Risk
- Equity: $99,798.08 | Cash: $99,552.75 | Buying power: $398,897.91
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $98.62 | $-1.22 (-1.23%) |
| JNJ | long | 0.325894297 | $76.80 | +$1.80 (2.40%) |
| WELL | long | 0.11425542 | $24.32 | $-0.68 (-2.74%) |
| WMT | long | 0.377715036 | $45.59 | $-4.41 (-8.82%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.52%, breadth=64.56%)
- Candidates: 16 | Selected: 10 | Excluded: 69
- Scanned at: 2026-06-15T22:50:20Z

### Trade Plan
- Plan ID: `trade_plan-20260615T225020-7870d4cc`
- Generated: 2026-06-15T22:50:20Z | Expires: 2026-06-16T04:50:20Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - AEP BUY $25.00 @ $129.31 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260615T225021-f0b8c4d0`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260615T225020-495189ce

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-16

**Generated:** 2026-06-16T22:35:23Z  **Run ID:** daily_summary-2026-06-16

### Account & Risk
- Equity: $99,800.91 | Cash: $99,552.75 | Buying power: $398,905.84
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $101.42 | +$1.58 (1.58%) |
| JNJ | long | 0.325894297 | $76.64 | +$1.64 (2.19%) |
| WELL | long | 0.11425542 | $24.39 | $-0.61 (-2.43%) |
| WMT | long | 0.377715036 | $45.70 | $-4.30 (-8.60%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+10.09%, breadth=69.62%)
- Candidates: 15 | Selected: 10 | Excluded: 69
- Scanned at: 2026-06-16T22:35:22Z

### Trade Plan
- Plan ID: `trade_plan-20260616T223523-aac6ff24`
- Generated: 2026-06-16T22:35:23Z | Expires: 2026-06-17T04:35:23Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - SRE BUY $25.00 @ $91.73 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260616T223523-664e60b5`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260616T223522-10cf09e2

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-16

**Generated:** 2026-06-16T22:53:34Z  **Run ID:** daily_summary-2026-06-16

### Account & Risk
- Equity: $99,800.91 | Cash: $99,552.75 | Buying power: $398,905.84
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $101.42 | +$1.58 (1.58%) |
| JNJ | long | 0.325894297 | $76.64 | +$1.64 (2.19%) |
| WELL | long | 0.11425542 | $24.39 | $-0.61 (-2.43%) |
| WMT | long | 0.377715036 | $45.70 | $-4.30 (-8.60%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+10.09%, breadth=69.62%)
- Candidates: 15 | Selected: 10 | Excluded: 69
- Scanned at: 2026-06-16T22:35:22Z

### Trade Plan
- Plan ID: `trade_plan-20260616T223523-aac6ff24`
- Generated: 2026-06-16T22:35:23Z | Expires: 2026-06-17T04:35:23Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - SRE BUY $25.00 @ $91.73 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260616T223523-664e60b5`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260616T223522-10cf09e2

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-17

**Generated:** 2026-06-17T22:26:05Z  **Run ID:** daily_summary-2026-06-17

### Account & Risk
- Equity: $99,797.47 | Cash: $99,552.75 | Buying power: $398,896.21
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $100.75 | +$0.91 (0.91%) |
| JNJ | long | 0.325894297 | $75.69 | +$0.69 (0.92%) |
| WELL | long | 0.11425542 | $23.65 | $-1.35 (-5.40%) |
| WMT | long | 0.377715036 | $44.63 | $-5.37 (-10.74%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+8.86%, breadth=62.03%)
- Candidates: 13 | Selected: 10 | Excluded: 69
- Scanned at: 2026-06-17T22:26:05Z

### Trade Plan
- Plan ID: `trade_plan-20260617T222605-fc02b41c`
- Generated: 2026-06-17T22:26:05Z | Expires: 2026-06-18T04:26:05Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - JNJ BUY $25.00 @ $233.92 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260617T222605-a541c465`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260617T222604-74be5a9c

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-17

**Generated:** 2026-06-17T22:45:48Z  **Run ID:** daily_summary-2026-06-17

### Account & Risk
- Equity: $99,797.47 | Cash: $99,552.75 | Buying power: $398,896.21
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $100.75 | +$0.91 (0.91%) |
| JNJ | long | 0.325894297 | $75.69 | +$0.69 (0.92%) |
| WELL | long | 0.11425542 | $23.65 | $-1.35 (-5.40%) |
| WMT | long | 0.377715036 | $44.63 | $-5.37 (-10.74%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+8.86%, breadth=62.03%)
- Candidates: 13 | Selected: 10 | Excluded: 69
- Scanned at: 2026-06-17T22:26:05Z

### Trade Plan
- Plan ID: `trade_plan-20260617T222605-fc02b41c`
- Generated: 2026-06-17T22:26:05Z | Expires: 2026-06-18T04:26:05Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - JNJ BUY $25.00 @ $233.92 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260617T222605-a541c465`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260617T222604-74be5a9c

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-18

**Generated:** 2026-06-18T22:33:22Z  **Run ID:** daily_summary-2026-06-18

### Account & Risk
- Equity: $99,796.15 | Cash: $99,552.75 | Buying power: $398,892.51
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $101.19 | +$1.35 (1.35%) |
| JNJ | long | 0.325894297 | $74.43 | $-0.57 (-0.76%) |
| WELL | long | 0.11425542 | $23.61 | $-1.39 (-5.56%) |
| WMT | long | 0.377715036 | $44.16 | $-5.84 (-11.68%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+10.00%, breadth=58.23%)
- Candidates: 16 | Selected: 10 | Excluded: 69
- Scanned at: 2026-06-18T22:33:20Z

### Trade Plan
- Plan ID: `trade_plan-20260618T223320-58ad17c2`
- Generated: 2026-06-18T22:33:20Z | Expires: 2026-06-19T04:33:20Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - LIN BUY $25.00 @ $512.17 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260618T223320-5aa6ece9`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260618T223320-ab5b0674

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-18

**Generated:** 2026-06-18T22:56:36Z  **Run ID:** daily_summary-2026-06-18

### Account & Risk
- Equity: $99,796.15 | Cash: $99,552.75 | Buying power: $398,892.51
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $101.19 | +$1.35 (1.35%) |
| JNJ | long | 0.325894297 | $74.43 | $-0.57 (-0.76%) |
| WELL | long | 0.11425542 | $23.61 | $-1.39 (-5.56%) |
| WMT | long | 0.377715036 | $44.16 | $-5.84 (-11.68%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+10.00%, breadth=58.23%)
- Candidates: 16 | Selected: 10 | Excluded: 69
- Scanned at: 2026-06-18T22:33:20Z

### Trade Plan
- Plan ID: `trade_plan-20260618T223320-58ad17c2`
- Generated: 2026-06-18T22:33:20Z | Expires: 2026-06-19T04:33:20Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - LIN BUY $25.00 @ $512.17 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260618T223320-5aa6ece9`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260618T223320-ab5b0674

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-19

**Generated:** 2026-06-19T21:49:24Z  **Run ID:** daily_summary-2026-06-19

### Account & Risk
- Equity: $99,796.24 | Cash: $99,552.75 | Buying power: $398,892.78
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $101.19 | +$1.35 (1.35%) |
| JNJ | long | 0.325894297 | $74.43 | $-0.57 (-0.76%) |
| WELL | long | 0.11425542 | $23.61 | $-1.39 (-5.56%) |
| WMT | long | 0.377715036 | $44.26 | $-5.74 (-11.48%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+10.00%, breadth=58.23%)
- Candidates: 16 | Selected: 10 | Excluded: 69
- Scanned at: 2026-06-19T21:49:23Z

### Trade Plan
- Plan ID: `trade_plan-20260619T214923-006f0e6c`
- Generated: 2026-06-19T21:49:23Z | Expires: 2026-06-20T03:49:23Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - LIN BUY $25.00 @ $512.17 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260619T214923-48d10a18`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260619T214923-d67ecf86

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-19

**Generated:** 2026-06-19T22:04:36Z  **Run ID:** daily_summary-2026-06-19

### Account & Risk
- Equity: $99,796.24 | Cash: $99,552.75 | Buying power: $398,892.78
- Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $101.19 | +$1.35 (1.35%) |
| JNJ | long | 0.325894297 | $74.43 | $-0.57 (-0.76%) |
| WELL | long | 0.11425542 | $23.61 | $-1.39 (-5.56%) |
| WMT | long | 0.377715036 | $44.26 | $-5.74 (-11.48%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+10.00%, breadth=58.23%)
- Candidates: 16 | Selected: 10 | Excluded: 69
- Scanned at: 2026-06-19T21:49:23Z

### Trade Plan
- Plan ID: `trade_plan-20260619T214923-006f0e6c`
- Generated: 2026-06-19T21:49:23Z | Expires: 2026-06-20T03:49:23Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - LIN BUY $25.00 @ $512.17 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260619T214923-48d10a18`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260619T214923-d67ecf86

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-22

**Generated:** 2026-06-22T22:25:33Z  **Run ID:** daily_summary-2026-06-22

### Account & Risk
- Equity: $99,799.47 | Cash: $99,552.75 | Buying power: $398,901.80
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $103.39 | +$3.55 (3.55%) |
| JNJ | long | 0.325894297 | $74.93 | $-0.07 (-0.09%) |
| WELL | long | 0.11425542 | $24.16 | $-0.84 (-3.36%) |
| WMT | long | 0.377715036 | $44.23 | $-5.77 (-11.54%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+10.85%, breadth=58.23%)
- Candidates: 17 | Selected: 10 | Excluded: 69
- Scanned at: 2026-06-22T22:25:33Z

### Trade Plan
- Plan ID: `trade_plan-20260622T222533-51c70f9f`
- Generated: 2026-06-22T22:25:33Z | Expires: 2026-06-23T04:25:33Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - WMT SELL $25.00 @ $117.10 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260622T222533-287edf7f`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260622T222532-a9a427bb

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-22

**Generated:** 2026-06-22T22:48:13Z  **Run ID:** daily_summary-2026-06-22

### Account & Risk
- Equity: $99,799.47 | Cash: $99,552.75 | Buying power: $398,901.80
- Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $103.39 | +$3.55 (3.55%) |
| JNJ | long | 0.325894297 | $74.93 | $-0.07 (-0.09%) |
| WELL | long | 0.11425542 | $24.16 | $-0.84 (-3.36%) |
| WMT | long | 0.377715036 | $44.23 | $-5.77 (-11.54%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+10.85%, breadth=58.23%)
- Candidates: 17 | Selected: 10 | Excluded: 69
- Scanned at: 2026-06-22T22:25:33Z

### Trade Plan
- Plan ID: `trade_plan-20260622T222533-51c70f9f`
- Generated: 2026-06-22T22:25:33Z | Expires: 2026-06-23T04:25:33Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - WMT SELL $25.00 @ $117.10 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260622T222533-287edf7f`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260622T222532-a9a427bb

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-23

**Generated:** 2026-06-23T22:04:25Z  **Run ID:** daily_summary-2026-06-23

### Account & Risk
- Equity: $99,804.38 | Cash: $99,552.75 | Buying power: $398,915.58
- Peak: $99,804.38 | Drawdown: 0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $103.58 | +$3.74 (3.75%) |
| JNJ | long | 0.325894297 | $78.04 | +$3.04 (4.06%) |
| WELL | long | 0.11425542 | $24.87 | $-0.13 (-0.52%) |
| WMT | long | 0.377715036 | $45.14 | $-4.86 (-9.73%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+8.44%, breadth=62.03%)
- Candidates: 17 | Selected: 10 | Excluded: 69
- Scanned at: 2026-06-23T22:04:24Z

### Trade Plan
- Plan ID: `trade_plan-20260623T220424-c1b61181`
- Generated: 2026-06-23T22:04:24Z | Expires: 2026-06-24T04:04:24Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - AEP BUY $25.00 @ $133.68 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260623T220424-850a4bca`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260623T220424-90df8ed0

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-23

**Generated:** 2026-06-23T22:14:40Z  **Run ID:** daily_summary-2026-06-23

### Account & Risk
- Equity: $99,804.38 | Cash: $99,552.75 | Buying power: $398,915.58
- Peak: $99,804.38 | Drawdown: 0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $103.58 | +$3.74 (3.75%) |
| JNJ | long | 0.325894297 | $78.04 | +$3.04 (4.06%) |
| WELL | long | 0.11425542 | $24.87 | $-0.13 (-0.52%) |
| WMT | long | 0.377715036 | $45.14 | $-4.86 (-9.73%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+8.44%, breadth=62.03%)
- Candidates: 17 | Selected: 10 | Excluded: 69
- Scanned at: 2026-06-23T22:04:24Z

### Trade Plan
- Plan ID: `trade_plan-20260623T220424-c1b61181`
- Generated: 2026-06-23T22:04:24Z | Expires: 2026-06-24T04:04:24Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - AEP BUY $25.00 @ $133.68 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260623T220424-850a4bca`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260623T220424-90df8ed0

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-24

**Generated:** 2026-06-24T22:00:53Z  **Run ID:** daily_summary-2026-06-24

### Account & Risk
- Equity: $99,801.81 | Cash: $99,552.75 | Buying power: $398,908.36
- Peak: $99,804.38 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $101.32 | +$1.48 (1.48%) |
| JNJ | long | 0.325894297 | $77.89 | +$2.89 (3.85%) |
| WELL | long | 0.11425542 | $25.36 | +$0.36 (1.46%) |
| WMT | long | 0.377715036 | $44.48 | $-5.52 (-11.03%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+7.76%, breadth=67.09%)
- Candidates: 14 | Selected: 10 | Excluded: 69
- Scanned at: 2026-06-24T22:00:53Z

### Trade Plan
- Plan ID: `trade_plan-20260624T220053-1d9ba5e1`
- Generated: 2026-06-24T22:00:53Z | Expires: 2026-06-25T04:00:53Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - SRE BUY $25.00 @ $92.73 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260624T220053-711d3fae`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260624T220052-687b5be0

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-24

**Generated:** 2026-06-24T22:18:48Z  **Run ID:** daily_summary-2026-06-24

### Account & Risk
- Equity: $99,801.81 | Cash: $99,552.75 | Buying power: $398,908.36
- Peak: $99,804.38 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $101.32 | +$1.48 (1.48%) |
| JNJ | long | 0.325894297 | $77.89 | +$2.89 (3.85%) |
| WELL | long | 0.11425542 | $25.36 | +$0.36 (1.46%) |
| WMT | long | 0.377715036 | $44.48 | $-5.52 (-11.03%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+7.76%, breadth=67.09%)
- Candidates: 14 | Selected: 10 | Excluded: 69
- Scanned at: 2026-06-24T22:00:53Z

### Trade Plan
- Plan ID: `trade_plan-20260624T220053-1d9ba5e1`
- Generated: 2026-06-24T22:00:53Z | Expires: 2026-06-25T04:00:53Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - SRE BUY $25.00 @ $92.73 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260624T220053-711d3fae`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260624T220052-687b5be0

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-25

**Generated:** 2026-06-25T22:10:21Z  **Run ID:** daily_summary-2026-06-25

### Account & Risk
- Equity: $99,802.86 | Cash: $99,552.75 | Buying power: $398,911.32
- Peak: $99,804.38 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $100.77 | +$0.92 (0.93%) |
| JNJ | long | 0.325894297 | $79.91 | +$4.91 (6.55%) |
| WELL | long | 0.11425542 | $25.56 | +$0.56 (2.25%) |
| WMT | long | 0.377715036 | $43.87 | $-6.13 (-12.26%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+7.10%, breadth=63.29%)
- Candidates: 10 | Selected: 10 | Excluded: 69
- Scanned at: 2026-06-25T22:10:20Z

### Trade Plan
- Plan ID: `trade_plan-20260625T221020-b39e9ac0`
- Generated: 2026-06-25T22:10:20Z | Expires: 2026-06-26T04:10:20Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - SO BUY $25.00 @ $95.91 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260625T221021-fe45d71f`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260625T221020-04966aca

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-25

**Generated:** 2026-06-25T22:22:02Z  **Run ID:** daily_summary-2026-06-25

### Account & Risk
- Equity: $99,802.86 | Cash: $99,552.75 | Buying power: $398,911.32
- Peak: $99,804.38 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $100.77 | +$0.92 (0.93%) |
| JNJ | long | 0.325894297 | $79.91 | +$4.91 (6.55%) |
| WELL | long | 0.11425542 | $25.56 | +$0.56 (2.25%) |
| WMT | long | 0.377715036 | $43.87 | $-6.13 (-12.26%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+7.10%, breadth=63.29%)
- Candidates: 10 | Selected: 10 | Excluded: 69
- Scanned at: 2026-06-25T22:10:20Z

### Trade Plan
- Plan ID: `trade_plan-20260625T221020-b39e9ac0`
- Generated: 2026-06-25T22:10:20Z | Expires: 2026-06-26T04:10:20Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - SO BUY $25.00 @ $95.91 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260625T221021-fe45d71f`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260625T221020-04966aca

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-26

**Generated:** 2026-06-26T21:51:50Z  **Run ID:** daily_summary-2026-06-26

### Account & Risk
- Equity: $99,806.31 | Cash: $99,552.75 | Buying power: $398,920.96
- Peak: $99,806.35 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $101.11 | +$1.27 (1.27%) |
| JNJ | long | 0.325894297 | $82.84 | +$7.84 (10.46%) |
| WELL | long | 0.11425542 | $25.95 | +$0.95 (3.79%) |
| WMT | long | 0.377715036 | $43.66 | $-6.34 (-12.68%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+6.02%, breadth=62.03%)
- Candidates: 13 | Selected: 10 | Excluded: 69
- Scanned at: 2026-06-26T21:51:49Z

### Trade Plan
- Plan ID: `trade_plan-20260626T215150-fad49b07`
- Generated: 2026-06-26T21:51:50Z | Expires: 2026-06-27T03:51:50Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - DUK BUY $25.00 @ $128.38 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260626T215150-91523e5e`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260626T215149-a4909d95

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-26

**Generated:** 2026-06-26T22:14:31Z  **Run ID:** daily_summary-2026-06-26

### Account & Risk
- Equity: $99,806.31 | Cash: $99,552.75 | Buying power: $398,920.96
- Peak: $99,806.35 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $101.11 | +$1.27 (1.27%) |
| JNJ | long | 0.325894297 | $82.84 | +$7.84 (10.46%) |
| WELL | long | 0.11425542 | $25.95 | +$0.95 (3.79%) |
| WMT | long | 0.377715036 | $43.66 | $-6.34 (-12.68%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+6.02%, breadth=62.03%)
- Candidates: 13 | Selected: 10 | Excluded: 69
- Scanned at: 2026-06-26T21:51:49Z

### Trade Plan
- Plan ID: `trade_plan-20260626T215150-fad49b07`
- Generated: 2026-06-26T21:51:50Z | Expires: 2026-06-27T03:51:50Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - DUK BUY $25.00 @ $128.38 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260626T215150-91523e5e`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260626T215149-a4909d95

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-29

**Generated:** 2026-06-29T21:59:10Z  **Run ID:** daily_summary-2026-06-29

### Account & Risk
- Equity: $99,806.81 | Cash: $99,552.75 | Buying power: $398,922.37
- Peak: $99,806.81 | Drawdown: 0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $100.54 | +$0.70 (0.70%) |
| JNJ | long | 0.325894297 | $84.21 | +$9.21 (12.28%) |
| WELL | long | 0.11425542 | $26.02 | +$1.02 (4.08%) |
| WMT | long | 0.377715036 | $43.29 | $-6.71 (-13.41%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+7.33%, breadth=59.49%)
- Candidates: 10 | Selected: 9 | Excluded: 70
- Scanned at: 2026-06-29T21:59:09Z

### Trade Plan
- Plan ID: `trade_plan-20260629T215910-86afd73d`
- Generated: 2026-06-29T21:59:10Z | Expires: 2026-06-30T03:59:10Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - SRE BUY $25.00 @ $93.96 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260629T215910-ba5fe9b0`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260629T215909-ca4723cc

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-29

**Generated:** 2026-06-29T22:08:47Z  **Run ID:** daily_summary-2026-06-29

### Account & Risk
- Equity: $99,806.81 | Cash: $99,552.75 | Buying power: $398,922.37
- Peak: $99,806.81 | Drawdown: 0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $100.54 | +$0.70 (0.70%) |
| JNJ | long | 0.325894297 | $84.21 | +$9.21 (12.28%) |
| WELL | long | 0.11425542 | $26.02 | +$1.02 (4.08%) |
| WMT | long | 0.377715036 | $43.29 | $-6.71 (-13.41%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+7.33%, breadth=59.49%)
- Candidates: 10 | Selected: 9 | Excluded: 70
- Scanned at: 2026-06-29T21:59:09Z

### Trade Plan
- Plan ID: `trade_plan-20260629T215910-86afd73d`
- Generated: 2026-06-29T21:59:10Z | Expires: 2026-06-30T03:59:10Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - SRE BUY $25.00 @ $93.96 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260629T215910-ba5fe9b0`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260629T215909-ca4723cc

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-30

**Generated:** 2026-06-30T22:03:50Z  **Run ID:** daily_summary-2026-06-30

### Account & Risk
- Equity: $99,801.14 | Cash: $99,552.75 | Buying power: $398,906.51
- Peak: $99,806.81 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $96.54 | $-3.30 (-3.31%) |
| JNJ | long | 0.325894297 | $83.11 | +$8.11 (10.81%) |
| WELL | long | 0.11425542 | $25.93 | +$0.93 (3.73%) |
| WMT | long | 0.377715036 | $42.81 | $-7.19 (-14.37%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+8.17%, breadth=60.76%)
- Candidates: 15 | Selected: 10 | Excluded: 69
- Scanned at: 2026-06-30T22:03:50Z

### Trade Plan
- Plan ID: `trade_plan-20260630T220350-6225e7ec`
- Generated: 2026-06-30T22:03:50Z | Expires: 2026-07-01T04:03:50Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - WMT SELL $25.00 @ $113.35 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260630T220350-4bf7ab4f`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260630T220350-928c3264

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-06-30

**Generated:** 2026-06-30T22:15:29Z  **Run ID:** daily_summary-2026-06-30

### Account & Risk
- Equity: $99,801.14 | Cash: $99,552.75 | Buying power: $398,906.51
- Peak: $99,806.81 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $96.54 | $-3.30 (-3.31%) |
| JNJ | long | 0.325894297 | $83.11 | +$8.11 (10.81%) |
| WELL | long | 0.11425542 | $25.93 | +$0.93 (3.73%) |
| WMT | long | 0.377715036 | $42.81 | $-7.19 (-14.37%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+8.17%, breadth=60.76%)
- Candidates: 15 | Selected: 10 | Excluded: 69
- Scanned at: 2026-06-30T22:03:50Z

### Trade Plan
- Plan ID: `trade_plan-20260630T220350-6225e7ec`
- Generated: 2026-06-30T22:03:50Z | Expires: 2026-07-01T04:03:50Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - WMT SELL $25.00 @ $113.35 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260630T220350-4bf7ab4f`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260630T220350-928c3264

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-01

**Generated:** 2026-07-01T22:07:39Z  **Run ID:** daily_summary-2026-07-01

### Account & Risk
- Equity: $99,796.30 | Cash: $99,552.75 | Buying power: $398,892.95
- Peak: $99,806.81 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $93.91 | $-5.93 (-5.94%) |
| JNJ | long | 0.325894297 | $82.41 | +$7.41 (9.87%) |
| WELL | long | 0.11425542 | $26.30 | +$1.30 (5.20%) |
| WMT | long | 0.377715036 | $40.94 | $-9.06 (-18.13%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+8.39%, breadth=60.76%)
- Candidates: 18 | Selected: 10 | Excluded: 69
- Scanned at: 2026-07-01T22:07:38Z

### Trade Plan
- Plan ID: `trade_plan-20260701T220738-ea134a4e`
- Generated: 2026-07-01T22:07:38Z | Expires: 2026-07-02T04:07:38Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - AEP BUY $25.00 @ $135.06 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260701T220738-c6b39704`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260701T220738-3c07b5a9

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-01

**Generated:** 2026-07-01T22:17:56Z  **Run ID:** daily_summary-2026-07-01

### Account & Risk
- Equity: $99,796.30 | Cash: $99,552.75 | Buying power: $398,892.95
- Peak: $99,806.81 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $93.91 | $-5.93 (-5.94%) |
| JNJ | long | 0.325894297 | $82.41 | +$7.41 (9.87%) |
| WELL | long | 0.11425542 | $26.30 | +$1.30 (5.20%) |
| WMT | long | 0.377715036 | $40.94 | $-9.06 (-18.13%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+8.39%, breadth=60.76%)
- Candidates: 18 | Selected: 10 | Excluded: 69
- Scanned at: 2026-07-01T22:07:38Z

### Trade Plan
- Plan ID: `trade_plan-20260701T220738-ea134a4e`
- Generated: 2026-07-01T22:07:38Z | Expires: 2026-07-02T04:07:38Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - AEP BUY $25.00 @ $135.06 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260701T220738-c6b39704`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260701T220738-3c07b5a9

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-02

**Generated:** 2026-07-02T21:49:02Z  **Run ID:** daily_summary-2026-07-02

### Account & Risk
- Equity: $99,800.08 | Cash: $99,552.75 | Buying power: $398,903.53
- Peak: $99,806.81 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $92.84 | $-7.01 (-7.02%) |
| JNJ | long | 0.325894297 | $85.35 | +$10.35 (13.80%) |
| WELL | long | 0.11425542 | $26.97 | +$1.97 (7.89%) |
| WMT | long | 0.377715036 | $42.17 | $-7.83 (-15.66%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+8.43%, breadth=65.82%)
- Candidates: 17 | Selected: 10 | Excluded: 69
- Scanned at: 2026-07-02T21:49:02Z

### Trade Plan
- Plan ID: `trade_plan-20260702T214902-9a75395b`
- Generated: 2026-07-02T21:49:02Z | Expires: 2026-07-03T03:49:02Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - WMT SELL $25.00 @ $111.65 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260702T214902-7d627cb6`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260702T214901-8a37a1e1

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-02

**Generated:** 2026-07-02T22:07:35Z  **Run ID:** daily_summary-2026-07-02

### Account & Risk
- Equity: $99,800.08 | Cash: $99,552.75 | Buying power: $398,903.53
- Peak: $99,806.81 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $92.84 | $-7.01 (-7.02%) |
| JNJ | long | 0.325894297 | $85.35 | +$10.35 (13.80%) |
| WELL | long | 0.11425542 | $26.97 | +$1.97 (7.89%) |
| WMT | long | 0.377715036 | $42.17 | $-7.83 (-15.66%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+8.43%, breadth=65.82%)
- Candidates: 17 | Selected: 10 | Excluded: 69
- Scanned at: 2026-07-02T21:49:02Z

### Trade Plan
- Plan ID: `trade_plan-20260702T214902-9a75395b`
- Generated: 2026-07-02T21:49:02Z | Expires: 2026-07-03T03:49:02Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - WMT SELL $25.00 @ $111.65 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260702T214902-7d627cb6`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260702T214901-8a37a1e1

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-03

**Generated:** 2026-07-03T21:44:38Z  **Run ID:** daily_summary-2026-07-03

### Account & Risk
- Equity: $99,800.52 | Cash: $99,552.75 | Buying power: $398,904.77
- Peak: $99,806.81 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $92.84 | $-7.01 (-7.02%) |
| JNJ | long | 0.325894297 | $85.72 | +$10.72 (14.30%) |
| WELL | long | 0.11425542 | $26.97 | +$1.97 (7.89%) |
| WMT | long | 0.377715036 | $42.24 | $-7.76 (-15.51%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+8.43%, breadth=65.82%)
- Candidates: 17 | Selected: 10 | Excluded: 69
- Scanned at: 2026-07-03T21:44:37Z

### Trade Plan
- Plan ID: `trade_plan-20260703T214437-e4bef21e`
- Generated: 2026-07-03T21:44:37Z | Expires: 2026-07-04T03:44:37Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - WMT SELL $25.00 @ $111.84 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260703T214437-2034b4f3`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260703T214437-af0b552b

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-03

**Generated:** 2026-07-03T22:05:18Z  **Run ID:** daily_summary-2026-07-03

### Account & Risk
- Equity: $99,800.52 | Cash: $99,552.75 | Buying power: $398,904.77
- Peak: $99,806.81 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $92.84 | $-7.01 (-7.02%) |
| JNJ | long | 0.325894297 | $85.72 | +$10.72 (14.30%) |
| WELL | long | 0.11425542 | $26.97 | +$1.97 (7.89%) |
| WMT | long | 0.377715036 | $42.24 | $-7.76 (-15.51%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+8.43%, breadth=65.82%)
- Candidates: 17 | Selected: 10 | Excluded: 69
- Scanned at: 2026-07-03T21:44:37Z

### Trade Plan
- Plan ID: `trade_plan-20260703T214437-e4bef21e`
- Generated: 2026-07-03T21:44:37Z | Expires: 2026-07-04T03:44:37Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - WMT SELL $25.00 @ $111.84 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260703T214437-2034b4f3`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260703T214437-af0b552b

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-06

**Generated:** 2026-07-06T22:02:54Z  **Run ID:** daily_summary-2026-07-06

### Account & Risk
- Equity: $99,798.03 | Cash: $99,552.75 | Buying power: $398,897.79
- Peak: $99,806.81 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $92.54 | $-7.30 (-7.31%) |
| JNJ | long | 0.325894297 | $84.41 | +$9.41 (12.54%) |
| WELL | long | 0.11425542 | $26.59 | +$1.59 (6.34%) |
| WMT | long | 0.377715036 | $41.75 | $-8.25 (-16.50%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+10.19%, breadth=67.09%)
- Candidates: 6 | Selected: 6 | Excluded: 73
- Scanned at: 2026-07-06T22:02:53Z

### Trade Plan
- Plan ID: `trade_plan-20260706T220253-ce45bb34`
- Generated: 2026-07-06T22:02:53Z | Expires: 2026-07-07T04:02:53Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - WMT SELL $25.00 @ $110.53 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260706T220253-723ec81a`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260706T220253-184a2bb8

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-06

**Generated:** 2026-07-06T22:14:32Z  **Run ID:** daily_summary-2026-07-06

### Account & Risk
- Equity: $99,798.03 | Cash: $99,552.75 | Buying power: $398,897.79
- Peak: $99,806.81 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $92.54 | $-7.30 (-7.31%) |
| JNJ | long | 0.325894297 | $84.41 | +$9.41 (12.54%) |
| WELL | long | 0.11425542 | $26.59 | +$1.59 (6.34%) |
| WMT | long | 0.377715036 | $41.75 | $-8.25 (-16.50%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+10.19%, breadth=67.09%)
- Candidates: 6 | Selected: 6 | Excluded: 73
- Scanned at: 2026-07-06T22:02:53Z

### Trade Plan
- Plan ID: `trade_plan-20260706T220253-ce45bb34`
- Generated: 2026-07-06T22:02:53Z | Expires: 2026-07-07T04:02:53Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - WMT SELL $25.00 @ $110.53 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260706T220253-723ec81a`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260706T220253-184a2bb8

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-07

**Generated:** 2026-07-07T22:00:15Z  **Run ID:** daily_summary-2026-07-07

### Account & Risk
- Equity: $99,804.00 | Cash: $99,552.75 | Buying power: $398,914.50
- Peak: $99,806.81 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $94.77 | $-5.07 (-5.08%) |
| JNJ | long | 0.325894297 | $87.18 | +$12.18 (16.24%) |
| WELL | long | 0.11425542 | $27.15 | +$2.15 (8.60%) |
| WMT | long | 0.377715036 | $42.15 | $-7.85 (-15.70%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.43%, breadth=68.35%)
- Candidates: 18 | Selected: 10 | Excluded: 69
- Scanned at: 2026-07-07T22:00:14Z

### Trade Plan
- Plan ID: `trade_plan-20260707T220014-6ee6690d`
- Generated: 2026-07-07T22:00:14Z | Expires: 2026-07-08T04:00:14Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - JNJ BUY $25.00 @ $267.16 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260707T220014-21926ccf`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260707T220014-e61b1e68

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-07

**Generated:** 2026-07-07T22:11:17Z  **Run ID:** daily_summary-2026-07-07

### Account & Risk
- Equity: $99,804.00 | Cash: $99,552.75 | Buying power: $398,914.50
- Peak: $99,806.81 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $94.77 | $-5.07 (-5.08%) |
| JNJ | long | 0.325894297 | $87.18 | +$12.18 (16.24%) |
| WELL | long | 0.11425542 | $27.15 | +$2.15 (8.60%) |
| WMT | long | 0.377715036 | $42.15 | $-7.85 (-15.70%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.43%, breadth=68.35%)
- Candidates: 18 | Selected: 10 | Excluded: 69
- Scanned at: 2026-07-07T22:00:14Z

### Trade Plan
- Plan ID: `trade_plan-20260707T220014-6ee6690d`
- Generated: 2026-07-07T22:00:14Z | Expires: 2026-07-08T04:00:14Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - JNJ BUY $25.00 @ $267.16 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260707T220014-21926ccf`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260707T220014-e61b1e68

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-08

**Generated:** 2026-07-08T21:47:46Z  **Run ID:** daily_summary-2026-07-08

### Account & Risk
- Equity: $99,802.16 | Cash: $99,552.75 | Buying power: $398,909.36
- Peak: $99,806.81 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $94.18 | $-5.66 (-5.67%) |
| JNJ | long | 0.325894297 | $85.82 | +$10.82 (14.43%) |
| WELL | long | 0.11425542 | $26.72 | +$1.72 (6.90%) |
| WMT | long | 0.377715036 | $42.68 | $-7.32 (-14.64%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+8.37%, breadth=63.29%)
- Candidates: 9 | Selected: 9 | Excluded: 70
- Scanned at: 2026-07-08T21:47:45Z

### Trade Plan
- Plan ID: `trade_plan-20260708T214745-3d7f3bc6`
- Generated: 2026-07-08T21:47:45Z | Expires: 2026-07-09T03:47:45Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - DUK BUY $25.00 @ $126.83 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260708T214745-9ba17cf0`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260708T214745-6bc8a133

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-08

**Generated:** 2026-07-08T22:06:45Z  **Run ID:** daily_summary-2026-07-08

### Account & Risk
- Equity: $99,802.16 | Cash: $99,552.75 | Buying power: $398,909.36
- Peak: $99,806.81 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $94.18 | $-5.66 (-5.67%) |
| JNJ | long | 0.325894297 | $85.82 | +$10.82 (14.43%) |
| WELL | long | 0.11425542 | $26.72 | +$1.72 (6.90%) |
| WMT | long | 0.377715036 | $42.68 | $-7.32 (-14.64%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+8.37%, breadth=63.29%)
- Candidates: 9 | Selected: 9 | Excluded: 70
- Scanned at: 2026-07-08T21:47:45Z

### Trade Plan
- Plan ID: `trade_plan-20260708T214745-3d7f3bc6`
- Generated: 2026-07-08T21:47:45Z | Expires: 2026-07-09T03:47:45Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - DUK BUY $25.00 @ $126.83 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260708T214745-9ba17cf0`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260708T214745-6bc8a133

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-09

**Generated:** 2026-07-09T22:07:39Z  **Run ID:** daily_summary-2026-07-09

### Account & Risk
- Equity: $99,801.66 | Cash: $99,552.75 | Buying power: $398,907.94
- Peak: $99,806.81 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $95.88 | $-3.96 (-3.97%) |
| JNJ | long | 0.325894297 | $84.36 | +$9.36 (12.49%) |
| WELL | long | 0.11425542 | $26.52 | +$1.52 (6.08%) |
| WMT | long | 0.377715036 | $42.14 | $-7.86 (-15.72%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+8.64%, breadth=63.29%)
- Candidates: 17 | Selected: 10 | Excluded: 69
- Scanned at: 2026-07-09T22:07:38Z

### Trade Plan
- Plan ID: `trade_plan-20260709T220739-718a7acd`
- Generated: 2026-07-09T22:07:39Z | Expires: 2026-07-10T04:07:39Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - UNP BUY $25.00 @ $285.02 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260709T220739-d59fc65c`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260709T220738-05730e47

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-09

**Generated:** 2026-07-09T22:28:09Z  **Run ID:** daily_summary-2026-07-09

### Account & Risk
- Equity: $99,801.66 | Cash: $99,552.75 | Buying power: $398,907.94
- Peak: $99,806.81 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $95.88 | $-3.96 (-3.97%) |
| JNJ | long | 0.325894297 | $84.36 | +$9.36 (12.49%) |
| WELL | long | 0.11425542 | $26.52 | +$1.52 (6.08%) |
| WMT | long | 0.377715036 | $42.14 | $-7.86 (-15.72%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+8.64%, breadth=63.29%)
- Candidates: 17 | Selected: 10 | Excluded: 69
- Scanned at: 2026-07-09T22:07:38Z

### Trade Plan
- Plan ID: `trade_plan-20260709T220739-718a7acd`
- Generated: 2026-07-09T22:07:39Z | Expires: 2026-07-10T04:07:39Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - UNP BUY $25.00 @ $285.02 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260709T220739-d59fc65c`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260709T220738-05730e47

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-10

**Generated:** 2026-07-10T21:40:49Z  **Run ID:** daily_summary-2026-07-10

### Account & Risk
- Equity: $99,803.41 | Cash: $99,552.75 | Buying power: $398,912.86
- Peak: $99,806.81 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $97.39 | $-2.45 (-2.45%) |
| JNJ | long | 0.325894297 | $83.77 | +$8.77 (11.69%) |
| WELL | long | 0.11425542 | $26.46 | +$1.46 (5.84%) |
| WMT | long | 0.377715036 | $43.04 | $-6.96 (-13.92%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.47%, breadth=67.09%)
- Candidates: 21 | Selected: 10 | Excluded: 69
- Scanned at: 2026-07-10T21:40:48Z

### Trade Plan
- Plan ID: `trade_plan-20260710T214049-1f07822a`
- Generated: 2026-07-10T21:40:49Z | Expires: 2026-07-11T03:40:49Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - JNJ BUY $25.00 @ $256.93 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260710T214049-d5b36c7a`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260710T214048-7ba5ccfc

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-10

**Generated:** 2026-07-10T22:04:11Z  **Run ID:** daily_summary-2026-07-10

### Account & Risk
- Equity: $99,803.41 | Cash: $99,552.75 | Buying power: $398,912.86
- Peak: $99,806.81 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $97.39 | $-2.45 (-2.45%) |
| JNJ | long | 0.325894297 | $83.77 | +$8.77 (11.69%) |
| WELL | long | 0.11425542 | $26.46 | +$1.46 (5.84%) |
| WMT | long | 0.377715036 | $43.04 | $-6.96 (-13.92%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+9.47%, breadth=67.09%)
- Candidates: 21 | Selected: 10 | Excluded: 69
- Scanned at: 2026-07-10T21:40:48Z

### Trade Plan
- Plan ID: `trade_plan-20260710T214049-1f07822a`
- Generated: 2026-07-10T21:40:49Z | Expires: 2026-07-11T03:40:49Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - JNJ BUY $25.00 @ $256.93 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260710T214049-d5b36c7a`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260710T214048-7ba5ccfc

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-13

**Generated:** 2026-07-13T21:35:12Z  **Run ID:** daily_summary-2026-07-13

### Account & Risk
- Equity: $99,803.25 | Cash: $99,552.75 | Buying power: $398,912.40
- Peak: $99,806.81 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $96.31 | $-3.53 (-3.54%) |
| JNJ | long | 0.325894297 | $84.06 | +$9.06 (12.08%) |
| WELL | long | 0.11425542 | $26.81 | +$1.81 (7.22%) |
| WMT | long | 0.377715036 | $43.32 | $-6.68 (-13.35%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+8.66%, breadth=68.35%)
- Candidates: 16 | Selected: 10 | Excluded: 69
- Scanned at: 2026-07-13T21:35:11Z

### Trade Plan
- Plan ID: `trade_plan-20260713T213511-db1f9cf1`
- Generated: 2026-07-13T21:35:11Z | Expires: 2026-07-14T03:35:11Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - AEP BUY $25.00 @ $135.58 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260713T213512-2a7884d7`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260713T213511-61b7448a

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-13

**Generated:** 2026-07-13T21:57:37Z  **Run ID:** daily_summary-2026-07-13

### Account & Risk
- Equity: $99,803.25 | Cash: $99,552.75 | Buying power: $398,912.40
- Peak: $99,806.81 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $96.31 | $-3.53 (-3.54%) |
| JNJ | long | 0.325894297 | $84.06 | +$9.06 (12.08%) |
| WELL | long | 0.11425542 | $26.81 | +$1.81 (7.22%) |
| WMT | long | 0.377715036 | $43.32 | $-6.68 (-13.35%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+8.66%, breadth=68.35%)
- Candidates: 16 | Selected: 10 | Excluded: 69
- Scanned at: 2026-07-13T21:35:11Z

### Trade Plan
- Plan ID: `trade_plan-20260713T213511-db1f9cf1`
- Generated: 2026-07-13T21:35:11Z | Expires: 2026-07-14T03:35:11Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - AEP BUY $25.00 @ $135.58 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260713T213512-2a7884d7`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260713T213511-61b7448a

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-14

**Generated:** 2026-07-14T21:37:13Z  **Run ID:** daily_summary-2026-07-14

### Account & Risk
- Equity: $99,800.73 | Cash: $99,552.75 | Buying power: $398,905.34
- Peak: $99,806.81 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $95.00 | $-4.84 (-4.84%) |
| JNJ | long | 0.325894297 | $83.01 | +$8.01 (10.67%) |
| WELL | long | 0.11425542 | $26.96 | +$1.96 (7.86%) |
| WMT | long | 0.377715036 | $43.00 | $-7.00 (-13.99%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+8.35%, breadth=65.82%)
- Candidates: 17 | Selected: 10 | Excluded: 69
- Scanned at: 2026-07-14T21:37:12Z

### Trade Plan
- Plan ID: `trade_plan-20260714T213713-a62850ed`
- Generated: 2026-07-14T21:37:13Z | Expires: 2026-07-15T03:37:13Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - WMT SELL $25.00 @ $113.85 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260714T213713-847c2444`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260714T213712-b02c558c

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-14

**Generated:** 2026-07-14T21:58:36Z  **Run ID:** daily_summary-2026-07-14

### Account & Risk
- Equity: $99,800.73 | Cash: $99,552.75 | Buying power: $398,905.34
- Peak: $99,806.81 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $95.00 | $-4.84 (-4.84%) |
| JNJ | long | 0.325894297 | $83.01 | +$8.01 (10.67%) |
| WELL | long | 0.11425542 | $26.96 | +$1.96 (7.86%) |
| WMT | long | 0.377715036 | $43.00 | $-7.00 (-13.99%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+8.35%, breadth=65.82%)
- Candidates: 17 | Selected: 10 | Excluded: 69
- Scanned at: 2026-07-14T21:37:12Z

### Trade Plan
- Plan ID: `trade_plan-20260714T213713-a62850ed`
- Generated: 2026-07-14T21:37:13Z | Expires: 2026-07-15T03:37:13Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - WMT SELL $25.00 @ $113.85 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260714T213713-847c2444`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260714T213712-b02c558c

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-15

**Generated:** 2026-07-15T21:38:07Z  **Run ID:** daily_summary-2026-07-15

### Account & Risk
- Equity: $99,797.40 | Cash: $99,552.75 | Buying power: $398,896.02
- Peak: $99,806.81 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $94.74 | $-5.10 (-5.11%) |
| JNJ | long | 0.325894297 | $80.66 | +$5.66 (7.54%) |
| WELL | long | 0.11425542 | $26.65 | +$1.65 (6.62%) |
| WMT | long | 0.377715036 | $42.59 | $-7.41 (-14.82%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+8.57%, breadth=65.82%)
- Candidates: 14 | Selected: 10 | Excluded: 69
- Scanned at: 2026-07-15T21:38:07Z

### Trade Plan
- Plan ID: `trade_plan-20260715T213807-2fa8b047`
- Generated: 2026-07-15T21:38:07Z | Expires: 2026-07-16T03:38:07Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - WMT SELL $25.00 @ $112.76 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260715T213807-e3866d25`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260715T213806-5cd5f262

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-15

**Generated:** 2026-07-15T22:01:59Z  **Run ID:** daily_summary-2026-07-15

### Account & Risk
- Equity: $99,797.40 | Cash: $99,552.75 | Buying power: $398,896.02
- Peak: $99,806.81 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $94.74 | $-5.10 (-5.11%) |
| JNJ | long | 0.325894297 | $80.66 | +$5.66 (7.54%) |
| WELL | long | 0.11425542 | $26.65 | +$1.65 (6.62%) |
| WMT | long | 0.377715036 | $42.59 | $-7.41 (-14.82%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+8.57%, breadth=65.82%)
- Candidates: 14 | Selected: 10 | Excluded: 69
- Scanned at: 2026-07-15T21:38:07Z

### Trade Plan
- Plan ID: `trade_plan-20260715T213807-2fa8b047`
- Generated: 2026-07-15T21:38:07Z | Expires: 2026-07-16T03:38:07Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - WMT SELL $25.00 @ $112.76 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260715T213807-e3866d25`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260715T213806-5cd5f262

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-16

**Generated:** 2026-07-16T21:44:47Z  **Run ID:** daily_summary-2026-07-16

### Account & Risk
- Equity: $99,798.76 | Cash: $99,552.75 | Buying power: $398,899.83
- Peak: $99,806.81 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $93.50 | $-6.35 (-6.36%) |
| JNJ | long | 0.325894297 | $81.49 | +$6.49 (8.66%) |
| WELL | long | 0.11425542 | $27.59 | +$2.59 (10.37%) |
| WMT | long | 0.377715036 | $43.43 | $-6.57 (-13.14%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+8.24%, breadth=70.89%)
- Candidates: 18 | Selected: 10 | Excluded: 69
- Scanned at: 2026-07-16T21:44:47Z

### Trade Plan
- Plan ID: `trade_plan-20260716T214447-b201047b`
- Generated: 2026-07-16T21:44:47Z | Expires: 2026-07-17T03:44:47Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - AEP BUY $25.00 @ $133.10 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260716T214447-9b5b6418`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260716T214446-72078d67

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-16

**Generated:** 2026-07-16T22:04:13Z  **Run ID:** daily_summary-2026-07-16

### Account & Risk
- Equity: $99,798.76 | Cash: $99,552.75 | Buying power: $398,899.83
- Peak: $99,806.81 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $93.50 | $-6.35 (-6.36%) |
| JNJ | long | 0.325894297 | $81.49 | +$6.49 (8.66%) |
| WELL | long | 0.11425542 | $27.59 | +$2.59 (10.37%) |
| WMT | long | 0.377715036 | $43.43 | $-6.57 (-13.14%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+8.24%, breadth=70.89%)
- Candidates: 18 | Selected: 10 | Excluded: 69
- Scanned at: 2026-07-16T21:44:47Z

### Trade Plan
- Plan ID: `trade_plan-20260716T214447-b201047b`
- Generated: 2026-07-16T21:44:47Z | Expires: 2026-07-17T03:44:47Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - AEP BUY $25.00 @ $133.10 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260716T214447-9b5b6418`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260716T214446-72078d67

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-17

**Generated:** 2026-07-17T21:32:15Z  **Run ID:** daily_summary-2026-07-17

### Account & Risk
- Equity: $99,800.48 | Cash: $99,552.75 | Buying power: $398,904.64
- Peak: $99,806.81 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $94.50 | $-5.34 (-5.35%) |
| JNJ | long | 0.325894297 | $82.30 | +$7.30 (9.73%) |
| WELL | long | 0.11425542 | $27.79 | +$2.79 (11.17%) |
| WMT | long | 0.377715036 | $43.13 | $-6.87 (-13.74%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+7.63%, breadth=69.62%)
- Candidates: 10 | Selected: 10 | Excluded: 69
- Scanned at: 2026-07-17T21:32:14Z

### Trade Plan
- Plan ID: `trade_plan-20260717T213215-7f950558`
- Generated: 2026-07-17T21:32:15Z | Expires: 2026-07-18T03:32:15Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - UNP BUY $25.00 @ $301.65 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260717T213215-a52ef8b2`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260717T213214-09caf481

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-17

**Generated:** 2026-07-17T21:55:03Z  **Run ID:** daily_summary-2026-07-17

### Account & Risk
- Equity: $99,800.48 | Cash: $99,552.75 | Buying power: $398,904.64
- Peak: $99,806.81 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $94.50 | $-5.34 (-5.35%) |
| JNJ | long | 0.325894297 | $82.30 | +$7.30 (9.73%) |
| WELL | long | 0.11425542 | $27.79 | +$2.79 (11.17%) |
| WMT | long | 0.377715036 | $43.13 | $-6.87 (-13.74%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+7.63%, breadth=69.62%)
- Candidates: 10 | Selected: 10 | Excluded: 69
- Scanned at: 2026-07-17T21:32:14Z

### Trade Plan
- Plan ID: `trade_plan-20260717T213215-7f950558`
- Generated: 2026-07-17T21:32:15Z | Expires: 2026-07-18T03:32:15Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - UNP BUY $25.00 @ $301.65 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260717T213215-a52ef8b2`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260717T213214-09caf481

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-20

**Generated:** 2026-07-20T21:48:22Z  **Run ID:** daily_summary-2026-07-20

### Account & Risk
- Equity: $99,798.50 | Cash: $99,552.75 | Buying power: $398,899.11
- Peak: $99,806.81 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $94.25 | $-5.59 (-5.60%) |
| JNJ | long | 0.325894297 | $81.10 | +$6.10 (8.13%) |
| WELL | long | 0.11425542 | $27.97 | +$2.97 (11.90%) |
| WMT | long | 0.377715036 | $42.43 | $-7.57 (-15.15%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+7.22%, breadth=64.56%)
- Candidates: 17 | Selected: 10 | Excluded: 69
- Scanned at: 2026-07-20T21:48:22Z

### Trade Plan
- Plan ID: `trade_plan-20260720T214822-76ea9492`
- Generated: 2026-07-20T21:48:22Z | Expires: 2026-07-21T03:48:22Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - UNP BUY $25.00 @ $296.20 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260720T214822-c643ea04`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260720T214821-c93b3473

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-20

**Generated:** 2026-07-20T22:00:17Z  **Run ID:** daily_summary-2026-07-20

### Account & Risk
- Equity: $99,798.50 | Cash: $99,552.75 | Buying power: $398,899.11
- Peak: $99,806.81 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $94.25 | $-5.59 (-5.60%) |
| JNJ | long | 0.325894297 | $81.10 | +$6.10 (8.13%) |
| WELL | long | 0.11425542 | $27.97 | +$2.97 (11.90%) |
| WMT | long | 0.377715036 | $42.43 | $-7.57 (-15.15%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+7.22%, breadth=64.56%)
- Candidates: 17 | Selected: 10 | Excluded: 69
- Scanned at: 2026-07-20T21:48:22Z

### Trade Plan
- Plan ID: `trade_plan-20260720T214822-76ea9492`
- Generated: 2026-07-20T21:48:22Z | Expires: 2026-07-21T03:48:22Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - UNP BUY $25.00 @ $296.20 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260720T214822-c643ea04`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260720T214821-c93b3473

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-21

**Generated:** 2026-07-21T21:45:28Z  **Run ID:** daily_summary-2026-07-21

### Account & Risk
- Equity: $99,799.40 | Cash: $99,552.75 | Buying power: $398,901.61
- Peak: $99,806.81 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $95.23 | $-4.61 (-4.62%) |
| JNJ | long | 0.325894297 | $81.68 | +$6.68 (8.91%) |
| WELL | long | 0.11425542 | $28.15 | +$3.15 (12.60%) |
| WMT | long | 0.377715036 | $41.58 | $-8.42 (-16.84%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+8.18%, breadth=63.29%)
- Candidates: 10 | Selected: 9 | Excluded: 70
- Scanned at: 2026-07-21T21:45:27Z

### Trade Plan
- Plan ID: `trade_plan-20260721T214528-45e9c078`
- Generated: 2026-07-21T21:45:28Z | Expires: 2026-07-22T03:45:28Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - WMT SELL $25.00 @ $110.09 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260721T214528-2bdba340`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260721T214527-9233fa6b

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-21

**Generated:** 2026-07-21T22:03:47Z  **Run ID:** daily_summary-2026-07-21

### Account & Risk
- Equity: $99,799.40 | Cash: $99,552.75 | Buying power: $398,901.61
- Peak: $99,806.81 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $95.23 | $-4.61 (-4.62%) |
| JNJ | long | 0.325894297 | $81.68 | +$6.68 (8.91%) |
| WELL | long | 0.11425542 | $28.15 | +$3.15 (12.60%) |
| WMT | long | 0.377715036 | $41.58 | $-8.42 (-16.84%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+8.18%, breadth=63.29%)
- Candidates: 10 | Selected: 9 | Excluded: 70
- Scanned at: 2026-07-21T21:45:27Z

### Trade Plan
- Plan ID: `trade_plan-20260721T214528-45e9c078`
- Generated: 2026-07-21T21:45:28Z | Expires: 2026-07-22T03:45:28Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - WMT SELL $25.00 @ $110.09 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260721T214528-2bdba340`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260721T214527-9233fa6b

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-22

**Generated:** 2026-07-22T21:43:29Z  **Run ID:** daily_summary-2026-07-22

### Account & Risk
- Equity: $99,800.81 | Cash: $99,552.75 | Buying power: $398,905.56
- Peak: $99,806.81 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $95.31 | $-4.53 (-4.54%) |
| JNJ | long | 0.325894297 | $83.43 | +$8.43 (11.24%) |
| WELL | long | 0.11425542 | $28.00 | +$3.00 (11.99%) |
| WMT | long | 0.377715036 | $41.32 | $-8.68 (-17.36%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+10.30%, breadth=64.56%)
- Candidates: 10 | Selected: 10 | Excluded: 69
- Scanned at: 2026-07-22T21:43:28Z

### Trade Plan
- Plan ID: `trade_plan-20260722T214328-0b021f40`
- Generated: 2026-07-22T21:43:28Z | Expires: 2026-07-23T03:43:28Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - V BUY $25.00 @ $353.42 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260722T214328-c46db8a7`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260722T214328-c2185bef

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-22

**Generated:** 2026-07-22T22:04:04Z  **Run ID:** daily_summary-2026-07-22

### Account & Risk
- Equity: $99,800.81 | Cash: $99,552.75 | Buying power: $398,905.56
- Peak: $99,806.81 | Drawdown: -0.01% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $95.31 | $-4.53 (-4.54%) |
| JNJ | long | 0.325894297 | $83.43 | +$8.43 (11.24%) |
| WELL | long | 0.11425542 | $28.00 | +$3.00 (11.99%) |
| WMT | long | 0.377715036 | $41.32 | $-8.68 (-17.36%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+10.30%, breadth=64.56%)
- Candidates: 10 | Selected: 10 | Excluded: 69
- Scanned at: 2026-07-22T21:43:28Z

### Trade Plan
- Plan ID: `trade_plan-20260722T214328-0b021f40`
- Generated: 2026-07-22T21:43:28Z | Expires: 2026-07-23T03:43:28Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - V BUY $25.00 @ $353.42 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260722T214328-c46db8a7`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260722T214328-c2185bef

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-23

**Generated:** 2026-07-23T21:41:27Z  **Run ID:** daily_summary-2026-07-23

### Account & Risk
- Equity: $99,801.88 | Cash: $99,552.75 | Buying power: $99,552.75
- Peak: $99,806.81 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $95.76 | $-4.08 (-4.09%) |
| JNJ | long | 0.325894297 | $84.41 | +$9.41 (12.54%) |
| WELL | long | 0.11425542 | $28.23 | +$3.23 (12.91%) |
| WMT | long | 0.377715036 | $40.74 | $-9.26 (-18.52%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+7.69%, breadth=63.29%)
- Candidates: 11 | Selected: 10 | Excluded: 69
- Scanned at: 2026-07-23T21:41:27Z

### Trade Plan
- Plan ID: `trade_plan-20260723T214127-c001095d`
- Generated: 2026-07-23T21:41:27Z | Expires: 2026-07-24T03:41:27Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - WMT SELL $25.00 @ $107.86 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260723T214127-5155295a`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260723T214126-a2e355ac

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-23

**Generated:** 2026-07-23T22:04:43Z  **Run ID:** daily_summary-2026-07-23

### Account & Risk
- Equity: $99,801.88 | Cash: $99,552.75 | Buying power: $99,552.75
- Peak: $99,806.81 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $95.76 | $-4.08 (-4.09%) |
| JNJ | long | 0.325894297 | $84.41 | +$9.41 (12.54%) |
| WELL | long | 0.11425542 | $28.23 | +$3.23 (12.91%) |
| WMT | long | 0.377715036 | $40.74 | $-9.26 (-18.52%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+7.69%, breadth=63.29%)
- Candidates: 11 | Selected: 10 | Excluded: 69
- Scanned at: 2026-07-23T21:41:27Z

### Trade Plan
- Plan ID: `trade_plan-20260723T214127-c001095d`
- Generated: 2026-07-23T21:41:27Z | Expires: 2026-07-24T03:41:27Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - WMT SELL $25.00 @ $107.86 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260723T214127-5155295a`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260723T214126-a2e355ac

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-24

**Generated:** 2026-07-24T21:44:41Z  **Run ID:** daily_summary-2026-07-24

### Account & Risk
- Equity: $99,809.09 | Cash: $99,552.75 | Buying power: $398,928.75
- Peak: $99,809.69 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $100.45 | +$0.61 (0.61%) |
| JNJ | long | 0.325894297 | $85.75 | +$10.75 (14.33%) |
| WELL | long | 0.11425542 | $28.80 | +$3.80 (15.20%) |
| WMT | long | 0.377715036 | $41.34 | $-8.66 (-17.33%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+7.25%, breadth=62.03%)
- Candidates: 16 | Selected: 10 | Excluded: 69
- Scanned at: 2026-07-24T21:44:41Z

### Trade Plan
- Plan ID: `trade_plan-20260724T214441-9712f160`
- Generated: 2026-07-24T21:44:41Z | Expires: 2026-07-25T03:44:41Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - WMT SELL $25.00 @ $109.44 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260724T214441-80461aa0`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260724T214440-22b1b1cf

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-24

**Generated:** 2026-07-24T22:05:14Z  **Run ID:** daily_summary-2026-07-24

### Account & Risk
- Equity: $99,809.09 | Cash: $99,552.75 | Buying power: $398,928.75
- Peak: $99,809.69 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $100.45 | +$0.61 (0.61%) |
| JNJ | long | 0.325894297 | $85.75 | +$10.75 (14.33%) |
| WELL | long | 0.11425542 | $28.80 | +$3.80 (15.20%) |
| WMT | long | 0.377715036 | $41.34 | $-8.66 (-17.33%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+7.25%, breadth=62.03%)
- Candidates: 16 | Selected: 10 | Excluded: 69
- Scanned at: 2026-07-24T21:44:41Z

### Trade Plan
- Plan ID: `trade_plan-20260724T214441-9712f160`
- Generated: 2026-07-24T21:44:41Z | Expires: 2026-07-25T03:44:41Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - WMT SELL $25.00 @ $109.44 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260724T214441-80461aa0`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260724T214440-22b1b1cf

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-27

**Generated:** 2026-07-27T21:47:13Z  **Run ID:** daily_summary-2026-07-27

### Account & Risk
- Equity: $99,808.50 | Cash: $99,552.75 | Buying power: $398,927.10
- Peak: $99,809.69 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $96.98 | $-2.86 (-2.86%) |
| JNJ | long | 0.325894297 | $86.95 | +$11.95 (15.93%) |
| WELL | long | 0.11425542 | $29.59 | +$4.59 (18.37%) |
| WMT | long | 0.377715036 | $42.23 | $-7.77 (-15.55%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+7.20%, breadth=65.82%)
- Candidates: 13 | Selected: 10 | Excluded: 69
- Scanned at: 2026-07-27T21:47:12Z

### Trade Plan
- Plan ID: `trade_plan-20260727T214713-d4331e7f`
- Generated: 2026-07-27T21:47:13Z | Expires: 2026-07-28T03:47:13Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - NEE BUY $25.00 @ $88.81 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260727T214713-70331527`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260727T214712-294205cc

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-27

**Generated:** 2026-07-27T22:08:19Z  **Run ID:** daily_summary-2026-07-27

### Account & Risk
- Equity: $99,808.50 | Cash: $99,552.75 | Buying power: $398,927.10
- Peak: $99,809.69 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $96.98 | $-2.86 (-2.86%) |
| JNJ | long | 0.325894297 | $86.95 | +$11.95 (15.93%) |
| WELL | long | 0.11425542 | $29.59 | +$4.59 (18.37%) |
| WMT | long | 0.377715036 | $42.23 | $-7.77 (-15.55%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+7.20%, breadth=65.82%)
- Candidates: 13 | Selected: 10 | Excluded: 69
- Scanned at: 2026-07-27T21:47:12Z

### Trade Plan
- Plan ID: `trade_plan-20260727T214713-d4331e7f`
- Generated: 2026-07-27T21:47:13Z | Expires: 2026-07-28T03:47:13Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - NEE BUY $25.00 @ $88.81 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260727T214713-70331527`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (0)
- Pass: 0 | Fail: 0

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260727T214712-294205cc

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
## Daily Summary — 2026-07-28

**Generated:** 2026-07-28T21:46:19Z  **Run ID:** daily_summary-2026-07-28

### Account & Risk
- Equity: $99,807.38 | Cash: $99,552.75 | Buying power: $398,923.97
- Peak: $99,809.69 | Drawdown: -0.00% | Positions: 4

### Positions (4)
| Symbol | Side | Qty | Market Value | Unrealized P/L |
|--------|------|-----|--------------|----------------|
| EQIX | long | 0.092649719 | $96.85 | $-2.99 (-3.00%) |
| JNJ | long | 0.325894297 | $87.17 | +$12.17 (16.23%) |
| WELL | long | 0.11425542 | $27.83 | +$2.83 (11.32%) |
| WMT | long | 0.377715036 | $42.78 | $-7.22 (-14.44%) |

### Open Orders (0)
None.

### Trigger Scan
- Regime: **RISK_ON** (SPY 200DMA=✓, 6m ROC=+6.93%, breadth=69.62%)
- Candidates: 10 | Selected: 7 | Excluded: 72
- Scanned at: 2026-07-28T21:46:18Z

### Trade Plan
- Plan ID: `trade_plan-20260728T214618-b319f24b`
- Generated: 2026-07-28T21:46:18Z | Expires: 2026-07-29T03:46:18Z
- Approved for execution: NO | Reason: approve_paper_flag_not_set
- All risk checks pass: YES
- Proposed orders (1):
  - UNP BUY $25.00 @ $294.37 (limit, day)

### Latest Execution Report (Dry Run)
- Run ID: `execution-20260728T214618-6f71cbd7`
- All gates pass: NO
- Failed gates: QUOTE_FRESHNESS

### Dry Runs Today (1)
- Pass: 0 | Fail: 1
  - QUOTE_FRESHNESS: 1x

### Paper Executions Today (0)
None today.

### Order Monitor
- Tracked: 14 | Filled: 14 | Missing: 0 | Expired: 0 | Rejected: 0 | Active: 0
- Runs today: 2 | Latest: order_monitor-20260728T214618-a5e97239

### Alerts (total=23, today=0)
- By source: tradingview=21, test=2
- By next_step: request_trade_plan_unapproved=17, request_data_refresh=5, log_only=1

### Alert Routes (total=5, today=0)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By action: refresh_requested=4, logged=1

### Data Quality
- Status: **PASS** | Issues: 0 | Wide spreads: 0 | Missing bars: 0 | Insufficient bars: 0
- Generated: 2026-05-12T15:33:05Z

---
