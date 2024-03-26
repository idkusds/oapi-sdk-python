# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_document_response_body import GetDocumentResponseBody


class GetDocumentResponse(BaseResponse):
    _types = {
        "data": GetDocumentResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetDocumentResponseBody] = None
        init(self, d, self._types)
