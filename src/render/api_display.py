import json

from pathlib import Path
from serialize import Encodable, JSONDict, Serializable
from common import atomic_write


class APIDisplay(Encodable, Serializable):
    def __init__(self, base_url: str, filename: str, refresh_rate: int):
        self.filename = filename
        self.firmware_url: str | None = None
        self.image_url = base_url + '/content/bitmap/index.png'
        self.image_url_timeout = 5
        self.refresh_rate = refresh_rate
        self.reset_firmware = False
        self.special_function = 'sleep'
        self.update_firmware = False

    def encode(self) -> JSONDict:
        return {
            'filename': self.filename,
            'firmware_url': self.firmware_url,
            'image_url': self.image_url,
            'image_url_timeout': self.image_url_timeout,
            'refresh_rate': self.refresh_rate,
            'reset_firmware': self.reset_firmware,
            'special_function': self.special_function,
            'update_firmware': self.update_firmware,
        }

    def to_json(self) -> str:
        return json.dumps(self.encode(), indent=4, sort_keys=True)

    def write(
            self, root_dir: Path, subdir: Path = Path('api/display/index.json')
    ):
        atomic_write(
            root_dir / subdir,
            lambda f: f.write(self.to_json()),
        )
