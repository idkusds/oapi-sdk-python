# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_leave_employ_expire_record_response_body import GetLeaveEmployExpireRecordResponseBody


class GetLeaveEmployExpireRecordResponse(BaseResponse):
    _types = {
        "data": GetLeaveEmployExpireRecordResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetLeaveEmployExpireRecordResponseBody] = None
        init(self, d, self._types)
