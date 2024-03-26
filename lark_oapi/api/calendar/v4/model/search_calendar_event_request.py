# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .search_calendar_event_request_body import SearchCalendarEventRequestBody


class SearchCalendarEventRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None
        self.calendar_id: Optional[str] = None
        self.request_body: Optional[SearchCalendarEventRequestBody] = None

    @staticmethod
    def builder() -> "SearchCalendarEventRequestBuilder":
        return SearchCalendarEventRequestBuilder()


class SearchCalendarEventRequestBuilder(object):

    def __init__(self) -> None:
        search_calendar_event_request = SearchCalendarEventRequest()
        search_calendar_event_request.http_method = HttpMethod.POST
        search_calendar_event_request.uri = "/open-apis/calendar/v4/calendars/:calendar_id/events/search"
        search_calendar_event_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._search_calendar_event_request: SearchCalendarEventRequest = search_calendar_event_request

    def user_id_type(self, user_id_type: str) -> "SearchCalendarEventRequestBuilder":
        self._search_calendar_event_request.user_id_type = user_id_type
        self._search_calendar_event_request.add_query("user_id_type", user_id_type)
        return self

    def page_token(self, page_token: str) -> "SearchCalendarEventRequestBuilder":
        self._search_calendar_event_request.page_token = page_token
        self._search_calendar_event_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: int) -> "SearchCalendarEventRequestBuilder":
        self._search_calendar_event_request.page_size = page_size
        self._search_calendar_event_request.add_query("page_size", page_size)
        return self

    def calendar_id(self, calendar_id: str) -> "SearchCalendarEventRequestBuilder":
        self._search_calendar_event_request.calendar_id = calendar_id
        self._search_calendar_event_request.paths["calendar_id"] = str(calendar_id)
        return self

    def request_body(self, request_body: SearchCalendarEventRequestBody) -> "SearchCalendarEventRequestBuilder":
        self._search_calendar_event_request.request_body = request_body
        self._search_calendar_event_request.body = request_body
        return self

    def build(self) -> SearchCalendarEventRequest:
        return self._search_calendar_event_request
