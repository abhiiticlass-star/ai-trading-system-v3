def get_support_resistance(df):

    support = round(df["low"].tail(20).min(), 5)

    resistance = round(
        df["high"].tail(20).max(),
        5
    )

    return support, resistance
