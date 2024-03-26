# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .update_department_response_body import UpdateDepartmentResponseBody


class UpdateDepartmentResponse(BaseResponse):
    _types = {
        "data": UpdateDepartmentResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[UpdateDepartmentResponseBody] = None
        init(self, d, self._types)
