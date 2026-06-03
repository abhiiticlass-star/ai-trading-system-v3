from flask import Flask, request
from flask_cors import CORS
import pandas as pd

from market_data import get_candles
from features import create_features
from indicators import add_indicators
from signal_engine import predict_signal

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return {"status": "PRO AI SYSTEM RUNNING"}


@app.route("/signal")
def signal():

    pair = request.args.get("pair", "EURUSD")

    candles = get_candles(pair)

    if not candles or len(candles) < 10:
        return {
            "pair": pair,
            "signal": "AVOID",
            "reason": "No candle data"
        }

    df = pd.DataFrame(candles)
    df = create_features(df)
    df = add_indicators(df)

    last = df.iloc[-1]

    features = [
        last["body"],
        last["range"],
        last["trend"],
        last["momentum"]
    ]

    result = predict_signal(features, df)

    return {
        "pair": pair,
        **result
    }


# 🔥 NEW: Candlestick API
@app.route("/candles")
def candles():

    pair = request.args.get("pair", "EURUSD")

    data = get_candles(pair)

    return {
        "pair": pair,
        "candles": data[-50:]
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
