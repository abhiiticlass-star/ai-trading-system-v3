import requests
from config import API_KEY, BASE_URL

def get_candles(pair="EURUSD"):
    url = f"{BASE_URL}?function=FX_INTRADAY&from_symbol=EUR&to_symbol=USD&interval=1min&apikey={API_KEY}"
    r = requests.get(url)
    data = r.json()

    try:
        candles = data["Time Series FX (1min)"]
    except:
        return []

    result = []

    for k, v in list(candles.items())[:50]:
        result.append({
            "open": float(v["1. open"]),
            "high": float(v["2. high"]),
            "low": float(v["3. low"]),
            "close": float(v["4. close"])
        })

    return result
