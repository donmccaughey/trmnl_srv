from __future__ import annotations

import json
import sys

from datetime import datetime

from .api_display import write_api_display
from .api_setup import write_api_setup
from .bitmap import write_bitmap
from .constants import CELL_HEIGHT, HEIGHT, WIDTH
from .date_and_time import write_date_and_time
from .forecast import write_forecast
from .giants_games_today import write_giants_games_today
from .intro_screen import write_intro_screen
from .logs import list_log_files, write_log_message
from .options import Options
from .screen import Screen


options = Options.parse()

print('Rendering...')


content_file = options.web_root / 'content/index.json'
with content_file.open('r') as f:
    content = json.load(f)

log_files = list_log_files(options.web_root)
most_recent_log_file = log_files[-1] if log_files else None


if options.intro_screen:
    screen = write_intro_screen()
else:
    screen = Screen(WIDTH, HEIGHT, CELL_HEIGHT)
    write_date_and_time(content, screen)
    write_forecast(content, screen)
    write_giants_games_today(content, screen)
    if most_recent_log_file:
        write_log_message(most_recent_log_file, screen)
write_bitmap(screen, options.web_root)
write_api_display(content, options.base_url, options.web_root)
write_api_setup(options.base_url, options.web_root)


sys.exit(0)
