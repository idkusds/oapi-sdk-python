# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_custom_attr_response_body import ListCustomAttrResponseBody


class ListCustomAttrResponse(BaseResponse):
    _types = {
        "data": ListCustomAttrResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListCustomAttrResponseBody] = None
        init(self, d, self._types)
