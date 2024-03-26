# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .room_level import RoomLevel


class CreateRoomLevelRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[RoomLevel] = None

    @staticmethod
    def builder() -> "CreateRoomLevelRequestBuilder":
        return CreateRoomLevelRequestBuilder()


class CreateRoomLevelRequestBuilder(object):

    def __init__(self) -> None:
        create_room_level_request = CreateRoomLevelRequest()
        create_room_level_request.http_method = HttpMethod.POST
        create_room_level_request.uri = "/open-apis/vc/v1/room_levels"
        create_room_level_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._create_room_level_request: CreateRoomLevelRequest = create_room_level_request

    def request_body(self, request_body: RoomLevel) -> "CreateRoomLevelRequestBuilder":
        self._create_room_level_request.request_body = request_body
        self._create_room_level_request.body = request_body
        return self

    def build(self) -> CreateRoomLevelRequest:
        return self._create_room_level_request
