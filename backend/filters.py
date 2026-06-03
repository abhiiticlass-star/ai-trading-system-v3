from datetime import datetime

def session_filter():
    hour = datetime.utcnow().hour

    # London + NY session (simple logic)
    if 7 <= hour <= 20:
        return 1
    return 0


def volatility_filter(df):
    recent = df["high"].iloc[-1] - df["low"].iloc[-1]

    if recent > 0.0010:
        return 1
    return 0
