# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_data_source_response_body import ListDataSourceResponseBody


class ListDataSourceResponse(BaseResponse):
    _types = {
        "data": ListDataSourceResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListDataSourceResponseBody] = None
        init(self, d, self._types)
