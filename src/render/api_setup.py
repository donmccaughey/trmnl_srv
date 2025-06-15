import json

from pathlib import Path
from serialize import Encodable, JSONDict, Serializable
from common import atomic_write


class APISetup(Encodable, Serializable):
    def __init__(self, base_url: str):
        self.api_key = '123456789'
        self.friendly_id = 'TRMNL123'
        self.image_url = base_url + '/content/bitmap/index.png'
        self.message = 'Welcome to trmnl_srv!'

    def encode(self) -> JSONDict:
        return {
            'api_key': self.api_key,
            'friendly_id': self.friendly_id,
            'image_url': self.image_url,
            'message': self.message,
        }

    def to_json(self) -> str:
        return json.dumps(self.encode(), indent=4, sort_keys=True)

    def write(
            self, root_dir: Path, subdir: Path = Path('api/setup/index.json')
    ):
        atomic_write(
            root_dir / subdir,
            lambda f: f.write(self.to_json()),
        )
