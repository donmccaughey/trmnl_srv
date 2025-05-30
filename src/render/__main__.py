from __future__ import annotations

import json
import sys

from .api_display import APIDisplay
from .api_setup import APISetup
from .bitmap import write_bitmap
from .constants import CELL_HEIGHT, HEIGHT, WIDTH
from .date_and_time import write_date_and_time
from .forecast import write_forecast
from .giants_games_today import write_giants_games_today
from .intro_screen import write_intro_screen
from .logs import write_log_message
from .next_muni import write_next_muni
from .options import Options
from .screen import Screen


options = Options.parse()

print('Rendering...')


content_file = options.web_root / 'content/index.json'
with content_file.open('r') as f:
    content = json.load(f)


if options.intro_screen:
    screen = write_intro_screen()
else:
    screen = Screen(WIDTH, HEIGHT, CELL_HEIGHT)
    write_date_and_time(content, screen)
    write_next_muni(content, screen)
    write_forecast(content, screen)
    write_giants_games_today(content, screen)
    write_log_message(content, screen)
write_bitmap(screen, options.web_root)
APIDisplay(
    base_url=options.base_url,
    filename=content['updated'],
    refresh_rate=content['refresh_rate'],
).write(options.web_root)
APISetup(options.base_url).write(options.web_root)


sys.exit(0)
