from __future__ import annotations

from argparse import ArgumentParser, Namespace
from pathlib import Path
from typing import Self

from common import CommonOptions


class Options(CommonOptions):
    def __init__(self, web_root: Path, port: int):
        super().__init__(web_root)
        self.port = port

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
