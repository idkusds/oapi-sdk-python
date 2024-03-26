# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .resume_source import ResumeSource


class ListResumeSourceResponseBody(object):
    _types = {
        "items": List[ResumeSource],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.items: Optional[List[ResumeSource]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListResumeSourceResponseBodyBuilder":
        return ListResumeSourceResponseBodyBuilder()


class ListResumeSourceResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_resume_source_response_body = ListResumeSourceResponseBody()

    def items(self, items: List[ResumeSource]) -> "ListResumeSourceResponseBodyBuilder":
        self._list_resume_source_response_body.items = items
        return self

    def page_token(self, page_token: str) -> "ListResumeSourceResponseBodyBuilder":
        self._list_resume_source_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "ListResumeSourceResponseBodyBuilder":
        self._list_resume_source_response_body.has_more = has_more
        return self

    def build(self) -> "ListResumeSourceResponseBody":
        return self._list_resume_source_response_body
