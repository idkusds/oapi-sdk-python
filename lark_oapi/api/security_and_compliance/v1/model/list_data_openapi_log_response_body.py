# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .openapi_log import OpenapiLog


class ListDataOpenapiLogResponseBody(object):
    _types = {
        "items": List[OpenapiLog],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.items: Optional[List[OpenapiLog]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListDataOpenapiLogResponseBodyBuilder":
        return ListDataOpenapiLogResponseBodyBuilder()


class ListDataOpenapiLogResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_data_openapi_log_response_body = ListDataOpenapiLogResponseBody()

    def items(self, items: List[OpenapiLog]) -> "ListDataOpenapiLogResponseBodyBuilder":
        self._list_data_openapi_log_response_body.items = items
        return self

    def page_token(self, page_token: str) -> "ListDataOpenapiLogResponseBodyBuilder":
        self._list_data_openapi_log_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "ListDataOpenapiLogResponseBodyBuilder":
        self._list_data_openapi_log_response_body.has_more = has_more
        return self

    def build(self) -> "ListDataOpenapiLogResponseBody":
        return self._list_data_openapi_log_response_body
