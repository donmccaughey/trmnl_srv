import json
import sys

from datetime import datetime, timedelta, timezone
from gather.weather import Weather
from common import atomic_write

from .five11 import Five11
from .giants_games import GiantsGame
from .logs import get_log
from .options import Options
from .refresh_rate import get_refresh_rate


TWO_MINUTES = timedelta(minutes=2)
HALF_HOUR = timedelta(minutes=30)


options = Options.parse()

print('Gathering...')

now = datetime.now(timezone.utc)
now_iso_date = now.isoformat(sep=' ', timespec='seconds')

content = {
    'forecast': {
        'updated': '1970-01-01 00:00:00+00:00',
    },
    'giants_games_today': [],
    'log': {},
    'muni': {
        'updated': '1970-01-01 00:00:00+00:00',
    },
    'refresh_rate': 60,
    '~source_data': {
        'forecast_response': {},
        'forecast_hourly_response': {},
        'points_response': {},
        'stop_monitoring_response': {},
    },
    'updated': now_iso_date,
}

content_file = options.web_root / 'content/index.json'
if content_file.exists():
    with content_file.open('r') as f:
        content = json.load(f)
        last_updated = datetime.fromisoformat(content['updated'])
        content['updated'] = now_iso_date


last_weather_update = datetime.fromisoformat(content['forecast']['updated'])
time_since_last_weather_update = now - last_weather_update
if time_since_last_weather_update >= HALF_HOUR:
    print('- fetching from api.weather.gov')

    content['forecast'] = {
        'updated': now_iso_date,
    }
    content['~source_data']['points_response'] = {}
    content['~source_data']['forecast_response'] = {}
    content['~source_data']['forecast_hourly_response'] = {}

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


content['log'] = get_log(options.trmnl_logs)


last_muni_update = datetime.fromisoformat(content['muni']['updated'])
time_since_last_muni_update = now - last_muni_update
if time_since_last_muni_update >= TWO_MINUTES:
    print('- fetching from api.511.org')

    content['muni'] = {
        'updated': now_iso_date,
    }
    content['~source_data']['stop_monitoring_response'] = {}

    muni_t = Five11(options.five11_org_key)
    if muni_t.get_stop_monitoring():
        content['~source_data']['stop_monitoring_response'] = muni_t.stop_monitoring_response

        if muni_t.expected_arrival_times:
            content['muni']['expected_arrival_times'] = [
                arrival_time.isoformat(sep=' ', timespec='seconds')
                for arrival_time in muni_t.expected_arrival_times
            ]
        else:
            content['muni']['error'] = muni_t.error


content['refresh_rate'] = get_refresh_rate(now)


atomic_write(
    content_file,
    lambda f: json.dump(content, f, indent=4, sort_keys=True),
)


sys.exit(0)
