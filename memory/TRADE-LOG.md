# Trade Log

Execution attempts, submitted paper orders, skips, errors, and position-monitor outcomes are logged here.

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T15:31:20Z",
  "run_id": "execution-20260512T153120-a20828c0",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "3db855f6bc252467eed8d7675c053c1b94dddde0c5ae7bf5ada481935cd557be",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.02559465,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Position monitor completed

```json
{
  "drawdown": 0.0,
  "equity": 40000.0,
  "generated_at": "2026-05-12T15:31:20Z",
  "position_count": 0,
  "run_id": "position_monitor-20260512T153120-83bf6e24",
  "schema_version": "0.1.0",
  "status": "OK",
  "use_alpaca": false,
  "violations": []
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T15:31:30Z",
  "run_id": "execution-20260512T153129-86d9b9f0",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "781e14195cfc473146586404e3c3d9e8b38a2f06bfad35867b68bb43f158a0ed",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.01597525,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T15:32:53Z",
  "run_id": "execution-20260512T153253-0ba5873e",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "acc6818ef018c8530abf46de23e1ffc4400a4dbbb91ce543fda54c6929e4ca0e",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.023264183333333334,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Position monitor completed

```json
{
  "drawdown": 0.0,
  "equity": 40000.0,
  "generated_at": "2026-05-12T15:32:53Z",
  "position_count": 0,
  "run_id": "position_monitor-20260512T153253-f5b2f106",
  "schema_version": "0.1.0",
  "status": "OK",
  "use_alpaca": false,
  "violations": []
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T15:33:05Z",
  "run_id": "execution-20260512T153305-15251a6c",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "209321ee8bfc8308e88d3f37670894bc67fdc87e7ea8621a81b6ded9262aaa5e",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.013966983333333332,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Position monitor completed

```json
{
  "drawdown": 0.0,
  "equity": 40000.0,
  "generated_at": "2026-05-12T15:33:05Z",
  "position_count": 0,
  "run_id": "position_monitor-20260512T153305-53451c31",
  "schema_version": "0.1.0",
  "status": "OK",
  "use_alpaca": false,
  "violations": []
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T15:33:12Z",
  "run_id": "execution-20260512T153311-29338c98",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "eafa80017fbe07fddac1b2e89bb027ea4845eeb38c9940dd532a26d16ed642bb",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.016075883333333332,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T16:25:43Z",
  "run_id": "execution-20260512T162543-f43bd673",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "8775d5146cc11c1af1ebf14fdd8b2fa5c4ecdf4f94d15577d3e2bbb212508e12",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.010717966666666667,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T16:41:43Z",
  "run_id": "execution-20260512T164143-d22ae89d",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "704c77858eb7b24f9b54c7a1e9924cc05a21a5b37f8bb3f8da5f6fd0bb8e5841",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.0046165166666666665,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T16:56:01Z",
  "run_id": "execution-20260512T165601-c8d84990",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "43c6e75e13b2091d0ef514e42e32c4645ef595f00933206e90df501659d3fdbb",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.010833116666666667,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T17:09:04Z",
  "run_id": "execution-20260512T170904-4530a860",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "45e42630febca33310762bd820c61df313580a19f15d3cad2c47422ad66e32af",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.01146715,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## Execution attempt completed

```json
{
  "candidate_order_count": 11,
  "confirm_paper": false,
  "dry_run": true,
  "generated_at": "2026-05-12T17:09:39Z",
  "run_id": "execution-20260512T170939-8ba4104f",
  "schema_version": "0.1.0",
  "skipped": [
    {
      "reason": "dry_run_execution",
      "symbol": "APD"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BIL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BKNG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "BLK"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "DIS"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "EOG"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "KO"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "LLY"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "ORCL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WELL"
    },
    {
      "reason": "dry_run_execution",
      "symbol": "WMT"
    }
  ],
  "status": "DRY_RUN_NO_SUBMISSION",
  "submitted": [],
  "trade_plan_hash": "50ac2d692a66edd4310fcb296642f30c215fed8f5c373fb323d25e6285688d27",
  "validation": [
    {
      "id": "PLAN_EXISTS",
      "passed": true,
      "reason": "data/latest/trade_plan.json exists."
    },
    {
      "id": "PLAN_NOT_EXPIRED",
      "passed": true,
      "reason": "Plan expiry must be in the future."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "PAPER_ONLY_SETTINGS",
      "passed": true,
      "reason": "Runtime settings must be paper-only."
    },
    {
      "id": "MARKET_CLOCK_OPEN",
      "passed": true,
      "reason": "Alpaca market clock must be open for submission."
    },
    {
      "id": "PLAN_NOT_DRY_RUN",
      "passed": false,
      "reason": "Actual submission requires a non-dry-run approved paper plan."
    },
    {
      "id": "PLAN_TRADE_CRITICAL_SOURCE_ALPACA",
      "passed": false,
      "reason": "Actual submission requires a plan generated from Alpaca paper data, not mock data."
    },
    {
      "details": {
        "allow_paper_order_submission": false,
        "alpaca_api_key_present": false,
        "alpaca_api_secret_present": false,
        "alpaca_data_feed": "iex",
        "alpaca_paper": true,
        "live_trading_confirmed": false,
        "trading_mode": "paper"
      },
      "id": "NO_LIVE_TRADING",
      "passed": true,
      "reason": "Trading mode is paper-only and live confirmation is false."
    },
    {
      "details": {
        "total_weight": 1.0000000000000002
      },
      "id": "TOTAL_WEIGHT_LIMIT",
      "passed": true,
      "reason": "Target gross exposure must be <= 100%."
    },
    {
      "details": {
        "targets": {
          "APD": 0.084553,
          "BIL": 0.1,
          "BKNG": 0.081628,
          "BLK": 0.09616,
          "DIS": 0.091409,
          "EOG": 0.094018,
          "KO": 0.087681,
          "LLY": 0.08698,
          "ORCL": 0.093499,
          "WELL": 0.09616,
          "WMT": 0.087912
        }
      },
      "id": "LONG_ONLY_TARGETS",
      "passed": true,
      "reason": "All targets must be non-negative."
    },
    {
      "details": {
        "APD": "equity_or_etf",
        "BIL": "equity_or_etf",
        "BKNG": "equity_or_etf",
        "BLK": "equity_or_etf",
        "DIS": "equity_or_etf",
        "EOG": "equity_or_etf",
        "KO": "equity_or_etf",
        "LLY": "equity_or_etf",
        "ORCL": "equity_or_etf",
        "WELL": "equity_or_etf",
        "WMT": "equity_or_etf"
      },
      "id": "NO_OPTIONS_OR_CRYPTO",
      "passed": true,
      "reason": "Targets must be US equities/ETFs only."
    },
    {
      "details": {
        "unknown_symbols": []
      },
      "id": "UNIVERSE_ONLY",
      "passed": true,
      "reason": "Targets must be in configured universe or approved fallback set."
    },
    {
      "details": {
        "cap": 0.12,
        "overweight": {}
      },
      "id": "MAX_POSITION_WEIGHT",
      "passed": true,
      "reason": "Individual stock weights must stay under cap."
    },
    {
      "details": {
        "cap": 10,
        "stock_holdings": 10
      },
      "id": "MAX_HOLDINGS",
      "passed": true,
      "reason": "Number of stock holdings must stay under cap."
    },
    {
      "details": {
        "cap": 2,
        "sector_counts": {
          "101": 1,
          "102": 1,
          "103": 1,
          "104": 1,
          "105": 1,
          "107": 2,
          "108": 1,
          "110": 1,
          "111": 1
        }
      },
      "id": "SECTOR_CAPS",
      "passed": true,
      "reason": "Sector name counts must stay under cap."
    },
    {
      "details": {
        "oversells": []
      },
      "id": "NO_SHORT_SELLS",
      "passed": true,
      "reason": "Sell orders must not exceed current long quantity."
    },
    {
      "details": {
        "source_data_hash_present": true
      },
      "id": "DATA_SOURCE_HASH_PRESENT",
      "passed": true,
      "reason": "Snapshot must include source data hash."
    },
    {
      "details": {
        "age_minutes": 0.007178916666666666,
        "max_age_minutes": 90.0
      },
      "id": "PLAN_EXISTS_AND_FRESH",
      "passed": true,
      "reason": "Market snapshot must be fresh enough for plan generation."
    },
    {
      "details": {
        "data_source": "dry_run_mock_alpaca_compatible",
        "required": false,
        "run_mode": "dry_run"
      },
      "id": "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER",
      "passed": true,
      "reason": "Paper approval/execution requires Alpaca paper trade-critical data; dry-run mock data is allowed only for no-submit validation."
    },
    {
      "details": {
        "max_open_orders": 25,
        "open_order_count": 0
      },
      "id": "MAX_OPEN_ORDERS",
      "passed": true,
      "reason": "Open orders must stay within configured operational cap before new submissions."
    },
    {
      "details": {
        "max_spread_pct": 0.02,
        "wide_spreads": {}
      },
      "id": "QUOTE_SPREAD_LIMIT",
      "passed": true,
      "reason": "Target quote spreads must be below configured limit."
    },
    {
      "details": {},
      "id": "NO_SECRETS_IN_OUTPUT",
      "passed": true,
      "reason": "No secrets are required or emitted by risk gate output."
    }
  ]
}
```

## dry_run_execute run

```json
{
  "all_gates_pass": true,
  "dry_run": true,
  "failed_gates": [],
  "generated_at": "2026-05-12T17:21:53Z",
  "no_submit_reason": "dry_run_mode",
  "orders_ready": 11,
  "orders_validated": 11,
  "plan_id": "trade_plan-20260512T171215-200ec4ba",
  "run_id": "execution-20260512T172153-12e1a120",
  "status": "DRY_RUN_PASS",
  "trade_plan_hash": "0d9edf4f1ccc2f9df3dad0de535b6faad1673807e4f71a748eaa2b3b4e8dd139"
}
```
