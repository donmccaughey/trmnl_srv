from __future__ import annotations

import json
import sys

from datetime import datetime
from importlib import resources
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from PIL.ImageFont import FreeTypeFont
from textwrap import wrap
from zoneinfo import ZoneInfo

from .screen import Screen


BASE_URL = 'http://10.0.0.239:4000'
BLACK = 0
CELL_HEIGHT = 32  # alternate values: 40, 24, 20
ONE_BIT = '1'
WHITE = 1


def load_font(cell_height: int) -> FreeTypeFont | ImageFont:
    if package_name := __package__:
        with resources.path(package_name, 'AtkinsonHyperlegibleMono-Regular.otf') as font_path:
            return ImageFont.truetype(font_path, cell_height)
    else:
        sys.stderr.write('Unable to load font.\n')
        return ImageFont.load_default(size=cell_height - 1)


print('Rendering...')


content_dir = Path('../tmp')
content_dir.mkdir(parents=True, exist_ok=True)
content_file = content_dir / 'content.json'
with content_file.open('r') as f:
    content = json.load(f)


screen = Screen(800, 480, CELL_HEIGHT)


# date / time
time_zone = ZoneInfo('America/Los_Angeles')
updated_utc = datetime.fromisoformat(content['updated'])
updated_pt = updated_utc.astimezone(time_zone)

updated_date = updated_pt.strftime('%A %d %B %Y')
screen.write(1, 1, updated_date)

updated_time = updated_pt.strftime('%I:%M %p')
screen.write_reverse(screen.cols - 1 - 1, 1, updated_time)


# forecast
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


image = Image.new(ONE_BIT, screen.size, color=WHITE)
draw = ImageDraw.Draw(image)

draw.rectangle(screen.rectangle, outline=BLACK, width=1)

font = load_font(screen.cell_height)
for j, line in enumerate(screen.grid):
    for i, ch in enumerate(line):
        x = i * screen.cell_width
        y = j * screen.cell_height
        draw.text((x, y), ch, fill=BLACK, font=font)


image_dir = Path('../tmp')
image_dir.mkdir(parents=True, exist_ok=True)

png_file = image_dir / 'image.png'
image.save(png_file)


api_display_json = {
    'filename': content['updated'],
    'firmware_url': None,
    'image_url': BASE_URL + '/bitmap',
    'image_url_timeout': 5,
    'refresh_rate': 30,
    'reset_firmware': False,
    'special_function': 'sleep',
    'update_firmware': False,
}

api_display_dir = Path('../tmp')
api_display_dir.mkdir(parents=True, exist_ok=True)

api_display_file = api_display_dir / 'api_display.json'
with open(api_display_file, 'w') as f:
    json.dump(api_display_json, f, indent=4, sort_keys=True)


sys.exit(0)
