from datetime import datetime
import pytz

def current_session():

    india = pytz.timezone("Asia/Kolkata")

    now = datetime.now(india)

    hour = now.hour

    if 12 <= hour <= 17:
        return "London"

    if 17 <= hour <= 22:
        return "New York"

    return "Asian"
