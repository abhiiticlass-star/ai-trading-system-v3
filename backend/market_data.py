import requests

API_KEY = "8e9f4f263cd044cdb3a0a6972179737a"

def get_candles(pair="EURUSD"):

    try:
        url = "https://api.twelvedata.com/time_series"

        # IMPORTANT: correct symbol format
        symbol_map = {
            "EURUSD": "EUR/USD",
            "GBPUSD": "GBP/USD",
            "USDJPY": "USD/JPY",
            "AUDUSD": "AUD/USD"
        }

        symbol = symbol_map.get(pair, "EUR/USD")

        params = {
            "symbol": symbol,
            "interval": "1min",
            "outputsize": 50,
            "apikey": API_KEY
        }

        r = requests.get(url, params=params, timeout=10)
        data = r.json()

        # 🔥 DEBUG SAFE CHECK
        if "values" not in data:
            print("API RESPONSE ERROR:", data)
            return []

        candles = data["values"]

        result = []
        for c in candles:
            result.append({
                "open": float(c["open"]),
                "high": float(c["high"]),
                "low": float(c["low"]),
                "close": float(c["close"])
            })

        return result

    except Exception as e:
        print("EXCEPTION:", e)
        return []
