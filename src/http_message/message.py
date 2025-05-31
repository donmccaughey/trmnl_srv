from datetime import datetime
from itertools import islice
from typing import Generator

from .header import Header


class Message:
    def __init__(
            self,
            start_line: str,
            headers: list[Header],
            body: bytes | str | None
    ):
        self.start_line = start_line
        self.headers = headers
        self.body = body

    def __contains__(self, item: str) -> bool:
        for header in self.headers:
            if header.name == item:
                return True
        return False

    def __getitem__(self, item: str) -> str | int | datetime:
        for header in self.headers:
            if header.name == item:
                return header.value
        raise KeyError(item)

    def get(self, item: str, default=None, /) -> str | int | datetime:
        for header in self.headers:
            if header.name == item:
                return header.value
        return default

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}: {self.start_line}>'

    def __str__(self) -> str:
        parts = [self.start_line]
        for header in sorted(self.headers):
            parts.append(str(header))
        parts.append('')

        if isinstance(self.body, bytes):
            parts.extend(octet_stream_preview(self.body))
        elif isinstance(self.body, str):
            parts.append(self.body)
        elif self.body is None:
            parts.append('')
        else:
            raise TypeError(f'body is {type(self.body)}')

        return '\n'.join(parts)


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


def octet_stream_preview(buffer: bytes) -> Generator[str, None, None]:
    segment_size = 16
    segment_count = 9
    total_bytes = len(buffer)
    return (
        octet_stream_preview_line(i, segment, segment_count, total_bytes)
        for i, segment in enumerate_segments(buffer, segment_size, segment_count)
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
