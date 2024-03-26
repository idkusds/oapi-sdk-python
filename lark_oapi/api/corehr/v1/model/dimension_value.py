# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DimensionValue(object):
    _types = {
        "api_name": str,
        "value_list": List[str],
    }

    def __init__(self, d=None):
        self.api_name: Optional[str] = None
        self.value_list: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DimensionValueBuilder":
        return DimensionValueBuilder()


class DimensionValueBuilder(object):
    def __init__(self) -> None:
        self._dimension_value = DimensionValue()

    def api_name(self, api_name: str) -> "DimensionValueBuilder":
        self._dimension_value.api_name = api_name
        return self

    def value_list(self, value_list: List[str]) -> "DimensionValueBuilder":
        self._dimension_value.value_list = value_list
        return self

    def build(self) -> "DimensionValue":
        return self._dimension_value
