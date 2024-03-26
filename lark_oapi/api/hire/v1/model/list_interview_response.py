# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_interview_response_body import ListInterviewResponseBody


class ListInterviewResponse(BaseResponse):
    _types = {
        "data": ListInterviewResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListInterviewResponseBody] = None
        init(self, d, self._types)
