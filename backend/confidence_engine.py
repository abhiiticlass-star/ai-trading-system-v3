def confidence_score(
    trend,
    pattern,
    breakout
):

    score = 50

    if trend == "Bullish":
        score += 15

    if pattern != "None":
        score += 10

    if breakout:
        score += 15

    if score > 95:
        score = 95

    return score
