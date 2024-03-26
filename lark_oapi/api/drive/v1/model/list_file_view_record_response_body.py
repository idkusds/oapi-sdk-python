# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .file_view_record import FileViewRecord


class ListFileViewRecordResponseBody(object):
    _types = {
        "items": List[FileViewRecord],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.items: Optional[List[FileViewRecord]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListFileViewRecordResponseBodyBuilder":
        return ListFileViewRecordResponseBodyBuilder()


class ListFileViewRecordResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_file_view_record_response_body = ListFileViewRecordResponseBody()

    def items(self, items: List[FileViewRecord]) -> "ListFileViewRecordResponseBodyBuilder":
        self._list_file_view_record_response_body.items = items
        return self

    def page_token(self, page_token: str) -> "ListFileViewRecordResponseBodyBuilder":
        self._list_file_view_record_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "ListFileViewRecordResponseBodyBuilder":
        self._list_file_view_record_response_body.has_more = has_more
        return self

    def build(self) -> "ListFileViewRecordResponseBody":
        return self._list_file_view_record_response_body
