# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .file import File


class ListFileResponseBody(object):
    _types = {
        "files": List[File],
        "next_page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.files: Optional[List[File]] = None
        self.next_page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListFileResponseBodyBuilder":
        return ListFileResponseBodyBuilder()


class ListFileResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_file_response_body = ListFileResponseBody()

    def files(self, files: List[File]) -> "ListFileResponseBodyBuilder":
        self._list_file_response_body.files = files
        return self

    def next_page_token(self, next_page_token: str) -> "ListFileResponseBodyBuilder":
        self._list_file_response_body.next_page_token = next_page_token
        return self

    def has_more(self, has_more: bool) -> "ListFileResponseBodyBuilder":
        self._list_file_response_body.has_more = has_more
        return self

    def build(self) -> "ListFileResponseBody":
        return self._list_file_response_body
