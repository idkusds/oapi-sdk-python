# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .patch_app_table_response_body import PatchAppTableResponseBody


class PatchAppTableResponse(BaseResponse):
    _types = {
        "data": PatchAppTableResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[PatchAppTableResponseBody] = None
        init(self, d, self._types)
