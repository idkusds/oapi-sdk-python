# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .interview_extend import InterviewExtend


class ListInterviewResponseBody(object):
    _types = {
        "items": List[InterviewExtend],
        "has_more": bool,
        "page_token": str,
    }

    def __init__(self, d=None):
        self.items: Optional[List[InterviewExtend]] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListInterviewResponseBodyBuilder":
        return ListInterviewResponseBodyBuilder()


class ListInterviewResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_interview_response_body = ListInterviewResponseBody()

    def items(self, items: List[InterviewExtend]) -> "ListInterviewResponseBodyBuilder":
        self._list_interview_response_body.items = items
        return self

    def has_more(self, has_more: bool) -> "ListInterviewResponseBodyBuilder":
        self._list_interview_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListInterviewResponseBodyBuilder":
        self._list_interview_response_body.page_token = page_token
        return self

    def build(self) -> "ListInterviewResponseBody":
        return self._list_interview_response_body
