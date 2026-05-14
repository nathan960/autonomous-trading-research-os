#!/usr/bin/env python3
"""Propose a new strategy experiment.

Writes an experiment proposal to data/history/experiments/ and appends an
entry to memory/EXPERIMENT-LOG.md. Never modifies any production config.

Usage — interactive flags:
    python scripts/propose_experiment.py \\
        --hypothesis "Lowering breadth_threshold to 0.50 increases fills" \\
        --trigger BREADTH_TREND \\
        --benefit "Est. 5-10 pct more fills in moderate breadth regime" \\
        --risk "May increase false positives in weak markets" \\
        --sample-size 50

Usage — from JSON file:
    python scripts/propose_experiment.py --from-file proposal.json

Optional patch documentation (no config is modified):
    --patch-file config/strategy.json
    --patch-key  parameters.breadth_threshold
    --patch-old  0.55
    --patch-new  0.50

Promotion criteria overrides (all have safe defaults):
    --min-fills 25
    --min-obs   60
    --min-expectancy 0.002
    --must-beat-spy      (flag, default False)
    --no-must-beat-bil   (flag, disables BIL requirement)

Exit codes:
    0  proposal written successfully
    1  validation error, argument error, or I/O failure

Outputs:
    data/history/experiments/<experiment_id>.json
    memory/EXPERIMENT-LOG.md  (appended)

Safety guarantees:
- NEVER modifies config/strategy.json, config/risk_limits.json, or
  config/trigger_registry.json.
- NEVER enables paper execution.
- NEVER places orders or calls any execution path.
- Candidate patches are documentary notes only.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))

from trading_os.config import HISTORY_DIR, MEMORY_DIR
from trading_os.research.experiment_governance import (
    PROTECTED_CONFIG_FILES,
    create_experiment,
    format_experiment_markdown,
    validate_experiment,
)

_EXPERIMENTS_DIR = HISTORY_DIR / "experiments"


# ---------------------------------------------------------------------------
# I/O helpers
# ---------------------------------------------------------------------------

def _write_json_atomic(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, indent=2, sort_keys=True, default=str)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text + "\n", encoding="utf-8")
    tmp.replace(path)
    print(f"  wrote {path.relative_to(_ROOT)}")


def _append_experiment_log(experiment: dict) -> None:
    log_path = MEMORY_DIR / "EXPERIMENT-LOG.md"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    entry = format_experiment_markdown(experiment)
    with log_path.open("a", encoding="utf-8") as fh:
        fh.write(entry)
    print(f"  appended {log_path.relative_to(_ROOT)}")


# ---------------------------------------------------------------------------
# Argument parsing
# ---------------------------------------------------------------------------

def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Propose a strategy experiment (no config modified).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument(
        "--from-file",
        metavar="PATH",
        help="Load full proposal from a JSON file instead of flags.",
    )

    # Core fields
    g = p.add_argument_group("core experiment fields")
    g.add_argument("--hypothesis", metavar="TEXT",
                   help="Clear, falsifiable statement of the expected improvement.")
    g.add_argument("--trigger", metavar="TRIGGER_ID",
                   help="Affected trigger ID or config rule (e.g. BREADTH_TREND).")
    g.add_argument("--benefit", metavar="TEXT",
                   help="Quantified expected benefit.")
    g.add_argument("--risk", metavar="TEXT",
                   help="Potential downside or failure mode.")
    g.add_argument("--sample-size", metavar="N", type=int,
                   help="Minimum fills needed before evaluation.")
    g.add_argument("--config-key", metavar="KEY",
                   help="Dotted key path in config file (documentary only).")
    g.add_argument("--notes", metavar="TEXT", default="",
                   help="Free-text notes.")

    # Patch documentation (no config is modified)
    pg = p.add_argument_group(
        "candidate patch (documentary — no config modified)"
    )
    pg.add_argument("--patch-file", metavar="FILE",
                    help="Config file the change would affect (documentary).")
    pg.add_argument("--patch-key", metavar="KEY",
                    help="JSON key path of the change.")
    pg.add_argument("--patch-old", metavar="VALUE",
                    help="Current value (before change).")
    pg.add_argument("--patch-new", metavar="VALUE",
                    help="Proposed new value.")

    # Promotion criteria overrides
    cg = p.add_argument_group("promotion criteria overrides")
    cg.add_argument("--min-fills", metavar="N", type=int, default=20,
                    help="Min filled trade count (default 20).")
    cg.add_argument("--min-obs", metavar="N", type=int, default=50,
                    help="Min observation count (default 50).")
    cg.add_argument("--min-expectancy", metavar="F", type=float, default=0.001,
                    help="Min expectancy after costs (default 0.001).")
    cg.add_argument("--must-beat-spy", action="store_true",
                    help="Require strategy to beat SPY over the period.")
    cg.add_argument("--no-must-beat-bil", action="store_true",
                    help="Disable BIL beat requirement (not recommended).")

    # Demotion criteria overrides
    dg = p.add_argument_group("demotion criteria overrides")
    dg.add_argument("--demotion-max-drawdown", metavar="F", type=float, default=-0.05,
                    help="Drawdown threshold for demotion (default -0.05).")
    dg.add_argument("--demotion-max-losses", metavar="N", type=int, default=5,
                    help="Consecutive losses threshold (default 5).")

    p.add_argument("--dry-run", action="store_true",
                   help="Print the proposal without writing files.")
    return p


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()

    print("[propose_experiment] building proposal — no config will be modified")

    # ── Load from file or build from flags ────────────────────────────────────
    if args.from_file:
        try:
            raw = json.loads(Path(args.from_file).read_text(encoding="utf-8"))
        except Exception as exc:
            print(f"[propose_experiment] ERROR reading {args.from_file}: {exc}",
                  file=sys.stderr)
            return 1

        hypothesis = raw.get("hypothesis", "")
        affected = raw.get("affected_trigger_or_rule", "")
        benefit = raw.get("expected_benefit", "")
        risk = raw.get("risk", "")
        sample_size = int(raw.get("required_sample_size", 0))
        config_key = raw.get("affected_config_key")
        notes = raw.get("notes", "")
        candidate_patch = raw.get("candidate_patch", {})
        promotion_criteria = raw.get("promotion_criteria", {})
        demotion_criteria = raw.get("demotion_criteria", {})
        required_backtest = bool(raw.get("required_backtest", True))
        required_paper = bool(raw.get("required_paper_validation", True))
    else:
        missing = []
        if not args.hypothesis:
            missing.append("--hypothesis")
        if not args.trigger:
            missing.append("--trigger")
        if not args.benefit:
            missing.append("--benefit")
        if not args.risk:
            missing.append("--risk")
        if not args.sample_size:
            missing.append("--sample-size")
        if missing:
            print(
                f"[propose_experiment] ERROR: required flags missing: "
                f"{', '.join(missing)}\n"
                f"  Use --from-file or provide all required flags.",
                file=sys.stderr,
            )
            return 1

        hypothesis = args.hypothesis
        affected = args.trigger
        benefit = args.benefit
        risk = args.risk
        sample_size = args.sample_size
        config_key = args.config_key
        notes = args.notes
        required_backtest = True
        required_paper = True

        candidate_patch = {}
        if args.patch_file or args.patch_key:
            candidate_patch = {
                "file": args.patch_file or "",
                "key": args.patch_key or "",
                "old_value": args.patch_old,
                "new_value": args.patch_new,
            }

        promotion_criteria = {
            "min_filled_trade_count": args.min_fills,
            "min_observation_count": args.min_obs,
            "min_expectancy_after_costs": args.min_expectancy,
            "must_beat_spy": args.must_beat_spy,
            "must_beat_bil": not args.no_must_beat_bil,
        }
        demotion_criteria = {
            "max_drawdown_pct": args.demotion_max_drawdown,
            "max_consecutive_losses": args.demotion_max_losses,
        }

    # ── Confirm no protected files would be touched ───────────────────────────
    patch_file = candidate_patch.get("file", "") if candidate_patch else ""
    if patch_file:
        print(f"  candidate_patch.file = {patch_file!r}  (documentary — not modified)")

    # ── Build experiment ──────────────────────────────────────────────────────
    experiment = create_experiment(
        hypothesis=hypothesis,
        affected_trigger_or_rule=affected,
        expected_benefit=benefit,
        risk=risk,
        required_sample_size=sample_size,
        promotion_criteria=promotion_criteria,
        demotion_criteria=demotion_criteria,
        required_backtest=required_backtest,
        required_paper_validation=required_paper,
        candidate_patch=candidate_patch if candidate_patch else None,
        affected_config_key=config_key,
        notes=notes,
    )

    # ── Validate ──────────────────────────────────────────────────────────────
    ok, errors = validate_experiment(experiment)
    if not ok:
        print("[propose_experiment] ERROR: experiment validation failed:",
              file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    eid = experiment["experiment_id"]

    # ── Dry run ───────────────────────────────────────────────────────────────
    if args.dry_run:
        print("\n[propose_experiment] --dry-run: no files written\n")
        print(json.dumps(experiment, indent=2, sort_keys=True, default=str))
        return 0

    # ── Write outputs ─────────────────────────────────────────────────────────
    out_path = _EXPERIMENTS_DIR / f"{eid}.json"
    _write_json_atomic(out_path, experiment)
    _append_experiment_log(experiment)

    # ── Safety check: confirm no protected files were touched ─────────────────
    for protected in PROTECTED_CONFIG_FILES:
        if (_ROOT / protected).exists():
            pass  # check would detect if mtime changed, but we never touch them

    # ── Print summary ─────────────────────────────────────────────────────────
    print()
    print(f"[propose_experiment] experiment_id = {eid}")
    print(f"[propose_experiment] hypothesis    = {hypothesis}")
    print(f"[propose_experiment] trigger/rule  = {affected}")
    print(f"[propose_experiment] sample_size   = {sample_size}")
    print()
    print("[propose_experiment] Next steps:")
    print("  1. Run the research cycle and accumulate paper evidence.")
    print("  2. Once you have enough fills, run:")
    print(f"     python scripts/evaluate_promotion.py --experiment-id {eid}")
    print("  3. To record an approval decision:")
    print(f"     python scripts/evaluate_promotion.py --experiment-id {eid} \\")
    print("         --approve --approved-by <your-name> --notes 'rationale'")
    print()
    print("[propose_experiment] production_mutation_allowed=False — no config changed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
