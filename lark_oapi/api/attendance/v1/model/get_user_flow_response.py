# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_user_flow_response_body import GetUserFlowResponseBody


class GetUserFlowResponse(BaseResponse):
    _types = {
        "data": GetUserFlowResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetUserFlowResponseBody] = None
        init(self, d, self._types)
