# Alert Router — Design & Operations Guide

## Overview

`scripts/route_alert.py` reads a previously ingested external alert (stored by
`scripts/ingest_alert.py`) and routes it to the appropriate safe research action based
on the alert's `next_step` value.

**This layer is research-only.**  It never places orders, never calls
`execute_paper.py`, never passes `--approve-paper` to `generate_trade_plan.py`, and
never generates an approved trade plan.  Human review is always required before any
paper order can reach execution.

---

## Hard constraints

| Constraint | Detail |
|---|---|
| `ENABLE_PAPER_EXECUTION` | **Always `false`** — hardcoded in workflow, checked at runtime. |
| `LIVE_TRADING_CONFIRMED` | **Must not be `true`** — router refuses to run if set. |
| Order placement | **Never.** No connection to `execute_paper.py` or `paper_executor.py`. |
| `--approve-paper` | **Never passed** to `generate_trade_plan.py`. |
| `approved_for_execution` | **Verified `false`** in trade plan after `run_unapproved_plan`. |
| Crypto / options | **Rejected** at router level (same as intake). |
| Execution intent fields | **Rejected**: `execute`, `execute_paper`, `submit_order`, `order`, `approved_for_execution=true`. |
| Secrets | **Never printed or logged.** |

---

## `route_mode` values

| `route_mode` | What happens |
|---|---|
| `record_only` | Write route record and logs. No scripts invoked. Default. |
| `run_refresh` | Also invoke `refresh_data.py` + `monitor_positions.py`. |
| `run_unapproved_plan` | Also invoke full pipeline: `refresh_data.py`, `monitor_positions.py`, `scan_triggers.py`, `generate_trade_plan.py` (no `--approve-paper`). |

### Compatibility matrix

| `next_step` | `record_only` | `run_refresh` | `run_unapproved_plan` |
|---|:---:|:---:|:---:|
| `log_only` | ✓ | ✗ | ✗ |
| `request_alert_review` | ✓ | ✗ | ✗ |
| `request_data_refresh` | ✓ | ✓ | ✗ |
| `request_trade_plan_unapproved` | ✓ | ✓ | ✓ |

An incompatible combination fails closed with exit code 1 before any artifact is written.

---

## Output: route record

Every routing call writes a JSON record to:

```
data/history/alerts/routes/<route_id>.json
```

The `route_id` is stable and human-readable:
`route_<UTC_compact>_<safe_alert_id>_<hash8>`.

### Route record schema

```json
{
  "route_id": "route_20260513T160000_tv_aapl_200dma_a1b2c3d4",
  "routed_at": "2026-05-13T16:00:00Z",
  "alert_id": "tv-aapl-200dma",
  "source": "tradingview",
  "symbol": "AAPL",
  "trigger_id": null,
  "condition": "Close crossed above 200-day SMA",
  "next_step": "request_trade_plan_unapproved",
  "route_mode": "record_only",
  "action_taken": "plan_requested",
  "scripts_run": [],
  "safety_checks": {
    "trade_execution_allowed": false,
    "blocked_by_default": true,
    "execute_paper_called": false,
    "approve_paper_passed": false,
    "enable_paper_execution_checked_false": true,
    "live_trading_confirmed_checked_false": true,
    "no_execution_intent_fields": true,
    "approved_trade_plan_created": false,
    "execution_called": false
  },
  "blocked": false,
  "block_reason": null,
  "generated_files": [],
  "trade_execution_allowed": false,
  "approved_trade_plan_created": false,
  "execution_called": false,
  "suggested_scripts": [
    "python scripts/refresh_data.py",
    "python scripts/monitor_positions.py",
    "python scripts/scan_triggers.py",
    "python scripts/generate_trade_plan.py"
  ],
  "data_hashes": {}
}
```

The `scripts_run` field is updated in-place after the CLI finishes executing
sub-processes.  For `record_only`, it remains `[]`.

---

## Memory log updates

| Log file | Updated when |
|---|---|
| `memory/TRIGGER-LOG.md` | Every routing call |
| `memory/SIGNAL-LOG.md` | `log_only`, `request_alert_review`, `request_trade_plan_unapproved` |
| `memory/RESEARCH-CONTEXT.md` | `request_alert_review` only |

---

## CLI usage

### Locate by alert_id

```bash
python scripts/route_alert.py --alert-id tv-20260512-aapl-200dma --route-mode record_only
```

### Locate most-recent alert

```bash
python scripts/route_alert.py --latest --route-mode record_only
```

### With data refresh (request_data_refresh or request_trade_plan_unapproved)

```bash
python scripts/route_alert.py --alert-id <id> --route-mode run_refresh
```

Runs `refresh_data.py` and `monitor_positions.py`.  Does **not** generate a trade plan.

### With full pipeline (request_trade_plan_unapproved only)

```bash
python scripts/route_alert.py --alert-id <id> --route-mode run_unapproved_plan
```

Runs `refresh_data.py`, `monitor_positions.py`, `scan_triggers.py`,
`generate_trade_plan.py` — all without `--approve-paper`.

After the pipeline, the router reads `data/latest/trade_plan.json` and fails (exit 1)
if `approval.approved_for_execution` is `true`.

### Dry-run (validates only, writes nothing)

```bash
python scripts/route_alert.py --latest --route-mode record_only --dry-run
```

### Locate by file path (backward-compat)

```bash
python scripts/route_alert.py --alert-file data/history/alerts/alert-foo.json --route-mode record_only
```

---

## Exit codes

| Code | Meaning |
|---|---|
| `0` | Routed successfully; all applicable scripts passed. |
| `1` | Safety violation, missing file, incompatible `route_mode`, pipeline failure, or trade plan approval check failed. |

---

## Two-step workflow (intake → route)

```bash
# Step 1: ingest the alert
python scripts/ingest_alert.py --payload '{"symbol":"AAPL","next_step":"request_alert_review"}'

# Step 2: route it
python scripts/route_alert.py --latest --route-mode record_only
```

---

## GitHub Actions workflow

`alert-router.yml` is `workflow_dispatch`-only.

### Inputs

| Input | Type | Default | Description |
|---|---|---|---|
| `alert_id` | string | `""` | Alert ID to route; leave blank to route `--latest`. |
| `latest` | choice | `false` | Use `--latest` when `alert_id` is blank. |
| `route_mode` | choice | `record_only` | `record_only` / `run_refresh` / `run_unapproved_plan`. |

### Committed outputs

```
data/history/alerts/routes/      route records
memory/TRIGGER-LOG.md            updated every run
memory/SIGNAL-LOG.md             updated for log_only, review, plan requests
memory/RESEARCH-CONTEXT.md       updated for request_alert_review
data/latest/                     updated only when refresh or plan pipeline ran
```

---

## Safety architecture

```
TradingView alert
    │
    ▼
ingest_alert.py  →  data/history/alerts/alert-<id>.json
    │               (trade_execution_allowed=false  blocked_by_default=true)
    │
    ▼
route_alert.py
    ├── validate_alert_safety()   ← rejects execution intent fields, crypto, bad flags
    ├── validate_route_mode()     ← fails closed on incompatible combinations
    │
    ├── record_only  →  writes route record + logs  (no scripts)
    │
    ├── run_refresh  →  refresh_data.py + monitor_positions.py
    │                   (never execute_paper.py)
    │
    └── run_unapproved_plan  →  refresh_data.py + monitor_positions.py
                                + scan_triggers.py + generate_trade_plan.py
                                (never --approve-paper)
                                + check_trade_plan_not_approved()  ← fails if approved
                                 ↓
                              human review required
                                 ↓
                              execute_paper.py  (manual, separate step)
```

No path through `route_alert.py` reaches `execute_paper.py`.

---

## What this layer does NOT do

- Does not submit orders to Alpaca.
- Does not call `execute_paper.py`.
- Does not set `approved_for_execution=true` anywhere.
- Does not pass `--approve-paper` to `generate_trade_plan.py`.
- Does not enable live trading.
- Does not support crypto, options, futures, or forex.
- Does not read Alpaca API keys for `record_only` routing.
