# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_employee_type_response_body import ListEmployeeTypeResponseBody


class ListEmployeeTypeResponse(BaseResponse):
    _types = {
        "data": ListEmployeeTypeResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListEmployeeTypeResponseBody] = None
        init(self, d, self._types)
