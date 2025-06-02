from datetime import datetime
from zoneinfo import ZoneInfo

from .header import Header
from .request import Request
from .text_entity import TextEntity


def test_request_repr():
    headers = [
        Header('Accept', 'application/json'),
        Header('User-Agent', 'Python'),
    ]
    request = Request('GET', 'http://example.com', headers, entity=None)
    assert repr(request) == '<Request: GET http://example.com HTTP/1.1>'


def test_request_with_no_host_no_user_agent_and_no_body():
    pt = ZoneInfo('America/Los_Angeles')
    dt = datetime(2025, 5, 25, 22, 7, 17, tzinfo=pt)
    headers = [
        Header('Accept', 'application/json'),
        Header('Date', dt)
    ]
    request = Request('GET', 'http://example.com', headers, entity=None)

    assert str(request) == (
        'GET http://example.com HTTP/1.1\n'
        'Accept: application/json\n'
        'Date: Mon, 26 May 2025 05:07:17 GMT\n'
        'Host: example.com\n'
        'User-Agent: Python\n'
        '\n'
    )


def test_request_with_no_date():
    headers = [
        Header('Accept', 'application/json'),
        Header('Host', 'www.example.com'),
        Header('User-Agent', 'Test'),
    ]
    request = Request('GET', '/foo/bar', headers, entity=None)

    assert 'Date' in request


def test_request_with_json_body():
    pt = ZoneInfo('America/Los_Angeles')
    dt = datetime(2025, 5, 25, 22, 7, 17, tzinfo=pt)
    headers = [
        Header('Accept', 'application/json'),
        Header('Content-Type', 'application/json'),
        Header('Date', dt)
    ]
    entity = TextEntity(
        '{\n'
        '    "foo": "bar",\n'
        '    "baz": 42\n'
        '}',
        content_type='application/json',
    )
    request = Request('POST', 'http://example.com', headers, entity)

    assert str(request) == (
        'POST http://example.com HTTP/1.1\n'
        'Accept: application/json\n'
        'Content-Type: application/json\n'
        'Date: Mon, 26 May 2025 05:07:17 GMT\n'
        'Host: example.com\n'
        'User-Agent: Python\n'
        '\n'
        '{\n'
        '    "baz": 42,\n'
        '    "foo": "bar"\n'
        '}'
    )
