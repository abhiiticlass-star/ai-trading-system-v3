import pandas as pd

def create_features(df):
    df["body"] = abs(df["close"] - df["open"])
    df["range"] = df["high"] - df["low"]
    df["bullish"] = (df["close"] > df["open"]).astype(int)

    df["ema5"] = df["close"].ewm(span=5).mean()
    df["ema10"] = df["close"].ewm(span=10).mean()
    df["trend"] = (df["ema5"] > df["ema10"]).astype(int)

    return df
