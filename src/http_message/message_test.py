from .header import Header
from .message import Message


def test_message_with_no_body():
    headers = [
        Header('Accept', 'application/json'),
        Header('User-Agent', 'Python'),
    ]
    message = Message('TEST message', headers, body=None)

    expected = (
        'TEST message\n'
        'Accept: application/json\n'
        'User-Agent: Python\n'
        '\n'
    )
    assert str(message) == expected


def test_message_with_string_body():
    headers = [
        Header('Content-Type', 'text/plain'),
    ]
    body = 'This is a test message'
    message = Message('TEST message', headers, body)

    expected = (
        'TEST message\n'
        'Content-Type: text/plain\n'
        '\n'
        'This is a test message'
    )
    assert str(message) == expected


def test_message_with_bytes_body():
    headers = [
        Header('Content-Type', 'application/octet-stream'),
    ]
    body = bytes.fromhex('deadbeef')
    message = Message('TEST message', headers, body)

    expected = (
        'TEST message\n'
        'Content-Type: application/octet-stream\n'
        '\n'
        'dead beef'
    )
    assert str(message) == expected
