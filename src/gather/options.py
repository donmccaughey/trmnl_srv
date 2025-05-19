from __future__ import annotations

import sys

from argparse import ArgumentParser
from dataclasses import dataclass
from pathlib import Path
from typing import Self


@dataclass
class Options:
    web_root: Path

    @classmethod
    def parse(cls, args: list[str] | None = None) -> Self:
        if not args:
            args = sys.argv[1:]

        parser = ArgumentParser()
        parser.add_argument('--web-root', type=Path, required=True)
        namespace = parser.parse_args(args)
        return cls(namespace.web_root)
