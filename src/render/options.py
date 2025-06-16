from __future__ import annotations

from argparse import ArgumentParser, Namespace
from dataclasses import dataclass
from typing import Self

from common import CommonOptions


@dataclass
class Options(CommonOptions):
    base_url: str
    intro_screen: bool

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
