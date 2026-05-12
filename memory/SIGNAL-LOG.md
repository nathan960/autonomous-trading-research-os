# Signal Log

Candidate ranking, trade-plan generation, and no-trade reasons are logged here.

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T153120-a8d76fc7",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T153120-b24052c1",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "3db855f6bc252467eed8d7675c053c1b94dddde0c5ae7bf5ada481935cd557be"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T153129-62645e34",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T153129-9869c4d7",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "781e14195cfc473146586404e3c3d9e8b38a2f06bfad35867b68bb43f158a0ed"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T153253-d75f00af",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T153253-0f139ccb",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "acc6818ef018c8530abf46de23e1ffc4400a4dbbb91ce543fda54c6929e4ca0e"
}
```

## Trade plan generated

```json
{
  "approval_status": "BLOCKED",
  "candidate_order_count": 11,
  "failed_gates": [
    "TRADE_CRITICAL_SOURCE_IS_ALPACA_PAPER"
  ],
  "run_id": "trade_plan-20260512T153300-41352dc4",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "66e19502a46c261f9951c0a598c6ff33647003f663b581b39f96e00fec45a5aa"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T153305-2d0c50dd",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T153305-8ba0bff3",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "209321ee8bfc8308e88d3f37670894bc67fdc87e7ea8621a81b6ded9262aaa5e"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T153311-53c96d1b",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T153311-897f45cf",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "eafa80017fbe07fddac1b2e89bb027ea4845eeb38c9940dd532a26d16ed642bb"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T162543-93cf6035",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T162543-0b935930",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "8775d5146cc11c1af1ebf14fdd8b2fa5c4ecdf4f94d15577d3e2bbb212508e12"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T164143-e7366237",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T164143-5d007d4b",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "704c77858eb7b24f9b54c7a1e9924cc05a21a5b37f8bb3f8da5f6fd0bb8e5841"
}
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T165601-127b46b9",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T165601-f14ddffe",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "43c6e75e13b2091d0ef514e42e32c4645ef595f00933206e90df501659d3fdbb"
}
```

## scan_triggers candidates  (2026-05-12T16:56:03Z)

```
  WMT       score=0.2220  atr_pct=0.0109  [SELECTED]
  APD       score=0.2198  atr_pct=0.0114  [SELECTED]
  DIS       score=0.2113  atr_pct=0.0105  [SELECTED]
  ORCL      score=0.2093  atr_pct=0.0103  [SELECTED]
  LLY       score=0.2016  atr_pct=0.0111  [SELECTED]
  BLK       score=0.1996  atr_pct=0.0098  [SELECTED]
  BKNG      score=0.1969  atr_pct=0.0118  [SELECTED]
  KO        score=0.1963  atr_pct=0.0110  [SELECTED]
  WELL      score=0.1905  atr_pct=0.0099  [SELECTED]
  EOG       score=0.1862  atr_pct=0.0102  [SELECTED]
  UNP       score=0.1859  atr_pct=0.0099  [candidate]
  CRM       score=0.1782  atr_pct=0.0104  [candidate]
  PG        score=0.1768  atr_pct=0.0105  [candidate]
  COST      score=0.1717  atr_pct=0.0115  [candidate]
  PEP       score=0.1712  atr_pct=0.0108  [candidate]
  MCD       score=0.1708  atr_pct=0.0111  [candidate]
  XOM       score=0.1671  atr_pct=0.0105  [candidate]
  WFC       score=0.1666  atr_pct=0.0117  [candidate]
  NFLX      score=0.1564  atr_pct=0.0103  [candidate]
  GOOGL     score=0.1557  atr_pct=0.0103  [candidate]
  CL        score=0.1537  atr_pct=0.0102  [candidate]
  AMGN      score=0.1489  atr_pct=0.0099  [candidate]
  MS        score=0.1472  atr_pct=0.0094  [candidate]
  LMT       score=0.1454  atr_pct=0.0105  [candidate]
  ABBV      score=0.1442  atr_pct=0.0116  [candidate]
  INTU      score=0.1425  atr_pct=0.0106  [candidate]
  TSLA      score=0.1422  atr_pct=0.0098  [candidate]
  GS        score=0.1396  atr_pct=0.0103  [candidate]
  HD        score=0.1392  atr_pct=0.0109  [candidate]
  CSCO      score=0.1378  atr_pct=0.0110  [candidate]
  NVDA      score=0.1334  atr_pct=0.0107  [candidate]
  AXP       score=0.1333  atr_pct=0.0111  [candidate]
  BAC       score=0.1318  atr_pct=0.0095  [candidate]
  EQIX      score=0.1316  atr_pct=0.0103  [candidate]
  AAPL      score=0.1295  atr_pct=0.0100  [candidate]
  NKE       score=0.1268  atr_pct=0.0109  [candidate]
  AMT       score=0.1266  atr_pct=0.0109  [candidate]
  AMD       score=0.1264  atr_pct=0.0094  [candidate]
  MSFT      score=0.1260  atr_pct=0.0112  [candidate]
  GE        score=0.1218  atr_pct=0.0112  [candidate]
  DE        score=0.1209  atr_pct=0.0109  [candidate]
  COP       score=0.1205  atr_pct=0.0099  [candidate]
  PLD       score=0.1175  atr_pct=0.0106  [candidate]
  AMZN      score=0.1169  atr_pct=0.0094  [candidate]
  ISRG      score=0.1167  atr_pct=0.0096  [candidate]
  SO        score=0.1155  atr_pct=0.0097  [candidate]
  CMCSA     score=0.1111  atr_pct=0.0120  [candidate]
  SLB       score=0.1033  atr_pct=0.0103  [candidate]
  CVX       score=0.1017  atr_pct=0.0108  [candidate]
  CAT       score=0.1004  atr_pct=0.0095  [candidate]
  ABT       score=0.0984  atr_pct=0.0102  [candidate]
  TMO       score=0.0967  atr_pct=0.0114  [candidate]
  HON       score=0.0966  atr_pct=0.0099  [candidate]
  ECL       score=0.0911  atr_pct=0.0110  [candidate]
  AEP       score=0.0909  atr_pct=0.0102  [candidate]
  META      score=0.0870  atr_pct=0.0105  [candidate]
  LIN       score=0.0845  atr_pct=0.0097  [candidate]
  SHW       score=0.0805  atr_pct=0.0099  [candidate]
  BA        score=0.0774  atr_pct=0.0100  [candidate]
  PM        score=0.0751  atr_pct=0.0108  [candidate]
  SRE       score=0.0718  atr_pct=0.0099  [candidate]
  JPM       score=0.0696  atr_pct=0.0103  [candidate]
  O         score=0.0676  atr_pct=0.0095  [candidate]
  TMUS      score=0.0606  atr_pct=0.0112  [candidate]
  MA        score=0.0588  atr_pct=0.0107  [candidate]
  NEE       score=0.0588  atr_pct=0.0108  [candidate]
  UPS       score=0.0465  atr_pct=0.0117  [candidate]
  UNH       score=0.0403  atr_pct=0.0114  [candidate]
  AVGO      score=0.0366  atr_pct=0.0094  [candidate]
  JNJ       score=0.0301  atr_pct=0.0100  [candidate]
  SBUX      score=0.0298  atr_pct=0.0100  [candidate]
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T170904-8a409ef7",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T170904-f7d8ce6c",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "45e42630febca33310762bd820c61df313580a19f15d3cad2c47422ad66e32af"
}
```

## scan_triggers candidates  (2026-05-12T17:09:22Z)

```
  WMT       score=0.2220  atr_pct=0.0109  [SELECTED]
  APD       score=0.2198  atr_pct=0.0114  [SELECTED]
  DIS       score=0.2113  atr_pct=0.0105  [SELECTED]
  ORCL      score=0.2093  atr_pct=0.0103  [SELECTED]
  LLY       score=0.2016  atr_pct=0.0111  [SELECTED]
  BLK       score=0.1996  atr_pct=0.0098  [SELECTED]
  BKNG      score=0.1969  atr_pct=0.0118  [SELECTED]
  KO        score=0.1963  atr_pct=0.0110  [SELECTED]
  WELL      score=0.1905  atr_pct=0.0099  [SELECTED]
  EOG       score=0.1862  atr_pct=0.0102  [SELECTED]
  UNP       score=0.1859  atr_pct=0.0099  [candidate]
  CRM       score=0.1782  atr_pct=0.0104  [candidate]
  PG        score=0.1768  atr_pct=0.0105  [candidate]
  COST      score=0.1717  atr_pct=0.0115  [candidate]
  PEP       score=0.1712  atr_pct=0.0108  [candidate]
  MCD       score=0.1708  atr_pct=0.0111  [candidate]
  XOM       score=0.1671  atr_pct=0.0105  [candidate]
  WFC       score=0.1666  atr_pct=0.0117  [candidate]
  NFLX      score=0.1564  atr_pct=0.0103  [candidate]
  GOOGL     score=0.1557  atr_pct=0.0103  [candidate]
  CL        score=0.1537  atr_pct=0.0102  [candidate]
  AMGN      score=0.1489  atr_pct=0.0099  [candidate]
  MS        score=0.1472  atr_pct=0.0094  [candidate]
  LMT       score=0.1454  atr_pct=0.0105  [candidate]
  ABBV      score=0.1442  atr_pct=0.0116  [candidate]
  INTU      score=0.1425  atr_pct=0.0106  [candidate]
  TSLA      score=0.1422  atr_pct=0.0098  [candidate]
  GS        score=0.1396  atr_pct=0.0103  [candidate]
  HD        score=0.1392  atr_pct=0.0109  [candidate]
  CSCO      score=0.1378  atr_pct=0.0110  [candidate]
  NVDA      score=0.1334  atr_pct=0.0107  [candidate]
  AXP       score=0.1333  atr_pct=0.0111  [candidate]
  BAC       score=0.1318  atr_pct=0.0095  [candidate]
  EQIX      score=0.1316  atr_pct=0.0103  [candidate]
  AAPL      score=0.1295  atr_pct=0.0100  [candidate]
  NKE       score=0.1268  atr_pct=0.0109  [candidate]
  AMT       score=0.1266  atr_pct=0.0109  [candidate]
  AMD       score=0.1264  atr_pct=0.0094  [candidate]
  MSFT      score=0.1260  atr_pct=0.0112  [candidate]
  GE        score=0.1218  atr_pct=0.0112  [candidate]
  DE        score=0.1209  atr_pct=0.0109  [candidate]
  COP       score=0.1205  atr_pct=0.0099  [candidate]
  PLD       score=0.1175  atr_pct=0.0106  [candidate]
  AMZN      score=0.1169  atr_pct=0.0094  [candidate]
  ISRG      score=0.1167  atr_pct=0.0096  [candidate]
  SO        score=0.1155  atr_pct=0.0097  [candidate]
  CMCSA     score=0.1111  atr_pct=0.0120  [candidate]
  SLB       score=0.1033  atr_pct=0.0103  [candidate]
  CVX       score=0.1017  atr_pct=0.0108  [candidate]
  CAT       score=0.1004  atr_pct=0.0095  [candidate]
  ABT       score=0.0984  atr_pct=0.0102  [candidate]
  TMO       score=0.0967  atr_pct=0.0114  [candidate]
  HON       score=0.0966  atr_pct=0.0099  [candidate]
  ECL       score=0.0911  atr_pct=0.0110  [candidate]
  AEP       score=0.0909  atr_pct=0.0102  [candidate]
  META      score=0.0870  atr_pct=0.0105  [candidate]
  LIN       score=0.0845  atr_pct=0.0097  [candidate]
  SHW       score=0.0805  atr_pct=0.0099  [candidate]
  BA        score=0.0774  atr_pct=0.0100  [candidate]
  PM        score=0.0751  atr_pct=0.0108  [candidate]
  SRE       score=0.0718  atr_pct=0.0099  [candidate]
  JPM       score=0.0696  atr_pct=0.0103  [candidate]
  O         score=0.0676  atr_pct=0.0095  [candidate]
  TMUS      score=0.0606  atr_pct=0.0112  [candidate]
  MA        score=0.0588  atr_pct=0.0107  [candidate]
  NEE       score=0.0588  atr_pct=0.0108  [candidate]
  UPS       score=0.0465  atr_pct=0.0117  [candidate]
  UNH       score=0.0403  atr_pct=0.0114  [candidate]
  AVGO      score=0.0366  atr_pct=0.0094  [candidate]
  JNJ       score=0.0301  atr_pct=0.0100  [candidate]
  SBUX      score=0.0298  atr_pct=0.0100  [candidate]
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T170939-c91a027a",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T170939-ca1e3ddf",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "50ac2d692a66edd4310fcb296642f30c215fed8f5c373fb323d25e6285688d27"
}
```

## scan_triggers candidates  (2026-05-12T17:12:15Z)

```
  WMT       score=0.2220  atr_pct=0.0109  [SELECTED]
  APD       score=0.2198  atr_pct=0.0114  [SELECTED]
  DIS       score=0.2113  atr_pct=0.0105  [SELECTED]
  ORCL      score=0.2093  atr_pct=0.0103  [SELECTED]
  LLY       score=0.2016  atr_pct=0.0111  [SELECTED]
  BLK       score=0.1996  atr_pct=0.0098  [SELECTED]
  BKNG      score=0.1969  atr_pct=0.0118  [SELECTED]
  KO        score=0.1963  atr_pct=0.0110  [SELECTED]
  WELL      score=0.1905  atr_pct=0.0099  [SELECTED]
  EOG       score=0.1862  atr_pct=0.0102  [SELECTED]
  UNP       score=0.1859  atr_pct=0.0099  [candidate]
  CRM       score=0.1782  atr_pct=0.0104  [candidate]
  PG        score=0.1768  atr_pct=0.0105  [candidate]
  COST      score=0.1717  atr_pct=0.0115  [candidate]
  PEP       score=0.1712  atr_pct=0.0108  [candidate]
  MCD       score=0.1708  atr_pct=0.0111  [candidate]
  XOM       score=0.1671  atr_pct=0.0105  [candidate]
  WFC       score=0.1666  atr_pct=0.0117  [candidate]
  NFLX      score=0.1564  atr_pct=0.0103  [candidate]
  GOOGL     score=0.1557  atr_pct=0.0103  [candidate]
  CL        score=0.1537  atr_pct=0.0102  [candidate]
  AMGN      score=0.1489  atr_pct=0.0099  [candidate]
  MS        score=0.1472  atr_pct=0.0094  [candidate]
  LMT       score=0.1454  atr_pct=0.0105  [candidate]
  ABBV      score=0.1442  atr_pct=0.0116  [candidate]
  INTU      score=0.1425  atr_pct=0.0106  [candidate]
  TSLA      score=0.1422  atr_pct=0.0098  [candidate]
  GS        score=0.1396  atr_pct=0.0103  [candidate]
  HD        score=0.1392  atr_pct=0.0109  [candidate]
  CSCO      score=0.1378  atr_pct=0.0110  [candidate]
  NVDA      score=0.1334  atr_pct=0.0107  [candidate]
  AXP       score=0.1333  atr_pct=0.0111  [candidate]
  BAC       score=0.1318  atr_pct=0.0095  [candidate]
  EQIX      score=0.1316  atr_pct=0.0103  [candidate]
  AAPL      score=0.1295  atr_pct=0.0100  [candidate]
  NKE       score=0.1268  atr_pct=0.0109  [candidate]
  AMT       score=0.1266  atr_pct=0.0109  [candidate]
  AMD       score=0.1264  atr_pct=0.0094  [candidate]
  MSFT      score=0.1260  atr_pct=0.0112  [candidate]
  GE        score=0.1218  atr_pct=0.0112  [candidate]
  DE        score=0.1209  atr_pct=0.0109  [candidate]
  COP       score=0.1205  atr_pct=0.0099  [candidate]
  PLD       score=0.1175  atr_pct=0.0106  [candidate]
  AMZN      score=0.1169  atr_pct=0.0094  [candidate]
  ISRG      score=0.1167  atr_pct=0.0096  [candidate]
  SO        score=0.1155  atr_pct=0.0097  [candidate]
  CMCSA     score=0.1111  atr_pct=0.0120  [candidate]
  SLB       score=0.1033  atr_pct=0.0103  [candidate]
  CVX       score=0.1017  atr_pct=0.0108  [candidate]
  CAT       score=0.1004  atr_pct=0.0095  [candidate]
  ABT       score=0.0984  atr_pct=0.0102  [candidate]
  TMO       score=0.0967  atr_pct=0.0114  [candidate]
  HON       score=0.0966  atr_pct=0.0099  [candidate]
  ECL       score=0.0911  atr_pct=0.0110  [candidate]
  AEP       score=0.0909  atr_pct=0.0102  [candidate]
  META      score=0.0870  atr_pct=0.0105  [candidate]
  LIN       score=0.0845  atr_pct=0.0097  [candidate]
  SHW       score=0.0805  atr_pct=0.0099  [candidate]
  BA        score=0.0774  atr_pct=0.0100  [candidate]
  PM        score=0.0751  atr_pct=0.0108  [candidate]
  SRE       score=0.0718  atr_pct=0.0099  [candidate]
  JPM       score=0.0696  atr_pct=0.0103  [candidate]
  O         score=0.0676  atr_pct=0.0095  [candidate]
  TMUS      score=0.0606  atr_pct=0.0112  [candidate]
  MA        score=0.0588  atr_pct=0.0107  [candidate]
  NEE       score=0.0588  atr_pct=0.0108  [candidate]
  UPS       score=0.0465  atr_pct=0.0117  [candidate]
  UNH       score=0.0403  atr_pct=0.0114  [candidate]
  AVGO      score=0.0366  atr_pct=0.0094  [candidate]
  JNJ       score=0.0301  atr_pct=0.0100  [candidate]
  SBUX      score=0.0298  atr_pct=0.0100  [candidate]
```

## Signal candidates ranked

```json
{
  "risk_on": true,
  "run_id": "trigger_scan-20260512T173526-5a0b79b8",
  "selected": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ],
  "top_candidates": [
    {
      "atr_pct": 0.010938144972713254,
      "latest_close": 66.8464,
      "momentum_score": 0.2219724443399539,
      "roc126": 0.1373329000403234,
      "roc252": 0.3066119886395844,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "WMT"
    },
    {
      "atr_pct": 0.011372719049647961,
      "latest_close": 397.8635,
      "momentum_score": 0.21978791670686748,
      "roc126": 0.13492012327521374,
      "roc252": 0.3046557101385212,
      "sector": "Materials",
      "sector_code": 111,
      "symbol": "APD"
    },
    {
      "atr_pct": 0.010519655190385375,
      "latest_close": 397.0028,
      "momentum_score": 0.21129738787910313,
      "roc126": 0.1280501180324216,
      "roc252": 0.29454465772578464,
      "sector": "Communication Services",
      "sector_code": 102,
      "symbol": "DIS"
    },
    {
      "atr_pct": 0.010284519834542934,
      "latest_close": 131.123,
      "momentum_score": 0.20930406978644833,
      "roc126": 0.12509921188225848,
      "roc252": 0.2935089276906382,
      "sector": "Technology",
      "sector_code": 101,
      "symbol": "ORCL"
    },
    {
      "atr_pct": 0.01105538114772093,
      "latest_close": 104.6392,
      "momentum_score": 0.2015814864072044,
      "roc126": 0.12588511881385211,
      "roc252": 0.2772778540005567,
      "sector": "Health Care",
      "sector_code": 105,
      "symbol": "LLY"
    },
    {
      "atr_pct": 0.009817870296887523,
      "latest_close": 368.9824,
      "momentum_score": 0.19955606214422494,
      "roc126": 0.12881908572306133,
      "roc252": 0.27029303856538855,
      "sector": "Financials",
      "sector_code": 104,
      "symbol": "BLK"
    },
    {
      "atr_pct": 0.011780188713451269,
      "latest_close": 131.4487,
      "momentum_score": 0.19692295910538415,
      "roc126": 0.1223765416286704,
      "roc252": 0.2714693765820979,
      "sector": "Consumer Discretionary",
      "sector_code": 103,
      "symbol": "BKNG"
    },
    {
      "atr_pct": 0.01096697673112274,
      "latest_close": 345.884,
      "momentum_score": 0.19631743002941815,
      "roc126": 0.12744057846016243,
      "roc252": 0.26519428159867386,
      "sector": "Consumer Staples",
      "sector_code": 107,
      "symbol": "KO"
    },
    {
      "atr_pct": 0.009923952009687284,
      "latest_close": 150.8377,
      "momentum_score": 0.19048644316063956,
      "roc126": 0.12370392885185888,
      "roc252": 0.25726895746942025,
      "sector": "Real Estate",
      "sector_code": 110,
      "symbol": "WELL"
    },
    {
      "atr_pct": 0.01022783604659481,
      "latest_close": 290.7738,
      "momentum_score": 0.1861546764474581,
      "roc126": 0.11825238476886102,
      "roc252": 0.25405696812605516,
      "sector": "Energy",
      "sector_code": 108,
      "symbol": "EOG"
    }
  ]
}
```

## Trade plan generated

```json
{
  "approval_status": "DRY_RUN_ONLY",
  "candidate_order_count": 11,
  "failed_gates": [],
  "run_id": "trade_plan-20260512T173526-e2c36cfc",
  "target_reason": "risk_on_stock_basket_inverse_atr_weighted",
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
  },
  "trade_plan_hash": "054760162b875c1258d7e9eeb6d0b1da74f538139859fea34e629b163a5ffba4"
}
```
