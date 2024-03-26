# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_file_comment_response_body import CreateFileCommentResponseBody


class CreateFileCommentResponse(BaseResponse):
    _types = {
        "data": CreateFileCommentResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateFileCommentResponseBody] = None
        init(self, d, self._types)
