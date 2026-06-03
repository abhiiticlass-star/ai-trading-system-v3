import pandas as pd

from indicators import get_trend, rsi
from patterns import detect_pattern
from support_resistance import get_support_resistance
from breakout import breakout_check
from session_filter import current_session
from volatility import volatility
from confidence_engine import confidence_score

def generate_signal(df):

    if df is None or len(df) < 50:
        return {
            "signal": "AVOID",
            "reason": "Not enough data"
        }

    df["rsi"] = rsi(df["close"])

    trend = get_trend(df)

    pattern = detect_pattern(df)

    support, resistance = get_support_resistance(df)

    breakout = breakout_check(
        df,
        support,
        resistance
    )

    session = current_session()

    vol = volatility(df)

    confidence = confidence_score(
        trend,
        pattern,
        breakout
    )

    latest_rsi = df["rsi"].iloc[-1]

    signal = "AVOID"

    up_probability = 0.50
    down_probability = 0.50

    # BUY Logic
    if (
        trend == "Bullish"
        and latest_rsi > 50
        and confidence >= 70
    ):

        signal = "BUY"

        up_probability = round(
            confidence / 100,
            2
        )

        down_probability = round(
            1 - up_probability,
            2
        )

    # SELL Logic
    elif (
        trend == "Bearish"
        and latest_rsi < 50
        and confidence >= 70
    ):

        signal = "SELL"

        down_probability = round(
            confidence / 100,
            2
        )

        up_probability = round(
            1 - down_probability,
            2
        )

    return {

        "signal": signal,

        "confidence": confidence,

        "up_probability": up_probability,

        "down_probability": down_probability,

        "trend_m1": trend,

        "trend_m5": trend,

        "support": support,

        "resistance": resistance,

        "breakout": breakout,

        "pattern": pattern,

        "session": session,

        "volatility": vol,

        "analysis":
        "Layer Structural Confluence"
    }
