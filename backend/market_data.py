import requests
import pandas as pd

API_KEY = "8e9f4f263cd044cdb3a0a6972179737a"

def get_candles(pair="EURUSD", timeframe="1min"):

    try:

        url = "https://api.twelvedata.com/time_series"

        symbol_map = {
            "EURUSD": "EUR/USD",
            "GBPUSD": "GBP/USD",
            "USDJPY": "USD/JPY",
            "AUDUSD": "AUD/USD"
        }

        symbol = symbol_map.get(pair, "EUR/USD")

        params = {
            "symbol": symbol,
            "interval": timeframe,
            "outputsize": 100,
            "apikey": API_KEY
        }

        response = requests.get(
            url,
            params=params,
            timeout=15
        )

        data = response.json()

        if "values" not in data:

            print("TWELVEDATA ERROR:", data)

            return []

        candles = []

        for candle in data["values"]:

            candles.append({

                "open": float(candle["open"]),
                "high": float(candle["high"]),
                "low": float(candle["low"]),
                "close": float(candle["close"])

            })

        candles.reverse()

        return candles

    except Exception as e:

        print("MARKET DATA ERROR:", e)

        return []


def get_market_data(
    pair="EURUSD",
    timeframe="1min"
):

    candles = get_candles(
        pair,
        timeframe
    )

    if not candles:

        return pd.DataFrame()

    return pd.DataFrame(candles)
