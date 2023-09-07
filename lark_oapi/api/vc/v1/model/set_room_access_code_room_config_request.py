# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .set_room_access_code_room_config_request_body import SetRoomAccessCodeRoomConfigRequestBody


class SetRoomAccessCodeRoomConfigRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[SetRoomAccessCodeRoomConfigRequestBody] = None

    @staticmethod
    def builder() -> "SetRoomAccessCodeRoomConfigRequestBuilder":
        return SetRoomAccessCodeRoomConfigRequestBuilder()


class SetRoomAccessCodeRoomConfigRequestBuilder(object):

    def __init__(self) -> None:
        set_room_access_code_room_config_request = SetRoomAccessCodeRoomConfigRequest()
        set_room_access_code_room_config_request.http_method = HttpMethod.POST
        set_room_access_code_room_config_request.uri = "/open-apis/vc/v1/room_configs/set_room_access_code"
        set_room_access_code_room_config_request.token_types = {AccessTokenType.TENANT}
        self._set_room_access_code_room_config_request: SetRoomAccessCodeRoomConfigRequest = set_room_access_code_room_config_request

    def request_body(self,
                     request_body: SetRoomAccessCodeRoomConfigRequestBody) -> "SetRoomAccessCodeRoomConfigRequestBuilder":
        self._set_room_access_code_room_config_request.request_body = request_body
        self._set_room_access_code_room_config_request.body = request_body
        return self

    def build(self) -> SetRoomAccessCodeRoomConfigRequest:
        return self._set_room_access_code_room_config_request
