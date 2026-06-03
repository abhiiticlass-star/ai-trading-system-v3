import joblib

model = joblib.load("model.pkl")

def predict_signal(features):
    prob = model.predict_proba([features])[0]

    up = float(prob[1])
    down = float(prob[0])

    if up >= 0.70:
        signal = "BUY"
    elif down >= 0.70:
        signal = "SELL"
    else:
        signal = "AVOID"

    return {
        "signal": signal,
        "up_probability": up,
        "down_probability": down
    }
