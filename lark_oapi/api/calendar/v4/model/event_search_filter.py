# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .time_info import TimeInfo


class EventSearchFilter(object):
    _types = {
        "start_time": TimeInfo,
        "end_time": TimeInfo,
        "user_ids": List[str],
        "room_ids": List[str],
        "chat_ids": List[str],
    }

    def __init__(self, d=None):
        self.start_time: Optional[TimeInfo] = None
        self.end_time: Optional[TimeInfo] = None
        self.user_ids: Optional[List[str]] = None
        self.room_ids: Optional[List[str]] = None
        self.chat_ids: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EventSearchFilterBuilder":
        return EventSearchFilterBuilder()


class EventSearchFilterBuilder(object):
    def __init__(self) -> None:
        self._event_search_filter = EventSearchFilter()

    def start_time(self, start_time: TimeInfo) -> "EventSearchFilterBuilder":
        self._event_search_filter.start_time = start_time
        return self

    def end_time(self, end_time: TimeInfo) -> "EventSearchFilterBuilder":
        self._event_search_filter.end_time = end_time
        return self

    def user_ids(self, user_ids: List[str]) -> "EventSearchFilterBuilder":
        self._event_search_filter.user_ids = user_ids
        return self

    def room_ids(self, room_ids: List[str]) -> "EventSearchFilterBuilder":
        self._event_search_filter.room_ids = room_ids
        return self

    def chat_ids(self, chat_ids: List[str]) -> "EventSearchFilterBuilder":
        self._event_search_filter.chat_ids = chat_ids
        return self

    def build(self) -> "EventSearchFilter":
        return self._event_search_filter
