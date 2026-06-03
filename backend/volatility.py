def volatility(df):

    rng = (
        df["high"].tail(20).mean()
        -
        df["low"].tail(20).mean()
    )

    if rng > 0.001:
        return "High"

    if rng > 0.0005:
        return "Medium"

    return "Low"
