from .header import Header
from .message import Message


class Response(Message):
    def __init__(
            self,
            status_code: int,
            reason_phrase: str,
            headers: list[Header],
            body: bytes | str | None
    ):
        self.status_code = status_code
        self.reason_phrase = reason_phrase
        status_line = f'HTTP/1.1 {status_code} {reason_phrase}'
        super().__init__(status_line, headers, body)

    @property
    def status_line(self) -> str:
        return self.start_line

    @property
    def is_informational(self) -> bool:
        return 100 <= self.status_code < 200

    @property
    def is_success(self) -> bool:
        return 200 <= self.status_code < 300

    @property
    def is_redirect(self) -> bool:
        return 300 <= self.status_code < 400

    @property
    def is_client_error(self) -> bool:
        return 400 <= self.status_code < 500

    @property
    def is_server_error(self) -> bool:
        return 500 <= self.status_code < 600