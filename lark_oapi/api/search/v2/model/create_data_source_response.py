# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_data_source_response_body import CreateDataSourceResponseBody


class CreateDataSourceResponse(BaseResponse):
    _types = {
        "data": CreateDataSourceResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateDataSourceResponseBody] = None
        init(self, d, self._types)
