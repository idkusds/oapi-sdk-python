# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class BatchDeleteAppTableRequestBody(object):
    _types = {
        "table_ids": List[str],
    }

    def __init__(self, d=None):
        self.table_ids: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchDeleteAppTableRequestBodyBuilder":
        return BatchDeleteAppTableRequestBodyBuilder()


class BatchDeleteAppTableRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._batch_delete_app_table_request_body = BatchDeleteAppTableRequestBody()

    def table_ids(self, table_ids: List[str]) -> "BatchDeleteAppTableRequestBodyBuilder":
        self._batch_delete_app_table_request_body.table_ids = table_ids
        return self

    def build(self) -> "BatchDeleteAppTableRequestBody":
        return self._batch_delete_app_table_request_body
