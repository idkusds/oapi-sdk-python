# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .remove_instance_comment_response_body import RemoveInstanceCommentResponseBody


class RemoveInstanceCommentResponse(BaseResponse):
    _types = {
        "data": RemoveInstanceCommentResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[RemoveInstanceCommentResponseBody] = None
        init(self, d, self._types)
