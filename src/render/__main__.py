from __future__ import annotations

import json
import sys

from datetime import datetime
from importlib import resources
from PIL import Image, ImageDraw, ImageFont
from PIL.ImageFont import FreeTypeFont
from textwrap import wrap
from zoneinfo import ZoneInfo

from .options import Options
from .screen import Screen


BASE_URL = 'http://10.0.0.100:4000'
BLACK = 0
CELL_HEIGHT = 32  # alternate values: 40, 24, 20
ONE_BIT = '1'
WHITE = 1
WIDTH = 800
HEIGHT = 480


def load_font(cell_height: int) -> FreeTypeFont | ImageFont:
    if package_name := __package__:
        with resources.path(package_name, 'AtkinsonHyperlegibleMono-Regular.otf') as font_path:
            return ImageFont.truetype(font_path, cell_height)
    else:
        sys.stderr.write('Unable to load font.\n')
        return ImageFont.load_default(size=cell_height - 1)


options = Options.parse()

print('Rendering...')


content_dir = options.web_root / 'content'
content_file = content_dir / 'index.json'
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


def write_intro_screen():
    screen = Screen(WIDTH, HEIGHT, 64)

    line1 = 'Welcome to'
    line2 = 'trmnl_srv!'
    line_width = max(len(line1), len(line2))
    col = (screen.cols - line_width + 1) // 2
    row = (screen.rows - 2 + 1) // 2

    screen.write(col, row, line1)
    screen.write(col, row + 1, line2)

    return screen


# screen = write_intro_screen()


image = Image.new(ONE_BIT, screen.size, color=WHITE)
draw = ImageDraw.Draw(image)

draw.rectangle(screen.rectangle, outline=BLACK, width=1)

font = load_font(screen.cell_height)
for j, line in enumerate(screen.grid):
    for i, ch in enumerate(line):
        x = i * screen.cell_width
        y = j * screen.cell_height
        draw.text((x, y), ch, fill=BLACK, font=font)


image_dir = options.web_root / 'content/bitmap'
image_dir.mkdir(parents=True, exist_ok=True)

image_file = image_dir / 'index.png'
image.save(image_file)


api_display_json = {
    'filename': content['updated'],
    'firmware_url': None,
    'image_url': BASE_URL + '/content/bitmap/index.png',
    'image_url_timeout': 5,
    'refresh_rate': 60,
    'reset_firmware': False,
    'special_function': 'sleep',
    'update_firmware': False,
}

api_display_dir = options.web_root / 'api/display'
api_display_dir.mkdir(parents=True, exist_ok=True)

api_display_file = api_display_dir / 'index.json'
with open(api_display_file, 'w') as f:
    json.dump(api_display_json, f, indent=4, sort_keys=True)


api_setup_json = {
    'api_key': '123456789',
    'friendly_id': 'TRMNL123',
    'image_url': BASE_URL + '/content/bitmap/index.png',
    'message': 'Welcome to trmnl_srv!'
}

api_setup_dir = options.web_root / 'api/setup'
api_setup_dir.mkdir(parents=True, exist_ok=True)

api_setup_file = api_setup_dir / 'index.json'
with open(api_setup_file, 'w') as f:
    json.dump(api_setup_json, f, indent=4, sort_keys=True)


sys.exit(0)
