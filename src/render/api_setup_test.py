import json

from io import StringIO
from pathlib import Path

from .api_setup import APISetup


def test_api_setup():
    api_setup = APISetup('https://example.com')
    assert api_setup.image_url == 'https://example.com/content/bitmap/index.png'

    encoded = api_setup.encode()
    assert encoded == {
        'api_key': '123456789',
        'friendly_id': 'TRMNL123',
        'image_url': 'https://example.com/content/bitmap/index.png',
        'message': 'Welcome to trmnl_srv!',
    }
    assert api_setup.to_json() == (
        '{\n'
        '    "api_key": "123456789",\n'
        '    "friendly_id": "TRMNL123",\n'
        '    "image_url": "https://example.com/content/bitmap/index.png",\n'
        '    "message": "Welcome to trmnl_srv!"\n'
        '}'
    )


def test_write(monkeypatch):
    import render.api_setup

    calls = []
    monkeypatch.setattr(
        render.api_setup, 'atomic_write', lambda a, b: calls.append((a, b))
    )

    api_setup = APISetup('https://example.com')
    api_setup.write(Path('/srv/www'))

    assert len(calls) == 1

    path, write = calls.pop()
    assert path == Path('/srv/www/api/setup/index.json')
    assert callable(write)

    f = StringIO()
    write(f)
    written = f.getvalue()
    json_dict = json.loads(written)
    assert isinstance(json_dict, dict)
    assert json_dict == api_setup.encode()
