from pathlib import Path
from pytest import raises

from .common_options import CommonOptions


def test_parse():
    common_options = CommonOptions.parse(['--web-root', 'foo/bar'])
    assert common_options.web_root == Path('foo/bar')


def test_parse_missing_option():
    with raises(SystemExit):
        CommonOptions.parse([])
    with raises(SystemExit):
        CommonOptions.parse(['--web-root'])
