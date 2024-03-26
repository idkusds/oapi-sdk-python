# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class MeetingMinute(object):
    _types = {
        "doc_token": str,
        "doc_url": str,
    }

    def __init__(self, d=None):
        self.doc_token: Optional[str] = None
        self.doc_url: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MeetingMinuteBuilder":
        return MeetingMinuteBuilder()


class MeetingMinuteBuilder(object):
    def __init__(self) -> None:
        self._meeting_minute = MeetingMinute()

    def doc_token(self, doc_token: str) -> "MeetingMinuteBuilder":
        self._meeting_minute.doc_token = doc_token
        return self

    def doc_url(self, doc_url: str) -> "MeetingMinuteBuilder":
        self._meeting_minute.doc_url = doc_url
        return self

    def build(self) -> "MeetingMinute":
        return self._meeting_minute
