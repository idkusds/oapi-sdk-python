# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .schema_property import SchemaProperty
from .schema_display import SchemaDisplay


class Schema(object):
    _types = {
        "properties": List[SchemaProperty],
        "display": SchemaDisplay,
        "schema_id": str,
    }

    def __init__(self, d=None):
        self.properties: Optional[List[SchemaProperty]] = None
        self.display: Optional[SchemaDisplay] = None
        self.schema_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SchemaBuilder":
        return SchemaBuilder()


class SchemaBuilder(object):
    def __init__(self) -> None:
        self._schema = Schema()

    def properties(self, properties: List[SchemaProperty]) -> "SchemaBuilder":
        self._schema.properties = properties
        return self

    def display(self, display: SchemaDisplay) -> "SchemaBuilder":
        self._schema.display = display
        return self

    def schema_id(self, schema_id: str) -> "SchemaBuilder":
        self._schema.schema_id = schema_id
        return self

    def build(self) -> "Schema":
        return self._schema
