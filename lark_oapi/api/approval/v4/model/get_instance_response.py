# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_instance_response_body import GetInstanceResponseBody


class GetInstanceResponse(BaseResponse):
    _types = {
        "data": GetInstanceResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetInstanceResponseBody] = None
        init(self, d, self._types)
