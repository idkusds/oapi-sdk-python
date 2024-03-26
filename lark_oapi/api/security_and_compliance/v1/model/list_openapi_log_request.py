# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ListOpenapiLogRequest(object):
    _types = {
        "api_keys": List[str],
        "start_time": int,
        "end_time": int,
        "app_id": str,
        "page_size": int,
        "page_token": str,
    }

    def __init__(self, d=None):
        self.api_keys: Optional[List[str]] = None
        self.start_time: Optional[int] = None
        self.end_time: Optional[int] = None
        self.app_id: Optional[str] = None
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListOpenapiLogRequestBuilder":
        return ListOpenapiLogRequestBuilder()


class ListOpenapiLogRequestBuilder(object):
    def __init__(self) -> None:
        self._list_openapi_log_request = ListOpenapiLogRequest()

    def api_keys(self, api_keys: List[str]) -> "ListOpenapiLogRequestBuilder":
        self._list_openapi_log_request.api_keys = api_keys
        return self

    def start_time(self, start_time: int) -> "ListOpenapiLogRequestBuilder":
        self._list_openapi_log_request.start_time = start_time
        return self

    def end_time(self, end_time: int) -> "ListOpenapiLogRequestBuilder":
        self._list_openapi_log_request.end_time = end_time
        return self

    def app_id(self, app_id: str) -> "ListOpenapiLogRequestBuilder":
        self._list_openapi_log_request.app_id = app_id
        return self

    def page_size(self, page_size: int) -> "ListOpenapiLogRequestBuilder":
        self._list_openapi_log_request.page_size = page_size
        return self

    def page_token(self, page_token: str) -> "ListOpenapiLogRequestBuilder":
        self._list_openapi_log_request.page_token = page_token
        return self

    def build(self) -> "ListOpenapiLogRequest":
        return self._list_openapi_log_request
