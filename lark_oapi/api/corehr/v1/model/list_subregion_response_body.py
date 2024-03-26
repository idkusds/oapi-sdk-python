# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .subregion import Subregion


class ListSubregionResponseBody(object):
    _types = {
        "items": List[Subregion],
        "has_more": bool,
        "page_token": str,
    }

    def __init__(self, d=None):
        self.items: Optional[List[Subregion]] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListSubregionResponseBodyBuilder":
        return ListSubregionResponseBodyBuilder()


class ListSubregionResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_subregion_response_body = ListSubregionResponseBody()

    def items(self, items: List[Subregion]) -> "ListSubregionResponseBodyBuilder":
        self._list_subregion_response_body.items = items
        return self

    def has_more(self, has_more: bool) -> "ListSubregionResponseBodyBuilder":
        self._list_subregion_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListSubregionResponseBodyBuilder":
        self._list_subregion_response_body.page_token = page_token
        return self

    def build(self) -> "ListSubregionResponseBody":
        return self._list_subregion_response_body
