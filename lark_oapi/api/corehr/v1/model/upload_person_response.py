# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .upload_person_response_body import UploadPersonResponseBody


class UploadPersonResponse(BaseResponse):
    _types = {
        "data": UploadPersonResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[UploadPersonResponseBody] = None
        init(self, d, self._types)
