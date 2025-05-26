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
