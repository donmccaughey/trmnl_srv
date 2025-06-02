from itertools import islice
from typing import Generator

from .entity import Entity


class OctetEntity(Entity):
    def __init__(self, octets: bytes):
        super().__init__()
        self.octets = octets

    @property
    def body(self) -> bytes:
        return self.octets

    def lines(self, limit: int = -1) -> Generator[str, None, None]:
        segment_size = 16
        segment_count = limit
        total_bytes = len(self.octets)
        return (
            octet_stream_preview_line(i, segment, segment_count, total_bytes)
            for i, segment
            in enumerate_segments(self.octets, segment_size, segment_count)
        )


def ascii_byte(byte: int) -> str:
    return chr(byte) if 0x20 <= byte < 0x7f else '.'


def ascii_bytes(buffer: bytes, sep: str = ' ', bytes_per_sep: int = 4) -> Generator[str, None, None]:
    for i, byte in enumerate(buffer):
        if i and not i % bytes_per_sep:
            yield sep
        yield ascii_byte(byte)


def enumerate_segments(buffer: bytes, segment_size: int = 16, segment_count: int = -1) -> Generator[tuple[int, bytes], None, None]:
    if -1 == segment_count:
        yield from enumerate(split_buffer(buffer, segment_size))
    else:
        yield from enumerate(
            islice(
                split_buffer(buffer, segment_size),
                segment_count
            )
        )


def octet_stream_preview_line(i: int, segment: bytes, segment_count: int, total_bytes: int) -> str:
    last_segment_index = segment_count - 1
    if i == last_segment_index:
        return f'... ({total_bytes:,} bytes total)'
    else:
        return segment_preview(segment)


def segment_preview(segment: bytes, sep: str = ' ', bytes_per_sep: int = 4) -> str:
    hex_dump = segment.hex(sep, -bytes_per_sep)
    ascii_dump = ''.join(ascii_bytes(segment, sep, bytes_per_sep))
    return f'{hex_dump:35} | {ascii_dump}'


def split_buffer(buffer: bytes, segment_size: int = 16) -> Generator[bytes, None, None]:
    buffer_end = len(buffer)
    for i in range(0, buffer_end, segment_size):
        end = i + segment_size
        if end > buffer_end:
            end = buffer_end
        yield buffer[i:end]
