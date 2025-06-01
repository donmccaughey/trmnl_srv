from datetime import datetime

from .entity import Entity
from .header import Header


class Message:
    def __init__(
            self,
            start_line: str,
            headers: list[Header],
            entity: Entity | None,
    ):
        self.start_line = start_line
        self.headers = headers
        self.entity = entity

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
        return '\n'.join(self.lines())

    def lines(self, entity_lines_limit: int = -1) -> list[str]:
        lines = [self.start_line]
        for header in sorted(self.headers):
            lines.append(str(header))

        lines.append('')

        if self.entity:
            content_type = self.get('Content-Type', 'text/plain')
            lines.extend(self.entity.lines(content_type, entity_lines_limit))
        else:
            lines.append('')

        return lines
