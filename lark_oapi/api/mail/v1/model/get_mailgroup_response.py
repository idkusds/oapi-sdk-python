# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_mailgroup_response_body import GetMailgroupResponseBody


class GetMailgroupResponse(BaseResponse):
    _types = {
        "data": GetMailgroupResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetMailgroupResponseBody] = None
        init(self, d, self._types)
