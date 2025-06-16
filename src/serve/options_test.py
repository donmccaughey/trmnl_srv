from pathlib import Path
from pytest import raises

from .options import Options


def test_parse():
    options = Options.parse(['--web-root', 'foo/bar'])
    assert options.web_root == Path('foo/bar')
    assert options.port == 4001


def test_parse_port():
    options = Options.parse([
        '--web-root', 'foo/bar',
        '--port', '5000',
    ])
    assert options.web_root == Path('foo/bar')
    assert options.port == 5000


def test_parse_missing_option():
    with raises(SystemExit):
        Options.parse([])
    with raises(SystemExit):
        Options.parse(['--web-root'])
    with raises(SystemExit):
        Options.parse([
            '--web-root', 'foo/bar',
            '--port',
        ])
