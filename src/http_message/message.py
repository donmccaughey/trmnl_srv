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

    def __str__(self) -> str:
        parts = [self.start_line]
        for header in self.headers:
            parts.append(str(header))
        parts.append('')

        if isinstance(self.body, bytes):
            size = len(self.body)
            count = 10
            if size < 320:
                count = size // 32 + 1
            for i in range(count):
                begin = i * 32
                end = min((i + 1) * 32, size)
                hex_dump = self.body[begin:end].hex(' ', 2)
                parts.append(hex_dump)
            if size > 320:
                parts.append(f'... ({size:,} bytes)')
        elif isinstance(self.body, str):
            parts.append(self.body)
        elif self.body is None:
            parts.append('')
        else:
            raise TypeError(f'body is {type(self.body)}')

        return '\n'.join(parts)
