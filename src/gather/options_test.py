import os

from pathlib import Path
from pytest import fixture, mark, raises

from .options import Options


@fixture()
def five11_org_key():
    os.environ['FIVE11_ORG_KEY'] = 'my-secret-key'
    yield
    if 'FIVE11_ORG_KEY' in os.environ:
        del os.environ['FIVE11_ORG_KEY']


@fixture()
def no_five11_org_key():
    previous_value = None
    if 'FIVE11_ORG_KEY' in os.environ:
        previous_value = os.environ['FIVE11_ORG_KEY']
        del os.environ['FIVE11_ORG_KEY']
    yield
    if previous_value:
        os.environ['FIVE11_ORG_KEY'] = previous_value


@mark.usefixtures('five11_org_key')
def test_parse():
    options = Options.parse(['--web-root', 'foo/bar'])
    assert options.five11_org_key == 'my-secret-key'
    assert options.web_root == Path('foo/bar')


@mark.usefixtures('no_five11_org_key')
def test_parse_missing_env():
    with raises(KeyError):
        Options.parse(['--web-root', 'foo/bar'])


@mark.usefixtures('five11_org_key')
def test_parse_missing_option():
    with raises(SystemExit):
        Options.parse([])
    with raises(SystemExit):
        Options.parse(['--web-root'])
