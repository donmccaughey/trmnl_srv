from __future__ import annotations

import os

from argparse import Namespace
from pathlib import Path
from typing import Self

from common import CommonOptions


class Options(CommonOptions):
    def __init__(self, web_root: Path, five11_org_key: str):
        super().__init__(web_root)
        self.five11_org_key = five11_org_key

    @classmethod
    def from_namespace(cls, namespace: Namespace) -> Self:
        five11_org_key = os.environ['FIVE11_ORG_KEY']

        return cls(
            five11_org_key=five11_org_key,
            web_root=namespace.web_root,
        )
