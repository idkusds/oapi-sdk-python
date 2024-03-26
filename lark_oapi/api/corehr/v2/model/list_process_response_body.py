# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ListProcessResponseBody(object):
    _types = {
        "process_ids": List[str],
        "has_more": bool,
        "page_token": str,
    }

    def __init__(self, d=None):
        self.process_ids: Optional[List[str]] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListProcessResponseBodyBuilder":
        return ListProcessResponseBodyBuilder()


class ListProcessResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_process_response_body = ListProcessResponseBody()

    def process_ids(self, process_ids: List[str]) -> "ListProcessResponseBodyBuilder":
        self._list_process_response_body.process_ids = process_ids
        return self

    def has_more(self, has_more: bool) -> "ListProcessResponseBodyBuilder":
        self._list_process_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListProcessResponseBodyBuilder":
        self._list_process_response_body.page_token = page_token
        return self

    def build(self) -> "ListProcessResponseBody":
        return self._list_process_response_body
