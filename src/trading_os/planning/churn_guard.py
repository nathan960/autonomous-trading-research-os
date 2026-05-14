"""Churn guard: cooldown and daily order-count controls for paper trading.

Pure functions only — no I/O, no network calls, no secrets.
build_trade_plan calls filter_churn_blocked to enforce:
  - per-symbol buy/sell cooldown minutes
  - same-day roundtrip cooldown
  - max orders per symbol per day
  - max total paper orders per day

gate_daily_order_limits in execution_gates.py provides defense in depth.

Skip reason codes:
  recent_same_symbol_buy        — buy within buy cooldown window
  recent_same_symbol_sell       — sell within sell cooldown window
  same_day_roundtrip_block      — both buy and sell on same calendar day
  max_orders_per_symbol_per_day — per-symbol daily cap reached
  max_total_orders_per_day      — global daily cap reached
"""
from __future__ import annotations

from typing import Optional


# ---------------------------------------------------------------------------
# Timestamp helpers
# ---------------------------------------------------------------------------

def _date_str(iso: str) -> str:
    """Extract YYYY-MM-DD from ISO timestamp; empty string on failure."""
    return iso[:10] if iso and len(iso) >= 10 else ""


def _minutes_since(past_iso: str, now_iso: str) -> Optional[float]:
    """Minutes elapsed between past_iso and now_iso.  None if unparseable."""
    if not past_iso or not now_iso:
        return None
    try:
        from datetime import datetime, timezone

        def _parse(s: str) -> datetime:
            return datetime.fromisoformat(s.replace("Z", "+00:00"))

        delta = _parse(now_iso) - _parse(past_iso)
        return delta.total_seconds() / 60.0
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Lifecycle list filters
# ---------------------------------------------------------------------------

def get_orders_today(lifecycles: list, today_str: str) -> list:
    """Return lifecycles whose submitted_at falls on today_str (YYYY-MM-DD)."""
    return [
        lc for lc in lifecycles
        if isinstance(lc, dict)
        and _date_str(lc.get("submitted_at", "")) == today_str
    ]


def get_symbol_orders_today(lifecycles: list, symbol: str, today_str: str) -> list:
    """Return lifecycles for symbol submitted on today_str."""
    return [
        lc for lc in get_orders_today(lifecycles, today_str)
        if lc.get("symbol") == symbol
    ]


def get_recent_orders(
    lifecycles: list,
    symbol: str,
    side: str,
    minutes: float,
    now_iso: str,
) -> list:
    """Return lifecycles for symbol/side submitted within the last N minutes."""
    result = []
    for lc in lifecycles:
        if not isinstance(lc, dict):
            continue
        if lc.get("symbol") != symbol:
            continue
        if lc.get("side") != side:
            continue
        elapsed = _minutes_since(lc.get("submitted_at", ""), now_iso)
        if elapsed is not None and 0 <= elapsed <= minutes:
            result.append(lc)
    return result


# ---------------------------------------------------------------------------
# Individual check functions
# ---------------------------------------------------------------------------

def check_symbol_cooldown(
    lifecycles: list,
    symbol: str,
    side: str,
    now_iso: str,
    risk_limits: dict,
) -> dict:
    """Check same-symbol buy or sell cooldown. Returns {passes, skip_reason}."""
    if side == "buy":
        cooldown_minutes = float(risk_limits.get("same_symbol_buy_cooldown_minutes", 0))
        skip_code = "recent_same_symbol_buy"
    elif side == "sell":
        cooldown_minutes = float(risk_limits.get("same_symbol_sell_cooldown_minutes", 0))
        skip_code = "recent_same_symbol_sell"
    else:
        return {"passes": True, "skip_reason": None}

    if cooldown_minutes <= 0:
        return {"passes": True, "skip_reason": None}

    recent = get_recent_orders(lifecycles, symbol, side, cooldown_minutes, now_iso)
    if recent:
        last_submitted = recent[-1].get("submitted_at", "?")
        return {
            "passes": False,
            "skip_reason": (
                f"{skip_code}({symbol},{side},last={last_submitted},"
                f"cooldown={int(cooldown_minutes)}min)"
            ),
        }
    return {"passes": True, "skip_reason": None}


def check_roundtrip_cooldown(
    lifecycles: list,
    symbol: str,
    today_str: str,
    risk_limits: dict,
) -> dict:
    """Block same-day roundtrip: if both buy and sell for symbol exist today, block.

    Applies to both buy and sell orders.
    """
    days = float(risk_limits.get("same_symbol_roundtrip_cooldown_days", 0))
    if days <= 0:
        return {"passes": True, "skip_reason": None}

    today_orders = get_symbol_orders_today(lifecycles, symbol, today_str)
    has_buy = any(lc.get("side") == "buy" for lc in today_orders)
    has_sell = any(lc.get("side") == "sell" for lc in today_orders)

    if has_buy and has_sell:
        return {
            "passes": False,
            "skip_reason": f"same_day_roundtrip_block({symbol},today={today_str})",
        }
    return {"passes": True, "skip_reason": None}


def check_daily_symbol_limit(
    lifecycles: list,
    symbol: str,
    today_str: str,
    risk_limits: dict,
) -> dict:
    """Block if symbol already has max_orders_per_symbol_per_day orders today."""
    limit = risk_limits.get("max_orders_per_symbol_per_day")
    if limit is None:
        return {"passes": True, "skip_reason": None}
    limit = int(limit)
    if limit <= 0:
        return {"passes": True, "skip_reason": None}

    count = len(get_symbol_orders_today(lifecycles, symbol, today_str))
    if count >= limit:
        return {
            "passes": False,
            "skip_reason": (
                f"max_orders_per_symbol_per_day({symbol},count={count},limit={limit})"
            ),
        }
    return {"passes": True, "skip_reason": None}


def check_daily_total_limit(
    lifecycles: list,
    today_str: str,
    risk_limits: dict,
) -> dict:
    """Block if total orders submitted today >= max_total_paper_orders_per_day."""
    limit = risk_limits.get("max_total_paper_orders_per_day")
    if limit is None:
        return {"passes": True, "skip_reason": None}
    limit = int(limit)
    if limit <= 0:
        return {"passes": True, "skip_reason": None}

    count = len(get_orders_today(lifecycles, today_str))
    if count >= limit:
        return {
            "passes": False,
            "skip_reason": f"max_total_orders_per_day(count={count},limit={limit})",
        }
    return {"passes": True, "skip_reason": None}


# ---------------------------------------------------------------------------
# Composite filter
# ---------------------------------------------------------------------------

def filter_churn_blocked(
    orders: list,
    lifecycles: list,
    risk_limits: dict,
    now_iso: str,
) -> tuple:
    """Split orders into (ok, churn_blocked) applying all cooldown/daily-limit rules.

    Blocked orders have skip_reason set.  Priority order:
      1. same_symbol_buy_cooldown_minutes / same_symbol_sell_cooldown_minutes
      2. same_symbol_roundtrip_cooldown_days
      3. max_orders_per_symbol_per_day
      4. max_total_paper_orders_per_day  (checked against existing lifecycle history)
    """
    today_str = _date_str(now_iso)
    ok: list = []
    blocked: list = []

    for o in orders:
        sym = o.get("symbol", "")
        side = o.get("side", "buy")

        # 1. Cooldown
        cd = check_symbol_cooldown(lifecycles, sym, side, now_iso, risk_limits)
        if not cd["passes"]:
            bo = dict(o)
            bo["skip_reason"] = cd["skip_reason"]
            blocked.append(bo)
            continue

        # 2. Roundtrip
        rt = check_roundtrip_cooldown(lifecycles, sym, today_str, risk_limits)
        if not rt["passes"]:
            bo = dict(o)
            bo["skip_reason"] = rt["skip_reason"]
            blocked.append(bo)
            continue

        # 3. Per-symbol daily limit
        sl = check_daily_symbol_limit(lifecycles, sym, today_str, risk_limits)
        if not sl["passes"]:
            bo = dict(o)
            bo["skip_reason"] = sl["skip_reason"]
            blocked.append(bo)
            continue

        ok.append(o)

    # 4. Global daily total — checks against existing history, not proposed orders
    total_check = check_daily_total_limit(lifecycles, today_str, risk_limits)
    if not total_check["passes"]:
        for o in ok:
            bo = dict(o)
            bo["skip_reason"] = total_check["skip_reason"]
            blocked.append(bo)
        ok = []

    return ok, blocked
