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
## Weekly Review — 2026-05-07 to 2026-05-13 (7 days)

**Generated:** 2026-05-13T19:35:01Z  **Run ID:** weekly_review-2026-05-13

### Trigger Scans
- Total runs: 0 | Risk-on: 0 | Risk-off: 0
- Avg candidates: 0.0 | Avg excluded: 0.0

### Dry Runs
- Total: 0 | Pass: 0 | Fail: 0

### Paper Executions
- Attempts: 4 | Orders submitted: 4
  - [2026-05-13] WELL BUY $25.0 @ $218.9 (PAPER_SUBMITTED)
  - [2026-05-13] JNJ BUY $25.0 @ $230.26 (PAPER_SUBMITTED)
  - [2026-05-13] EQIX BUY $25.0 @ $1084.52 (PAPER_SUBMITTED)
  - [2026-05-13] EQIX SELL $25.0 @ $1084.25 (PAPER_ORDER_ERRORS)

### Order Lifecycle
- Monitor runs: 11 | Tracked: 14
- Fills: 6 | Missing: 6 | Expired: 0 | Rejected: 0 | Canceled: 0

### External Alerts
- Ingested this period: 8 (all-time: 8)
- Routes this period: 5 (all-time: 5)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By next_step: request_trade_plan_unapproved=2, request_data_refresh=5, log_only=1

### Risk State
- Equity: $99,803.07 | Peak: $99,803.14 | Drawdown: -0.00% | Positions: 3
- Last updated: 2026-05-13T19:33:16Z

### Operational Issues (2)
- Paper execution execution-20260513T193130-305917e5 had unexpected status: PAPER_ORDER_ERRORS
- 6 order(s) have lifecycle_status=missing — verify on broker.

### Research Observations
- 4 paper execution attempt(s), 4 order(s) submitted.
- 6 order fill(s) confirmed by order monitor.
- 8 external alert(s) ingested this period, 5 routed.

---
## Weekly Review — 2026-05-07 to 2026-05-13 (7 days)

**Generated:** 2026-05-13T19:46:16Z  **Run ID:** weekly_review-2026-05-13

### Trigger Scans
- Total runs: 0 | Risk-on: 0 | Risk-off: 0
- Avg candidates: 0.0 | Avg excluded: 0.0

### Dry Runs
- Total: 0 | Pass: 0 | Fail: 0

### Paper Executions
- Attempts: 4 | Orders submitted: 4
  - [2026-05-13] WELL BUY $25.0 @ $218.9 (PAPER_SUBMITTED)
  - [2026-05-13] JNJ BUY $25.0 @ $230.26 (PAPER_SUBMITTED)
  - [2026-05-13] EQIX BUY $25.0 @ $1084.52 (PAPER_SUBMITTED)
  - [2026-05-13] EQIX SELL $25.0 @ $1084.25 (PAPER_ORDER_ERRORS)

### Order Lifecycle
- Monitor runs: 11 | Unique orders: 3
- Fills: 3 | Partial: 0 | Missing: 0 | Expired: 0 | Rejected: 0 | Canceled: 0
- Latest lifecycle by order (3):
  - TOS-20260513T160035-WELL-BUY | WELL buy | status=filled fill=$218.808 qty=0.11425542 notional=$25.0 | checked=2026-05-13T19:32:15Z
  - TOS-20260513T192526-JNJ-BUY | JNJ buy | status=filled fill=$230.248 qty=0.108578576 notional=$25.0 | checked=2026-05-13T19:32:15Z
  - TOS-20260513T192934-EQIX-BUY | EQIX buy | status=filled fill=$1084.37 qty=0.023054861 notional=$25.0 | checked=2026-05-13T19:32:15Z

### External Alerts
- Ingested this period: 8 (all-time: 8)
- Routes this period: 5 (all-time: 5)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By next_step: request_trade_plan_unapproved=2, request_data_refresh=5, log_only=1

### Risk State
- Equity: $99,803.07 | Peak: $99,803.14 | Drawdown: -0.00% | Positions: 3
- Last updated: 2026-05-13T19:33:16Z

### Operational Issues (1)
- Paper execution execution-20260513T193130-305917e5 had unexpected status: PAPER_ORDER_ERRORS

### Research Observations
- 4 paper execution attempt(s), 4 order(s) submitted.
- 3 order fill(s) confirmed by order monitor.
- 8 external alert(s) ingested this period, 5 routed.

---
## Weekly Review — 2026-05-07 to 2026-05-13 (7 days)

**Generated:** 2026-05-13T21:05:22Z  **Run ID:** weekly_review-2026-05-13

### Trigger Scans
- Total runs: 0 | Risk-on: 0 | Risk-off: 0
- Avg candidates: 0.0 | Avg excluded: 0.0

### Dry Runs
- Total: 0 | Pass: 0 | Fail: 0

### Paper Executions
- Attempts: 4 | Orders submitted: 4
  - [2026-05-13] WELL BUY $25.0 @ $218.9 (PAPER_SUBMITTED)
  - [2026-05-13] JNJ BUY $25.0 @ $230.26 (PAPER_SUBMITTED)
  - [2026-05-13] EQIX BUY $25.0 @ $1084.52 (PAPER_SUBMITTED)
  - [2026-05-13] EQIX SELL $25.0 @ $1084.25 (PAPER_ORDER_ERRORS)

### Order Lifecycle
- Monitor runs: 13 | Unique orders: 3
- Fills: 3 | Partial: 0 | Missing: 0 | Expired: 0 | Rejected: 0 | Canceled: 0
- Latest lifecycle by order (3):
  - TOS-20260513T160035-WELL-BUY | WELL buy | status=filled fill=$218.808 qty=0.11425542 notional=$25.0 | checked=2026-05-13T21:02:02Z
  - TOS-20260513T192526-JNJ-BUY | JNJ buy | status=filled fill=$230.248 qty=0.108578576 notional=$25.0 | checked=2026-05-13T21:02:02Z
  - TOS-20260513T192934-EQIX-BUY | EQIX buy | status=filled fill=$1084.37 qty=0.023054861 notional=$25.0 | checked=2026-05-13T21:02:02Z

### External Alerts
- Ingested this period: 8 (all-time: 8)
- Routes this period: 5 (all-time: 5)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By next_step: request_trade_plan_unapproved=2, request_data_refresh=5, log_only=1

### Risk State
- Equity: $99,802.92 | Peak: $99,803.14 | Drawdown: -0.00% | Positions: 3
- Last updated: 2026-05-13T21:01:10Z

### Operational Issues (1)
- Paper execution execution-20260513T193130-305917e5 had unexpected status: PAPER_ORDER_ERRORS

### Research Observations
- 4 paper execution attempt(s), 4 order(s) submitted.
- 3 order fill(s) confirmed by order monitor.
- 8 external alert(s) ingested this period, 5 routed.

---
## Weekly Review — 2026-05-09 to 2026-05-15 (7 days)

**Generated:** 2026-05-15T22:29:46Z  **Run ID:** weekly_review-2026-05-15

### Trigger Scans
- Total runs: 0 | Risk-on: 0 | Risk-off: 0
- Avg candidates: 0.0 | Avg excluded: 0.0

### Dry Runs
- Total: 0 | Pass: 0 | Fail: 0

### Paper Executions
- Attempts: 23 | Orders submitted: 15
  - [2026-05-13] WELL BUY $25.0 @ $218.9 (PAPER_SUBMITTED)
  - [2026-05-13] JNJ BUY $25.0 @ $230.26 (PAPER_SUBMITTED)
  - [2026-05-13] EQIX BUY $25.0 @ $1084.52 (PAPER_SUBMITTED)
  - [2026-05-13] EQIX SELL $25.0 @ $1084.25 (PAPER_ORDER_ERRORS)
  - [2026-05-14] EQIX BUY $25.0 @ $1079.73 (PAPER_SUBMITTED)
  - [2026-05-14] JNJ BUY $25.0 @ $230.12 (PAPER_SUBMITTED)
  - [2026-05-14] EQIX SELL $25.0 @ $1078.28 (PAPER_SUBMITTED)
  - [2026-05-14] EQIX BUY $25.0 @ $1078.43 (PAPER_SUBMITTED)
  - [2026-05-14] EQIX BUY $25.0 @ $1076.96 (PAPER_SUBMITTED)
  - [2026-05-14] WMT BUY $25.0 @ $132.36 (PAPER_SUBMITTED)
  - [2026-05-14] JNJ BUY $25.0 @ $230.05 (PAPER_SUBMITTED)
  - [2026-05-14] WMT BUY $25.0 @ $132.48 (PAPER_SUBMITTED)
  - [2026-05-14] EQIX BUY $25.0 @ $1078.96 (PAPER_SUBMITTED)
  - [2026-05-14] EQIX SELL $25.0 @ $1076.63 (PAPER_SUBMITTED)
  - [2026-05-14] EQIX BUY $25.0 @ $1076.63 (PAPER_SUBMITTED)

### Order Lifecycle
- Monitor runs: 69 | Unique orders: 14
- Fills: 14 | Partial: 0 | Missing: 0 | Expired: 0 | Rejected: 0 | Canceled: 0
- Latest lifecycle by order (14):
  - TOS-20260513T160035-WELL-BUY | WELL buy | status=filled fill=$218.808 qty=0.11425542 notional=$25.0 | checked=2026-05-15T21:41:03Z
  - TOS-20260513T192526-JNJ-BUY | JNJ buy | status=filled fill=$230.248 qty=0.108578576 notional=$25.0 | checked=2026-05-15T21:41:03Z
  - TOS-20260513T192934-EQIX-BUY | EQIX buy | status=filled fill=$1084.37 qty=0.023054861 notional=$25.0 | checked=2026-05-15T21:41:03Z
  - TOS-20260514T145625-EQIX-BUY | EQIX buy | status=filled fill=$1079.5 qty=0.023158869 notional=$25.0 | checked=2026-05-15T21:41:03Z
  - TOS-20260514T154323-JNJ-BUY | JNJ buy | status=filled fill=$230.116 qty=0.108640859 notional=$25.0 | checked=2026-05-15T21:41:03Z
  - TOS-20260514T154543-EQIX-SELL | EQIX sell | status=filled fill=$1078.442 qty=0.023181589 notional=$25.0 | checked=2026-05-15T21:41:03Z
  - TOS-20260514T154817-EQIX-BUY | EQIX buy | status=filled fill=$1078.41 qty=0.023182277 notional=$25.0 | checked=2026-05-15T21:41:03Z
  - TOS-20260514T163113-EQIX-BUY | EQIX buy | status=filled fill=$1076.89 qty=0.023214998 notional=$25.0 | checked=2026-05-15T21:41:03Z
  - TOS-20260514T165232-WMT-BUY | WMT buy | status=filled fill=$132.276 qty=0.18899876 notional=$25.0 | checked=2026-05-15T21:41:03Z
  - TOS-20260514T171739-JNJ-BUY | JNJ buy | status=filled fill=$230.044 qty=0.108674862 notional=$25.0 | checked=2026-05-15T21:41:03Z
  - TOS-20260514T171844-WMT-BUY | WMT buy | status=filled fill=$132.474 qty=0.188716276 notional=$25.0 | checked=2026-05-15T21:41:03Z
  - TOS-20260514T172103-EQIX-BUY | EQIX buy | status=filled fill=$1076.82 qty=0.023216507 notional=$25.0 | checked=2026-05-15T21:41:03Z
  - TOS-20260514T172226-EQIX-SELL | EQIX sell | status=filled fill=$1076.718 qty=0.023218707 notional=$25.0 | checked=2026-05-15T21:41:03Z
  - TOS-20260514T172335-EQIX-BUY | EQIX buy | status=filled fill=$1076.542 qty=0.023222503 notional=$25.0 | checked=2026-05-15T21:41:03Z

### External Alerts
- Ingested this period: 12 (all-time: 12)
- Routes this period: 5 (all-time: 5)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By next_step: request_trade_plan_unapproved=6, request_data_refresh=5, log_only=1

### Risk State
- Equity: $99,799.26 | Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4
- Last updated: 2026-05-15T21:41:02Z

### Operational Issues (9)
- Paper execution execution-20260513T193130-305917e5 had unexpected status: PAPER_ORDER_ERRORS
- Paper execution execution-20260514T134814-b4369954 had unexpected status: PAPER_FAIL
- Paper execution execution-20260514T135504-19cce5c5 had unexpected status: PAPER_FAIL
- Paper execution execution-20260514T150121-0f807e87 had unexpected status: PAPER_BLOCKED
- Paper execution execution-20260514T171953-fe151e9b had unexpected status: PAPER_BLOCKED
- Paper execution execution-20260514T174900-1d804822 had unexpected status: PAPER_BLOCKED
- Paper execution execution-20260514T175023-d2a85437 had unexpected status: PAPER_BLOCKED
- Paper execution execution-20260514T175221-05f9ad9c had unexpected status: PAPER_BLOCKED
- Paper execution execution-20260514T175739-c2e2d180 had unexpected status: PAPER_BLOCKED

### Research Observations
- 23 paper execution attempt(s), 15 order(s) submitted.
- 14 order fill(s) confirmed by order monitor.
- 12 external alert(s) ingested this period, 5 routed.

---
## Weekly Review — 2026-05-16 to 2026-05-22 (7 days)

**Generated:** 2026-05-22T22:33:52Z  **Run ID:** weekly_review-2026-05-22

### Trigger Scans
- Total runs: 0 | Risk-on: 0 | Risk-off: 0
- Avg candidates: 0.0 | Avg excluded: 0.0

### Dry Runs
- Total: 0 | Pass: 0 | Fail: 0

### Paper Executions
- Attempts: 0 | Orders submitted: 0

### Order Lifecycle
- Monitor runs: 10 | Unique orders: 14
- Fills: 14 | Partial: 0 | Missing: 0 | Expired: 0 | Rejected: 0 | Canceled: 0
- Latest lifecycle by order (14):
  - TOS-20260513T160035-WELL-BUY | WELL buy | status=filled fill=$218.808 qty=0.11425542 notional=$25.0 | checked=2026-05-22T21:51:47Z
  - TOS-20260513T192526-JNJ-BUY | JNJ buy | status=filled fill=$230.248 qty=0.108578576 notional=$25.0 | checked=2026-05-22T21:51:47Z
  - TOS-20260513T192934-EQIX-BUY | EQIX buy | status=filled fill=$1084.37 qty=0.023054861 notional=$25.0 | checked=2026-05-22T21:51:47Z
  - TOS-20260514T145625-EQIX-BUY | EQIX buy | status=filled fill=$1079.5 qty=0.023158869 notional=$25.0 | checked=2026-05-22T21:51:47Z
  - TOS-20260514T154323-JNJ-BUY | JNJ buy | status=filled fill=$230.116 qty=0.108640859 notional=$25.0 | checked=2026-05-22T21:51:47Z
  - TOS-20260514T154543-EQIX-SELL | EQIX sell | status=filled fill=$1078.442 qty=0.023181589 notional=$25.0 | checked=2026-05-22T21:51:47Z
  - TOS-20260514T154817-EQIX-BUY | EQIX buy | status=filled fill=$1078.41 qty=0.023182277 notional=$25.0 | checked=2026-05-22T21:51:47Z
  - TOS-20260514T163113-EQIX-BUY | EQIX buy | status=filled fill=$1076.89 qty=0.023214998 notional=$25.0 | checked=2026-05-22T21:51:47Z
  - TOS-20260514T165232-WMT-BUY | WMT buy | status=filled fill=$132.276 qty=0.18899876 notional=$25.0 | checked=2026-05-22T21:51:47Z
  - TOS-20260514T171739-JNJ-BUY | JNJ buy | status=filled fill=$230.044 qty=0.108674862 notional=$25.0 | checked=2026-05-22T21:51:47Z
  - TOS-20260514T171844-WMT-BUY | WMT buy | status=filled fill=$132.474 qty=0.188716276 notional=$25.0 | checked=2026-05-22T21:51:47Z
  - TOS-20260514T172103-EQIX-BUY | EQIX buy | status=filled fill=$1076.82 qty=0.023216507 notional=$25.0 | checked=2026-05-22T21:51:47Z
  - TOS-20260514T172226-EQIX-SELL | EQIX sell | status=filled fill=$1076.718 qty=0.023218707 notional=$25.0 | checked=2026-05-22T21:51:47Z
  - TOS-20260514T172335-EQIX-BUY | EQIX buy | status=filled fill=$1076.542 qty=0.023222503 notional=$25.0 | checked=2026-05-22T21:51:47Z

### External Alerts
- Ingested this period: 9 (all-time: 21)
- Routes this period: 0 (all-time: 5)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By next_step: request_trade_plan_unapproved=9

### Risk State
- Equity: $99,799.22 | Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4
- Last updated: 2026-05-22T21:51:45Z

### Operational Issues (0)
None identified.

### Research Observations
- No paper executions this period.
- 14 order fill(s) confirmed by order monitor.
- 9 external alert(s) ingested this period, 0 routed.

---
## Weekly Review — 2026-05-23 to 2026-05-29 (7 days)

**Generated:** 2026-05-29T22:50:13Z  **Run ID:** weekly_review-2026-05-29

### Trigger Scans
- Total runs: 0 | Risk-on: 0 | Risk-off: 0
- Avg candidates: 0.0 | Avg excluded: 0.0

### Dry Runs
- Total: 0 | Pass: 0 | Fail: 0

### Paper Executions
- Attempts: 0 | Orders submitted: 0

### Order Lifecycle
- Monitor runs: 10 | Unique orders: 14
- Fills: 14 | Partial: 0 | Missing: 0 | Expired: 0 | Rejected: 0 | Canceled: 0
- Latest lifecycle by order (14):
  - TOS-20260513T160035-WELL-BUY | WELL buy | status=filled fill=$218.808 qty=0.11425542 notional=$25.0 | checked=2026-05-29T22:18:29Z
  - TOS-20260513T192526-JNJ-BUY | JNJ buy | status=filled fill=$230.248 qty=0.108578576 notional=$25.0 | checked=2026-05-29T22:18:29Z
  - TOS-20260513T192934-EQIX-BUY | EQIX buy | status=filled fill=$1084.37 qty=0.023054861 notional=$25.0 | checked=2026-05-29T22:18:29Z
  - TOS-20260514T145625-EQIX-BUY | EQIX buy | status=filled fill=$1079.5 qty=0.023158869 notional=$25.0 | checked=2026-05-29T22:18:29Z
  - TOS-20260514T154323-JNJ-BUY | JNJ buy | status=filled fill=$230.116 qty=0.108640859 notional=$25.0 | checked=2026-05-29T22:18:29Z
  - TOS-20260514T154543-EQIX-SELL | EQIX sell | status=filled fill=$1078.442 qty=0.023181589 notional=$25.0 | checked=2026-05-29T22:18:29Z
  - TOS-20260514T154817-EQIX-BUY | EQIX buy | status=filled fill=$1078.41 qty=0.023182277 notional=$25.0 | checked=2026-05-29T22:18:29Z
  - TOS-20260514T163113-EQIX-BUY | EQIX buy | status=filled fill=$1076.89 qty=0.023214998 notional=$25.0 | checked=2026-05-29T22:18:29Z
  - TOS-20260514T165232-WMT-BUY | WMT buy | status=filled fill=$132.276 qty=0.18899876 notional=$25.0 | checked=2026-05-29T22:18:29Z
  - TOS-20260514T171739-JNJ-BUY | JNJ buy | status=filled fill=$230.044 qty=0.108674862 notional=$25.0 | checked=2026-05-29T22:18:29Z
  - TOS-20260514T171844-WMT-BUY | WMT buy | status=filled fill=$132.474 qty=0.188716276 notional=$25.0 | checked=2026-05-29T22:18:29Z
  - TOS-20260514T172103-EQIX-BUY | EQIX buy | status=filled fill=$1076.82 qty=0.023216507 notional=$25.0 | checked=2026-05-29T22:18:29Z
  - TOS-20260514T172226-EQIX-SELL | EQIX sell | status=filled fill=$1076.718 qty=0.023218707 notional=$25.0 | checked=2026-05-29T22:18:29Z
  - TOS-20260514T172335-EQIX-BUY | EQIX buy | status=filled fill=$1076.542 qty=0.023222503 notional=$25.0 | checked=2026-05-29T22:18:29Z

### External Alerts
- Ingested this period: 2 (all-time: 23)
- Routes this period: 0 (all-time: 5)
- Execution called (ever): NO
- Approved plan created (ever): NO
- By next_step: request_trade_plan_unapproved=2

### Risk State
- Equity: $99,792.28 | Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4
- Last updated: 2026-05-29T22:18:28Z

### Operational Issues (0)
None identified.

### Research Observations
- No paper executions this period.
- 14 order fill(s) confirmed by order monitor.
- 2 external alert(s) ingested this period, 0 routed.

---
## Weekly Review — 2026-05-30 to 2026-06-05 (7 days)

**Generated:** 2026-06-05T22:41:07Z  **Run ID:** weekly_review-2026-06-05

### Trigger Scans
- Total runs: 0 | Risk-on: 0 | Risk-off: 0
- Avg candidates: 0.0 | Avg excluded: 0.0

### Dry Runs
- Total: 0 | Pass: 0 | Fail: 0

### Paper Executions
- Attempts: 0 | Orders submitted: 0

### Order Lifecycle
- Monitor runs: 10 | Unique orders: 14
- Fills: 14 | Partial: 0 | Missing: 0 | Expired: 0 | Rejected: 0 | Canceled: 0
- Latest lifecycle by order (14):
  - TOS-20260513T160035-WELL-BUY | WELL buy | status=filled fill=$218.808 qty=0.11425542 notional=$25.0 | checked=2026-06-05T22:05:50Z
  - TOS-20260513T192526-JNJ-BUY | JNJ buy | status=filled fill=$230.248 qty=0.108578576 notional=$25.0 | checked=2026-06-05T22:05:50Z
  - TOS-20260513T192934-EQIX-BUY | EQIX buy | status=filled fill=$1084.37 qty=0.023054861 notional=$25.0 | checked=2026-06-05T22:05:50Z
  - TOS-20260514T145625-EQIX-BUY | EQIX buy | status=filled fill=$1079.5 qty=0.023158869 notional=$25.0 | checked=2026-06-05T22:05:50Z
  - TOS-20260514T154323-JNJ-BUY | JNJ buy | status=filled fill=$230.116 qty=0.108640859 notional=$25.0 | checked=2026-06-05T22:05:50Z
  - TOS-20260514T154543-EQIX-SELL | EQIX sell | status=filled fill=$1078.442 qty=0.023181589 notional=$25.0 | checked=2026-06-05T22:05:50Z
  - TOS-20260514T154817-EQIX-BUY | EQIX buy | status=filled fill=$1078.41 qty=0.023182277 notional=$25.0 | checked=2026-06-05T22:05:50Z
  - TOS-20260514T163113-EQIX-BUY | EQIX buy | status=filled fill=$1076.89 qty=0.023214998 notional=$25.0 | checked=2026-06-05T22:05:50Z
  - TOS-20260514T165232-WMT-BUY | WMT buy | status=filled fill=$132.276 qty=0.18899876 notional=$25.0 | checked=2026-06-05T22:05:50Z
  - TOS-20260514T171739-JNJ-BUY | JNJ buy | status=filled fill=$230.044 qty=0.108674862 notional=$25.0 | checked=2026-06-05T22:05:50Z
  - TOS-20260514T171844-WMT-BUY | WMT buy | status=filled fill=$132.474 qty=0.188716276 notional=$25.0 | checked=2026-06-05T22:05:50Z
  - TOS-20260514T172103-EQIX-BUY | EQIX buy | status=filled fill=$1076.82 qty=0.023216507 notional=$25.0 | checked=2026-06-05T22:05:50Z
  - TOS-20260514T172226-EQIX-SELL | EQIX sell | status=filled fill=$1076.718 qty=0.023218707 notional=$25.0 | checked=2026-06-05T22:05:50Z
  - TOS-20260514T172335-EQIX-BUY | EQIX buy | status=filled fill=$1076.542 qty=0.023222503 notional=$25.0 | checked=2026-06-05T22:05:50Z

### External Alerts
- Ingested this period: 0 (all-time: 23)
- Routes this period: 0 (all-time: 5)
- Execution called (ever): NO
- Approved plan created (ever): NO

### Risk State
- Equity: $99,796.70 | Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4
- Last updated: 2026-06-05T22:05:49Z

### Operational Issues (0)
None identified.

### Research Observations
- No paper executions this period.
- 14 order fill(s) confirmed by order monitor.

---
## Weekly Review — 2026-06-06 to 2026-06-12 (7 days)

**Generated:** 2026-06-12T22:56:27Z  **Run ID:** weekly_review-2026-06-12

### Trigger Scans
- Total runs: 0 | Risk-on: 0 | Risk-off: 0
- Avg candidates: 0.0 | Avg excluded: 0.0

### Dry Runs
- Total: 0 | Pass: 0 | Fail: 0

### Paper Executions
- Attempts: 0 | Orders submitted: 0

### Order Lifecycle
- Monitor runs: 10 | Unique orders: 14
- Fills: 14 | Partial: 0 | Missing: 0 | Expired: 0 | Rejected: 0 | Canceled: 0
- Latest lifecycle by order (14):
  - TOS-20260513T160035-WELL-BUY | WELL buy | status=filled fill=$218.808 qty=0.11425542 notional=$25.0 | checked=2026-06-12T22:14:33Z
  - TOS-20260513T192526-JNJ-BUY | JNJ buy | status=filled fill=$230.248 qty=0.108578576 notional=$25.0 | checked=2026-06-12T22:14:33Z
  - TOS-20260513T192934-EQIX-BUY | EQIX buy | status=filled fill=$1084.37 qty=0.023054861 notional=$25.0 | checked=2026-06-12T22:14:33Z
  - TOS-20260514T145625-EQIX-BUY | EQIX buy | status=filled fill=$1079.5 qty=0.023158869 notional=$25.0 | checked=2026-06-12T22:14:33Z
  - TOS-20260514T154323-JNJ-BUY | JNJ buy | status=filled fill=$230.116 qty=0.108640859 notional=$25.0 | checked=2026-06-12T22:14:33Z
  - TOS-20260514T154543-EQIX-SELL | EQIX sell | status=filled fill=$1078.442 qty=0.023181589 notional=$25.0 | checked=2026-06-12T22:14:33Z
  - TOS-20260514T154817-EQIX-BUY | EQIX buy | status=filled fill=$1078.41 qty=0.023182277 notional=$25.0 | checked=2026-06-12T22:14:33Z
  - TOS-20260514T163113-EQIX-BUY | EQIX buy | status=filled fill=$1076.89 qty=0.023214998 notional=$25.0 | checked=2026-06-12T22:14:33Z
  - TOS-20260514T165232-WMT-BUY | WMT buy | status=filled fill=$132.276 qty=0.18899876 notional=$25.0 | checked=2026-06-12T22:14:33Z
  - TOS-20260514T171739-JNJ-BUY | JNJ buy | status=filled fill=$230.044 qty=0.108674862 notional=$25.0 | checked=2026-06-12T22:14:33Z
  - TOS-20260514T171844-WMT-BUY | WMT buy | status=filled fill=$132.474 qty=0.188716276 notional=$25.0 | checked=2026-06-12T22:14:33Z
  - TOS-20260514T172103-EQIX-BUY | EQIX buy | status=filled fill=$1076.82 qty=0.023216507 notional=$25.0 | checked=2026-06-12T22:14:33Z
  - TOS-20260514T172226-EQIX-SELL | EQIX sell | status=filled fill=$1076.718 qty=0.023218707 notional=$25.0 | checked=2026-06-12T22:14:33Z
  - TOS-20260514T172335-EQIX-BUY | EQIX buy | status=filled fill=$1076.542 qty=0.023222503 notional=$25.0 | checked=2026-06-12T22:14:33Z

### External Alerts
- Ingested this period: 0 (all-time: 23)
- Routes this period: 0 (all-time: 5)
- Execution called (ever): NO
- Approved plan created (ever): NO

### Risk State
- Equity: $99,799.13 | Peak: $99,803.14 | Drawdown: -0.00% | Positions: 4
- Last updated: 2026-06-12T22:14:31Z

### Operational Issues (0)
None identified.

### Research Observations
- No paper executions this period.
- 14 order fill(s) confirmed by order monitor.

---
## Weekly Review — 2026-06-13 to 2026-06-19 (7 days)

**Generated:** 2026-06-19T22:30:57Z  **Run ID:** weekly_review-2026-06-19

### Trigger Scans
- Total runs: 0 | Risk-on: 0 | Risk-off: 0
- Avg candidates: 0.0 | Avg excluded: 0.0

### Dry Runs
- Total: 0 | Pass: 0 | Fail: 0

### Paper Executions
- Attempts: 0 | Orders submitted: 0

### Order Lifecycle
- Monitor runs: 10 | Unique orders: 14
- Fills: 14 | Partial: 0 | Missing: 0 | Expired: 0 | Rejected: 0 | Canceled: 0
- Latest lifecycle by order (14):
  - TOS-20260513T160035-WELL-BUY | WELL buy | status=filled fill=$218.808 qty=0.11425542 notional=$25.0 | checked=2026-06-19T21:49:23Z
  - TOS-20260513T192526-JNJ-BUY | JNJ buy | status=filled fill=$230.248 qty=0.108578576 notional=$25.0 | checked=2026-06-19T21:49:23Z
  - TOS-20260513T192934-EQIX-BUY | EQIX buy | status=filled fill=$1084.37 qty=0.023054861 notional=$25.0 | checked=2026-06-19T21:49:23Z
  - TOS-20260514T145625-EQIX-BUY | EQIX buy | status=filled fill=$1079.5 qty=0.023158869 notional=$25.0 | checked=2026-06-19T21:49:23Z
  - TOS-20260514T154323-JNJ-BUY | JNJ buy | status=filled fill=$230.116 qty=0.108640859 notional=$25.0 | checked=2026-06-19T21:49:23Z
  - TOS-20260514T154543-EQIX-SELL | EQIX sell | status=filled fill=$1078.442 qty=0.023181589 notional=$25.0 | checked=2026-06-19T21:49:23Z
  - TOS-20260514T154817-EQIX-BUY | EQIX buy | status=filled fill=$1078.41 qty=0.023182277 notional=$25.0 | checked=2026-06-19T21:49:23Z
  - TOS-20260514T163113-EQIX-BUY | EQIX buy | status=filled fill=$1076.89 qty=0.023214998 notional=$25.0 | checked=2026-06-19T21:49:23Z
  - TOS-20260514T165232-WMT-BUY | WMT buy | status=filled fill=$132.276 qty=0.18899876 notional=$25.0 | checked=2026-06-19T21:49:23Z
  - TOS-20260514T171739-JNJ-BUY | JNJ buy | status=filled fill=$230.044 qty=0.108674862 notional=$25.0 | checked=2026-06-19T21:49:23Z
  - TOS-20260514T171844-WMT-BUY | WMT buy | status=filled fill=$132.474 qty=0.188716276 notional=$25.0 | checked=2026-06-19T21:49:23Z
  - TOS-20260514T172103-EQIX-BUY | EQIX buy | status=filled fill=$1076.82 qty=0.023216507 notional=$25.0 | checked=2026-06-19T21:49:23Z
  - TOS-20260514T172226-EQIX-SELL | EQIX sell | status=filled fill=$1076.718 qty=0.023218707 notional=$25.0 | checked=2026-06-19T21:49:23Z
  - TOS-20260514T172335-EQIX-BUY | EQIX buy | status=filled fill=$1076.542 qty=0.023222503 notional=$25.0 | checked=2026-06-19T21:49:23Z

### External Alerts
- Ingested this period: 0 (all-time: 23)
- Routes this period: 0 (all-time: 5)
- Execution called (ever): NO
- Approved plan created (ever): NO

### Risk State
- Equity: $99,796.24 | Peak: $99,803.14 | Drawdown: -0.01% | Positions: 4
- Last updated: 2026-06-19T21:49:21Z

### Operational Issues (0)
None identified.

### Research Observations
- No paper executions this period.
- 14 order fill(s) confirmed by order monitor.

---
## Weekly Review — 2026-06-20 to 2026-06-26 (7 days)

**Generated:** 2026-06-26T22:43:51Z  **Run ID:** weekly_review-2026-06-26

### Trigger Scans
- Total runs: 0 | Risk-on: 0 | Risk-off: 0
- Avg candidates: 0.0 | Avg excluded: 0.0

### Dry Runs
- Total: 0 | Pass: 0 | Fail: 0

### Paper Executions
- Attempts: 0 | Orders submitted: 0

### Order Lifecycle
- Monitor runs: 10 | Unique orders: 14
- Fills: 14 | Partial: 0 | Missing: 0 | Expired: 0 | Rejected: 0 | Canceled: 0
- Latest lifecycle by order (14):
  - TOS-20260513T160035-WELL-BUY | WELL buy | status=filled fill=$218.808 qty=0.11425542 notional=$25.0 | checked=2026-06-26T21:51:49Z
  - TOS-20260513T192526-JNJ-BUY | JNJ buy | status=filled fill=$230.248 qty=0.108578576 notional=$25.0 | checked=2026-06-26T21:51:49Z
  - TOS-20260513T192934-EQIX-BUY | EQIX buy | status=filled fill=$1084.37 qty=0.023054861 notional=$25.0 | checked=2026-06-26T21:51:49Z
  - TOS-20260514T145625-EQIX-BUY | EQIX buy | status=filled fill=$1079.5 qty=0.023158869 notional=$25.0 | checked=2026-06-26T21:51:49Z
  - TOS-20260514T154323-JNJ-BUY | JNJ buy | status=filled fill=$230.116 qty=0.108640859 notional=$25.0 | checked=2026-06-26T21:51:49Z
  - TOS-20260514T154543-EQIX-SELL | EQIX sell | status=filled fill=$1078.442 qty=0.023181589 notional=$25.0 | checked=2026-06-26T21:51:49Z
  - TOS-20260514T154817-EQIX-BUY | EQIX buy | status=filled fill=$1078.41 qty=0.023182277 notional=$25.0 | checked=2026-06-26T21:51:49Z
  - TOS-20260514T163113-EQIX-BUY | EQIX buy | status=filled fill=$1076.89 qty=0.023214998 notional=$25.0 | checked=2026-06-26T21:51:49Z
  - TOS-20260514T165232-WMT-BUY | WMT buy | status=filled fill=$132.276 qty=0.18899876 notional=$25.0 | checked=2026-06-26T21:51:49Z
  - TOS-20260514T171739-JNJ-BUY | JNJ buy | status=filled fill=$230.044 qty=0.108674862 notional=$25.0 | checked=2026-06-26T21:51:49Z
  - TOS-20260514T171844-WMT-BUY | WMT buy | status=filled fill=$132.474 qty=0.188716276 notional=$25.0 | checked=2026-06-26T21:51:49Z
  - TOS-20260514T172103-EQIX-BUY | EQIX buy | status=filled fill=$1076.82 qty=0.023216507 notional=$25.0 | checked=2026-06-26T21:51:49Z
  - TOS-20260514T172226-EQIX-SELL | EQIX sell | status=filled fill=$1076.718 qty=0.023218707 notional=$25.0 | checked=2026-06-26T21:51:49Z
  - TOS-20260514T172335-EQIX-BUY | EQIX buy | status=filled fill=$1076.542 qty=0.023222503 notional=$25.0 | checked=2026-06-26T21:51:49Z

### External Alerts
- Ingested this period: 0 (all-time: 23)
- Routes this period: 0 (all-time: 5)
- Execution called (ever): NO
- Approved plan created (ever): NO

### Risk State
- Equity: $99,806.31 | Peak: $99,806.35 | Drawdown: 0.00% | Positions: 4
- Last updated: 2026-06-26T21:51:47Z

### Operational Issues (0)
None identified.

### Research Observations
- No paper executions this period.
- 14 order fill(s) confirmed by order monitor.

---
## Weekly Review — 2026-06-27 to 2026-07-03 (7 days)

**Generated:** 2026-07-03T22:32:19Z  **Run ID:** weekly_review-2026-07-03

### Trigger Scans
- Total runs: 0 | Risk-on: 0 | Risk-off: 0
- Avg candidates: 0.0 | Avg excluded: 0.0

### Dry Runs
- Total: 0 | Pass: 0 | Fail: 0

### Paper Executions
- Attempts: 0 | Orders submitted: 0

### Order Lifecycle
- Monitor runs: 10 | Unique orders: 14
- Fills: 14 | Partial: 0 | Missing: 0 | Expired: 0 | Rejected: 0 | Canceled: 0
- Latest lifecycle by order (14):
  - TOS-20260513T160035-WELL-BUY | WELL buy | status=filled fill=$218.808 qty=0.11425542 notional=$25.0 | checked=2026-07-03T21:44:37Z
  - TOS-20260513T192526-JNJ-BUY | JNJ buy | status=filled fill=$230.248 qty=0.108578576 notional=$25.0 | checked=2026-07-03T21:44:37Z
  - TOS-20260513T192934-EQIX-BUY | EQIX buy | status=filled fill=$1084.37 qty=0.023054861 notional=$25.0 | checked=2026-07-03T21:44:37Z
  - TOS-20260514T145625-EQIX-BUY | EQIX buy | status=filled fill=$1079.5 qty=0.023158869 notional=$25.0 | checked=2026-07-03T21:44:37Z
  - TOS-20260514T154323-JNJ-BUY | JNJ buy | status=filled fill=$230.116 qty=0.108640859 notional=$25.0 | checked=2026-07-03T21:44:37Z
  - TOS-20260514T154543-EQIX-SELL | EQIX sell | status=filled fill=$1078.442 qty=0.023181589 notional=$25.0 | checked=2026-07-03T21:44:37Z
  - TOS-20260514T154817-EQIX-BUY | EQIX buy | status=filled fill=$1078.41 qty=0.023182277 notional=$25.0 | checked=2026-07-03T21:44:37Z
  - TOS-20260514T163113-EQIX-BUY | EQIX buy | status=filled fill=$1076.89 qty=0.023214998 notional=$25.0 | checked=2026-07-03T21:44:37Z
  - TOS-20260514T165232-WMT-BUY | WMT buy | status=filled fill=$132.276 qty=0.18899876 notional=$25.0 | checked=2026-07-03T21:44:37Z
  - TOS-20260514T171739-JNJ-BUY | JNJ buy | status=filled fill=$230.044 qty=0.108674862 notional=$25.0 | checked=2026-07-03T21:44:37Z
  - TOS-20260514T171844-WMT-BUY | WMT buy | status=filled fill=$132.474 qty=0.188716276 notional=$25.0 | checked=2026-07-03T21:44:37Z
  - TOS-20260514T172103-EQIX-BUY | EQIX buy | status=filled fill=$1076.82 qty=0.023216507 notional=$25.0 | checked=2026-07-03T21:44:37Z
  - TOS-20260514T172226-EQIX-SELL | EQIX sell | status=filled fill=$1076.718 qty=0.023218707 notional=$25.0 | checked=2026-07-03T21:44:37Z
  - TOS-20260514T172335-EQIX-BUY | EQIX buy | status=filled fill=$1076.542 qty=0.023222503 notional=$25.0 | checked=2026-07-03T21:44:37Z

### External Alerts
- Ingested this period: 0 (all-time: 23)
- Routes this period: 0 (all-time: 5)
- Execution called (ever): NO
- Approved plan created (ever): NO

### Risk State
- Equity: $99,800.52 | Peak: $99,806.81 | Drawdown: -0.01% | Positions: 4
- Last updated: 2026-07-03T21:44:34Z

### Operational Issues (0)
None identified.

### Research Observations
- No paper executions this period.
- 14 order fill(s) confirmed by order monitor.

---
## Weekly Review — 2026-07-04 to 2026-07-10 (7 days)

**Generated:** 2026-07-10T22:31:29Z  **Run ID:** weekly_review-2026-07-10

### Trigger Scans
- Total runs: 0 | Risk-on: 0 | Risk-off: 0
- Avg candidates: 0.0 | Avg excluded: 0.0

### Dry Runs
- Total: 0 | Pass: 0 | Fail: 0

### Paper Executions
- Attempts: 0 | Orders submitted: 0

### Order Lifecycle
- Monitor runs: 10 | Unique orders: 14
- Fills: 14 | Partial: 0 | Missing: 0 | Expired: 0 | Rejected: 0 | Canceled: 0
- Latest lifecycle by order (14):
  - TOS-20260513T160035-WELL-BUY | WELL buy | status=filled fill=$218.808 qty=0.11425542 notional=$25.0 | checked=2026-07-10T21:40:48Z
  - TOS-20260513T192526-JNJ-BUY | JNJ buy | status=filled fill=$230.248 qty=0.108578576 notional=$25.0 | checked=2026-07-10T21:40:48Z
  - TOS-20260513T192934-EQIX-BUY | EQIX buy | status=filled fill=$1084.37 qty=0.023054861 notional=$25.0 | checked=2026-07-10T21:40:48Z
  - TOS-20260514T145625-EQIX-BUY | EQIX buy | status=filled fill=$1079.5 qty=0.023158869 notional=$25.0 | checked=2026-07-10T21:40:48Z
  - TOS-20260514T154323-JNJ-BUY | JNJ buy | status=filled fill=$230.116 qty=0.108640859 notional=$25.0 | checked=2026-07-10T21:40:48Z
  - TOS-20260514T154543-EQIX-SELL | EQIX sell | status=filled fill=$1078.442 qty=0.023181589 notional=$25.0 | checked=2026-07-10T21:40:48Z
  - TOS-20260514T154817-EQIX-BUY | EQIX buy | status=filled fill=$1078.41 qty=0.023182277 notional=$25.0 | checked=2026-07-10T21:40:48Z
  - TOS-20260514T163113-EQIX-BUY | EQIX buy | status=filled fill=$1076.89 qty=0.023214998 notional=$25.0 | checked=2026-07-10T21:40:48Z
  - TOS-20260514T165232-WMT-BUY | WMT buy | status=filled fill=$132.276 qty=0.18899876 notional=$25.0 | checked=2026-07-10T21:40:48Z
  - TOS-20260514T171739-JNJ-BUY | JNJ buy | status=filled fill=$230.044 qty=0.108674862 notional=$25.0 | checked=2026-07-10T21:40:48Z
  - TOS-20260514T171844-WMT-BUY | WMT buy | status=filled fill=$132.474 qty=0.188716276 notional=$25.0 | checked=2026-07-10T21:40:48Z
  - TOS-20260514T172103-EQIX-BUY | EQIX buy | status=filled fill=$1076.82 qty=0.023216507 notional=$25.0 | checked=2026-07-10T21:40:48Z
  - TOS-20260514T172226-EQIX-SELL | EQIX sell | status=filled fill=$1076.718 qty=0.023218707 notional=$25.0 | checked=2026-07-10T21:40:48Z
  - TOS-20260514T172335-EQIX-BUY | EQIX buy | status=filled fill=$1076.542 qty=0.023222503 notional=$25.0 | checked=2026-07-10T21:40:48Z

### External Alerts
- Ingested this period: 0 (all-time: 23)
- Routes this period: 0 (all-time: 5)
- Execution called (ever): NO
- Approved plan created (ever): NO

### Risk State
- Equity: $99,803.41 | Peak: $99,806.81 | Drawdown: -0.00% | Positions: 4
- Last updated: 2026-07-10T21:40:46Z

### Operational Issues (0)
None identified.

### Research Observations
- No paper executions this period.
- 14 order fill(s) confirmed by order monitor.

---
## Weekly Review — 2026-07-11 to 2026-07-17 (7 days)

**Generated:** 2026-07-17T22:13:41Z  **Run ID:** weekly_review-2026-07-17

### Trigger Scans
- Total runs: 0 | Risk-on: 0 | Risk-off: 0
- Avg candidates: 0.0 | Avg excluded: 0.0

### Dry Runs
- Total: 0 | Pass: 0 | Fail: 0

### Paper Executions
- Attempts: 0 | Orders submitted: 0

### Order Lifecycle
- Monitor runs: 10 | Unique orders: 14
- Fills: 14 | Partial: 0 | Missing: 0 | Expired: 0 | Rejected: 0 | Canceled: 0
- Latest lifecycle by order (14):
  - TOS-20260513T160035-WELL-BUY | WELL buy | status=filled fill=$218.808 qty=0.11425542 notional=$25.0 | checked=2026-07-17T21:32:14Z
  - TOS-20260513T192526-JNJ-BUY | JNJ buy | status=filled fill=$230.248 qty=0.108578576 notional=$25.0 | checked=2026-07-17T21:32:14Z
  - TOS-20260513T192934-EQIX-BUY | EQIX buy | status=filled fill=$1084.37 qty=0.023054861 notional=$25.0 | checked=2026-07-17T21:32:14Z
  - TOS-20260514T145625-EQIX-BUY | EQIX buy | status=filled fill=$1079.5 qty=0.023158869 notional=$25.0 | checked=2026-07-17T21:32:14Z
  - TOS-20260514T154323-JNJ-BUY | JNJ buy | status=filled fill=$230.116 qty=0.108640859 notional=$25.0 | checked=2026-07-17T21:32:14Z
  - TOS-20260514T154543-EQIX-SELL | EQIX sell | status=filled fill=$1078.442 qty=0.023181589 notional=$25.0 | checked=2026-07-17T21:32:14Z
  - TOS-20260514T154817-EQIX-BUY | EQIX buy | status=filled fill=$1078.41 qty=0.023182277 notional=$25.0 | checked=2026-07-17T21:32:14Z
  - TOS-20260514T163113-EQIX-BUY | EQIX buy | status=filled fill=$1076.89 qty=0.023214998 notional=$25.0 | checked=2026-07-17T21:32:14Z
  - TOS-20260514T165232-WMT-BUY | WMT buy | status=filled fill=$132.276 qty=0.18899876 notional=$25.0 | checked=2026-07-17T21:32:14Z
  - TOS-20260514T171739-JNJ-BUY | JNJ buy | status=filled fill=$230.044 qty=0.108674862 notional=$25.0 | checked=2026-07-17T21:32:14Z
  - TOS-20260514T171844-WMT-BUY | WMT buy | status=filled fill=$132.474 qty=0.188716276 notional=$25.0 | checked=2026-07-17T21:32:14Z
  - TOS-20260514T172103-EQIX-BUY | EQIX buy | status=filled fill=$1076.82 qty=0.023216507 notional=$25.0 | checked=2026-07-17T21:32:14Z
  - TOS-20260514T172226-EQIX-SELL | EQIX sell | status=filled fill=$1076.718 qty=0.023218707 notional=$25.0 | checked=2026-07-17T21:32:14Z
  - TOS-20260514T172335-EQIX-BUY | EQIX buy | status=filled fill=$1076.542 qty=0.023222503 notional=$25.0 | checked=2026-07-17T21:32:14Z

### External Alerts
- Ingested this period: 0 (all-time: 23)
- Routes this period: 0 (all-time: 5)
- Execution called (ever): NO
- Approved plan created (ever): NO

### Risk State
- Equity: $99,800.48 | Peak: $99,806.81 | Drawdown: -0.01% | Positions: 4
- Last updated: 2026-07-17T21:32:13Z

### Operational Issues (0)
None identified.

### Research Observations
- No paper executions this period.
- 14 order fill(s) confirmed by order monitor.

---
## Weekly Review — 2026-07-18 to 2026-07-24 (7 days)

**Generated:** 2026-07-24T22:33:51Z  **Run ID:** weekly_review-2026-07-24

### Trigger Scans
- Total runs: 0 | Risk-on: 0 | Risk-off: 0
- Avg candidates: 0.0 | Avg excluded: 0.0

### Dry Runs
- Total: 0 | Pass: 0 | Fail: 0

### Paper Executions
- Attempts: 0 | Orders submitted: 0

### Order Lifecycle
- Monitor runs: 10 | Unique orders: 14
- Fills: 14 | Partial: 0 | Missing: 0 | Expired: 0 | Rejected: 0 | Canceled: 0
- Latest lifecycle by order (14):
  - TOS-20260513T160035-WELL-BUY | WELL buy | status=filled fill=$218.808 qty=0.11425542 notional=$25.0 | checked=2026-07-24T21:44:40Z
  - TOS-20260513T192526-JNJ-BUY | JNJ buy | status=filled fill=$230.248 qty=0.108578576 notional=$25.0 | checked=2026-07-24T21:44:40Z
  - TOS-20260513T192934-EQIX-BUY | EQIX buy | status=filled fill=$1084.37 qty=0.023054861 notional=$25.0 | checked=2026-07-24T21:44:40Z
  - TOS-20260514T145625-EQIX-BUY | EQIX buy | status=filled fill=$1079.5 qty=0.023158869 notional=$25.0 | checked=2026-07-24T21:44:40Z
  - TOS-20260514T154323-JNJ-BUY | JNJ buy | status=filled fill=$230.116 qty=0.108640859 notional=$25.0 | checked=2026-07-24T21:44:40Z
  - TOS-20260514T154543-EQIX-SELL | EQIX sell | status=filled fill=$1078.442 qty=0.023181589 notional=$25.0 | checked=2026-07-24T21:44:40Z
  - TOS-20260514T154817-EQIX-BUY | EQIX buy | status=filled fill=$1078.41 qty=0.023182277 notional=$25.0 | checked=2026-07-24T21:44:40Z
  - TOS-20260514T163113-EQIX-BUY | EQIX buy | status=filled fill=$1076.89 qty=0.023214998 notional=$25.0 | checked=2026-07-24T21:44:40Z
  - TOS-20260514T165232-WMT-BUY | WMT buy | status=filled fill=$132.276 qty=0.18899876 notional=$25.0 | checked=2026-07-24T21:44:40Z
  - TOS-20260514T171739-JNJ-BUY | JNJ buy | status=filled fill=$230.044 qty=0.108674862 notional=$25.0 | checked=2026-07-24T21:44:40Z
  - TOS-20260514T171844-WMT-BUY | WMT buy | status=filled fill=$132.474 qty=0.188716276 notional=$25.0 | checked=2026-07-24T21:44:40Z
  - TOS-20260514T172103-EQIX-BUY | EQIX buy | status=filled fill=$1076.82 qty=0.023216507 notional=$25.0 | checked=2026-07-24T21:44:40Z
  - TOS-20260514T172226-EQIX-SELL | EQIX sell | status=filled fill=$1076.718 qty=0.023218707 notional=$25.0 | checked=2026-07-24T21:44:40Z
  - TOS-20260514T172335-EQIX-BUY | EQIX buy | status=filled fill=$1076.542 qty=0.023222503 notional=$25.0 | checked=2026-07-24T21:44:40Z

### External Alerts
- Ingested this period: 0 (all-time: 23)
- Routes this period: 0 (all-time: 5)
- Execution called (ever): NO
- Approved plan created (ever): NO

### Risk State
- Equity: $99,809.09 | Peak: $99,809.69 | Drawdown: -0.00% | Positions: 4
- Last updated: 2026-07-24T21:44:38Z

### Operational Issues (0)
None identified.

### Research Observations
- No paper executions this period.
- 14 order fill(s) confirmed by order monitor.

---
## Weekly Review — 2026-07-25 to 2026-07-31 (7 days)

**Generated:** 2026-07-31T22:32:08Z  **Run ID:** weekly_review-2026-07-31

### Trigger Scans
- Total runs: 0 | Risk-on: 0 | Risk-off: 0
- Avg candidates: 0.0 | Avg excluded: 0.0

### Dry Runs
- Total: 0 | Pass: 0 | Fail: 0

### Paper Executions
- Attempts: 0 | Orders submitted: 0

### Order Lifecycle
- Monitor runs: 10 | Unique orders: 14
- Fills: 14 | Partial: 0 | Missing: 0 | Expired: 0 | Rejected: 0 | Canceled: 0
- Latest lifecycle by order (14):
  - TOS-20260513T160035-WELL-BUY | WELL buy | status=filled fill=$218.808 qty=0.11425542 notional=$25.0 | checked=2026-07-31T21:45:41Z
  - TOS-20260513T192526-JNJ-BUY | JNJ buy | status=filled fill=$230.248 qty=0.108578576 notional=$25.0 | checked=2026-07-31T21:45:41Z
  - TOS-20260513T192934-EQIX-BUY | EQIX buy | status=filled fill=$1084.37 qty=0.023054861 notional=$25.0 | checked=2026-07-31T21:45:41Z
  - TOS-20260514T145625-EQIX-BUY | EQIX buy | status=filled fill=$1079.5 qty=0.023158869 notional=$25.0 | checked=2026-07-31T21:45:41Z
  - TOS-20260514T154323-JNJ-BUY | JNJ buy | status=filled fill=$230.116 qty=0.108640859 notional=$25.0 | checked=2026-07-31T21:45:41Z
  - TOS-20260514T154543-EQIX-SELL | EQIX sell | status=filled fill=$1078.442 qty=0.023181589 notional=$25.0 | checked=2026-07-31T21:45:41Z
  - TOS-20260514T154817-EQIX-BUY | EQIX buy | status=filled fill=$1078.41 qty=0.023182277 notional=$25.0 | checked=2026-07-31T21:45:41Z
  - TOS-20260514T163113-EQIX-BUY | EQIX buy | status=filled fill=$1076.89 qty=0.023214998 notional=$25.0 | checked=2026-07-31T21:45:41Z
  - TOS-20260514T165232-WMT-BUY | WMT buy | status=filled fill=$132.276 qty=0.18899876 notional=$25.0 | checked=2026-07-31T21:45:41Z
  - TOS-20260514T171739-JNJ-BUY | JNJ buy | status=filled fill=$230.044 qty=0.108674862 notional=$25.0 | checked=2026-07-31T21:45:41Z
  - TOS-20260514T171844-WMT-BUY | WMT buy | status=filled fill=$132.474 qty=0.188716276 notional=$25.0 | checked=2026-07-31T21:45:41Z
  - TOS-20260514T172103-EQIX-BUY | EQIX buy | status=filled fill=$1076.82 qty=0.023216507 notional=$25.0 | checked=2026-07-31T21:45:41Z
  - TOS-20260514T172226-EQIX-SELL | EQIX sell | status=filled fill=$1076.718 qty=0.023218707 notional=$25.0 | checked=2026-07-31T21:45:41Z
  - TOS-20260514T172335-EQIX-BUY | EQIX buy | status=filled fill=$1076.542 qty=0.023222503 notional=$25.0 | checked=2026-07-31T21:45:41Z

### External Alerts
- Ingested this period: 0 (all-time: 23)
- Routes this period: 0 (all-time: 5)
- Execution called (ever): NO
- Approved plan created (ever): NO

### Risk State
- Equity: $99,799.75 | Peak: $99,809.69 | Drawdown: -0.01% | Positions: 4
- Last updated: 2026-07-31T21:45:40Z

### Operational Issues (0)
None identified.

### Research Observations
- No paper executions this period.
- 14 order fill(s) confirmed by order monitor.

---
## Weekly Review — 2026-08-01 to 2026-08-07 (7 days)

**Generated:** 2026-08-07T22:05:11Z  **Run ID:** weekly_review-2026-08-07

### Trigger Scans
- Total runs: 0 | Risk-on: 0 | Risk-off: 0
- Avg candidates: 0.0 | Avg excluded: 0.0

### Dry Runs
- Total: 0 | Pass: 0 | Fail: 0

### Paper Executions
- Attempts: 0 | Orders submitted: 0

### Order Lifecycle
- Monitor runs: 10 | Unique orders: 14
- Fills: 14 | Partial: 0 | Missing: 0 | Expired: 0 | Rejected: 0 | Canceled: 0
- Latest lifecycle by order (14):
  - TOS-20260513T160035-WELL-BUY | WELL buy | status=filled fill=$218.808 qty=0.11425542 notional=$25.0 | checked=2026-08-07T21:21:38Z
  - TOS-20260513T192526-JNJ-BUY | JNJ buy | status=filled fill=$230.248 qty=0.108578576 notional=$25.0 | checked=2026-08-07T21:21:38Z
  - TOS-20260513T192934-EQIX-BUY | EQIX buy | status=filled fill=$1084.37 qty=0.023054861 notional=$25.0 | checked=2026-08-07T21:21:38Z
  - TOS-20260514T145625-EQIX-BUY | EQIX buy | status=filled fill=$1079.5 qty=0.023158869 notional=$25.0 | checked=2026-08-07T21:21:38Z
  - TOS-20260514T154323-JNJ-BUY | JNJ buy | status=filled fill=$230.116 qty=0.108640859 notional=$25.0 | checked=2026-08-07T21:21:38Z
  - TOS-20260514T154543-EQIX-SELL | EQIX sell | status=filled fill=$1078.442 qty=0.023181589 notional=$25.0 | checked=2026-08-07T21:21:38Z
  - TOS-20260514T154817-EQIX-BUY | EQIX buy | status=filled fill=$1078.41 qty=0.023182277 notional=$25.0 | checked=2026-08-07T21:21:38Z
  - TOS-20260514T163113-EQIX-BUY | EQIX buy | status=filled fill=$1076.89 qty=0.023214998 notional=$25.0 | checked=2026-08-07T21:21:38Z
  - TOS-20260514T165232-WMT-BUY | WMT buy | status=filled fill=$132.276 qty=0.18899876 notional=$25.0 | checked=2026-08-07T21:21:38Z
  - TOS-20260514T171739-JNJ-BUY | JNJ buy | status=filled fill=$230.044 qty=0.108674862 notional=$25.0 | checked=2026-08-07T21:21:38Z
  - TOS-20260514T171844-WMT-BUY | WMT buy | status=filled fill=$132.474 qty=0.188716276 notional=$25.0 | checked=2026-08-07T21:21:38Z
  - TOS-20260514T172103-EQIX-BUY | EQIX buy | status=filled fill=$1076.82 qty=0.023216507 notional=$25.0 | checked=2026-08-07T21:21:38Z
  - TOS-20260514T172226-EQIX-SELL | EQIX sell | status=filled fill=$1076.718 qty=0.023218707 notional=$25.0 | checked=2026-08-07T21:21:38Z
  - TOS-20260514T172335-EQIX-BUY | EQIX buy | status=filled fill=$1076.542 qty=0.023222503 notional=$25.0 | checked=2026-08-07T21:21:38Z

### External Alerts
- Ingested this period: 0 (all-time: 23)
- Routes this period: 0 (all-time: 5)
- Execution called (ever): NO
- Approved plan created (ever): NO

### Risk State
- Equity: $99,802.96 | Peak: $99,809.69 | Drawdown: -0.01% | Positions: 4
- Last updated: 2026-08-07T21:21:37Z

### Operational Issues (0)
None identified.

### Research Observations
- No paper executions this period.
- 14 order fill(s) confirmed by order monitor.

---
## Weekly Review — 2026-08-08 to 2026-08-14 (7 days)

**Generated:** 2026-08-14T21:48:57Z  **Run ID:** weekly_review-2026-08-14

### Trigger Scans
- Total runs: 0 | Risk-on: 0 | Risk-off: 0
- Avg candidates: 0.0 | Avg excluded: 0.0

### Dry Runs
- Total: 0 | Pass: 0 | Fail: 0

### Paper Executions
- Attempts: 0 | Orders submitted: 0

### Order Lifecycle
- Monitor runs: 9 | Unique orders: 14
- Fills: 14 | Partial: 0 | Missing: 0 | Expired: 0 | Rejected: 0 | Canceled: 0
- Latest lifecycle by order (14):
  - TOS-20260513T160035-WELL-BUY | WELL buy | status=filled fill=$218.808 qty=0.11425542 notional=$25.0 | checked=2026-08-14T21:01:59Z
  - TOS-20260513T192526-JNJ-BUY | JNJ buy | status=filled fill=$230.248 qty=0.108578576 notional=$25.0 | checked=2026-08-14T21:01:59Z
  - TOS-20260513T192934-EQIX-BUY | EQIX buy | status=filled fill=$1084.37 qty=0.023054861 notional=$25.0 | checked=2026-08-14T21:01:59Z
  - TOS-20260514T145625-EQIX-BUY | EQIX buy | status=filled fill=$1079.5 qty=0.023158869 notional=$25.0 | checked=2026-08-14T21:01:59Z
  - TOS-20260514T154323-JNJ-BUY | JNJ buy | status=filled fill=$230.116 qty=0.108640859 notional=$25.0 | checked=2026-08-14T21:01:59Z
  - TOS-20260514T154543-EQIX-SELL | EQIX sell | status=filled fill=$1078.442 qty=0.023181589 notional=$25.0 | checked=2026-08-14T21:01:59Z
  - TOS-20260514T154817-EQIX-BUY | EQIX buy | status=filled fill=$1078.41 qty=0.023182277 notional=$25.0 | checked=2026-08-14T21:01:59Z
  - TOS-20260514T163113-EQIX-BUY | EQIX buy | status=filled fill=$1076.89 qty=0.023214998 notional=$25.0 | checked=2026-08-14T21:01:59Z
  - TOS-20260514T165232-WMT-BUY | WMT buy | status=filled fill=$132.276 qty=0.18899876 notional=$25.0 | checked=2026-08-14T21:01:59Z
  - TOS-20260514T171739-JNJ-BUY | JNJ buy | status=filled fill=$230.044 qty=0.108674862 notional=$25.0 | checked=2026-08-14T21:01:59Z
  - TOS-20260514T171844-WMT-BUY | WMT buy | status=filled fill=$132.474 qty=0.188716276 notional=$25.0 | checked=2026-08-14T21:01:59Z
  - TOS-20260514T172103-EQIX-BUY | EQIX buy | status=filled fill=$1076.82 qty=0.023216507 notional=$25.0 | checked=2026-08-14T21:01:59Z
  - TOS-20260514T172226-EQIX-SELL | EQIX sell | status=filled fill=$1076.718 qty=0.023218707 notional=$25.0 | checked=2026-08-14T21:01:59Z
  - TOS-20260514T172335-EQIX-BUY | EQIX buy | status=filled fill=$1076.542 qty=0.023222503 notional=$25.0 | checked=2026-08-14T21:01:59Z

### External Alerts
- Ingested this period: 0 (all-time: 23)
- Routes this period: 0 (all-time: 5)
- Execution called (ever): NO
- Approved plan created (ever): NO

### Risk State
- Equity: $99,810.20 | Peak: $99,810.20 | Drawdown: 0.00% | Positions: 4
- Last updated: 2026-08-14T21:01:57Z

### Operational Issues (0)
None identified.

### Research Observations
- No paper executions this period.
- 14 order fill(s) confirmed by order monitor.

---
## Weekly Review — 2026-08-15 to 2026-08-21 (7 days)

**Generated:** 2026-08-21T21:48:16Z  **Run ID:** weekly_review-2026-08-21

### Trigger Scans
- Total runs: 0 | Risk-on: 0 | Risk-off: 0
- Avg candidates: 0.0 | Avg excluded: 0.0

### Dry Runs
- Total: 0 | Pass: 0 | Fail: 0

### Paper Executions
- Attempts: 0 | Orders submitted: 0

### Order Lifecycle
- Monitor runs: 10 | Unique orders: 14
- Fills: 14 | Partial: 0 | Missing: 0 | Expired: 0 | Rejected: 0 | Canceled: 0
- Latest lifecycle by order (14):
  - TOS-20260513T160035-WELL-BUY | WELL buy | status=filled fill=$218.808 qty=0.11425542 notional=$25.0 | checked=2026-08-21T20:59:35Z
  - TOS-20260513T192526-JNJ-BUY | JNJ buy | status=filled fill=$230.248 qty=0.108578576 notional=$25.0 | checked=2026-08-21T20:59:35Z
  - TOS-20260513T192934-EQIX-BUY | EQIX buy | status=filled fill=$1084.37 qty=0.023054861 notional=$25.0 | checked=2026-08-21T20:59:35Z
  - TOS-20260514T145625-EQIX-BUY | EQIX buy | status=filled fill=$1079.5 qty=0.023158869 notional=$25.0 | checked=2026-08-21T20:59:35Z
  - TOS-20260514T154323-JNJ-BUY | JNJ buy | status=filled fill=$230.116 qty=0.108640859 notional=$25.0 | checked=2026-08-21T20:59:35Z
  - TOS-20260514T154543-EQIX-SELL | EQIX sell | status=filled fill=$1078.442 qty=0.023181589 notional=$25.0 | checked=2026-08-21T20:59:35Z
  - TOS-20260514T154817-EQIX-BUY | EQIX buy | status=filled fill=$1078.41 qty=0.023182277 notional=$25.0 | checked=2026-08-21T20:59:35Z
  - TOS-20260514T163113-EQIX-BUY | EQIX buy | status=filled fill=$1076.89 qty=0.023214998 notional=$25.0 | checked=2026-08-21T20:59:35Z
  - TOS-20260514T165232-WMT-BUY | WMT buy | status=filled fill=$132.276 qty=0.18899876 notional=$25.0 | checked=2026-08-21T20:59:35Z
  - TOS-20260514T171739-JNJ-BUY | JNJ buy | status=filled fill=$230.044 qty=0.108674862 notional=$25.0 | checked=2026-08-21T20:59:35Z
  - TOS-20260514T171844-WMT-BUY | WMT buy | status=filled fill=$132.474 qty=0.188716276 notional=$25.0 | checked=2026-08-21T20:59:35Z
  - TOS-20260514T172103-EQIX-BUY | EQIX buy | status=filled fill=$1076.82 qty=0.023216507 notional=$25.0 | checked=2026-08-21T20:59:35Z
  - TOS-20260514T172226-EQIX-SELL | EQIX sell | status=filled fill=$1076.718 qty=0.023218707 notional=$25.0 | checked=2026-08-21T20:59:35Z
  - TOS-20260514T172335-EQIX-BUY | EQIX buy | status=filled fill=$1076.542 qty=0.023222503 notional=$25.0 | checked=2026-08-21T20:59:35Z

### External Alerts
- Ingested this period: 0 (all-time: 23)
- Routes this period: 0 (all-time: 5)
- Execution called (ever): NO
- Approved plan created (ever): NO

### Risk State
- Equity: $99,804.19 | Peak: $99,813.01 | Drawdown: -0.01% | Positions: 4
- Last updated: 2026-08-21T20:59:33Z

### Operational Issues (0)
None identified.

### Research Observations
- No paper executions this period.
- 14 order fill(s) confirmed by order monitor.

---
