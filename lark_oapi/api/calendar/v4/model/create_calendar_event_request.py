# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .calendar_event import CalendarEvent


class CreateCalendarEventRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.idempotency_key: Optional[str] = None
        self.user_id_type: Optional[str] = None
        self.calendar_id: Optional[str] = None
        self.request_body: Optional[CalendarEvent] = None

    @staticmethod
    def builder() -> "CreateCalendarEventRequestBuilder":
        return CreateCalendarEventRequestBuilder()


class CreateCalendarEventRequestBuilder(object):

    def __init__(self) -> None:
        create_calendar_event_request = CreateCalendarEventRequest()
        create_calendar_event_request.http_method = HttpMethod.POST
        create_calendar_event_request.uri = "/open-apis/calendar/v4/calendars/:calendar_id/events"
        create_calendar_event_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._create_calendar_event_request: CreateCalendarEventRequest = create_calendar_event_request

    def idempotency_key(self, idempotency_key: str) -> "CreateCalendarEventRequestBuilder":
        self._create_calendar_event_request.idempotency_key = idempotency_key
        self._create_calendar_event_request.add_query("idempotency_key", idempotency_key)
        return self

    def user_id_type(self, user_id_type: str) -> "CreateCalendarEventRequestBuilder":
        self._create_calendar_event_request.user_id_type = user_id_type
        self._create_calendar_event_request.add_query("user_id_type", user_id_type)
        return self

    def calendar_id(self, calendar_id: str) -> "CreateCalendarEventRequestBuilder":
        self._create_calendar_event_request.calendar_id = calendar_id
        self._create_calendar_event_request.paths["calendar_id"] = str(calendar_id)
        return self

    def request_body(self, request_body: CalendarEvent) -> "CreateCalendarEventRequestBuilder":
        self._create_calendar_event_request.request_body = request_body
        self._create_calendar_event_request.body = request_body
        return self

    def build(self) -> CreateCalendarEventRequest:
        return self._create_calendar_event_request
