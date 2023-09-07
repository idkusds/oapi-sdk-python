# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .set_checkboard_access_code_room_config_response_body import SetCheckboardAccessCodeRoomConfigResponseBody


class SetCheckboardAccessCodeRoomConfigResponse(BaseResponse):
    _types = {
        "data": SetCheckboardAccessCodeRoomConfigResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[SetCheckboardAccessCodeRoomConfigResponseBody] = None
        init(self, d, self._types)
