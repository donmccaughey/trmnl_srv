from typing import Protocol, runtime_checkable, Self


@runtime_checkable
class Deserializable(Protocol):
    @classmethod
    def from_json(cls, s: str) -> Self: ...
