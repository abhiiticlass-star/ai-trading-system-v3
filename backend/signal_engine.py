import joblib
from filters import session_filter, volatility_filter

model = joblib.load("model.pkl")


def predict_signal(features, df):

    session_ok = session_filter()
    vol_ok = volatility_filter(df)

    if session_ok == 0 or vol_ok == 0:
        return {
            "signal": "AVOID",
            "reason": "Market condition not good",
            "up_probability": 0.5,
            "down_probability": 0.5
        }

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
        "up_probability": round(up, 2),
        "down_probability": round(down, 2)
    }
