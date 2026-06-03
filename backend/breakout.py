def breakout_check(df, support, resistance):

    close = df["close"].iloc[-1]

    breakout = False

    if close > resistance:
        breakout = True

    if close < support:
        breakout = True

    return breakout
