from .header import Header
from .message import Message
from .octet_entity import OctetEntity
from .text_entity import TextEntity


def test_message_headers_implements_contains_and_getitem():
    headers = [
        Header('User-Agent', 'Python'),
        Header('Host', 'www.example.com'),
        Header('Content-Length', 71234),
        Header('Accept', 'application/json'),
        Header('Content-Type', 'text/plain'),
    ]
    message = Message('TEST message', headers, entity=None)

    assert 'Accept' in message
    assert message['Accept'] == 'application/json'

    assert 'Content-Disposition' not in message


def test_message_headers_get():
    headers = [
        Header('User-Agent', 'Python'),
        Header('Host', 'www.example.com'),
        Header('Content-Length', 71234),
        Header('Accept', 'application/json'),
        Header('Content-Type', 'text/plain'),
    ]
    message = Message('TEST message', headers, entity=None)

    assert message.get('Accept') == 'application/json'
    assert message.get('Content-Disposition') is None
    assert message.get('Connection', 'close') == 'close'


def test_message_headers_are_sorted():
    headers = [
        Header('User-Agent', 'Python'),
        Header('Host', 'www.example.com'),
        Header('Content-Length', 71234),
        Header('Accept', 'application/json'),
        Header('Content-Type', 'text/plain'),
    ]
    message = Message('TEST message', headers, entity=None)

    expected = (
        'TEST message\n'
        'Accept: application/json\n'
        'Content-Length: 71234\n'
        'Content-Type: text/plain\n'
        'Host: www.example.com\n'
        'User-Agent: Python\n'
        '\n'
    )
    assert str(message) == expected


def test_message_repr():
    headers = [
        Header('Accept', 'application/json'),
        Header('User-Agent', 'Python'),
    ]
    message = Message('This is a test', headers, entity=None)
    assert repr(message) == '<Message: This is a test>'


def test_message_with_no_body():
    headers = [
        Header('Accept', 'application/json'),
        Header('User-Agent', 'Python'),
    ]
    message = Message('TEST message', headers, entity=None)

    assert message.lines() ==  [
        'TEST message',
        'Accept: application/json',
        'User-Agent: Python',
        '',
        '',
    ]
    assert str(message) == (
        'TEST message\n'
        'Accept: application/json\n'
        'User-Agent: Python\n'
        '\n'
    )


def test_message_with_string_body():
    headers = [
        Header('Content-Type', 'text/plain'),
    ]
    entity = TextEntity('This is a test message')
    message = Message('TEST message', headers, entity)

    assert message.lines(8) == [
        'TEST message',
        'Content-Type: text/plain',
        '',
        'This is a test message',
    ]


def test_message_with_short_json_body():
    headers = [
        Header('Content-Type', 'application/json'),
    ]
    entity = TextEntity(
        '{"foo":"bar","baz":42}', content_type='application/json'
    )
    message = Message('TEST message', headers, entity)

    assert message.lines(8) == [
        'TEST message',
        'Content-Type: application/json',
        '',
        '{',
        '    "baz": 42,',
        '    "foo": "bar"',
        '}',
    ]


def test_message_with_long_json_body():
    headers = [
        Header('Content-Type', 'application/json'),
    ]
    entity = TextEntity(
        '{"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8}',
        content_type='application/json',
    )
    message = Message('TEST message', headers, entity)

    assert message.lines(8) == [
        'TEST message',
        'Content-Type: application/json',
        '',
        '{',
        '    "1": 1,',
        '    "2": 2,',
        '    "3": 3,',
        '    "4": 4,',
        '    "5": 5,',
        '    ... (3 lines omitted)',
        '}',
    ]


def test_message_with_bytes_body():
    headers = [
        Header('Content-Type', 'application/octet-stream'),
    ]
    entity = OctetEntity(bytes.fromhex('deadbeef'))
    message = Message('TEST message', headers, entity)

    assert message.lines(8) == [
        'TEST message',
        'Content-Type: application/octet-stream',
        '',
        'deadbeef                            | ....',
    ]


def test_message_with_large_bytes_body():
    headers = [
        Header('Content-Type', 'application/octet-stream'),
    ]
    entity = OctetEntity(bytes((i % 256 for i in range(512))))
    message = Message('TEST message', headers, entity)

    assert message.lines(8) == [
        'TEST message',
        'Content-Type: application/octet-stream',
        '',
        '00010203 04050607 08090a0b 0c0d0e0f | .... .... .... ....',
        '10111213 14151617 18191a1b 1c1d1e1f | .... .... .... ....',
        '20212223 24252627 28292a2b 2c2d2e2f |  !"# $%&\' ()*+ ,-./',
        '30313233 34353637 38393a3b 3c3d3e3f | 0123 4567 89:; <=>?',
        '40414243 44454647 48494a4b 4c4d4e4f | @ABC DEFG HIJK LMNO',
        '50515253 54555657 58595a5b 5c5d5e5f | PQRS TUVW XYZ[ \\]^_',
        '60616263 64656667 68696a6b 6c6d6e6f | `abc defg hijk lmno',
        '... (512 bytes total)',
    ]
