# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .list_chat import ListChat


class ListChatResponseBody(object):
    _types = {
        "items": List[ListChat],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.items: Optional[List[ListChat]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListChatResponseBodyBuilder":
        return ListChatResponseBodyBuilder()


class ListChatResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_chat_response_body = ListChatResponseBody()

    def items(self, items: List[ListChat]) -> "ListChatResponseBodyBuilder":
        self._list_chat_response_body.items = items
        return self

    def page_token(self, page_token: str) -> "ListChatResponseBodyBuilder":
        self._list_chat_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "ListChatResponseBodyBuilder":
        self._list_chat_response_body.has_more = has_more
        return self

    def build(self) -> "ListChatResponseBody":
        return self._list_chat_response_body
