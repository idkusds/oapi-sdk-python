# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .room_level import RoomLevel


class GetRoomLevelResponseBody(object):
    _types = {
        "room_level": RoomLevel,
    }

    def __init__(self, d=None):
        self.room_level: Optional[RoomLevel] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetRoomLevelResponseBodyBuilder":
        return GetRoomLevelResponseBodyBuilder()


class GetRoomLevelResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_room_level_response_body = GetRoomLevelResponseBody()

    def room_level(self, room_level: RoomLevel) -> "GetRoomLevelResponseBodyBuilder":
        self._get_room_level_response_body.room_level = room_level
        return self

    def build(self) -> "GetRoomLevelResponseBody":
        return self._get_room_level_response_body
