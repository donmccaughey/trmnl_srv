from pathlib import Path
from pytest import raises

from .options import Options


def test_parse():
    options = Options.parse(['--web-root', 'foo/bar'])
    assert options.web_root == Path('foo/bar')
    assert options.base_url == 'http://127.0.0.1:4000'
    assert options.intro_screen is False


def test_parse_base_url():
    options = Options.parse([
        '--web-root', 'foo/bar',
        '--base-url', 'http://example.com',
    ])
    assert options.web_root == Path('foo/bar')
    assert options.base_url == 'http://example.com'
    assert options.intro_screen is False


def test_parse_intro_screen():
    options = Options.parse([
        '--web-root', 'foo/bar',
        '--intro-screen',
    ])
    assert options.web_root == Path('foo/bar')
    assert options.base_url == 'http://127.0.0.1:4000'
    assert options.intro_screen is True


def test_parse_missing_option():
    with raises(SystemExit):
        Options.parse([])
    with raises(SystemExit):
        Options.parse(['--web-root'])
    with raises(SystemExit):
        Options.parse([
            '--web-root', 'foo/bar',
            '--base-url',
        ])
