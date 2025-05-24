from datetime import datetime
from serialize import JSONDict
from zoneinfo import ZoneInfo

from .screen import Screen


def write_date_and_time(content: JSONDict, screen: Screen):
    time_zone = ZoneInfo('America/Los_Angeles')
    updated_utc = datetime.fromisoformat(content['updated'])
    updated_pt = updated_utc.astimezone(time_zone)

    updated_date = updated_pt.strftime('%A %d %B %Y')
    screen.write(1, 0, updated_date)

    updated_time = updated_pt.strftime('%I:%M %p')
    screen.write_reverse(screen.cols - 1 - 1, 0, updated_time)
