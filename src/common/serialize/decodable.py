from common.serialize.jsontype import JSONDict, JSONList
from typing import Protocol, runtime_checkable, Self


@runtime_checkable
class Decodable(Protocol):
    @classmethod
    def decode(cls, encoded: JSONDict | JSONList) -> Self: ...
