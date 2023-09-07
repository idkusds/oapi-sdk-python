# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .simplelist_group_member_response_body import SimplelistGroupMemberResponseBody


class SimplelistGroupMemberResponse(BaseResponse):
    _types = {
        "data": SimplelistGroupMemberResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[SimplelistGroupMemberResponseBody] = None
        init(self, d, self._types)
