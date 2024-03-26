# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .upload_attachment_response_body import UploadAttachmentResponseBody


class UploadAttachmentResponse(BaseResponse):
    _types = {
        "data": UploadAttachmentResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[UploadAttachmentResponseBody] = None
        init(self, d, self._types)
