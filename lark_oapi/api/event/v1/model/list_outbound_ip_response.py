# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_outbound_ip_response_body import ListOutboundIpResponseBody


class ListOutboundIpResponse(BaseResponse):
    _types = {
        "data": ListOutboundIpResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListOutboundIpResponseBody] = None
        init(self, d, self._types)
