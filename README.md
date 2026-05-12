# Autonomous Trading Research OS

A safe, auditable Alpaca **paper trading only** research-and-execution system for a SPY / S&P 500-style trend allocator.

This repository is designed so deterministic scripts create the trade-critical state, Git records every change, and automation can fail closed instead of placing unverified orders.

## Hard rules

- Paper trading only.
- Live trading is blocked in code.
- No options.
- No crypto.
- No shorting.
- No discretionary Claude trades.
- No trade without `data/latest/trade_plan.json`.
- No trade if any risk gate fails.
- No `.env` in cloud routines.
- Never print or commit secrets.
- GitHub/Git is the audit trail.
- Every trigger, skip, trade, error, and outcome must be logged.

## Layered system

| Layer | Script | Primary output |
|---|---|---|
| 1. Data Refresh | `scripts/data_refresh.py` | `data/latest/market_snapshot.json` |
| 2. Trigger Scan | `scripts/trigger_scan.py` | `data/latest/trigger_snapshot.json` |
| 3. Trade Plan Generation | `scripts/generate_trade_plan.py` | `data/latest/trade_plan.json` |
| 4. Trade Execution | `scripts/execute_trade_plan.py` | `data/latest/execution_report.json` |
| 5. Position Monitor | `scripts/position_monitor.py` | `data/latest/position_report.json` |
| 6. Research Context | `scripts/research_context.py` | `memory/RESEARCH-CONTEXT.md` |
| 7. Data Quality Review | `scripts/data_quality_review.py` | `data/latest/data_quality_report.json` |
| 8. Daily Summary | `scripts/daily_summary.py` | `memory/DAILY-SUMMARY.md` |
| 9. Weekly Review | `scripts/weekly_review.py` | `memory/WEEKLY-REVIEW.md` |
| 10. Strategy Improvement Review | `scripts/strategy_improvement_review.py` | `memory/EXPERIMENT-LOG.md`, `memory/PROMOTION-DECISIONS.md` |

## Initial strategy seed

The base allocator mirrors the supplied QuantConnect strategy:

- SPY regime filter: SPY close above 200-day SMA and 126-day ROC positive.
- Stock-level trend filter: candidate close above 200-day SMA.
- Momentum ranking: `0.5 * ROC126 + 0.5 * ROC252`.
- Volatility weighting: inverse ATR% using 20-day Wilder ATR.
- Sector caps: max names per sector.
- Risk-off fallback: BIL.
- Risk-on fallback when constituents are not ready: SPY.
- Long/cash only.

The seed universe in `config/universe.json` is a static S&P 500-style starting universe. Replace it with a vetted full SPY/S&P 500 constituent source only through an auditable PR.

## Local setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Local credentials are optional for dry runs. For local paper-account use only:

```bash
cp env.template .env
# edit .env locally; never commit it
```

Cloud routines must use environment variables managed by the runner, not a checked-in `.env` file.

## Dry-run setup check

These commands do not place trades:

```bash
python -m compileall src scripts tests
python scripts/run_all_dry_run.py
python -m unittest discover -s tests
```

`run_all_dry_run.py` uses deterministic mock Alpaca-compatible data and writes audit artifacts. Execution stays in dry-run mode and records a skip/no-submit event.

## Paper execution guard

Actual paper order submission requires all of the following:

1. `TRADING_MODE=paper`
2. `LIVE_TRADING_CONFIRMED` must not be true
3. `ALLOW_PAPER_ORDER_SUBMISSION=true`
4. A fresh `data/latest/trade_plan.json`
5. `approval.status == "APPROVED_FOR_PAPER"`
6. All risk gates pass
7. Market clock is open
8. The command includes `--confirm-paper`

Example paper-account sequence:

```bash
python scripts/data_refresh.py --alpaca
python scripts/trigger_scan.py
python scripts/generate_trade_plan.py --approve-paper
python scripts/execute_trade_plan.py --confirm-paper
python scripts/position_monitor.py --alpaca
```

By default, scripts run in dry-run mode and do not submit orders.

## Alpaca environment variables

```bash
ALPACA_API_KEY=
ALPACA_API_SECRET=
TRADING_MODE=paper
ALPACA_PAPER=true
ALPACA_DATA_FEED=iex
ALLOW_PAPER_ORDER_SUBMISSION=false
LIVE_TRADING_CONFIRMED=false
```

Never print these values. Never commit them. Never put them in cloud `.env` files.

## Source-of-truth workflow

Recommended routine workflow:

```bash
git pull --ff-only
python -m compileall src scripts tests
python scripts/run_all_dry_run.py
git status --short
git diff -- data latest memory config src scripts routines .claude README.md CLAUDE.md
git add .
git commit -m "Run audited dry-run pipeline"
git push
```

For production routines, use a safe branch/PR workflow if direct main pushes are unavailable or unsafe.

## Trade-critical vs research context

Alpaca is the only source for trade-critical account/position/order/clock/bar/quote/spread data. Web and connectors can be used for research notes and hypothesis generation only. They must not directly create orders or bypass deterministic risk gates.
