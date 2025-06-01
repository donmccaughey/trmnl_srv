import json

from itertools import islice
from typing import Generator, TypeAlias


Body: TypeAlias = bytes | str


class Entity:
    def __init__(self, body: Body):
        self.body = body

    def __str__(self) -> str:
        return '\n'.join(self.lines())

    def lines(self, content_type: str = 'text/plain', limit: int = -1) -> Generator[str, None, None]:
        if isinstance(self.body, bytes):
            yield from octet_stream_preview(self.body, limit)
        elif isinstance(self.body, str):
            yield from str_preview(content_type, self.body, limit)
        else:
            raise TypeError(f'body is {type(self.body)}')


def ascii_bytes(buffer: bytes, sep: str = ' ', bytes_per_sep: int = 4) -> str:
    chars = []
    for i, byte in enumerate(buffer):
        if i and not i % bytes_per_sep:
            chars.append(sep)
        ch = chr(byte) if 0x20 <= byte < 0x7f else '.'
        chars.append(ch)
    return ''.join(chars)


def enumerate_segments(buffer: bytes, segment_size: int = 16, segment_count: int = 8) -> Generator[tuple[int, bytes], None, None]:
    yield from enumerate(
        islice(
            split_buffer(buffer, segment_size),
            segment_count
        )
    )


def json_preview(body: Body, limit: int = -1) -> Generator[str, None, None]:
    try:
        parsed = json.loads(body)
        lines = json.dumps(parsed, ensure_ascii=True, indent=4, sort_keys=True).splitlines()
        if -1 == limit or len(lines) <= limit:
            yield from lines
        else:
            yield from lines[:limit - 2]
            yield f'    ... ({len(lines)} lines total)'
            yield lines[-1]
    except:
        yield from text_preview(body)


def octet_stream_preview(body: Body, limit: int = -1) -> Generator[str, None, None]:
    segment_size = 16
    segment_count = limit + 1
    total_bytes = len(body)
    return (
        octet_stream_preview_line(i, segment, segment_count, total_bytes)
        for i, segment
        in enumerate_segments(body, segment_size, segment_count)
    )


def octet_stream_preview_line(i: int, segment: bytes, segment_count: int, total_bytes: int) -> str:
    last_segment_index = segment_count - 1
    if i == last_segment_index:
        return f'... ({total_bytes:,} bytes total)'
    else:
        return segment_preview(segment)


def segment_preview(segment: bytes, sep: str = ' ', bytes_per_sep: int = 4) -> str:
    hex_dump = segment.hex(sep, -bytes_per_sep)
    ascii_dump = ascii_bytes(segment, sep, bytes_per_sep)
    return f'{hex_dump:35} | {ascii_dump}'


def split_buffer(buffer: bytes, segment_size: int = 16) -> Generator[bytes, None, None]:
    buffer_end = len(buffer)
    for i in range(0, buffer_end, segment_size):
        end = i + segment_size
        if end > buffer_end:
            end = buffer_end
        yield buffer[i:end]


def str_preview(content_type: str, body: Body, limit: int = -1) -> Generator[str, None, None]:
    if 'application/json' == content_type:
        yield from json_preview(body, limit)
    else:
        yield from text_preview(body, limit)


def text_preview(body: Body, limit: int = -1) -> Generator[str, None, None]:
    yield body
