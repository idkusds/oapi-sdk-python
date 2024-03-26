# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class SchemaDisplayFieldMapping(object):
    _types = {
        "display_field": str,
        "data_field": str,
    }

    def __init__(self, d=None):
        self.display_field: Optional[str] = None
        self.data_field: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SchemaDisplayFieldMappingBuilder":
        return SchemaDisplayFieldMappingBuilder()


class SchemaDisplayFieldMappingBuilder(object):
    def __init__(self) -> None:
        self._schema_display_field_mapping = SchemaDisplayFieldMapping()

    def display_field(self, display_field: str) -> "SchemaDisplayFieldMappingBuilder":
        self._schema_display_field_mapping.display_field = display_field
        return self

    def data_field(self, data_field: str) -> "SchemaDisplayFieldMappingBuilder":
        self._schema_display_field_mapping.data_field = data_field
        return self

    def build(self) -> "SchemaDisplayFieldMapping":
        return self._schema_display_field_mapping
