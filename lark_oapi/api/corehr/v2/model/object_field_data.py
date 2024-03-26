# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ObjectFieldData(object):
    _types = {
        "field_name": str,
        "value": str,
    }

    def __init__(self, d=None):
        self.field_name: Optional[str] = None
        self.value: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ObjectFieldDataBuilder":
        return ObjectFieldDataBuilder()


class ObjectFieldDataBuilder(object):
    def __init__(self) -> None:
        self._object_field_data = ObjectFieldData()

    def field_name(self, field_name: str) -> "ObjectFieldDataBuilder":
        self._object_field_data.field_name = field_name
        return self

    def value(self, value: str) -> "ObjectFieldDataBuilder":
        self._object_field_data.value = value
        return self

    def build(self) -> "ObjectFieldData":
        return self._object_field_data
