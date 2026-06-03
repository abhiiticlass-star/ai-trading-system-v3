import os
import joblib

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

# 🔥 SAFE MODEL LOAD (no crash)
model = None
if os.path.exists(MODEL_PATH):
    try:
        model = joblib.load(MODEL_PATH)
    except:
        model = None


def predict_signal(features, df=None):

    body, rng, bullish, trend = features

    # =========================
    # 🔥 CASE 1: ML MODEL AVAILABLE
    # =========================
    if model is not None:

        try:
            prob = model.predict_proba([features])[0]

            up = float(prob[1])
            down = float(prob[0])

            if up > 0.7:
                signal = "BUY"
            elif down > 0.7:
                signal = "SELL"
            else:
                signal = "AVOID"

            return {
                "signal": signal,
                "up_probability": round(up, 2),
                "down_probability": round(down, 2)
            }

        except:
            pass  # fallback to rule-based


    # =========================
    # 🔥 CASE 2: FALLBACK AI (ALWAYS WORKS)
    # =========================

    score = 0.5

    if bullish == 1:
        score += 0.2
    else:
        score -= 0.2

    if trend == 1:
        score += 0.25
    else:
        score -= 0.25

    if rng > body:
        score += 0.05

    # clamp
    up = max(0.1, min(0.9, score))
    down = 1 - up

    if up >= 0.65:
        signal = "BUY"
    elif down >= 0.65:
        signal = "SELL"
    else:
        signal = "AVOID"

    return {
        "signal": signal,
        "up_probability": round(up, 2),
        "down_probability": round(down, 2)
    }
