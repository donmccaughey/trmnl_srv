from datetime import datetime
from zoneinfo import ZoneInfo


TWO_MINUTES = 120
FIVE_MINUTES = 300
TEN_MINUTES = 600
HALF_HOUR = 1800
ONE_HOUR = 3600

pacific_time = ZoneInfo('America/Los_Angeles')


def get_refresh_rate(now: datetime) -> int:
    now_pt = now.astimezone(pacific_time)
    if 6 <= now_pt.hour < 8:
        return FIVE_MINUTES
    elif 8 <= now_pt.hour < 11:
        return TWO_MINUTES
    elif 11 <= now_pt.hour < 19:
        return TEN_MINUTES
    elif 19 <= now_pt.hour < 22:
        return HALF_HOUR
    else:
        return ONE_HOUR
