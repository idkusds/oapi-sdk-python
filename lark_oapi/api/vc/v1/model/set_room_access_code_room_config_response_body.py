# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class SetRoomAccessCodeRoomConfigResponseBody(object):
    _types = {
        "access_code": str,
    }

    def __init__(self, d=None):
        self.access_code: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SetRoomAccessCodeRoomConfigResponseBodyBuilder":
        return SetRoomAccessCodeRoomConfigResponseBodyBuilder()


class SetRoomAccessCodeRoomConfigResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._set_room_access_code_room_config_response_body = SetRoomAccessCodeRoomConfigResponseBody()

    def access_code(self, access_code: str) -> "SetRoomAccessCodeRoomConfigResponseBodyBuilder":
        self._set_room_access_code_room_config_response_body.access_code = access_code
        return self

    def build(self) -> "SetRoomAccessCodeRoomConfigResponseBody":
        return self._set_room_access_code_room_config_response_body
