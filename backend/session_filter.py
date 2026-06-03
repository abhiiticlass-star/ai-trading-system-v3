from datetime import datetime

def current_session():

    hour = datetime.utcnow().hour

    # UTC based rough sessions

    if 7 <= hour <= 15:
        return "London"

    if 12 <= hour <= 21:
        return "New York"

    return "Asian"
