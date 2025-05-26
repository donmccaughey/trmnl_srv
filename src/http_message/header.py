from datetime import datetime, timezone
from email.utils import format_datetime

class Header:
    def __init__(self, name: str, value: str | int | datetime):
        self.name = name
        self.value = value

    def __str__(self) -> str:
        if isinstance(self.value, datetime):
            dt = self.value.astimezone(timezone.utc)
            value = format_datetime(dt, usegmt=True)
        else:
            value = str(self.value)
        return f'{self.name}: {value}'
