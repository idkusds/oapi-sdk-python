# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_user_info_response_body import GetUserInfoResponseBody


class GetUserInfoResponse(BaseResponse):
    _types = {
        "data": GetUserInfoResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetUserInfoResponseBody] = None
        init(self, d, self._types)
