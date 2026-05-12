# Data Quality Review

Run Layer 7 Data Quality Review. Command: `python scripts/data_quality_review.py`. Check source labels, freshness, missing bars/quotes, and spreads. Fail closed if trade-critical data quality is bad.

Always run compile checks first, never print secrets, never force-push, and preserve auditability.
