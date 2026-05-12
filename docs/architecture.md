# Architecture

The system separates trade-critical deterministic state from research context.

## Trade-critical path

`Data Refresh -> Trigger Scan -> Trade Plan Generation -> Trade Execution -> Position Monitor`

Only Alpaca-derived account, position, order, clock, bar, quote, and spread data may feed this path.

## Research path

`Research Context -> Weekly Review -> Strategy Improvement Review`

Research can propose hypotheses but cannot create orders or change production strategy.

## Fail-closed controls

- Missing snapshot: trigger scan fails.
- Missing trigger snapshot: trade-plan generation fails.
- Missing trade plan: execution fails.
- Stale or unapproved plan: execution blocks.
- Any failed risk gate: execution blocks.
- Any live trading flag: execution blocks.

---

## Phase 1 core package: `src/trading_os/`

| Module | Responsibility |
|---|---|
| `config.py` | Load and schema-validate all required JSON config files and RISK-STATE.json |
| `schemas.py` | Pure-function validators for every config and state type; raise `SchemaError` on failure |
| `hashing.py` | Stable sha256 hash for JSON objects (canonical), raw files, and JSON files |
| `time_utils.py` | UTC timestamp creation (`utc_now_iso`), parsing (`parse_iso_utc`), and age (`iso_age_minutes`) |

### Config files validated by Phase 1

| File | Schema enforces |
|---|---|
| `config/strategy.json` | `paper_only` mode, no shorting/options/crypto, positive holdings cap |
| `config/risk_limits.json` | No live trading, negative drawdown thresholds, exposure ≤ 1.0 |
| `config/execution_policy.json` | Paper-only, all approval gates required, fail-closed |
| `config/universe.json` | Non-empty symbol list, benchmark, fallbacks |
| `config/sector_map.json` | Each symbol has sector name (string) and sector_code (int) |
| `config/trigger_registry.json` | Each trigger has id/layer/definition; `trade_direct` must be false |
| `memory/RISK-STATE.json` | Positive equity, non-negative position count, schema_version present |

## Layer execution order

```
1.  Data Refresh          — fetch Alpaca bars, quotes, positions → market_snapshot.json
2.  Trigger Scan          — evaluate regime + per-stock triggers → trigger_snapshot.json
3.  Trade Plan Generation — build target weights, apply gates   → trade_plan.json
4.  Trade Execution       — submit paper orders (all gates must pass)
5.  Position Monitor      — reconcile positions, update RISK-STATE.json
6.  Research Context      — summarise web/connector context (no order generation)
7.  Data Quality Review   — flag freshness, coverage, anomalies
8.  Daily Summary         — narrative summary of the day
9.  Weekly Review         — strategy performance review
10. Strategy Improvement  — evidence-backed improvement proposals only
```

## Safety invariants

- `TRADING_MODE=paper` is the only permitted mode; live mode raises at settings load.
- All risk gates must pass before any paper order is submitted.
- Triggers carry `trade_direct: false`; they inform plan generation, they never place orders.
- Secrets are never printed, logged, committed, or echoed.
- Config is immutable during a routine run; strategy changes require a PR with evidence.
- `scripts/validate_all.py` must exit 0 before any routine proceeds.
