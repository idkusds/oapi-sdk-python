# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_app_table_record_response_body import ListAppTableRecordResponseBody


class ListAppTableRecordResponse(BaseResponse):
    _types = {
        "data": ListAppTableRecordResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListAppTableRecordResponseBody] = None
        init(self, d, self._types)
