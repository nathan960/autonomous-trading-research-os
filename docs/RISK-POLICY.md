# Risk Policy

## Absolute constraints (non-negotiable)

These constraints are enforced in code and cannot be overridden by config, environment, or argument:

| Constraint | Enforcement |
|---|---|
| Paper trading only | `RuntimeSettings.validate_paper_only()` raises if `TRADING_MODE != paper` |
| No live trading | `LIVE_TRADING_CONFIRMED=false` required; any truthy value blocks execution |
| No shorting | `allow_shorting: false` enforced in strategy schema and risk gate `NO_SHORT_SELLS` |
| No options | `allow_options: false` enforced in strategy schema; option-like symbols classified and blocked |
| No crypto | `allow_crypto: false` enforced in strategy schema; crypto-like symbols classified and blocked |
| No discretionary trades | Orders only from a validated `trade_plan.json`; no ad-hoc order construction |
| Secrets never output | `NO_SECRETS_IN_OUTPUT` risk gate; `redact_mapping` used on any dict that may contain keys |

## Risk gates

Every gate must return `passed: true` before paper orders are submitted. A single failure blocks execution and the skip reason is logged.

| Gate ID | What it checks |
|---|---|
| `NO_LIVE_TRADING` | `TRADING_MODE=paper`, `ALPACA_PAPER=true`, `LIVE_TRADING_CONFIRMED=false` |
| `PLAN_EXISTS_AND_FRESH` | `trade_plan.json` exists and snapshot age ≤ `max_snapshot_age_minutes` |
| `ALPACA_REVALIDATION_REQUIRED` | Alpaca account, positions, orders, clock re-fetched in same run |
| `MARKET_CLOCK_OPEN_FOR_EXECUTION` | Market clock confirms open before order submission |
| `LONG_ONLY_TARGETS` | All target weights ≥ 0 |
| `NO_OPTIONS_OR_CRYPTO` | All target symbols classify as `equity_or_etf` |
| `NO_SHORT_SELLS` | No sell order would create a short position |
| `UNIVERSE_ONLY` | All target symbols in `universe.json` symbols + fallbacks + benchmark |
| `MAX_HOLDINGS` | Stock holdings count ≤ `parameters.max_holdings` |
| `MAX_POSITION_WEIGHT` | Individual weight ≤ `parameters.max_position_weight` |
| `SECTOR_CAPS` | Names per sector ≤ `parameters.max_names_per_sector` |
| `TOTAL_WEIGHT_LIMIT` | Sum of target weights ≤ 1.0001 |
| `DATA_SOURCE_HASH_PRESENT` | Snapshot includes `source_data_hash` |
| `QUOTE_SPREAD_LIMIT` | Spreads for targeted symbols ≤ `parameters.max_quote_spread_pct` |
| `NO_SECRETS_IN_OUTPUT` | Gate output contains no secret values |

## Numeric limits (from `config/risk_limits.json`)

| Limit | Default |
|---|---|
| Max portfolio gross exposure | 1.0 (100%) |
| Max position weight | 0.12 (12%) |
| Max holdings (stocks) | 10 |
| Max names per sector | 2 |
| Drawdown warn threshold | -5% |
| Drawdown block threshold | -10% |
| Min order notional | $25 |
| Max quote spread | 2% |

## Drawdown state

`memory/RISK-STATE.json` tracks `latest_equity`, `peak_equity`, and `drawdown = (latest - peak) / peak`. The position monitor updates this after each reconciliation. Drawdown block triggers a hard stop on new orders.

## Schema enforcement

`scripts/validate_all.py` validates all config files and `RISK-STATE.json` against their schemas before any routine runs. Missing files or constraint violations exit with code 1.
