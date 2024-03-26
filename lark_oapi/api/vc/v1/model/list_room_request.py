# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListRoomRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.room_level_id: Optional[str] = None
        self.user_id_type: Optional[str] = None

    @staticmethod
    def builder() -> "ListRoomRequestBuilder":
        return ListRoomRequestBuilder()


class ListRoomRequestBuilder(object):

    def __init__(self) -> None:
        list_room_request = ListRoomRequest()
        list_room_request.http_method = HttpMethod.GET
        list_room_request.uri = "/open-apis/vc/v1/rooms"
        list_room_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._list_room_request: ListRoomRequest = list_room_request

    def page_size(self, page_size: int) -> "ListRoomRequestBuilder":
        self._list_room_request.page_size = page_size
        self._list_room_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListRoomRequestBuilder":
        self._list_room_request.page_token = page_token
        self._list_room_request.add_query("page_token", page_token)
        return self

    def room_level_id(self, room_level_id: str) -> "ListRoomRequestBuilder":
        self._list_room_request.room_level_id = room_level_id
        self._list_room_request.add_query("room_level_id", room_level_id)
        return self

    def user_id_type(self, user_id_type: str) -> "ListRoomRequestBuilder":
        self._list_room_request.user_id_type = user_id_type
        self._list_room_request.add_query("user_id_type", user_id_type)
        return self

    def build(self) -> ListRoomRequest:
        return self._list_room_request
