# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .search_group_response_body import SearchGroupResponseBody


class SearchGroupResponse(BaseResponse):
    _types = {
        "data": SearchGroupResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[SearchGroupResponseBody] = None
        init(self, d, self._types)
