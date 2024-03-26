# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .raw_content_document_response_body import RawContentDocumentResponseBody


class RawContentDocumentResponse(BaseResponse):
    _types = {
        "data": RawContentDocumentResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[RawContentDocumentResponseBody] = None
        init(self, d, self._types)
