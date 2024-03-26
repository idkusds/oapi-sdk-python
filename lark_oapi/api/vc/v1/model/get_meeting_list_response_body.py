# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .meeting_info import MeetingInfo


class GetMeetingListResponseBody(object):
    _types = {
        "meeting_list": List[MeetingInfo],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.meeting_list: Optional[List[MeetingInfo]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetMeetingListResponseBodyBuilder":
        return GetMeetingListResponseBodyBuilder()


class GetMeetingListResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_meeting_list_response_body = GetMeetingListResponseBody()

    def meeting_list(self, meeting_list: List[MeetingInfo]) -> "GetMeetingListResponseBodyBuilder":
        self._get_meeting_list_response_body.meeting_list = meeting_list
        return self

    def page_token(self, page_token: str) -> "GetMeetingListResponseBodyBuilder":
        self._get_meeting_list_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "GetMeetingListResponseBodyBuilder":
        self._get_meeting_list_response_body.has_more = has_more
        return self

    def build(self) -> "GetMeetingListResponseBody":
        return self._get_meeting_list_response_body
