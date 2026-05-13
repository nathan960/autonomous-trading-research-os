# Trade Lineage

## Purpose

The lineage system creates a deterministic audit chain linking each filled order back to the trigger snapshot, signal candidates, and trade plan that produced it. This closes the loop between trigger performance evaluation and actual fill outcomes.

## Chain

```
trigger_snapshot.json
  → trigger_snapshot_hash (SHA-256 of snapshot content)
  → candidates[symbol] (symbol passed all eligibility gates)
  → trade_plan.json target (symbol selected for sizing)
  → proposed_order (limit price, notional, side)
  → execution_report (broker order ID, submitted_at)
  → broker order fill (fill_price, filled_qty, filled_at)
  → outcome_snapshot.json (current_return_pct, unrealized_pl)
  → trigger_performance.json (fill_count per trigger ID)
```

## Lineage Status Values

| Status | Meaning |
|--------|---------|
| `complete_from_trade_plan` | trigger_snapshot_hash recovered from current trade_plan.json (plan_id matched) |
| `complete_recovered_from_trigger_history` | hash recovered from JSONL trigger history; symbol was in `selected` at closest scan before fill |
| `partial_missing_trigger_snapshot_hash` | hash not recoverable; symbol in `candidates` in trigger history, trigger_ids inferred |
| `partial_missing_trigger_ids` | neither hash nor trigger_ids recoverable |

## Trigger ID Inference

If a symbol appeared in `candidates` in any trigger history entry within the lookback window, all six eligibility trigger IDs are inferred as having passed (because passing all of them is the prerequisite to appearing in candidates):

- `SPY_REGIME_200DMA_V1`
- `STOCK_TREND_200DMA_V1`
- `LIQUIDITY_GATE_V1`
- `SPREAD_GATE_V1`
- `MOMENTUM_BLEND_6M_12M_V1`
- `ATR_SIZING_V1`

## Outputs

| Path | Description |
|------|-------------|
| `data/latest/lineage_snapshot.json` | Current lineage snapshot (replaced each run) |
| `data/history/lineage/lineage_<date>-<hash8>.json` | Immutable history archive |
| `memory/SIGNAL-LOG.md` | Appended summary of fill/lineage per run |

## Scripts

```bash
# Build lineage snapshot (no execution path — safe to run anytime)
python scripts/build_lineage.py

# Extend lookback window to 14 days
python scripts/build_lineage.py --days 14

# Preview without writing files
python scripts/build_lineage.py --dry-run
```

## Workflow

The `lineage.yml` GitHub Actions workflow runs after market close (21:00 UTC weekdays) and:

1. Builds the lineage snapshot
2. Re-runs outcome tracking with lineage context (adds trigger fields to outcome records)
3. Re-scores triggers with fill counts populated from lineage

## Integration with Trigger Performance

`score_triggers.py` reads `data/latest/lineage_snapshot.json` and calls `collect_fill_counts_from_lineage()` to populate `fill_count` for each trigger ID. Without lineage, all trigger IDs report `fill_count=0` because execution reports do not embed trigger IDs directly.

## Root Cause Note

Trade plans are saved only to `data/latest/trade_plan.json` (overwritten each run). The `trigger_snapshot_hash` is not stored in execution reports. This means fills that complete after the next trigger scan can no longer be linked via the current trade plan — they require recovery from the JSONL trigger history in `data/history/triggers/`.

## Safety

- `ENABLE_PAPER_EXECUTION=false` — no orders placed
- `LIVE_TRADING_CONFIRMED=false` — no live trading enabled
- No Alpaca API calls in `build_lineage.py`
- Reads only from `data/latest/` and `data/history/`
- All writes go to `data/latest/lineage_snapshot.json`, `data/history/lineage/`, and `memory/SIGNAL-LOG.md`
