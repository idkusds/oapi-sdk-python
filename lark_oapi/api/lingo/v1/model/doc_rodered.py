# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DocRodered(object):
    _types = {
        "text": str,
    }

    def __init__(self, d=None):
        self.text: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DocRoderedBuilder":
        return DocRoderedBuilder()


class DocRoderedBuilder(object):
    def __init__(self) -> None:
        self._doc_rodered = DocRodered()

    def text(self, text: str) -> "DocRoderedBuilder":
        self._doc_rodered.text = text
        return self

    def build(self) -> "DocRodered":
        return self._doc_rodered
