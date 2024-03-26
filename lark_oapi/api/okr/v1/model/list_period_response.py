# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_period_response_body import ListPeriodResponseBody


class ListPeriodResponse(BaseResponse):
    _types = {
        "data": ListPeriodResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListPeriodResponseBody] = None
        init(self, d, self._types)
