from __future__ import annotations

from argparse import ArgumentParser, Namespace
from pathlib import Path
from typing import Self

from common import CommonOptions


class Options(CommonOptions):
    def __init__(self, web_root: Path, base_url: str, intro_screen: bool):
        super().__init__(web_root)
        self.base_url = base_url
        self.intro_screen = intro_screen

    @classmethod
    def add_arguments(cls, parser: ArgumentParser):
        super().add_arguments(parser)
        parser.add_argument(
            '--base-url', type=str, default='http://127.0.0.1:4000'
        )
        parser.add_argument('--intro-screen', action='store_true')

    @classmethod
    def from_namespace(cls, namespace: Namespace) -> Self:
        return cls(
            base_url=namespace.base_url,
            intro_screen=namespace.intro_screen,
            web_root=namespace.web_root,
        )
