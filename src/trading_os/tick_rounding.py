"""US equity/ETF limit price tick-rounding utility.

Alpaca (and US equity markets generally) enforce minimum price increments:
  - price >= $1.00  → penny increments (2 decimal places)
  - price <  $1.00  → sub-penny increments (4 decimal places)

Rounding policy (both buy and sell): ROUND_HALF_UP
  Round to the nearest valid tick; ties go up.
  This is the simplest deterministic rule, avoids broker rejection, and is
  appropriate for notional-based limit orders where the price is a cap/floor
  rather than an exact fill target.

All arithmetic uses decimal.Decimal to avoid floating-point formatting
artifacts (e.g. 1078.765 represented as 1078.7649999... in float).
"""
from __future__ import annotations

from decimal import ROUND_HALF_UP, Decimal, InvalidOperation
from typing import Optional

_TICK_GTE_ONE = Decimal("0.01")
_TICK_LT_ONE = Decimal("0.0001")
_ONE = Decimal("1.00")


def _tick_size(price_decimal: Decimal) -> Decimal:
    return _TICK_GTE_ONE if price_decimal >= _ONE else _TICK_LT_ONE


def round_to_tick(price: float, side: str = "buy") -> Decimal:
    """Round *price* to the nearest valid US equity/ETF tick.

    Args:
        price:  Raw limit price (float or int).  Must be positive.
        side:   "buy" or "sell" — accepted but does not change the rounding
                rule (both use ROUND_HALF_UP; see module docstring).

    Returns:
        Decimal rounded to the appropriate tick increment.

    Raises:
        ValueError  if price <= 0 or cannot be parsed.
    """
    try:
        d = Decimal(str(price))
    except InvalidOperation as exc:
        raise ValueError(f"cannot parse limit_price {price!r}: {exc}") from exc

    if d.is_nan() or d.is_infinite():
        raise ValueError(f"limit_price must be finite, got {price!r}")

    if d <= 0:
        raise ValueError(
            f"limit_price must be positive, got {price!r}"
        )

    tick = _tick_size(d)
    return d.quantize(tick, rounding=ROUND_HALF_UP)


def validate_tick_price(price: float) -> Optional[str]:
    """Return an error string if *price* is not a valid US equity/ETF tick, else None.

    A price is valid if it has at most 2 decimal places (price >= $1) or
    at most 4 decimal places (price < $1), and is strictly positive.
    """
    try:
        d = Decimal(str(price))
    except (InvalidOperation, TypeError, ValueError):
        return f"cannot parse price {price!r}"

    if d <= 0:
        return f"price must be positive, got {price}"

    tick = _tick_size(d)
    try:
        rounded = d.quantize(tick, rounding=ROUND_HALF_UP)
    except Exception:
        return f"cannot quantize price {price!r}"

    if d != rounded:
        places = "2" if d >= _ONE else "4"
        return (
            f"sub-tick increment: {price} has more than {places} decimal places "
            f"(rounded to {rounded})"
        )
    return None
