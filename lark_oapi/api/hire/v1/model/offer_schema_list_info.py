# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .offer_schema_child import OfferSchemaChild


class OfferSchemaListInfo(object):
    _types = {
        "schema_list": List[OfferSchemaChild],
    }

    def __init__(self, d=None):
        self.schema_list: Optional[List[OfferSchemaChild]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OfferSchemaListInfoBuilder":
        return OfferSchemaListInfoBuilder()


class OfferSchemaListInfoBuilder(object):
    def __init__(self) -> None:
        self._offer_schema_list_info = OfferSchemaListInfo()

    def schema_list(self, schema_list: List[OfferSchemaChild]) -> "OfferSchemaListInfoBuilder":
        self._offer_schema_list_info.schema_list = schema_list
        return self

    def build(self) -> "OfferSchemaListInfo":
        return self._offer_schema_list_info
