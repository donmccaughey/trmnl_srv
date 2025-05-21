import json
import sys

from datetime import datetime, timezone
from gather.weather import Weather
from utils import atomic_write

from .giants_games import GiantsGame
from .options import Options


options = Options.parse()

print('Gathering...')

content = {}

weather = Weather()
content['forecast'] = {}
if weather.get_points():
    content['forecast']['points_response'] = weather.points_response

    if weather.get_forecast():
        content['forecast']['forecast_response'] = weather.points_response
        content['forecast']['period_name'] = weather.period_name
        content['forecast']['detailed_forecast'] = weather.detailed_forecast
    else:
        content['forecast']['error'] = weather.error
else:
    content['forecast']['error'] = weather.error


giants_games = GiantsGame.get_games()
now = datetime.now()
todays_games = [game for game in giants_games if game.is_today(now)]
if todays_games:
    content['giants_games_today'] = [
        game.time.isoformat(timespec='minutes') for game in todays_games
    ]
else:
    content['giants_games_today'] = []


updated = datetime.now(timezone.utc)
content['updated'] = updated.isoformat(sep=' ', timespec='seconds')

atomic_write(
    options.web_root / 'content/index.json',
    lambda f: json.dump(content, f, indent=4, sort_keys=True),
)


sys.exit(0)
