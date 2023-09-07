# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_talent_response_body import GetTalentResponseBody


class GetTalentResponse(BaseResponse):
    _types = {
        "data": GetTalentResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetTalentResponseBody] = None
        init(self, d, self._types)
