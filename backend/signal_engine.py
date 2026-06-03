def predict_signal(features):

    body, rng, bullish, trend = features

    score = 0

    # candle direction
    if bullish == 1:
        score += 0.3
    else:
        score -= 0.3

    # trend filter
    if trend == 1:
        score += 0.4
    else:
        score -= 0.4

    # volatility filter
    if rng > body:
        score += 0.1

    # final probability conversion
    up_prob = 0.5 + score
    down_prob = 1 - up_prob

    # clamp values
    up_prob = max(0.1, min(0.9, up_prob))
    down_prob = 1 - up_prob

    if up_prob >= 0.65:
        signal = "BUY"
    elif down_prob >= 0.65:
        signal = "SELL"
    else:
        signal = "AVOID"

    return {
        "signal": signal,
        "up_probability": round(up_prob, 2),
        "down_probability": round(down_prob, 2)
    }
