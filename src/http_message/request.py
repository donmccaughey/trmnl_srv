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
        self.method = method
        self.url = url
        request_line = f'{method} {url} HTTP/1.1'
        super().__init__(request_line, headers, body)

    @property
    def request_line(self) -> str:
        return self.start_line
