from datetime import datetime, timezone
from email.utils import format_datetime
from typing import Any


class Header:
    def __init__(self, name: str, value: str | int | datetime):
        self.name = name
        self.value = value

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Header):
            return False
        return self.name == other.name and self.value == other.value

    def __hash__(self) -> int:
        return hash((self.name, self.value))

    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, Header):
            return False
        if self.name == other.name:
            return self.value < other.value
        else:
            return self.name < other.name

    def __repr__(self) -> str:
        if isinstance(self.value, datetime):
            dt = self.value.astimezone(timezone.utc)
            return f'Header({self.name!r}, {dt!r})'
        else:
            return f'Header({self.name!r}, {self.value!r})'

    def __str__(self) -> str:
        if isinstance(self.value, datetime):
            dt = self.value.astimezone(timezone.utc)
            value = format_datetime(dt, usegmt=True)
        else:
            value = str(self.value)
        return f'{self.name}: {value}'
