# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_by_department_bp_response_body import GetByDepartmentBpResponseBody


class GetByDepartmentBpResponse(BaseResponse):
    _types = {
        "data": GetByDepartmentBpResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetByDepartmentBpResponseBody] = None
        init(self, d, self._types)
