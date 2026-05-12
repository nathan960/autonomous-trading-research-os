# Weekly Review Routine

## Purpose

Run the Weekly Review layer in a stateless, auditable way.

## Commands

```bash
git pull --ff-only
python -m compileall src scripts tests
python scripts/weekly_review.py
git status --short
git diff
git add .
git commit -m "Weekly Review: audited run" || true
git push
```

## Safety notes

- Do not print secrets.
- Do not create `.env` in cloud.
- Do not bypass risk gates.
- If the script fails, log the error and stop.
