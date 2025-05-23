from __future__ import annotations

import json

from pathlib import Path
from serialize import Encodable, JSONDict, Serializable
from utils import atomic_write


class APISetup(Encodable, Serializable):
    def __init__(self, base_url: str):
        self.api_key = '123456789'
        self.friendly_id = 'TRMNL123'
        self.image_url = base_url + '/content/bitmap/index.png'
        self.message = 'Welcome to trmnl_srv!'

    def encode(self) -> JSONDict:
        return {
            'image_url': self.image_url,
            'api_key': self.api_key,
            'friendly_id': self.friendly_id,
            'message': self.message,
        }

    def to_json(self) -> str:
        return json.dumps(self.encode(), indent=4, sort_keys=True)

    def write(self, web_root: Path):
        atomic_write(
            web_root / 'api/setup/index.json',
            lambda f: f.write(self.to_json()),
        )
