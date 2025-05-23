import json

from io import StringIO
from pathlib import Path

from .api_display import APIDisplay


def test_api_display():
    api_display = APIDisplay(
        base_url='https://example.com',
        filename='some-random-filename',
        refresh_rate=42,
    )
    assert api_display.filename == 'some-random-filename'
    assert api_display.image_url == 'https://example.com/content/bitmap/index.png'
    assert api_display.refresh_rate == 42

    encoded = api_display.encode()
    assert encoded == {
        'filename': 'some-random-filename',
        'firmware_url': None,
        'image_url': 'https://example.com/content/bitmap/index.png',
        'image_url_timeout': 5,
        'refresh_rate': 42,
        'reset_firmware': False,
        'special_function': 'sleep',
        'update_firmware': False,
    }
    assert api_display.to_json() == (
        '{\n'
        '    "filename": "some-random-filename",\n'
        '    "firmware_url": null,\n'
        '    "image_url": "https://example.com/content/bitmap/index.png",\n'
        '    "image_url_timeout": 5,\n'
        '    "refresh_rate": 42,\n'
        '    "reset_firmware": false,\n'
        '    "special_function": "sleep",\n'
        '    "update_firmware": false\n'
        '}'
    )


def test_write(monkeypatch):
    import render.api_display

    calls = []
    monkeypatch.setattr(
        render.api_display, 'atomic_write', lambda a, b: calls.append((a, b))
    )

    api_display = APIDisplay(
        base_url='https://example.com',
        filename='some-random-filename',
        refresh_rate=42,
    )
    api_display.write(Path('/srv/www'))

    assert len(calls) == 1

    path, write = calls.pop()
    assert path == Path('/srv/www/api/display/index.json')
    assert callable(write)

    f = StringIO()
    write(f)
    written = f.getvalue()
    json_dict = json.loads(written)
    assert isinstance(json_dict, dict)
    assert json_dict == api_display.encode()
