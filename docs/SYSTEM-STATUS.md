# System Status Dashboard

The system status dashboard produces a single `data/latest/system_status.json`
artifact that tells you, at a glance, whether the system is ready for:

- A **research cycle** (data refresh → trigger scan → trade plan generation)
- A **manual paper execution** (order submission via `execute_paper.py`)
- A **scheduled paper execution** (always `false` — system policy requires manual confirmation)

## Running it

```bash
python scripts/system_status.py
```

Or trigger the **System Status** GitHub Actions workflow (manual dispatch or
auto-scheduled at 21:10 UTC on weekdays, after the Research Cycle).

## Status tiers

| Tier | Meaning |
|------|---------|
| **GREEN** | All checks pass. Research and paper execution are both safe (if plan is approved). |
| **YELLOW** | Research is safe but paper execution should wait. Typical causes: market closed (soft gate failure), risk state stale, trade plan missing or not yet approved. |
| **RED** | A hard blocker is present. Neither research nor execution should proceed until it is resolved. |

### RED blockers (hard — always block everything)

- Source integrity failed — a snapshot has `source=mock` or is missing the `source` field. Run `refresh_data.py` to overwrite with live Alpaca data.
- Execution policy violation — `live_trading_allowed=true`, `allow_shorting=true`, `allow_options=true`, `allow_crypto=true`, or `paper_only=false` in config files.
- Drawdown has breached the block threshold (default `max_drawdown_block_pct=-0.10`).
- Open orders exist for symbols that appear in the current trade plan (duplicates).
- Hard execution gate failures: `CANONICAL_SOURCE_INTEGRITY`, `TRADING_MODE_PAPER`, `ALPACA_PAPER_MODE`, `NO_PROHIBITED_ORDERS`, `RISK_LIMITS_RESPECTED`.

### YELLOW warnings (soft — research is safe, paper should wait)

- Market is closed: `MARKET_CLOCK_OPEN`, `QUOTE_FRESHNESS`, `SPREAD_NOT_TOO_WIDE` gate failures are expected off-hours and do not block research.
- Risk state is stale (older than 120 minutes) — run `monitor_positions.py`.
- Risk state is paused — investigate before resuming.
- Drawdown is between warn threshold (`-5%`) and block threshold (`-10%`).
- Data quality status is `WARNING` or `ERROR`.
- Trade plan is missing, expired, stale, or contains non-limit orders.
- Trade plan is currently approved for execution (expected only during an active paper cycle).

## Readiness flags

```json
{
  "overall_status": "GREEN",
  "safe_for_research_cycle": true,
  "safe_for_manual_paper_execution": true,
  "safe_for_scheduled_paper_execution": false
}
```

**`safe_for_research_cycle`** is `true` when:
- Source integrity passes (all canonical snapshots have `source=alpaca_paper`)
- Execution policy passes (no live trading, paper-only)
- Overall status is not RED

**`safe_for_manual_paper_execution`** is `true` when:
- All of the above hold
- All dry-run gates pass
- Trade plan is approved for execution (`approval.approved_for_execution=true`)
- No open orders conflict with planned symbols
- Drawdown is not at the block threshold
- Overall status is GREEN

**`safe_for_scheduled_paper_execution`** is always `false`. Paper execution requires
a human operator to explicitly trigger `manual-paper-cycle.yml` with the three
confirmation inputs. This is a system policy and cannot be changed at runtime.

## Key fields

| Field | Description |
|-------|-------------|
| `overall_status` | `GREEN`, `YELLOW`, or `RED` |
| `blocking_issues` | List of RED-tier problems that must be resolved |
| `warnings` | List of YELLOW-tier issues |
| `required_operator_actions` | Actionable steps to resolve issues |
| `latest_account_equity` | Alpaca paper account equity ($) |
| `cash` | Available cash |
| `buying_power` | Available buying power |
| `position_count` | Number of open positions |
| `open_order_count` | Number of open orders |
| `current_positions` | Compact list: symbol, qty, market_value, unrealized_pl |
| `latest_plan_id` | ID of the most recent trade plan |
| `trade_plan_approved_for_execution` | Whether the plan carries execution approval |
| `proposed_order_count` | Number of proposed orders in the plan |
| `proposed_orders` | Compact list: symbol, side, order_type, limit_price, notional, skip_reason |
| `dry_run_all_gates_pass` | Whether all dry-run execution gates passed |
| `failed_gates` | List of gate IDs that failed |
| `source_integrity_status` | `ok` or `failed` |
| `data_quality_status` | Status from the data quality snapshot |
| `risk_state.drawdown` | Current portfolio drawdown (0.0 = flat, -0.05 = -5%) |
| `risk_state.drawdown_warn` | `true` if drawdown ≥ warn threshold |
| `risk_state.drawdown_blocked` | `true` if drawdown ≥ block threshold (execution halted) |
| `risk_state.paused` | `true` if risk monitor paused execution |
| `risk_state.stale` | `true` if risk state is older than 120 minutes |
| `order_lifecycle_summary` | Filled/active/canceled/rejected/expired order counts |
| `outcome_summary` | Tracked outcome count and average return |
| `trigger_performance_summary` | Regime, fill rate, slippage, recommendation |
| `lineage_status` | Complete/partial lineage chain counts |
| `last_alert_count` | Number of trigger candidates from last scan |

## How to act on status

### RED — Source integrity failed

```bash
python scripts/refresh_data.py
python scripts/system_status.py   # re-check
```

### RED — Hard gate failure

```bash
python scripts/dry_run_execute.py   # re-run gates to see updated report
python scripts/system_status.py
```

### RED — Duplicate open orders

Wait for existing orders to fill, cancel, or expire (check Alpaca paper dashboard),
then run `monitor_orders.py` and re-check status.

### RED — Drawdown blocked

Do not attempt to reset the drawdown counter automatically. Review the position
history and paper outcomes, understand the loss, then manually update
`memory/RISK-STATE.json` only after you are satisfied the strategy is still sound.

### YELLOW — Risk state stale

```bash
python scripts/monitor_positions.py
python scripts/system_status.py
```

### YELLOW — Trade plan missing or stale

```bash
python scripts/refresh_data.py
python scripts/scan_triggers.py
python scripts/generate_trade_plan.py
python scripts/system_status.py
```

### YELLOW — Market closed (soft gates)

This is normal outside market hours. Research is still safe. Paper execution
will proceed correctly during market hours once the full research cycle runs.

## Memory log

Each run appends a human-readable entry to `memory/SYSTEM-STATUS.md`:

```
## System Status — 2026-01-15T21:10:00Z

**Overall:** GREEN  | Research: YES  | Paper Execution: YES  | Scheduled: NO (policy)

**Account:** equity=$10,000.00  drawdown=0.00%  positions=1  open_orders=0
**Trade Plan:** plan-001  approved=True
**Dry-run gates:** PASS  failed=[]

---
```

## Outputs

| Path | Contents |
|------|----------|
| `data/latest/system_status.json` | Full status document |
| `memory/SYSTEM-STATUS.md` | Appended human-readable log entry |
