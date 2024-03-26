# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .mailgroup import Mailgroup


class ListMailgroupResponseBody(object):
    _types = {
        "has_more": bool,
        "page_token": str,
        "items": List[Mailgroup],
    }

    def __init__(self, d=None):
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        self.items: Optional[List[Mailgroup]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListMailgroupResponseBodyBuilder":
        return ListMailgroupResponseBodyBuilder()


class ListMailgroupResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_mailgroup_response_body = ListMailgroupResponseBody()

    def has_more(self, has_more: bool) -> "ListMailgroupResponseBodyBuilder":
        self._list_mailgroup_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListMailgroupResponseBodyBuilder":
        self._list_mailgroup_response_body.page_token = page_token
        return self

    def items(self, items: List[Mailgroup]) -> "ListMailgroupResponseBodyBuilder":
        self._list_mailgroup_response_body.items = items
        return self

    def build(self) -> "ListMailgroupResponseBody":
        return self._list_mailgroup_response_body
