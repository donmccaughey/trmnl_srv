from __future__ import annotations

import json
import sys

from datetime import datetime
from textwrap import wrap
from utils import atomic_write
from zoneinfo import ZoneInfo

from .bitmap import write_bitmap
from .constants import CELL_HEIGHT, HEIGHT, WIDTH
from .intro_screen import write_intro_screen
from .options import Options
from .screen import Screen


options = Options.parse()
base_url = options.base_url

print('Rendering...')

content_file = options.web_root / 'content/index.json'
with content_file.open('r') as f:
    content = json.load(f)


screen = Screen(WIDTH, HEIGHT, CELL_HEIGHT)


# date / time
time_zone = ZoneInfo('America/Los_Angeles')
updated_utc = datetime.fromisoformat(content['updated'])
updated_pt = updated_utc.astimezone(time_zone)

updated_date = updated_pt.strftime('%A %d %B %Y')
screen.write(1, 1, updated_date)

updated_time = updated_pt.strftime('%I:%M %p')
screen.write_reverse(screen.cols - 1 - 1, 1, updated_time)


# forecast
if 'error' in content['forecast']:
    screen.write(1, 3, 'Weather:')

    status_code = content['forecast']['error']['status_code']
    reason = content['forecast']['error']['reason']
    screen.write(1, 4, f'    {status_code} {reason}')
else:
    period = content['forecast']['period_name']
    forecast_title = f'Weather {period}:'
    screen.write(1, 3, forecast_title)

    details = content['forecast']['detailed_forecast']
    detail_lines = wrap(
        details,
        width=screen.cols - 2,
        initial_indent='    ',
        break_long_words=True,
        break_on_hyphens=True,
        fix_sentence_endings=True,
    )
    row = 4
    for j, line in enumerate(detail_lines):
        screen.write(1, row + j, line)


if options.intro_screen:
    screen = write_intro_screen()


write_bitmap(screen, options.web_root)


api_display_json = {
    'filename': content['updated'],
    'firmware_url': None,
    'image_url': base_url + '/content/bitmap/index.png',
    'image_url_timeout': 5,
    'refresh_rate': 60,
    'reset_firmware': False,
    'special_function': 'sleep',
    'update_firmware': False,
}
atomic_write(
    options.web_root / 'api/display/index.json',
    lambda f: json.dump(api_display_json, f, indent=4, sort_keys=True)
)


api_setup_json = {
    'api_key': '123456789',
    'friendly_id': 'TRMNL123',
    'image_url': base_url + '/content/bitmap/index.png',
    'message': 'Welcome to trmnl_srv!'
}
atomic_write(
    options.web_root / 'api/setup/index.json',
    lambda f: json.dump(api_setup_json, f, indent=4, sort_keys=True)
)


sys.exit(0)
