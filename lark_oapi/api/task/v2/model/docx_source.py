# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DocxSource(object):
    _types = {
        "token": str,
        "block_id": str,
    }

    def __init__(self, d=None):
        self.token: Optional[str] = None
        self.block_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DocxSourceBuilder":
        return DocxSourceBuilder()


class DocxSourceBuilder(object):
    def __init__(self) -> None:
        self._docx_source = DocxSource()

    def token(self, token: str) -> "DocxSourceBuilder":
        self._docx_source.token = token
        return self

    def block_id(self, block_id: str) -> "DocxSourceBuilder":
        self._docx_source.block_id = block_id
        return self

    def build(self) -> "DocxSource":
        return self._docx_source
