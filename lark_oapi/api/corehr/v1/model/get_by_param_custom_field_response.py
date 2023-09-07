# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_by_param_custom_field_response_body import GetByParamCustomFieldResponseBody


class GetByParamCustomFieldResponse(BaseResponse):
    _types = {
        "data": GetByParamCustomFieldResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetByParamCustomFieldResponseBody] = None
        init(self, d, self._types)
