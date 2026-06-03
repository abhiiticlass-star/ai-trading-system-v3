import requests

def get_candles(pair="EURUSD"):

    try:
        url = "https://api.twelvedata.com/time_series"

        params = {
            "symbol": "EUR/USD",
            "interval": "1min",
            "outputsize": 50,
            "apikey": "YOUR_KEY"
        }

        r = requests.get(url, params=params, timeout=10)

        # 🔥 SAFE JSON CHECK
        try:
            data = r.json()
        except:
            return []

        if "values" not in data:
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
        print("API ERROR:", e)
        return []
