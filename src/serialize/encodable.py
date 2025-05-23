from serialize.jsontype import JSONDict, JSONList
from typing import Protocol, runtime_checkable


@runtime_checkable
class Encodable(Protocol):
    def encode(self) -> JSONDict | JSONList: ...
