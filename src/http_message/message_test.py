from .header import Header
from .message import ascii_bytes, enumerate_segments, Message, segment_preview, split_buffer


def test_ascii_bytes():
    buffer = bytes(range(0, 16))
    assert ascii_bytes(buffer) == '.... .... .... ....'

    buffer = bytes(range(32, 48))
    assert ascii_bytes(buffer) == ' !"# $%&\' ()*+ ,-./'

    buffer = bytes(range(64, 80))
    assert ascii_bytes(buffer) == '@ABC DEFG HIJK LMNO'

    buffer = bytes(range(112, 128))
    assert ascii_bytes(buffer) == 'pqrs tuvw xyz{ |}~.'


def test_enumerate_segments():
    buffer = bytes((i % 256 for i in range(512)))
    segments = list(enumerate_segments(buffer))

    assert len(segments) == 8
    assert segments[0] == (0, bytes(range(16)))
    assert segments[-1] == (7, bytes(range(112, 128)))


def test_enumerate_segments_for_small_final_segment():
    buffer = bytes(range(20))
    segments = list(enumerate_segments(buffer))

    assert len(segments) == 2
    assert segments[0] == (0, bytes(range(16)))
    assert segments[-1] == (1, bytes(range(16, 20)))


def test_message_headers_indexed():
    headers = [
        Header('User-Agent', 'Python'),
        Header('Host', 'www.example.com'),
        Header('Content-Length', 71234),
        Header('Accept', 'application/json'),
        Header('Content-Type', 'text/plain'),
    ]
    message = Message('TEST message', headers, body=None)

    assert 'Accept' in message
    assert message['Accept'] == 'application/json'

    assert 'Content-Disposition' not in message


def test_message_headers_are_sorted():
    headers = [
        Header('User-Agent', 'Python'),
        Header('Host', 'www.example.com'),
        Header('Content-Length', 71234),
        Header('Accept', 'application/json'),
        Header('Content-Type', 'text/plain'),
    ]
    message = Message('TEST message', headers, body=None)

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
    message = Message('This is a test', headers, body=None)
    assert repr(message) == '<Message: This is a test>'


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
        'deadbeef                            | ....'
    )
    assert str(message) == expected


def test_message_with_large_bytes_body():
    headers = [
        Header('Content-Type', 'application/octet-stream'),
    ]
    body = bytes((i % 256 for i in range(512)))
    message = Message('TEST message', headers, body)

    expected = (
        'TEST message\n'
        'Content-Type: application/octet-stream\n'
        '\n'
        '00010203 04050607 08090a0b 0c0d0e0f | .... .... .... ....\n'
        '10111213 14151617 18191a1b 1c1d1e1f | .... .... .... ....\n'
        '20212223 24252627 28292a2b 2c2d2e2f |  !"# $%&\' ()*+ ,-./\n'
        '30313233 34353637 38393a3b 3c3d3e3f | 0123 4567 89:; <=>?\n'
        '40414243 44454647 48494a4b 4c4d4e4f | @ABC DEFG HIJK LMNO\n'
        '50515253 54555657 58595a5b 5c5d5e5f | PQRS TUVW XYZ[ \\]^_\n'
        '60616263 64656667 68696a6b 6c6d6e6f | `abc defg hijk lmno\n'
        '70717273 74757677 78797a7b 7c7d7e7f | pqrs tuvw xyz{ |}~.\n'
        '... (512 bytes total)'
    )
    assert str(message) == expected


def test_segment_preview():
    segment = bytes(range(64, 80))
    assert segment_preview(segment) == (
        '40414243 44454647 48494a4b 4c4d4e4f | @ABC DEFG HIJK LMNO'
    )


def test_segment_preview_for_short_segment():
    segment = bytes.fromhex('deadbeef')
    assert segment_preview(segment) == (
        'deadbeef                            | ....'
    )


def test_split_buffer():
    buffer = bytes((i % 256 for i in range(512)))
    segments = list(split_buffer(buffer))

    assert len(segments) == 32
    assert len(segments[0]) == 16
    assert segments[0].hex(' ', -4) == (
        '00010203 04050607 08090a0b 0c0d0e0f'
    )
    assert segments[-1].hex(' ', -4) == (
        'f0f1f2f3 f4f5f6f7 f8f9fafb fcfdfeff'
    )


def test_split_buffer_with_segment_size():
    buffer = bytes((i % 256 for i in range(512)))
    segments = list(split_buffer(buffer, segment_size=8))

    assert len(segments) == 64
    assert len(segments[0]) == 8
    assert segments[0].hex(' ', -4) == '00010203 04050607'
    assert segments[-1].hex(' ', -4) == 'f8f9fafb fcfdfeff'


def test_split_buffer_for_empty_buffer():
    buffer = bytes()
    segments = list(split_buffer(buffer))

    assert len(segments) == 0


def test_split_buffer_for_small_single_segment():
    buffer = bytes(range(14))
    segments = list(split_buffer(buffer))

    assert len(segments) == 1
    assert len(segments[0]) == 14
    assert segments[0].hex(' ', -4) == (
        '00010203 04050607 08090a0b 0c0d'
    )


def test_split_buffer_for_small_final_segment():
    buffer = bytes(range(20))
    segments = list(split_buffer(buffer))

    assert len(segments) == 2

    assert len(segments[0]) == 16
    assert segments[0].hex(' ', -4) == (
        '00010203 04050607 08090a0b 0c0d0e0f'
    )

    assert len(segments[1]) == 4
    assert segments[1].hex(' ', -4) == '10111213'
