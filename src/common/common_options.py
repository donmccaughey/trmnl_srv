from __future__ import annotations

import sys

from argparse import ArgumentParser, Namespace
from dataclasses import dataclass
from pathlib import Path
from typing import Self


@dataclass
class CommonOptions:
    web_root: Path

    @classmethod
    def add_arguments(cls, parser: ArgumentParser):
        parser.add_argument('--web-root', type=Path, required=True)

    @classmethod
    def from_namespace(cls, namespace: Namespace) -> Self:
        return cls(web_root=namespace.web_root)

    @classmethod
    def parse(cls, args: list[str] | None = None) -> Self:
        if not args:
            args = sys.argv[1:]

        parser = ArgumentParser()
        cls.add_arguments(parser)

        namespace = parser.parse_args(args)
        return cls.from_namespace(namespace)
