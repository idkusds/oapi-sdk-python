# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .patch_task_response_body import PatchTaskResponseBody


class PatchTaskResponse(BaseResponse):
    _types = {
        "data": PatchTaskResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[PatchTaskResponseBody] = None
        init(self, d, self._types)
