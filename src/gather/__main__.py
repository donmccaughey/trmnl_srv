import json
import sys

from datetime import datetime, timezone
from pathlib import Path
from gather.weather import Weather


print('Gathering...')

content = {}

weather = Weather()
if weather.get_points():
    weather.get_forecast()
    content['forecast'] = {
        'period_name': weather.period_name,
        'detailed_forecast': weather.detailed_forecast,
    }

updated = datetime.now(timezone.utc)
content['updated'] = updated.isoformat(sep=' ', timespec='seconds')

content_dir = Path('../tmp')
content_dir.mkdir(parents=True, exist_ok=True)
content_file = content_dir / 'content.json'
with content_file.open('w') as f:
    json.dump(content, f)

sys.exit(0)
