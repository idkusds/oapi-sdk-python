# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_offer_schema_response_body import GetOfferSchemaResponseBody


class GetOfferSchemaResponse(BaseResponse):
    _types = {
        "data": GetOfferSchemaResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetOfferSchemaResponseBody] = None
        init(self, d, self._types)
