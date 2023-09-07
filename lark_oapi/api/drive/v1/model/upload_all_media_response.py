# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .upload_all_media_response_body import UploadAllMediaResponseBody


class UploadAllMediaResponse(BaseResponse):
    _types = {
        "data": UploadAllMediaResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[UploadAllMediaResponseBody] = None
        init(self, d, self._types)
