def add_indicators(df):

    df["ema5"] = df["close"].ewm(span=5).mean()
    df["ema10"] = df["close"].ewm(span=10).mean()

    df["trend"] = (df["ema5"] > df["ema10"]).astype(int)

    df["momentum"] = df["close"] - df["close"].shift(1)

    return df
