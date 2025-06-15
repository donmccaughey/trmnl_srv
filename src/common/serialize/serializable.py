from typing import Protocol, runtime_checkable


@runtime_checkable
class Serializable(Protocol):
    def to_json(self) -> str: ...
