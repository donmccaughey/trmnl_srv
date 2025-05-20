import json

from pathlib import Path
from utils import atomic_write


def write_api_setup(base_url: str, web_root: Path):
    api_setup_json = {
        'api_key': '123456789',
        'friendly_id': 'TRMNL123',
        'image_url': base_url + '/content/bitmap/index.png',
        'message': 'Welcome to trmnl_srv!'
    }
    atomic_write(
        web_root / 'api/setup/index.json',
        lambda f: json.dump(api_setup_json, f, indent=4, sort_keys=True)
    )
