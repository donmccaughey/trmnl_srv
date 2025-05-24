from __future__ import annotations

import os
import sys

from argparse import ArgumentParser
from dataclasses import dataclass
from pathlib import Path
from typing import Self


@dataclass
class Options:
    five11_org_key: str
    web_root: Path

    @classmethod
    def parse(cls, args: list[str] | None = None) -> Self:
        if not args:
            args = sys.argv[1:]

        parser = ArgumentParser()
        parser.add_argument('--web-root', type=Path, required=True)
        namespace = parser.parse_args(args)

        five11_org_key = os.environ['FIVE11_ORG_KEY']

        return cls(
            five11_org_key=five11_org_key,
            web_root=namespace.web_root,
        )
