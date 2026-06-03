from flask import Flask, request, jsonify
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
