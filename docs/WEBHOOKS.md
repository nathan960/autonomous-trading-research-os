# External Alert Intake (Webhooks)

## Overview

This system provides a **research-only** intake path for external scanners such as TradingView Pine Script alerts. Alerts are logged, deduplicated, and stored for human review. They **never** trigger order submission, never generate approved trade plans, and never call `execute_paper.py`.

## Hard constraints — these are non-negotiable

| Constraint | Detail |
|---|---|
| `trade_execution_allowed` | **Always `false`** in every persisted record, regardless of what the sender provides. |
| `blocked_by_default` | **Always `true`** in every persisted record. |
| Order placement | **Never.** This path has no connection to `execute_paper.py`. |
| Approved trade plan | **Never generated.** A human must run `generate_trade_plan.py --approve-paper` manually. |
| Crypto / options / futures / forex | **Rejected at intake.** Only US equity and ETF symbols are accepted. |
| Secrets | **Never printed or logged.** Alpaca keys are not needed and not used. |

## Allowed `next_step` values

External alerts may only request one of these research actions:

| `next_step` | Meaning |
|---|---|
| `log_only` | Record the alert for review; take no further action. |
| `request_data_refresh` | Flag that a data refresh may be warranted. |
| `request_alert_review` | Flag the alert for manual human review. |
| `request_trade_plan_unapproved` | Suggest (but do not approve) a trade plan review. |

Any other `next_step` value is rejected at intake.

## Alert payload schema

### Required fields

| Field | Type | Description |
|---|---|---|
| `symbol` | string | Ticker symbol (e.g. `"AAPL"`). Must be a US equity or ETF. |
| `next_step` | string | One of the four allowed values above. |

### Optional fields

| Field | Type | Description |
|---|---|---|
| `alert_id` | string | Caller-supplied unique ID. Used for deduplication. Generated from payload hash if absent. |
| `source` | string | Alert origin, e.g. `"tradingview"`. |
| `description` | string | Human-readable description of the signal. |
| `price` | number | Price at alert time. |
| `triggered_at` | string | ISO 8601 UTC timestamp of the signal. |
| `asset_class` | string | If present, must be `"us_equity"` or `"etf"`. `"crypto"`, `"options"`, `"futures"`, `"forex"` are rejected. |

### Rejected symbols

- Crypto tickers (BTC, ETH, SOL, etc.)
- Symbols containing `/` or `-` (e.g. `BTC-USD`, `ETH/USDC`)
- OCC-format option symbols (e.g. `AAPL230120C00150000`)

## Example payloads

### Minimal valid alert

```json
{
  "symbol": "AAPL",
  "next_step": "log_only"
}
```

### Full alert with all optional fields

```json
{
  "alert_id": "tv-20260512-aapl-200dma",
  "source": "tradingview",
  "symbol": "AAPL",
  "next_step": "request_alert_review",
  "description": "Close crossed above 200-day SMA",
  "price": 185.50,
  "triggered_at": "2026-05-12T15:00:00Z",
  "asset_class": "us_equity"
}
```

### Alert requesting unapproved trade plan review

```json
{
  "alert_id": "tv-20260512-msft-momentum",
  "source": "tradingview",
  "symbol": "MSFT",
  "next_step": "request_trade_plan_unapproved",
  "description": "6-month momentum score crossed threshold",
  "price": 420.00,
  "triggered_at": "2026-05-12T15:05:00Z"
}
```

## CLI usage

```bash
# Inline payload
python scripts/ingest_alert.py --payload '{"symbol":"AAPL","next_step":"log_only"}'

# From stdin (e.g. piped from curl or another script)
echo '{"symbol":"MSFT","next_step":"request_alert_review"}' | python scripts/ingest_alert.py
```

**Exit codes:**
- `0` — alert ingested successfully
- `1` — validation error, duplicate, JSON parse error, or I/O failure

## Output files

| Path | Description |
|---|---|
| `data/history/alerts/alert-<id>.json` | Persisted alert record (atomic write). Contains forced safety flags. |
| `memory/TRIGGER-LOG.md` | Append-only log entry for every ingested alert. |

## Alert Router

After an alert is ingested, `scripts/route_alert.py` dispatches it based on `next_step`.

### Router safety invariants

- Rejects any alert where `trade_execution_allowed` is not exactly `false`.
- Rejects any alert where `blocked_by_default` is not exactly `true`.
- Never calls `execute_paper.py`.
- Never passes `--approve-paper` to `generate_trade_plan.py`.
- Every routing decision is logged to `memory/TRIGGER-LOG.md`.

### Routing actions

| `next_step` | Action | Artifact written |
|---|---|---|
| `log_only` | Log only; no file written. | — |
| `request_alert_review` | Write review-request record. | `data/history/alerts/review-requests/review-<id>.json` |
| `request_data_refresh` | Write refresh-request record. | `data/history/alerts/refresh-requests/refresh-<id>.json` |
| `request_trade_plan_unapproved` | Write plan-request record with suggested (unapproved) pipeline commands. | `data/history/alerts/plan-requests/plan-request-<id>.json` |

For `request_trade_plan_unapproved`, the artifact includes `suggested_commands` pointing to
`scan_triggers.py` and `generate_trade_plan.py` (no `--approve-paper`). Human approval is
always required before a plan can reach execution.

### Router CLI

```bash
# Route the most recent alert
python scripts/route_alert.py --latest

# Route a specific alert file
python scripts/route_alert.py --alert-file data/history/alerts/alert-foo.json

# For request_trade_plan_unapproved: also invoke the pipeline (no --approve-paper)
python scripts/route_alert.py --latest --run-pipeline

# Validate safety only — no artifacts written
python scripts/route_alert.py --latest --dry-run
```

### Two-step pipeline (intake → route)

```bash
# Step 1: ingest the alert
python scripts/ingest_alert.py --payload '{"symbol":"AAPL","next_step":"request_alert_review"}'

# Step 2: route it
python scripts/route_alert.py --latest
```

## GitHub Actions

### Alert Intake (`alert-intake.yml`)

Runs on `workflow_dispatch` only, with a `payload` input field.

```
workflow_dispatch → ingest_alert.py → data/history/alerts/ + memory/TRIGGER-LOG.md → commit + push
```

`ENABLE_PAPER_EXECUTION` is hardcoded to `false`. No Alpaca secrets are used.

### Alert Router (`alert-router.yml`)

Runs on `workflow_dispatch` only, with `alert_id` and `run_pipeline` inputs.

```
workflow_dispatch → route_alert.py → routing artifact + memory logs → commit + push
```

`ENABLE_PAPER_EXECUTION` is hardcoded to `false`. `--approve-paper` is never passed.

## Connecting TradingView

> **Do not** point TradingView webhooks directly at `execute_paper.py` or any execution endpoint.

1. Create a Pine Script alert with a JSON message body matching the schema above.
2. Send the webhook payload to your relay server or via the GitHub Actions `workflow_dispatch` API.
3. The relay calls `ingest_alert.py --payload '...'`.
4. Review `memory/TRIGGER-LOG.md` and `data/history/alerts/` before any trade plan decision.
5. Optionally run `route_alert.py` to write the appropriate research artifact.

```
TradingView → relay → ingest_alert.py → route_alert.py → human review
  → (optional) generate_trade_plan.py (no --approve-paper) → manual approval → execute_paper.py
```

The last step (manual `execute_paper.py`) is never triggered automatically from an external alert.

## What this layer does NOT do

- Does not submit orders to Alpaca.
- Does not call `execute_paper.py`.
- Does not set `approved_for_execution=true` anywhere.
- Does not read Alpaca API keys (intake and router steps).
- Does not enable live trading.
- Does not support crypto, options, futures, or forex.
