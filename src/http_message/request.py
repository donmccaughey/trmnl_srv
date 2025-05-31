from datetime import datetime, timezone
from urllib.parse import urlparse

from .header import Header
from .message import Message


class Request(Message):
    def __init__(
            self,
            method: str,
            url: str,
            headers: list[Header],
            body: bytes | str | None
    ):
        request_line = f'{method} {url} HTTP/1.1'
        super().__init__(request_line, headers, body)

        if not 'Date' in self:
            self.headers.append(Header('Date', datetime.now(tz=timezone.utc)))
        if not 'Host' in self:
            url_parts = urlparse(url)
            if url_parts.netloc:
                self.headers.append(Header('Host', url_parts.netloc))
        if not 'User-Agent' in self:
            self.headers.append(Header('User-Agent', 'Python'))

        self.method = method
        self.url = url


    @property
    def request_line(self) -> str:
        return self.start_line
