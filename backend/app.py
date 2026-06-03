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
    try:
        pair = request.args.get("pair", "EURUSD")

        candles = get_candles(pair)

        # SAFE CHECK 1
        if not candles or len(candles) < 5:
            return {
                "pair": pair,
                "signal": "AVOID",
                "reason": "No candle data"
            }

        df = pd.DataFrame(candles)
        df = create_features(df)

        # SAFE CHECK 2
        if "body" not in df.columns:
            return {
                "pair": pair,
                "signal": "AVOID",
                "reason": "Feature error"
            }

        last = df.iloc[-1]

        features = [
            float(last["body"]),
            float(last["range"]),
            int(last["bullish"]),
            int(last["trend"])
        ]

        result = predict_signal(features)

        return {
            "pair": pair,
            **result
        }

    except Exception as e:
        return {
            "pair": pair,
            "signal": "AVOID",
            "error": str(e)
        }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
