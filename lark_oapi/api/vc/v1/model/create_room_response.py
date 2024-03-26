# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_room_response_body import CreateRoomResponseBody


class CreateRoomResponse(BaseResponse):
    _types = {
        "data": CreateRoomResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateRoomResponseBody] = None
        init(self, d, self._types)
