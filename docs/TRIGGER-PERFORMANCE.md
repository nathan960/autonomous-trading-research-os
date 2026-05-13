# Trigger Performance Scoring

Research-only tool to score trigger pass/fail rates, execution fill rates, and
unrealized P/L per paper trade. No execution path.

---

## Overview

| Script | Workflow | Output |
|--------|----------|--------|
| `scripts/score_triggers.py` | `trigger-performance.yml` | `data/latest/trigger_performance.json`, `data/history/trigger_performance/trigger_performance_<date>-<hash8>.json`, `memory/EXPERIMENT-LOG.md` |

---

## What it reads

- `data/latest/trigger_snapshot.json` — per-symbol pass/fail results (latest snapshot)
- `data/latest/trade_plan.json` — plan-layer blocks (blocked_symbols, run caps)
- `data/latest/outcome_snapshot.json` — filled order outcomes (P/L, slippage)
- `data/history/orders/order_monitor-*.json` — deduplicated fill records over the period
- `data/history/triggers/<date>.jsonl` — session-level regime stats over the period

---

## What it writes

| File | Mode |
|------|------|
| `data/latest/trigger_performance.json` | Replaced each run |
| `data/history/trigger_performance/trigger_performance_<YYYY-MM-DD>-<hash8>.json` | Create |
| `memory/EXPERIMENT-LOG.md` | Append (observations only, never strategy changes) |

---

## How it works

1. **Regime stats** — scans JSONL trigger history for the period. Records per-session
   risk-on/off counts, candidates, selections, and excluded counts.
2. **Symbol trigger stats** — reads `trigger_snapshot.json` for the latest scan. Records
   pass/fail counts per trigger (spread, trend, momentum, liquidity, ATR sizing).
3. **Plan-layer stats** — reads `trade_plan.json` blocked_symbols and run caps. Maps each
   skip_reason to a canonical trigger_id.
4. **Fill stats** — aggregates order monitor history over the period, deduplicated by
   `client_order_id` (latest `checked_at` wins).
5. **Outcome stats** — aggregates `outcome_snapshot.json` for current return and slippage.
6. Merges all stats and classifies each trigger with a recommendation label.
7. Writes snapshot and appends to `memory/EXPERIMENT-LOG.md`.

---

## Trigger IDs

| Trigger ID | Category | Description |
|-----------|---------|-------------|
| `SPY_REGIME_200DMA_V1` | `market_regime` | SPY above 200-day SMA and 6m momentum positive |
| `DATA_STALE_GATE_V1` | `data_gate` | Data freshness check |
| `STOCK_TREND_200DMA_V1` | `stock_trend` | Stock latest close above 200-day SMA |
| `MOMENTUM_BLEND_6M_12M_V1` | `momentum` | 6-month and 12-month ROC momentum blend |
| `LIQUIDITY_GATE_V1` | `liquidity` | Minimum 20-day average volume |
| `SPREAD_GATE_V1` | `spread_gate` | Bid-ask spread percentage limit |
| `ATR_SIZING_V1` | `sizing` | Inverse ATR% position sizing (not a gate) |
| `SECTOR_CAP` | `plan_layer` | Sector concentration cap |
| `MAX_HOLDINGS` | `plan_layer` | Maximum total holdings cap |
| `MAX_ORDERS_PER_RUN` | `plan_layer` | Orders-per-run cap |
| `DATA_READINESS` | `data_gate` | Insufficient price history for signal computation |

---

## Recommendation labels

| Label | Meaning |
|-------|---------|
| `operational_issue` | Spread or data gate blocking an unusually high fraction of candidates — review pipeline health |
| `needs_more_data` | Fewer than 20 symbol observations; stats are unreliable |
| `do_not_promote_yet` | Fewer than 20 fills; cannot draw P/L conclusions |
| `candidate_for_review` | Sufficient fills for exploratory review; requires backtest and peer review |
| `keep_observing` | Regime: fewer than 20 sessions; accumulating data |

---

## Minimum sample thresholds

- `MIN_FILL_SAMPLE = 20` — fills needed before P/L conclusions
- `MIN_SYMBOL_SAMPLE = 20` — symbol observations needed for reliable trigger stats

These thresholds are intentionally conservative. No trigger should be promoted
or demoted from a short paper run.

---

## Output JSON schema

### trigger_performance.json

```json
{
  "run_id": "trigger_performance-20260513T213000-abc12345",
  "generated_at": "2026-05-13T21:30:00Z",
  "period_start": "2026-05-07",
  "period_end": "2026-05-13",
  "days": 7,
  "status": "ok",
  "regime": {
    "trigger_id": "SPY_REGIME_200DMA_V1",
    "category": "market_regime",
    "sessions_total": 5,
    "sessions_risk_on": 5,
    "sessions_risk_off": 0,
    "risk_on_pct": 1.0,
    "avg_candidates_per_session": 12.0,
    "avg_selected_per_session": 3.0,
    "avg_excluded_per_session": 9.0,
    "regime_errors": [],
    "recommendation": "keep_observing",
    "recommendation_reason": "Only 5 session(s) — accumulating data."
  },
  "triggers": {
    "SPREAD_GATE_V1": {
      "trigger_id": "SPREAD_GATE_V1",
      "category": "spread_gate",
      "description": "Bid-ask spread percentage limit",
      "observation_count": 120,
      "passed_count": 110,
      "blocked_count": 10,
      "block_rate": 0.0833,
      "avg_spread_passing": 0.0008,
      "avg_spread_blocked": 0.0045,
      "recommendation": "needs_more_data",
      "recommendation_reason": "..."
    }
  },
  "fill_outcomes": {
    "total_outcomes": 3,
    "avg_slippage_pct": -0.0004,
    "avg_current_return_pct": 0.0093,
    "by_symbol": {"WELL": {...}},
    "sample_status": "insufficient_sample",
    "recommendation": "needs_more_data",
    "recommendation_reason": "..."
  },
  "execution_fill_stats": {
    "total_fills": 3,
    "total_tracked": 3
  },
  "operational_issues": [],
  "research_observations": ["..."],
  "safety_note": "All recommendations are research-only observations...",
  "performance_hash": "16 hex chars"
}
```

---

## Usage

```bash
# Run with full writes (7-day window)
python scripts/score_triggers.py

# Custom window
python scripts/score_triggers.py --days 14

# Preview without writing files
python scripts/score_triggers.py --dry-run

# Custom end date
python scripts/score_triggers.py --end-date 2026-05-10
```

### GitHub Actions

**Workflow:** `.github/workflows/trigger-performance.yml`

Scheduled: weekdays at 21:30 UTC (after outcome-tracker at 21:15).

---

## Skip reason → trigger_id mapping

| Skip reason fragment | Trigger ID |
|---------------------|-----------|
| `close_below_200dma` | `STOCK_TREND_200DMA_V1` |
| `spread_too_wide` | `SPREAD_GATE_V1` |
| `roc_6m_below_min` | `MOMENTUM_BLEND_6M_12M_V1` |
| `roc_12m_below_min` | `MOMENTUM_BLEND_6M_12M_V1` |
| `sector_cap` | `SECTOR_CAP` |
| `max_holdings_reached` | `MAX_HOLDINGS` |
| `capped_by_max_orders_per_run` | `MAX_ORDERS_PER_RUN` |
| `max_orders_per_run_cap` | `MAX_ORDERS_PER_RUN` |
| `insufficient_bars` | `DATA_READINESS` |
| `not_ready` | `DATA_READINESS` |
| *(anything else)* | `OTHER` |

---

## Limitations

- **No per-trigger fill attribution** — fills are not currently traced back to the
  specific trigger that selected them. Fill counts in `fill_outcomes` represent all
  fills in the period, not per-trigger fills.
- **Symbol trigger stats use latest snapshot only** — `trigger_snapshot.json` is a
  single-point-in-time snapshot. Multi-day history per trigger is not yet available.
- **Outcome windows** — P/L is the current unrealized return. Window-locked returns
  (1-day, 5-day, etc.) are tracked by the outcome tracker but not yet surfaced here.

---

## Safety constraints

- `ENABLE_PAPER_EXECUTION=false` hardcoded in workflow
- `LIVE_TRADING_CONFIRMED=false` hardcoded in workflow
- `execute_paper.py` is never called or imported
- `config/strategy.json`, `config/risk_limits.json`, and `config/trigger_registry.json`
  are never written
- `approved_for_execution` is never set
- Orders are never submitted, cancelled, or replaced

---

## Memory log

| File | Written by | Content |
|------|-----------|---------|
| `memory/EXPERIMENT-LOG.md` | `score_triggers.py` | Append-only; research observations and operational issues with action-item checkboxes |
