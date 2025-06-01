from abc import ABC, abstractmethod
from typing import Any, Generator


class Entity(ABC):
    def __str__(self) -> str:
        return '\n'.join(self.lines())

    @property
    @abstractmethod
    def body(self) -> Any: ...

    @abstractmethod
    def lines(self, limit: int = -1) -> Generator[str, None, None]: ...
