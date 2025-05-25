from datetime import datetime
from serialize import JSONDict
from zoneinfo import ZoneInfo

from .screen import Screen


def write_next_muni(content: JSONDict, screen: Screen):
    time_zone = ZoneInfo('America/Los_Angeles')
    times = [
        datetime.fromisoformat(time)
                .astimezone(time_zone)
                .strftime('%I:%M %p')
        for time in content['muni']['expected_arrival_times']
    ]
    message = 'Next T: ' + ', '.join(times)
    screen.write(1, 2, message)
