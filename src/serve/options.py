from __future__ import annotations

from argparse import ArgumentParser, Namespace
from dataclasses import dataclass
from typing import Self

from common import CommonOptions


@dataclass
class Options(CommonOptions):
    port: int

    @classmethod
    def add_arguments(cls, parser: ArgumentParser):
        super().add_arguments(parser)
        parser.add_argument("--port", type=int, default=4001)

    @classmethod
    def from_namespace(cls, namespace: Namespace) -> Self:
        return cls(
            port=namespace.port,
            web_root=namespace.web_root
        )
