# CLAUDE Operating Contract

You are operating inside **Autonomous Trading Research OS**.

## Non-negotiable rules

- Paper trading only.
- Never enable live trading.
- Never trade options.
- Never trade crypto.
- Never short.
- Never invent discretionary trades.
- Never place a trade without `data/latest/trade_plan.json`.
- Never submit orders if any risk gate fails.
- Never print, echo, log, or commit secrets.
- Never create or rely on `.env` in cloud routines.
- Never force-push.
- Every trigger, skip, trade, error, and outcome must be logged.

## Your job

Run deterministic scripts, preserve auditability, summarize evidence, and propose improvements only when backed by logs, backtests, or paper results. Do not mutate production strategy automatically.

## Layer order

1. Data Refresh
2. Trigger Scan
3. Trade Plan Generation
4. Trade Execution
5. Position Monitor
6. Research Context
7. Data Quality Review
8. Daily Summary
9. Weekly Review
10. Strategy Improvement Review

## Safe execution checklist

Before any paper order submission:

- Confirm `TRADING_MODE=paper`.
- Confirm live trading is disabled.
- Confirm `ALLOW_PAPER_ORDER_SUBMISSION=true`.
- Confirm `--confirm-paper` was passed.
- Confirm `trade_plan.json` exists, is fresh, and is approved for paper.
- Confirm all risk gates pass.
- Re-fetch Alpaca account, positions, orders, and market clock.
- Confirm market is open.
- Confirm proposed orders are long-only, equity/ETF only, and within caps.

If any condition is false, fail closed and log the skip reason.

## Stateless cloud routine model

Each routine should:

```bash
git clone <repo>
cd autonomous-trading-research-os
git pull --ff-only
python -m compileall src scripts tests
python <routine-script>
git status --short
git diff
git add .
git commit -m "<auditable routine message>" || true
git push
```

If direct main pushes are not safe or fail, use a branch and PR:

```bash
BRANCH="routine/<layer>-$(date -u +%Y%m%dT%H%M%SZ)"
git checkout -b "$BRANCH"
# run routine
git add .
git commit -m "<auditable routine message>"
git push -u origin "$BRANCH"
# open PR with summary, changed files, risk gates, and no-trade/trade outcome
```

If a run does not commit/push or open a PR, treat it as not completed.

## Research boundaries

Web/connectors may summarize context and propose hypotheses. They must not directly generate orders. The deterministic pipeline owns triggers, trade plans, risk gates, and execution.

## Strategy improvement rules

- Do not change production strategy from short paper runs.
- Separate facts, hypotheses, and unknowns.
- Require measurable evidence before proposing promotion.
- Any strategy change must be a candidate PR with rationale, backtest/paper evidence, and rollback notes.
