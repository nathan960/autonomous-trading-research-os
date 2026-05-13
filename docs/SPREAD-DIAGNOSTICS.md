# Spread Gate Diagnostics

## Problem

`SPREAD_GATE_V1` reports blocking ~67–95% of universe symbols when trigger scans
run after market close. This document explains the root cause and the diagnostic
tool built to classify spread failures.

## Root Cause (2026-05-13 Analysis)

All 3 confirmed fills (WELL, JNJ, EQIX) passed the spread gate during intraday
scans. The high block rate in `trigger_performance.json` comes from the latest
`trigger_snapshot.json`, which was captured at **20:39 UTC (after market close)**
using IEX quotes that are structurally unreliable after hours.

| Issue | Count | Classification |
|-------|-------|----------------|
| IEX ask_price=0.0 at close | 24 symbols | `zero_bid_or_ask` |
| IEX closing-print wide spreads (~9–12%) | 53 symbols | `off_hours_quote` |
| Genuine passes | 4 symbols | `pass` |

The spread gate threshold (2%) is **correct**. The problem is **data timing**:
IEX does not publish reliable NBBO quotes after the market closes.

## Failure Classes

| Class | Meaning |
|-------|---------|
| `pass` | spread_pct ≤ max_quote_spread_pct — gate passes |
| `missing_bid` | bid_price is None/absent from quote |
| `missing_ask` | ask_price is None/absent from quote |
| `zero_bid_or_ask` | bid or ask is 0.0 — IEX has no liquidity on that side |
| `off_hours_quote` | market is closed; spread is wide because IEX close quotes are unreliable |
| `stale_quote` | market was open but quote is >60 min old |
| `data_feed_limitation` | market was open, IEX quote coverage was insufficient (venue-only) |
| `wide_spread_real` | market was open, quote was fresh, non-IEX feed — genuine wide spread |
| `unknown` | bid/ask present, non-zero, but spread_pct couldn't be computed |

## Classification Priority

1. `missing_bid` / `missing_ask` — checked first (data integrity)
2. `zero_bid_or_ask` — checked second (zero prices)
3. If spread passes threshold → `pass`
4. If market is closed → `off_hours_quote`
5. If quote age > 60 min (market was open) → `stale_quote`
6. If IEX feed, market open, fresh quote → `data_feed_limitation`
7. If non-IEX feed, market open, fresh quote → `wide_spread_real`
8. Otherwise → `unknown`

## Script

```bash
# Diagnose using current market snapshot (best during market hours)
python scripts/diagnose_spreads.py

# Preview without writing files
python scripts/diagnose_spreads.py --dry-run
```

## Workflow

`spread-diagnostics.yml` runs at **15:30 UTC weekdays** (during US market
hours) and refreshes market data before running diagnostics. This ensures IEX
quotes are from an active trading session.

## Outputs

| Path | Description |
|------|-------------|
| `data/latest/spread_diagnostics.json` | Current diagnostic snapshot (replaced each run) |
| `data/history/data_quality/spread_diagnostics/` | Immutable history archive |
| `memory/DATA-QUALITY-LOG.md` | Appended summary |

## Recommendations (Operational Only)

Diagnostics produce only operational recommendations. Strategy changes require
separate evidence-backed proposals.

1. **Run during market hours** — the primary fix. `spread-diagnostics.yml`
   is scheduled at 15:30 UTC to capture intraday IEX quotes.

2. **Verify `ALPACA_DATA_FEED`** — if a SIP subscription exists and has been
   approved, SIP quotes provide full NBBO coverage and are more reliable after
   hours. Do not switch feeds without confirming Alpaca account permissions.

3. **Inspect quote timestamps** — zero-ask symbols should have timestamps at
   market close (20:00 UTC EDT). If timestamps are during market hours, this
   indicates a data ingestion issue, not a timing issue.

4. **Do not adjust the threshold** — `max_quote_spread_pct=0.02` is unchanged.
   A threshold change requires evidence of persistent wide spreads during
   market hours across multiple intraday scan sessions.

## Safety

- `ENABLE_PAPER_EXECUTION=false` — no orders placed
- `LIVE_TRADING_CONFIRMED=false` — no live trading
- No modifications to `risk_limits.json`, `strategy.json`, or any config
- `diagnose_spreads.py` reads only from `data/latest/` and `config/`
- All writes go to `data/latest/spread_diagnostics.json`,
  `data/history/data_quality/spread_diagnostics/`, and `memory/DATA-QUALITY-LOG.md`
