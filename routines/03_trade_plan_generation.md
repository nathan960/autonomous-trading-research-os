# Trade Plan Generation Routine

## Purpose

Run the Trade Plan Generation layer in a stateless, auditable way.

## Commands

```bash
git pull --ff-only
python -m compileall src scripts tests
python scripts/generate_trade_plan.py --approve-paper
git status --short
git diff
git add .
git commit -m "Trade Plan Generation: audited run" || true
git push
```

## Safety notes

- Do not print secrets.
- Do not create `.env` in cloud.
- Do not bypass risk gates.
- If the script fails, log the error and stop.
