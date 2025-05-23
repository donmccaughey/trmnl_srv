import json
import sys

from datetime import datetime, timezone
from gather.weather import Weather
from utils import atomic_write

from .giants_games import GiantsGame
from .logs import get_log
from .options import Options
from .refresh_rate import get_refresh_rate


options = Options.parse()

print('Gathering...')

now = datetime.now()
updated = now.astimezone(timezone.utc)


content = {
    'forecast': {},
    'giants_games_today': [],
    'log': get_log(options.web_root, skip_old=False),
    'refresh_rate': get_refresh_rate(now),
    '~source_data': {
        'forecast_response': {},
        'forecast_hourly_response': {},
        'points_response': {},
    },
    'updated': updated.isoformat(sep=' ', timespec='seconds'),
}

weather = Weather()
if weather.get_points():
    content['~source_data']['points_response'] = weather.points_response

    if weather.get_forecast():
        content['~source_data']['forecast_response'] = weather.forecast_response
        content['forecast']['period_name'] = weather.period_name
        content['forecast']['detailed_forecast'] = weather.detailed_forecast
    else:
        content['forecast']['error'] = weather.error

    if weather.get_forecast_hourly():
        content['~source_data']['forecast_hourly_response'] = weather.forecast_hourly_response
    else:
        content['forecast']['error'] = weather.error
else:
    content['forecast']['error'] = weather.error


giants_games = GiantsGame.get_games()
todays_games = [game for game in giants_games if game.is_today(now)]
if todays_games:
    content['giants_games_today'] = [
        game.time.isoformat(timespec='minutes') for game in todays_games
    ]
else:
    content['giants_games_today'] = []


atomic_write(
    options.web_root / 'content/index.json',
    lambda f: json.dump(content, f, indent=4, sort_keys=True),
)


sys.exit(0)
