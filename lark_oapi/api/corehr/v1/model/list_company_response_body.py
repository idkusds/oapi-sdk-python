# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .company import Company


class ListCompanyResponseBody(object):
    _types = {
        "items": List[Company],
        "has_more": bool,
        "page_token": str,
    }

    def __init__(self, d=None):
        self.items: Optional[List[Company]] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListCompanyResponseBodyBuilder":
        return ListCompanyResponseBodyBuilder()


class ListCompanyResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_company_response_body = ListCompanyResponseBody()

    def items(self, items: List[Company]) -> "ListCompanyResponseBodyBuilder":
        self._list_company_response_body.items = items
        return self

    def has_more(self, has_more: bool) -> "ListCompanyResponseBodyBuilder":
        self._list_company_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListCompanyResponseBodyBuilder":
        self._list_company_response_body.page_token = page_token
        return self

    def build(self) -> "ListCompanyResponseBody":
        return self._list_company_response_body
