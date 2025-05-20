from __future__ import annotations

import json
import sys

from utils import atomic_write

from .bitmap import write_bitmap
from .constants import CELL_HEIGHT, HEIGHT, WIDTH
from .date_and_time import write_date_and_time
from .forecast import write_forecast
from .intro_screen import write_intro_screen
from .options import Options
from .screen import Screen


options = Options.parse()
base_url = options.base_url

print('Rendering...')

content_file = options.web_root / 'content/index.json'
with content_file.open('r') as f:
    content = json.load(f)


if options.intro_screen:
    screen = write_intro_screen()
else:
    screen = Screen(WIDTH, HEIGHT, CELL_HEIGHT)
    write_date_and_time(content, screen)
    write_forecast(content, screen)
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
