# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class BatchCreateAppTableResponseBody(object):
    _types = {
        "table_ids": List[str],
    }

    def __init__(self, d=None):
        self.table_ids: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchCreateAppTableResponseBodyBuilder":
        return BatchCreateAppTableResponseBodyBuilder()


class BatchCreateAppTableResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._batch_create_app_table_response_body = BatchCreateAppTableResponseBody()

    def table_ids(self, table_ids: List[str]) -> "BatchCreateAppTableResponseBodyBuilder":
        self._batch_create_app_table_response_body.table_ids = table_ids
        return self

    def build(self) -> "BatchCreateAppTableResponseBody":
        return self._batch_create_app_table_response_body
