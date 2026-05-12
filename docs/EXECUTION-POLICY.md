# Execution Policy

## Paper-only mandate

This system is paper trading only. There is no code path that enables live order submission.  
`config/execution_policy.json` codifies this and is schema-validated on every run.

## Pre-execution checklist

The following conditions must all be true before any paper order is submitted. A single failure causes execution to fail closed and log the skip reason.

1. `TRADING_MODE=paper` environment variable.
2. `ALPACA_PAPER=true` environment variable.
3. `LIVE_TRADING_CONFIRMED=false` (or absent).
4. `ALLOW_PAPER_ORDER_SUBMISSION=true` environment variable.
5. `--confirm-paper` flag passed to the execution script.
6. `data/latest/trade_plan.json` exists, is fresh (≤ `plan_max_age_minutes`), and has `approval.status = APPROVED_PAPER`.
7. All risk gates pass (see [RISK-POLICY.md](RISK-POLICY.md)).
8. Alpaca account, positions, open orders, and market clock re-fetched in the same run.
9. Market clock confirms the session is open.
10. All proposed orders are long-only, equity/ETF only, and within weight/holdings caps.

## Allowed order types

- **Side**: `buy` or `sell` (liquidating longs only — no short-sells).
- **Asset classes**: US equities, ETFs, and cash-like ETFs (e.g. BIL).
- **Symbols**: Must be in `config/universe.json` symbols, fallbacks, or benchmark.
- **Notional minimum**: `min_order_notional` from `config/risk_limits.json` (default $25).

## Prohibited

- Live orders of any kind.
- Short-sells.
- Options of any kind.
- Crypto of any kind.
- Orders not derived from an approved `trade_plan.json`.
- Submitting orders when any risk gate has failed.
- Submitting orders when the market is closed.

## Fail-closed behaviour

If any pre-condition fails, execution:
1. Logs the skip reason to `memory/TRADE-LOG.md` and `memory/ERROR-LOG.md`.
2. Exits with a non-zero status code.
3. Does **not** submit any order.

There are no retries, partial submissions, or fallback paths that bypass the gate set.

## Audit trail

Every execution run (including skipped runs) produces:
- A `data/latest/execution_report.json` with gate results and outcome.
- A `memory/TRADE-LOG.md` append entry with run ID, timestamp, orders submitted or skipped, and skip reasons.

The run is considered incomplete if no commit and push (or PR) is made at the end of the cloud routine.
