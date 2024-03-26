# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_task_response_body import CreateTaskResponseBody


class CreateTaskResponse(BaseResponse):
    _types = {
        "data": CreateTaskResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateTaskResponseBody] = None
        init(self, d, self._types)
