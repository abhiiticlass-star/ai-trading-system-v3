import pandas as pd

def ema(series, period):
    return series.ewm(span=period, adjust=False).mean()

def rsi(series, period=14):

    delta = series.diff()

    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()

    rs = avg_gain / avg_loss

    return 100 - (100 / (1 + rs))

def get_trend(df):

    df["ema20"] = ema(df["close"], 20)
    df["ema50"] = ema(df["close"], 50)

    if df["ema20"].iloc[-1] > df["ema50"].iloc[-1]:
        return "Bullish"

    return "Bearish"
