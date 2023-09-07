# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_entity_response_body import GetEntityResponseBody


class GetEntityResponse(BaseResponse):
    _types = {
        "data": GetEntityResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetEntityResponseBody] = None
        init(self, d, self._types)
