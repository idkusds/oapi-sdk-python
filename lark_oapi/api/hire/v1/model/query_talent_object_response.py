# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .query_talent_object_response_body import QueryTalentObjectResponseBody


class QueryTalentObjectResponse(BaseResponse):
    _types = {
        "data": QueryTalentObjectResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[QueryTalentObjectResponseBody] = None
        init(self, d, self._types)
