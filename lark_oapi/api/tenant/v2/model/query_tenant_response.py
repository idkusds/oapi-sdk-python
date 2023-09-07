# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .query_tenant_response_body import QueryTenantResponseBody


class QueryTenantResponse(BaseResponse):
    _types = {
        "data": QueryTenantResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[QueryTenantResponseBody] = None
        init(self, d, self._types)
