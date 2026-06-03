from flask import Flask, jsonify, request
from flask_cors import CORS

from market_data import get_market_data
from signal_engine import generate_signal

app = Flask(__name__)

CORS(
    app,
    resources={
        r"/*": {
            "origins": "*"
        }
    }
)

@app.route("/")
def home():

    return jsonify({
        "status": "AI Trading System Running"
    })


@app.route("/signal")
def signal():

    try:

        pair = request.args.get(
            "pair",
            "EURUSD"
        )

        timeframe = request.args.get(
            "tf",
            "1min"
        )

        df = get_market_data(
            pair,
            timeframe
        )

        if df is None or len(df) == 0:

            return jsonify({
                "pair": pair,
                "signal": "AVOID",
                "reason": "No candle data"
            })

        result = generate_signal(df)

        result["pair"] = pair

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "signal": "AVOID",
            "error": str(e)
        })


@app.route("/health")
def health():

    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=10000
    )
