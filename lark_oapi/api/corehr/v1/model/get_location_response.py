# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_location_response_body import GetLocationResponseBody


class GetLocationResponse(BaseResponse):
    _types = {
        "data": GetLocationResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetLocationResponseBody] = None
        init(self, d, self._types)
