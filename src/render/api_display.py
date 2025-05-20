import json

from pathlib import Path
from typing import Any
from utils import atomic_write


def write_api_display(
        content: dict[str, Any],
        base_url: str,
        refresh_rate: int,
        web_root: Path,
):
    api_display_json = {
        'filename': content['updated'],
        'firmware_url': None,
        'image_url': base_url + '/content/bitmap/index.png',
        'image_url_timeout': 5,
        'refresh_rate': refresh_rate,
        'reset_firmware': False,
        'special_function': 'sleep',
        'update_firmware': False,
    }
    atomic_write(
        web_root / 'api/display/index.json',
        lambda f: json.dump(api_display_json, f, indent=4, sort_keys=True)
    )
