# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_app_table_record_response_body import CreateAppTableRecordResponseBody


class CreateAppTableRecordResponse(BaseResponse):
    _types = {
        "data": CreateAppTableRecordResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateAppTableRecordResponseBody] = None
        init(self, d, self._types)
