import json

from typing import Generator

from .entity import Entity


class TextEntity(Entity):
    def __init__(self, text: str, content_type: str = 'text/plain'):
        super().__init__()
        self.text = text
        self.content_type = content_type

    @property
    def body(self) -> str:
        return self.text

    def lines(self, limit: int = -1) -> Generator[str, None, None]:
        if 'application/json' == self.content_type:
            yield from application_json(self.text, limit)
        else:
            yield from plain_text(self.text, limit)


def application_json(text: str, limit: int = -1) -> Generator[str, None, None]:
    try:
        parsed = json.loads(text)
        lines = json.dumps(
            parsed, ensure_ascii=True, indent=4, sort_keys=True
        ).splitlines()
        if -1 == limit or len(lines) <= limit:
            yield from lines
        else:
            yield from lines[:limit - 2]
            yield f'    ... ({len(lines) - limit + 1} lines omitted)'
            yield lines[-1]
    except:
        yield from plain_text(text)


def plain_text(text: str, limit: int = -1) -> Generator[str, None, None]:
    lines = text.splitlines()
    # TODO: handle long lines
    if -1 == limit or len(lines) <= limit:
        yield from lines
    else:
        yield from lines[:limit - 1]
        yield f'... ({len(lines) - limit + 1} lines omitted)'
