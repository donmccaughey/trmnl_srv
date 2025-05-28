from datetime import datetime
from zoneinfo import ZoneInfo

from .header import Header


def test_string_value():
    header = Header('Host', 'www.example.com')
    assert str(header) == 'Host: www.example.com'


def test_int_value():
    header = Header('Content-Length', 71234)
    assert str(header) == 'Content-Length: 71234'


def test_datetime_value():
    pt = ZoneInfo('America/Los_Angeles')
    dt = datetime(2025, 5, 25, 22, 7, 17, tzinfo=pt)
    header = Header('Date', dt)
    assert str(header) == 'Date: Mon, 26 May 2025 05:07:17 GMT'


def test_repr():
    header = Header('Content-Length', 71234)
    assert repr(header) == "Header('Content-Length', 71234)"

    header = Header('Host', 'www.example.com')
    assert repr(header) == "Header('Host', 'www.example.com')"

    pt = ZoneInfo('America/Los_Angeles')
    dt = datetime(2025, 5, 25, 22, 7, 17, tzinfo=pt)
    header = Header('Date', dt)
    assert repr(header) == (
        "Header("
            "'Date', "
            "datetime.datetime("
                "2025, 5, 26, 5, 7, 17, tzinfo=datetime.timezone.utc"
            ")"
        ")"
    )


def test_equality():
    header1 = Header('Content-Type', 'text/plain')
    header1_dup = Header('Content-Type', 'text/plain')
    header2 = Header('Content-Type', 'text/html')
    header3 = Header('Content-Length', 71234)

    assert header1 == header1_dup
    assert header1_dup == header1

    assert header1 != header2
    assert header2 != header1

    assert header1 != header3
    assert header3 != header1


def test_hash():
    header1 = Header('Content-Type', 'text/plain')
    header1_dup = Header('Content-Type', 'text/plain')
    header2 = Header('Content-Type', 'text/html')
    header3 = Header('Content-Length', 71234)

    assert hash(header1) == hash(header1_dup)
    assert hash(header1) != hash(header2)
    assert hash(header1) != hash(header3)


def test_less_than():
    header1 = Header('Content-Type', 'text/html')
    header2 = Header('Content-Type', 'text/plain')
    header3 = Header('Host', 'www.example.com')

    assert header1 < header2
    assert header2 < header3
    assert header1 < header3


def test_greater_than():
    header1 = Header('Content-Type', 'text/html')
    header2 = Header('Content-Type', 'text/plain')
    header3 = Header('Host', 'www.example.com')

    assert header3 > header2
    assert header2 > header1
    assert header3 > header1
