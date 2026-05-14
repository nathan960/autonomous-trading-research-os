"""Tests for src/trading_os/research/experiment_governance.py.

Covers:
- validate_experiment: valid/invalid inputs, human_approval_required invariant
- create_experiment: structure, field defaults, hash presence
- evaluate_promotion: all criteria combinations, always-False invariants
- build_promotion_decision: approve/reject, required fields, error cases
- check_demotion: threshold triggers
- format_*: markdown output
- Safety invariants: production_mutation_allowed always False,
  human_approval_required always True, no config files mutated
- No execution path reachable from the module
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))

from trading_os.research.experiment_governance import (
    ABSOLUTE_MIN_FILLS,
    DECISION_APPROVED,
    DECISION_PENDING,
    DECISION_REJECTED,
    PROTECTED_CONFIG_FILES,
    STATUS_PROPOSED,
    VALID_STATUSES,
    build_promotion_decision,
    check_demotion,
    create_experiment,
    evaluate_promotion,
    format_experiment_markdown,
    format_promotion_decision_markdown,
    validate_experiment,
)


# ---------------------------------------------------------------------------
# Fixtures / builders
# ---------------------------------------------------------------------------

def _minimal_promotion_criteria(**overrides) -> dict:
    base = {
        "min_filled_trade_count": 20,
        "min_observation_count": 50,
        "min_expectancy_after_costs": 0.001,
        "no_risk_limit_breach": True,
        "no_operational_failures": True,
        "human_approval_required": True,
    }
    base.update(overrides)
    return base


def _minimal_demotion_criteria(**overrides) -> dict:
    base = {
        "max_drawdown_pct": -0.05,
        "max_consecutive_losses": 5,
        "min_expectancy_after_costs": -0.005,
    }
    base.update(overrides)
    return base


def _make_experiment(**overrides) -> dict:
    defaults = dict(
        hypothesis="Lowering breadth_threshold from 0.55 to 0.50 increases fills",
        affected_trigger_or_rule="BREADTH_TREND",
        expected_benefit="Est. 5-10 pct more fills in moderate breadth regime",
        risk="May increase false positives in weak markets",
        required_sample_size=50,
        promotion_criteria=_minimal_promotion_criteria(),
        demotion_criteria=_minimal_demotion_criteria(),
        experiment_id="exp-test-001",
        created_at="2026-01-01T00:00:00Z",
    )
    defaults.update(overrides)
    return create_experiment(**defaults)


def _make_passing_evaluation(experiment: dict) -> dict:
    return evaluate_promotion(
        experiment,
        filled_trade_count=25,
        observation_count=60,
        expectancy_after_costs=0.005,
        strategy_period_return_pct=0.08,
        spy_period_return_pct=0.05,
        bil_period_return_pct=0.01,
        risk_limit_breaches=[],
        operational_failures=[],
        drawdown=-0.02,
        consecutive_losses=1,
    )


# ---------------------------------------------------------------------------
# validate_experiment
# ---------------------------------------------------------------------------

class TestValidateExperiment:
    def test_valid_experiment_passes(self):
        exp = _make_experiment()
        ok, errors = validate_experiment(exp)
        assert ok is True
        assert errors == []

    def test_missing_hypothesis_fails(self):
        exp = _make_experiment()
        del exp["hypothesis"]
        ok, errors = validate_experiment(exp)
        assert ok is False
        assert any("hypothesis" in e for e in errors)

    def test_missing_affected_trigger_fails(self):
        exp = _make_experiment()
        del exp["affected_trigger_or_rule"]
        ok, errors = validate_experiment(exp)
        assert ok is False

    def test_missing_expected_benefit_fails(self):
        exp = _make_experiment()
        del exp["expected_benefit"]
        ok, errors = validate_experiment(exp)
        assert ok is False

    def test_missing_risk_fails(self):
        exp = _make_experiment()
        del exp["risk"]
        ok, errors = validate_experiment(exp)
        assert ok is False

    def test_empty_hypothesis_fails(self):
        exp = _make_experiment()
        exp["hypothesis"] = ""
        ok, errors = validate_experiment(exp)
        assert ok is False

    def test_zero_sample_size_fails(self):
        exp = _make_experiment(required_sample_size=1)
        exp["required_sample_size"] = 0
        ok, errors = validate_experiment(exp)
        assert ok is False

    def test_negative_sample_size_fails(self):
        exp = _make_experiment(required_sample_size=1)
        exp["required_sample_size"] = -5
        ok, errors = validate_experiment(exp)
        assert ok is False

    def test_non_numeric_sample_size_fails(self):
        exp = _make_experiment()
        exp["required_sample_size"] = "many"
        ok, errors = validate_experiment(exp)
        assert ok is False

    def test_missing_promotion_criteria_fails(self):
        exp = _make_experiment()
        del exp["promotion_criteria"]
        ok, errors = validate_experiment(exp)
        assert ok is False

    def test_missing_demotion_criteria_fails(self):
        exp = _make_experiment()
        del exp["demotion_criteria"]
        ok, errors = validate_experiment(exp)
        assert ok is False

    def test_promotion_criteria_missing_human_approval_field_fails(self):
        # create_experiment merges defaults, so mutate the dict after creation
        exp = _make_experiment()
        del exp["promotion_criteria"]["human_approval_required"]
        ok, errors = validate_experiment(exp)
        assert ok is False
        assert any("human_approval_required" in e for e in errors)

    def test_human_approval_required_false_fails(self):
        """human_approval_required cannot be waived."""
        exp = _make_experiment()
        exp["promotion_criteria"]["human_approval_required"] = False
        ok, errors = validate_experiment(exp)
        assert ok is False
        assert any("cannot be waived" in e or "human_approval_required" in e
                   for e in errors)

    def test_min_fills_below_absolute_floor_fails(self):
        pc = _minimal_promotion_criteria(min_filled_trade_count=ABSOLUTE_MIN_FILLS - 1)
        exp = _make_experiment(promotion_criteria=pc)
        ok, errors = validate_experiment(exp)
        assert ok is False
        assert any(str(ABSOLUTE_MIN_FILLS) in e for e in errors)

    def test_min_fills_at_absolute_floor_passes(self):
        pc = _minimal_promotion_criteria(min_filled_trade_count=ABSOLUTE_MIN_FILLS)
        exp = _make_experiment(promotion_criteria=pc)
        ok, errors = validate_experiment(exp)
        assert ok is True

    def test_demotion_criteria_missing_field_fails(self):
        # create_experiment merges defaults, so mutate the dict after creation
        exp = _make_experiment()
        del exp["demotion_criteria"]["max_drawdown_pct"]
        ok, errors = validate_experiment(exp)
        assert ok is False
        assert any("max_drawdown_pct" in e for e in errors)

    def test_promotion_criteria_not_dict_fails(self):
        exp = _make_experiment()
        exp["promotion_criteria"] = "not a dict"
        ok, errors = validate_experiment(exp)
        assert ok is False

    def test_demotion_criteria_not_dict_fails(self):
        exp = _make_experiment()
        exp["demotion_criteria"] = 42
        ok, errors = validate_experiment(exp)
        assert ok is False

    def test_multiple_errors_reported(self):
        exp = {}
        ok, errors = validate_experiment(exp)
        assert ok is False
        assert len(errors) > 1


# ---------------------------------------------------------------------------
# create_experiment
# ---------------------------------------------------------------------------

class TestCreateExperiment:
    def test_returns_dict(self):
        assert isinstance(_make_experiment(), dict)

    def test_has_experiment_id(self):
        assert _make_experiment()["experiment_id"] == "exp-test-001"

    def test_auto_generates_id_when_omitted(self):
        exp = create_experiment(
            hypothesis="Test hypothesis",
            affected_trigger_or_rule="X",
            expected_benefit="Y",
            risk="Z",
            required_sample_size=20,
            promotion_criteria=_minimal_promotion_criteria(),
            demotion_criteria=_minimal_demotion_criteria(),
        )
        assert exp["experiment_id"].startswith("exp-")

    def test_status_is_proposed(self):
        assert _make_experiment()["status"] == STATUS_PROPOSED

    def test_has_experiment_hash(self):
        h = _make_experiment()["experiment_hash"]
        assert isinstance(h, str) and len(h) > 0

    def test_hash_changes_with_different_hypothesis(self):
        e1 = _make_experiment(hypothesis="hypothesis one", experiment_id=None)
        e2 = _make_experiment(hypothesis="hypothesis two", experiment_id=None)
        assert e1["experiment_hash"] != e2["experiment_hash"]

    def test_production_mutation_allowed_always_false(self):
        """Core safety invariant."""
        assert _make_experiment()["production_mutation_allowed"] is False

    def test_human_approval_required_always_true(self):
        """Caller cannot waive human approval."""
        pc = _minimal_promotion_criteria(human_approval_required=False)
        exp = create_experiment(
            hypothesis="h", affected_trigger_or_rule="T",
            expected_benefit="b", risk="r",
            required_sample_size=20,
            promotion_criteria=pc,
            demotion_criteria=_minimal_demotion_criteria(),
        )
        assert exp["promotion_criteria"]["human_approval_required"] is True

    def test_promotion_criteria_merged_with_defaults(self):
        pc = {"min_filled_trade_count": 30}
        exp = create_experiment(
            hypothesis="h", affected_trigger_or_rule="T",
            expected_benefit="b", risk="r",
            required_sample_size=20,
            promotion_criteria=pc,
            demotion_criteria=_minimal_demotion_criteria(),
        )
        assert exp["promotion_criteria"]["min_filled_trade_count"] == 30
        assert "min_observation_count" in exp["promotion_criteria"]
        assert "min_expectancy_after_costs" in exp["promotion_criteria"]

    def test_demotion_criteria_merged_with_defaults(self):
        dc = {"max_drawdown_pct": -0.08}
        exp = create_experiment(
            hypothesis="h", affected_trigger_or_rule="T",
            expected_benefit="b", risk="r",
            required_sample_size=20,
            promotion_criteria=_minimal_promotion_criteria(),
            demotion_criteria=dc,
        )
        assert exp["demotion_criteria"]["max_drawdown_pct"] == -0.08
        assert "max_consecutive_losses" in exp["demotion_criteria"]

    def test_candidate_patch_stored(self):
        patch = {"file": "config/strategy.json", "key": "parameters.breadth_threshold",
                 "old_value": 0.55, "new_value": 0.50}
        exp = _make_experiment(candidate_patch=patch)
        assert exp["candidate_patch"]["key"] == "parameters.breadth_threshold"

    def test_candidate_patch_defaults_to_empty(self):
        exp = _make_experiment()
        assert exp["candidate_patch"] == {}

    def test_required_backtest_defaults_true(self):
        assert _make_experiment()["required_backtest"] is True

    def test_required_paper_validation_defaults_true(self):
        assert _make_experiment()["required_paper_validation"] is True

    def test_schema_version_present(self):
        assert "schema_version" in _make_experiment()

    def test_all_core_fields_present(self):
        exp = _make_experiment()
        for field in (
            "hypothesis", "affected_trigger_or_rule", "expected_benefit",
            "risk", "required_sample_size", "promotion_criteria",
            "demotion_criteria", "created_at", "status",
        ):
            assert field in exp, f"Missing field: {field}"


# ---------------------------------------------------------------------------
# evaluate_promotion
# ---------------------------------------------------------------------------

class TestEvaluatePromotion:
    def test_returns_dict(self):
        assert isinstance(evaluate_promotion(_make_experiment()), dict)

    def test_experiment_id_propagated(self):
        ev = evaluate_promotion(_make_experiment())
        assert ev["experiment_id"] == "exp-test-001"

    def test_production_mutation_allowed_always_false(self):
        ev = _make_passing_evaluation(_make_experiment())
        assert ev["production_mutation_allowed"] is False

    def test_human_approval_required_always_true(self):
        ev = _make_passing_evaluation(_make_experiment())
        assert ev["human_approval_required"] is True

    def test_promotion_ready_always_false(self):
        """evaluate_promotion never grants promotion automatically."""
        ev = _make_passing_evaluation(_make_experiment())
        assert ev["all_promotion_criteria_met"] is True
        assert ev["promotion_ready"] is False  # invariant

    def test_human_approved_always_false(self):
        ev = _make_passing_evaluation(_make_experiment())
        assert ev["human_approved"] is False

    def test_decision_starts_as_pending(self):
        ev = evaluate_promotion(_make_experiment())
        assert ev["decision"] == DECISION_PENDING

    def test_protected_files_listed(self):
        ev = evaluate_promotion(_make_experiment())
        for f in PROTECTED_CONFIG_FILES:
            assert f in ev["protected_files"]

    def test_fills_criteria_met_when_sufficient(self):
        ev = evaluate_promotion(_make_experiment(), filled_trade_count=25)
        assert ev["criteria_met"]["min_filled_trade_count"] is True

    def test_fills_criteria_not_met_when_insufficient(self):
        ev = evaluate_promotion(_make_experiment(), filled_trade_count=5)
        assert ev["criteria_met"]["min_filled_trade_count"] is False

    def test_observation_criteria_met(self):
        ev = evaluate_promotion(_make_experiment(), observation_count=55)
        assert ev["criteria_met"]["min_observation_count"] is True

    def test_observation_criteria_not_met(self):
        ev = evaluate_promotion(_make_experiment(), observation_count=10)
        assert ev["criteria_met"]["min_observation_count"] is False

    def test_expectancy_criteria_met(self):
        ev = evaluate_promotion(_make_experiment(), expectancy_after_costs=0.005)
        assert ev["criteria_met"]["positive_expectancy_after_costs"] is True

    def test_expectancy_criteria_not_met_when_none(self):
        ev = evaluate_promotion(_make_experiment(), expectancy_after_costs=None)
        assert ev["criteria_met"]["positive_expectancy_after_costs"] is False

    def test_expectancy_criteria_not_met_when_negative(self):
        ev = evaluate_promotion(_make_experiment(), expectancy_after_costs=-0.001)
        assert ev["criteria_met"]["positive_expectancy_after_costs"] is False

    def test_risk_breach_fails_criteria(self):
        ev = evaluate_promotion(
            _make_experiment(),
            risk_limit_breaches=["RISK_LIMITS_RESPECTED"],
        )
        assert ev["criteria_met"]["no_risk_limit_breach"] is False

    def test_no_breach_passes(self):
        ev = evaluate_promotion(_make_experiment(), risk_limit_breaches=[])
        assert ev["criteria_met"]["no_risk_limit_breach"] is True

    def test_operational_failure_fails_criteria(self):
        ev = evaluate_promotion(
            _make_experiment(),
            operational_failures=["order_rejected"],
        )
        assert ev["criteria_met"]["no_operational_failures"] is False

    def test_beats_spy_computed_when_both_present(self):
        ev = evaluate_promotion(
            _make_experiment(),
            strategy_period_return_pct=0.08,
            spy_period_return_pct=0.05,
        )
        assert ev["evidence"]["beats_spy"] is True

    def test_beats_spy_false_when_underperforms(self):
        ev = evaluate_promotion(
            _make_experiment(),
            strategy_period_return_pct=0.03,
            spy_period_return_pct=0.05,
        )
        assert ev["evidence"]["beats_spy"] is False

    def test_beats_spy_none_when_missing_data(self):
        ev = evaluate_promotion(_make_experiment())
        assert ev["evidence"]["beats_spy"] is None

    def test_beats_bil_computed(self):
        ev = evaluate_promotion(
            _make_experiment(),
            strategy_period_return_pct=0.06,
            bil_period_return_pct=0.01,
        )
        assert ev["evidence"]["beats_bil"] is True

    def test_must_beat_bil_requirement_checked(self):
        pc = _minimal_promotion_criteria(must_beat_bil=True)
        exp = _make_experiment(promotion_criteria=pc)
        ev = evaluate_promotion(
            exp,
            filled_trade_count=25, observation_count=60,
            expectancy_after_costs=0.005,
            strategy_period_return_pct=0.06,
            bil_period_return_pct=0.01,
        )
        assert ev["criteria_met"]["beats_bil"] is True

    def test_must_beat_bil_fails_when_below(self):
        pc = _minimal_promotion_criteria(must_beat_bil=True)
        exp = _make_experiment(promotion_criteria=pc)
        ev = evaluate_promotion(
            exp,
            filled_trade_count=25, observation_count=60,
            expectancy_after_costs=0.005,
            strategy_period_return_pct=0.005,
            bil_period_return_pct=0.01,
        )
        assert ev["criteria_met"]["beats_bil"] is False

    def test_must_beat_spy_off_by_default(self):
        """must_beat_spy defaults False — criteria_met.beats_spy = True regardless."""
        pc = _minimal_promotion_criteria(must_beat_spy=False)
        exp = _make_experiment(promotion_criteria=pc)
        ev = evaluate_promotion(
            exp,
            filled_trade_count=25, observation_count=60,
            expectancy_after_costs=0.005,
            strategy_period_return_pct=0.01,
            spy_period_return_pct=0.08,  # strategy underperforms SPY
        )
        assert ev["criteria_met"]["beats_spy"] is True  # requirement not active

    def test_all_criteria_met_true_when_everything_passes(self):
        ev = _make_passing_evaluation(_make_experiment())
        assert ev["all_promotion_criteria_met"] is True

    def test_all_criteria_met_false_when_any_fails(self):
        ev = evaluate_promotion(
            _make_experiment(),
            filled_trade_count=5,   # too few
            observation_count=60,
            expectancy_after_costs=0.005,
        )
        assert ev["all_promotion_criteria_met"] is False

    def test_pr_instructions_present(self):
        ev = evaluate_promotion(_make_experiment())
        pr = ev["candidate_pr_instructions"]
        assert isinstance(pr, str) and len(pr) > 0

    def test_pr_instructions_mention_experiment_id(self):
        ev = evaluate_promotion(_make_experiment())
        assert "exp-test-001" in ev["candidate_pr_instructions"]

    def test_pr_instructions_mention_no_config_modified(self):
        ev = evaluate_promotion(_make_experiment())
        assert "no config" in ev["candidate_pr_instructions"].lower()

    def test_pr_instructions_include_patch_details(self):
        patch = {
            "file": "config/strategy.json",
            "key": "parameters.breadth_threshold",
            "old_value": 0.55,
            "new_value": 0.50,
        }
        exp = _make_experiment(candidate_patch=patch)
        ev = evaluate_promotion(exp)
        pr = ev["candidate_pr_instructions"]
        assert "config/strategy.json" in pr
        assert "breadth_threshold" in pr


# ---------------------------------------------------------------------------
# evaluate_promotion — demotion checks
# ---------------------------------------------------------------------------

class TestDemotionChecks:
    def test_no_demotion_when_healthy(self):
        ev = evaluate_promotion(
            _make_experiment(),
            drawdown=-0.01,
            consecutive_losses=1,
            expectancy_after_costs=0.005,
        )
        assert ev["demotion_triggered"] is False
        assert ev["demotion_reasons"] == []

    def test_demotion_triggered_by_drawdown(self):
        ev = evaluate_promotion(
            _make_experiment(),
            drawdown=-0.06,  # exceeds default -0.05
        )
        assert ev["demotion_triggered"] is True
        assert any("drawdown" in r for r in ev["demotion_reasons"])

    def test_demotion_triggered_by_consecutive_losses(self):
        ev = evaluate_promotion(
            _make_experiment(),
            consecutive_losses=5,  # hits default max=5
        )
        assert ev["demotion_triggered"] is True
        assert any("consecutive_losses" in r for r in ev["demotion_reasons"])

    def test_demotion_triggered_by_negative_expectancy_floor(self):
        ev = evaluate_promotion(
            _make_experiment(),
            expectancy_after_costs=-0.006,  # below default floor -0.005
        )
        assert ev["demotion_triggered"] is True
        assert any("expectancy" in r for r in ev["demotion_reasons"])

    def test_multiple_demotion_reasons_collected(self):
        ev = evaluate_promotion(
            _make_experiment(),
            drawdown=-0.10,
            consecutive_losses=8,
            expectancy_after_costs=-0.01,
        )
        assert ev["demotion_triggered"] is True
        assert len(ev["demotion_reasons"]) >= 2

    def test_custom_demotion_thresholds_respected(self):
        dc = _minimal_demotion_criteria(max_drawdown_pct=-0.03)
        exp = _make_experiment(demotion_criteria=dc)
        ev = evaluate_promotion(exp, drawdown=-0.04)
        assert ev["demotion_triggered"] is True

    def test_drawdown_exactly_at_threshold_triggers(self):
        dc = _minimal_demotion_criteria(max_drawdown_pct=-0.05)
        exp = _make_experiment(demotion_criteria=dc)
        ev = evaluate_promotion(exp, drawdown=-0.05)
        assert ev["demotion_triggered"] is True

    def test_drawdown_just_above_threshold_no_trigger(self):
        dc = _minimal_demotion_criteria(max_drawdown_pct=-0.05)
        exp = _make_experiment(demotion_criteria=dc)
        ev = evaluate_promotion(exp, drawdown=-0.04)
        assert ev["demotion_triggered"] is False


# ---------------------------------------------------------------------------
# check_demotion
# ---------------------------------------------------------------------------

class TestCheckDemotion:
    def test_triggered_when_evaluation_triggered(self):
        ev = evaluate_promotion(_make_experiment(), drawdown=-0.10)
        result = check_demotion(_make_experiment(), ev)
        assert result["triggered"] is True

    def test_not_triggered_when_healthy(self):
        ev = evaluate_promotion(_make_experiment(), drawdown=-0.01)
        result = check_demotion(_make_experiment(), ev)
        assert result["triggered"] is False

    def test_recommendation_terminate_when_triggered(self):
        ev = evaluate_promotion(_make_experiment(), drawdown=-0.10)
        result = check_demotion(_make_experiment(), ev)
        assert "terminate" in result["recommendation"].lower() or \
               "reject" in result["recommendation"].lower()

    def test_recommendation_continue_when_not_triggered(self):
        ev = evaluate_promotion(_make_experiment(), drawdown=-0.01)
        result = check_demotion(_make_experiment(), ev)
        assert "continue" in result["recommendation"].lower()

    def test_production_mutation_allowed_false(self):
        ev = evaluate_promotion(_make_experiment())
        result = check_demotion(_make_experiment(), ev)
        assert result["production_mutation_allowed"] is False


# ---------------------------------------------------------------------------
# build_promotion_decision
# ---------------------------------------------------------------------------

class TestBuildPromotionDecision:
    def test_approved_decision(self):
        exp = _make_experiment()
        ev = _make_passing_evaluation(exp)
        decision = build_promotion_decision(
            exp, ev,
            decision=DECISION_APPROVED,
            approved_by="operator-alice",
            approval_notes="Evidence is sufficient.",
        )
        assert decision["decision"] == DECISION_APPROVED
        assert decision["human_approved"] is True
        assert decision["approved_by"] == "operator-alice"

    def test_rejected_decision(self):
        exp = _make_experiment()
        ev = evaluate_promotion(exp)
        decision = build_promotion_decision(
            exp, ev,
            decision=DECISION_REJECTED,
            approval_notes="Insufficient fills.",
        )
        assert decision["decision"] == DECISION_REJECTED
        assert decision["human_approved"] is False

    def test_production_mutation_allowed_always_false_on_approved(self):
        """Core safety invariant: even an approved decision cannot mutate config."""
        exp = _make_experiment()
        ev = _make_passing_evaluation(exp)
        decision = build_promotion_decision(
            exp, ev,
            decision=DECISION_APPROVED,
            approved_by="operator",
        )
        assert decision["production_mutation_allowed"] is False

    def test_production_mutation_allowed_always_false_on_rejected(self):
        exp = _make_experiment()
        ev = evaluate_promotion(exp)
        decision = build_promotion_decision(exp, ev, decision=DECISION_REJECTED)
        assert decision["production_mutation_allowed"] is False

    def test_approve_without_approved_by_raises(self):
        exp = _make_experiment()
        ev = _make_passing_evaluation(exp)
        with pytest.raises(ValueError, match="approved_by"):
            build_promotion_decision(exp, ev, decision=DECISION_APPROVED)

    def test_approve_with_blank_approved_by_raises(self):
        exp = _make_experiment()
        ev = _make_passing_evaluation(exp)
        with pytest.raises(ValueError):
            build_promotion_decision(
                exp, ev, decision=DECISION_APPROVED, approved_by="   "
            )

    def test_invalid_decision_value_raises(self):
        exp = _make_experiment()
        ev = evaluate_promotion(exp)
        with pytest.raises(ValueError, match="approved.*rejected"):
            build_promotion_decision(exp, ev, decision="maybe")

    def test_protected_files_listed(self):
        exp = _make_experiment()
        ev = evaluate_promotion(exp)
        decision = build_promotion_decision(exp, ev, decision=DECISION_REJECTED)
        for f in PROTECTED_CONFIG_FILES:
            assert f in decision["protected_files"]

    def test_evidence_summary_included(self):
        exp = _make_experiment()
        ev = _make_passing_evaluation(exp)
        decision = build_promotion_decision(
            exp, ev, decision=DECISION_APPROVED, approved_by="op"
        )
        assert "filled_trade_count" in decision["evidence_summary"]
        assert "expectancy_after_costs" in decision["evidence_summary"]

    def test_experiment_id_propagated(self):
        exp = _make_experiment()
        ev = evaluate_promotion(exp)
        decision = build_promotion_decision(exp, ev, decision=DECISION_REJECTED)
        assert decision["experiment_id"] == "exp-test-001"

    def test_demotion_triggered_propagated(self):
        exp = _make_experiment()
        ev = evaluate_promotion(exp, drawdown=-0.10)
        decision = build_promotion_decision(exp, ev, decision=DECISION_REJECTED)
        assert decision["demotion_triggered"] is True

    def test_all_criteria_met_propagated(self):
        exp = _make_experiment()
        ev = _make_passing_evaluation(exp)
        decision = build_promotion_decision(
            exp, ev, decision=DECISION_APPROVED, approved_by="op"
        )
        assert decision["all_promotion_criteria_met"] is True


# ---------------------------------------------------------------------------
# format functions
# ---------------------------------------------------------------------------

class TestFormatExperimentMarkdown:
    def test_returns_string(self):
        md = format_experiment_markdown(_make_experiment())
        assert isinstance(md, str)

    def test_contains_experiment_id(self):
        md = format_experiment_markdown(_make_experiment())
        assert "exp-test-001" in md

    def test_contains_hypothesis(self):
        md = format_experiment_markdown(_make_experiment())
        assert "breadth_threshold" in md

    def test_contains_safety_note(self):
        md = format_experiment_markdown(_make_experiment())
        assert "production_mutation_allowed=False" in md

    def test_contains_separator(self):
        md = format_experiment_markdown(_make_experiment())
        assert "---" in md

    def test_candidate_patch_shown_when_present(self):
        patch = {"file": "config/strategy.json", "key": "parameters.x",
                 "old_value": 1, "new_value": 2}
        exp = _make_experiment(candidate_patch=patch)
        md = format_experiment_markdown(exp)
        assert "config/strategy.json" in md
        assert "parameters.x" in md

    def test_notes_shown_when_present(self):
        exp = _make_experiment(notes="Initial proposal based on breadth analysis.")
        md = format_experiment_markdown(exp)
        assert "Initial proposal" in md

    def test_empty_dict_does_not_raise(self):
        md = format_experiment_markdown({})
        assert isinstance(md, str)


class TestFormatPromotionDecisionMarkdown:
    def test_returns_string(self):
        exp = _make_experiment()
        ev = evaluate_promotion(exp)
        decision = build_promotion_decision(exp, ev, decision=DECISION_REJECTED)
        md = format_promotion_decision_markdown(decision)
        assert isinstance(md, str)

    def test_contains_experiment_id(self):
        exp = _make_experiment()
        ev = evaluate_promotion(exp)
        decision = build_promotion_decision(exp, ev, decision=DECISION_REJECTED)
        md = format_promotion_decision_markdown(decision)
        assert "exp-test-001" in md

    def test_decision_shown_as_uppercase(self):
        exp = _make_experiment()
        ev = evaluate_promotion(exp)
        decision = build_promotion_decision(exp, ev, decision=DECISION_REJECTED)
        md = format_promotion_decision_markdown(decision)
        assert "REJECTED" in md

    def test_approved_by_shown(self):
        exp = _make_experiment()
        ev = _make_passing_evaluation(exp)
        decision = build_promotion_decision(
            exp, ev, decision=DECISION_APPROVED, approved_by="operator-bob"
        )
        md = format_promotion_decision_markdown(decision)
        assert "operator-bob" in md

    def test_safety_note_present(self):
        exp = _make_experiment()
        ev = evaluate_promotion(exp)
        decision = build_promotion_decision(exp, ev, decision=DECISION_REJECTED)
        md = format_promotion_decision_markdown(decision)
        assert "production_mutation_allowed=False" in md

    def test_empty_dict_does_not_raise(self):
        md = format_promotion_decision_markdown({})
        assert isinstance(md, str)


# ---------------------------------------------------------------------------
# Safety invariants — module-level
# ---------------------------------------------------------------------------

class TestModuleSafetyInvariants:
    def test_production_mutation_allowed_false_in_experiment(self):
        assert _make_experiment()["production_mutation_allowed"] is False

    def test_production_mutation_allowed_false_in_evaluation(self):
        assert evaluate_promotion(_make_experiment())["production_mutation_allowed"] is False

    def test_production_mutation_allowed_false_in_approved_decision(self):
        exp = _make_experiment()
        ev = _make_passing_evaluation(exp)
        decision = build_promotion_decision(
            exp, ev, decision=DECISION_APPROVED, approved_by="op"
        )
        assert decision["production_mutation_allowed"] is False

    def test_production_mutation_allowed_false_in_demotion(self):
        ev = evaluate_promotion(_make_experiment())
        result = check_demotion(_make_experiment(), ev)
        assert result["production_mutation_allowed"] is False

    def test_human_approval_required_invariant_in_experiment(self):
        exp = _make_experiment()
        assert exp["promotion_criteria"]["human_approval_required"] is True

    def test_human_approval_required_invariant_in_evaluation(self):
        ev = evaluate_promotion(_make_experiment())
        assert ev["human_approval_required"] is True

    def test_promotion_ready_always_false_from_evaluate(self):
        """evaluate_promotion never auto-promotes."""
        ev = _make_passing_evaluation(_make_experiment())
        assert ev["promotion_ready"] is False

    def test_human_approved_always_false_from_evaluate(self):
        ev = _make_passing_evaluation(_make_experiment())
        assert ev["human_approved"] is False

    def test_no_execute_paper_import(self):
        import importlib
        mod = importlib.import_module("trading_os.research.experiment_governance")
        assert not hasattr(mod, "execute_paper")
        assert not hasattr(mod, "submit_order")
        assert not hasattr(mod, "place_order")

    def test_no_execution_symbols_in_source(self):
        import inspect
        import trading_os.research.experiment_governance as mod
        src = inspect.getsource(mod)
        assert "execute_paper" not in src
        assert "ENABLE_PAPER_EXECUTION" not in src
        assert "submit_order" not in src

    def test_protected_files_listed_in_evaluation(self):
        ev = evaluate_promotion(_make_experiment())
        for f in PROTECTED_CONFIG_FILES:
            assert f in ev["protected_files"]

    def test_protected_files_listed_in_decision(self):
        exp = _make_experiment()
        ev = evaluate_promotion(exp)
        decision = build_promotion_decision(exp, ev, decision=DECISION_REJECTED)
        for f in PROTECTED_CONFIG_FILES:
            assert f in decision["protected_files"]

    def test_no_config_files_modified(self):
        """Calling all major functions does not touch any protected config."""
        import os
        root = Path(__file__).resolve().parents[1]
        protected = [root / f for f in PROTECTED_CONFIG_FILES]
        mtimes_before = {p: p.stat().st_mtime for p in protected if p.exists()}

        exp = _make_experiment()
        ev = _make_passing_evaluation(exp)
        build_promotion_decision(
            exp, ev, decision=DECISION_APPROVED, approved_by="test-op"
        )
        check_demotion(exp, ev)
        format_experiment_markdown(exp)
        format_promotion_decision_markdown(
            build_promotion_decision(exp, ev, decision=DECISION_REJECTED)
        )

        mtimes_after = {p: p.stat().st_mtime for p in protected if p.exists()}
        assert mtimes_before == mtimes_after, (
            "A protected config file was modified during tests"
        )


# ---------------------------------------------------------------------------
# Experiments cannot be auto-promoted — integration checks
# ---------------------------------------------------------------------------

class TestNoAutoPromotion:
    def test_even_perfect_evaluation_does_not_auto_promote(self):
        exp = _make_experiment()
        ev = evaluate_promotion(
            exp,
            filled_trade_count=100,
            observation_count=500,
            expectancy_after_costs=0.05,
            strategy_period_return_pct=0.20,
            spy_period_return_pct=0.10,
            bil_period_return_pct=0.02,
            risk_limit_breaches=[],
            operational_failures=[],
            drawdown=-0.005,
            consecutive_losses=0,
        )
        assert ev["all_promotion_criteria_met"] is True
        assert ev["promotion_ready"] is False      # still False
        assert ev["human_approved"] is False        # still False
        assert ev["production_mutation_allowed"] is False

    def test_approved_decision_does_not_claim_to_mutate_config(self):
        exp = _make_experiment()
        ev = _make_passing_evaluation(exp)
        decision = build_promotion_decision(
            exp, ev,
            decision=DECISION_APPROVED,
            approved_by="operator",
            approval_notes="Approved after review.",
        )
        # Even an explicit approval does not grant config mutation
        assert decision["production_mutation_allowed"] is False
        # The PR instructions guide the operator to do it manually
        pr = decision["candidate_pr_instructions"]
        assert "REMINDER" in pr or "no config" in pr.lower()
