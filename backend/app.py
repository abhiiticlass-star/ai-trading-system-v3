from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

from market_data import get_candles
from features import create_features
from signal_engine import predict_signal

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {"status": "AI Trading System Running"}

@app.route("/signal")
def signal():
    pair = request.args.get("pair", "EURUSD")

    candles = get_candles(pair)

    if len(candles) < 20:
        return {"error": "Not enough data"}

    df = pd.DataFrame(candles)
    df = create_features(df)

    last = df.iloc[-1]

    features = [
        last["body"],
        last["range"],
        last["bullish"],
        last["trend"]
    ]

    result = predict_signal(features)

    return {
        "pair": pair,
        **result
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
