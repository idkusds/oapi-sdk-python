# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .reply_calendar_event_request_body import ReplyCalendarEventRequestBody


class ReplyCalendarEventRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.calendar_id: Optional[str] = None
        self.event_id: Optional[str] = None
        self.request_body: Optional[ReplyCalendarEventRequestBody] = None

    @staticmethod
    def builder() -> "ReplyCalendarEventRequestBuilder":
        return ReplyCalendarEventRequestBuilder()


class ReplyCalendarEventRequestBuilder(object):

    def __init__(self) -> None:
        reply_calendar_event_request = ReplyCalendarEventRequest()
        reply_calendar_event_request.http_method = HttpMethod.POST
        reply_calendar_event_request.uri = "/open-apis/calendar/v4/calendars/:calendar_id/events/:event_id/reply"
        reply_calendar_event_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._reply_calendar_event_request: ReplyCalendarEventRequest = reply_calendar_event_request

    def calendar_id(self, calendar_id: str) -> "ReplyCalendarEventRequestBuilder":
        self._reply_calendar_event_request.calendar_id = calendar_id
        self._reply_calendar_event_request.paths["calendar_id"] = str(calendar_id)
        return self

    def event_id(self, event_id: str) -> "ReplyCalendarEventRequestBuilder":
        self._reply_calendar_event_request.event_id = event_id
        self._reply_calendar_event_request.paths["event_id"] = str(event_id)
        return self

    def request_body(self, request_body: ReplyCalendarEventRequestBody) -> "ReplyCalendarEventRequestBuilder":
        self._reply_calendar_event_request.request_body = request_body
        self._reply_calendar_event_request.body = request_body
        return self

    def build(self) -> ReplyCalendarEventRequest:
        return self._reply_calendar_event_request
