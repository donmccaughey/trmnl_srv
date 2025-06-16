from __future__ import annotations

import os

from argparse import Namespace
from dataclasses import dataclass
from typing import Self

from common import CommonOptions


@dataclass
class Options(CommonOptions):
    five11_org_key: str

    @classmethod
    def from_namespace(cls, namespace: Namespace) -> Self:
        five11_org_key = os.environ['FIVE11_ORG_KEY']

        return cls(
            five11_org_key=five11_org_key,
            web_root=namespace.web_root,
        )
