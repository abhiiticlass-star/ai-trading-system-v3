def predict_signal(features):

    # temporary logic (NO MODEL REQUIRED)
    body, rng, bullish, trend = features

    score = (bullish + trend) / 2

    if score > 0.7:
        return {
            "signal": "BUY",
            "up_probability": 0.75,
            "down_probability": 0.25
        }

    elif score < 0.3:
        return {
            "signal": "SELL",
            "up_probability": 0.25,
            "down_probability": 0.75
        }

    else:
        return {
            "signal": "AVOID",
            "up_probability": 0.5,
            "down_probability": 0.5
        }
