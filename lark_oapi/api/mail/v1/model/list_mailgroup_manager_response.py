# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_mailgroup_manager_response_body import ListMailgroupManagerResponseBody


class ListMailgroupManagerResponse(BaseResponse):
    _types = {
        "data": ListMailgroupManagerResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListMailgroupManagerResponseBody] = None
        init(self, d, self._types)
