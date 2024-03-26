# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class BatchDeleteDocumentBlockChildrenRequestBody(object):
    _types = {
        "start_index": int,
        "end_index": int,
    }

    def __init__(self, d=None):
        self.start_index: Optional[int] = None
        self.end_index: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchDeleteDocumentBlockChildrenRequestBodyBuilder":
        return BatchDeleteDocumentBlockChildrenRequestBodyBuilder()


class BatchDeleteDocumentBlockChildrenRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._batch_delete_document_block_children_request_body = BatchDeleteDocumentBlockChildrenRequestBody()

    def start_index(self, start_index: int) -> "BatchDeleteDocumentBlockChildrenRequestBodyBuilder":
        self._batch_delete_document_block_children_request_body.start_index = start_index
        return self

    def end_index(self, end_index: int) -> "BatchDeleteDocumentBlockChildrenRequestBodyBuilder":
        self._batch_delete_document_block_children_request_body.end_index = end_index
        return self

    def build(self) -> "BatchDeleteDocumentBlockChildrenRequestBody":
        return self._batch_delete_document_block_children_request_body
