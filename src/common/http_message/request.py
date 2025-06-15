import json
import requests

from datetime import datetime, timezone
from typing import Self
from urllib.parse import urlparse

from .entity import Entity
from .header import Header
from .message import Message
from .octet_entity import OctetEntity
from .text_entity import TextEntity


class Request(Message):
    def __init__(
            self,
            method: str,
            url: str,
            headers: list[Header],
            entity: Entity | None,
    ):
        request_line = f'{method} {url} HTTP/1.1'
        super().__init__(request_line, headers, entity)
        self.method = method
        self.url = url


    @property
    def request_line(self) -> str:
        return self.start_line

    @classmethod
    def from_requests(cls, request: requests.Request) -> Self:
        method = request.method
        url = request.url

        # TODO: detect and parse int and datetime header values
        headers = [
            Header(name, value) for name, value in request.headers.items()
        ]

        # TODO: handle `requests.Request.files`
        if request.data:
            if isinstance(request.data, bytes):
                entity = OctetEntity(request.data)
            elif isinstance(request.data, str):
                content_type = request.headers.get('Content-Type', 'text/plain')
                entity = TextEntity(request.data, content_type)
            else:
                raise TypeError(f'Unsupported type: {type(request.data)}')
        elif request.json:
            text = json.dumps(request.json)
            content_type = request.headers.get('Content-Type', 'text/plain')
            entity = TextEntity(text, content_type)
        else:
            entity = None

        return cls(method, url, headers, entity)
