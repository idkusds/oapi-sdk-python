# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .reserve_meeting_setting import ReserveMeetingSetting


class Reserve(object):
    _types = {
        "id": int,
        "meeting_no": str,
        "url": str,
        "app_link": str,
        "live_link": str,
        "end_time": int,
        "expire_status": int,
        "reserve_user_id": str,
        "meeting_settings": ReserveMeetingSetting,
    }

    def __init__(self, d=None):
        self.id: Optional[int] = None
        self.meeting_no: Optional[str] = None
        self.url: Optional[str] = None
        self.app_link: Optional[str] = None
        self.live_link: Optional[str] = None
        self.end_time: Optional[int] = None
        self.expire_status: Optional[int] = None
        self.reserve_user_id: Optional[str] = None
        self.meeting_settings: Optional[ReserveMeetingSetting] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ReserveBuilder":
        return ReserveBuilder()


class ReserveBuilder(object):
    def __init__(self) -> None:
        self._reserve = Reserve()

    def id(self, id: int) -> "ReserveBuilder":
        self._reserve.id = id
        return self

    def meeting_no(self, meeting_no: str) -> "ReserveBuilder":
        self._reserve.meeting_no = meeting_no
        return self

    def url(self, url: str) -> "ReserveBuilder":
        self._reserve.url = url
        return self

    def app_link(self, app_link: str) -> "ReserveBuilder":
        self._reserve.app_link = app_link
        return self

    def live_link(self, live_link: str) -> "ReserveBuilder":
        self._reserve.live_link = live_link
        return self

    def end_time(self, end_time: int) -> "ReserveBuilder":
        self._reserve.end_time = end_time
        return self

    def expire_status(self, expire_status: int) -> "ReserveBuilder":
        self._reserve.expire_status = expire_status
        return self

    def reserve_user_id(self, reserve_user_id: str) -> "ReserveBuilder":
        self._reserve.reserve_user_id = reserve_user_id
        return self

    def meeting_settings(self, meeting_settings: ReserveMeetingSetting) -> "ReserveBuilder":
        self._reserve.meeting_settings = meeting_settings
        return self

    def build(self) -> "Reserve":
        return self._reserve
