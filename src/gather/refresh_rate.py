from datetime import datetime
from zoneinfo import ZoneInfo


pacific_time = ZoneInfo('America/Los_Angeles')


def get_refresh_rate(now: datetime) -> int:
    now_pt = now.astimezone(pacific_time)
    if 6 <= now_pt.hour < 22:
        return 60
    else:
        return 300
