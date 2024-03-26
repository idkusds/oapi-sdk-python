# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .upload_prepare_media_response_body import UploadPrepareMediaResponseBody


class UploadPrepareMediaResponse(BaseResponse):
    _types = {
        "data": UploadPrepareMediaResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[UploadPrepareMediaResponseBody] = None
        init(self, d, self._types)
