# Trade Execution Routine

## Purpose

Run the Trade Execution layer in a stateless, auditable way.

## Commands

```bash
git pull --ff-only
python -m compileall src scripts tests
python scripts/execute_trade_plan.py --submit --confirm-paper
git status --short
git diff
git add .
git commit -m "Trade Execution: audited run" || true
git push
```

## Safety notes

- Do not print secrets.
- Do not create `.env` in cloud.
- Do not bypass risk gates.
- If the script fails, log the error and stop.
