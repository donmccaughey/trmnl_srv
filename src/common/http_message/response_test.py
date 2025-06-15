from .header import Header
from .response import Response
from .text_entity import TextEntity


def test_response_repr():
    headers = [
        Header('Content-Type', 'text/plain'),
        Header('Content-Length', 14),
    ]
    entity = TextEntity('This is a test', content_type='text/plain')
    response = Response(200, 'OK', headers, entity)
    assert repr(response) == '<Response: HTTP/1.1 200 OK>'


def test_response_with_no_body():
    headers = [
        Header('Location', 'https://example.com/other/resource'),
    ]
    response = Response(303, 'See Other', headers, None)

    assert str(response) == (
        'HTTP/1.1 303 See Other\n'
        'Location: https://example.com/other/resource\n'
        '\n'
    )


def test_response_with_json_body():
    headers = [
        Header('Content-Type', 'application/json'),
    ]
    entity = TextEntity(
        '{\n'
        '    "foo": "bar",\n'
        '    "baz": 42\n'
        '}',
        content_type='application/json',
    )
    response = Response(200, 'OK', headers, entity)

    assert str(response) == (
        'HTTP/1.1 200 OK\n'
        'Content-Type: application/json\n'
        '\n'
        '{\n'
        '    "baz": 42,\n'
        '    "foo": "bar"\n'
        '}'
    )
