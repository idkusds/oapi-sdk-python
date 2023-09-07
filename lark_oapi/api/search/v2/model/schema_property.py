# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .schema_filter_options import SchemaFilterOptions
from .schema_search_options import SchemaSearchOptions
from .schema_sort_options import SchemaSortOptions
from .schema_type_definitions import SchemaTypeDefinitions


class SchemaProperty(object):
    _types = {
        "name": str,
        "type": str,
        "is_searchable": bool,
        "is_sortable": bool,
        "is_returnable": bool,
        "sort_options": SchemaSortOptions,
        "type_definitions": SchemaTypeDefinitions,
        "search_options": SchemaSearchOptions,
        "is_filterable": bool,
        "filter_options": SchemaFilterOptions,
    }

    def __init__(self, d=None):
        self.name: Optional[str] = None
        self.type: Optional[str] = None
        self.is_searchable: Optional[bool] = None
        self.is_sortable: Optional[bool] = None
        self.is_returnable: Optional[bool] = None
        self.sort_options: Optional[SchemaSortOptions] = None
        self.type_definitions: Optional[SchemaTypeDefinitions] = None
        self.search_options: Optional[SchemaSearchOptions] = None
        self.is_filterable: Optional[bool] = None
        self.filter_options: Optional[SchemaFilterOptions] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SchemaPropertyBuilder":
        return SchemaPropertyBuilder()


class SchemaPropertyBuilder(object):
    def __init__(self) -> None:
        self._schema_property = SchemaProperty()

    def name(self, name: str) -> "SchemaPropertyBuilder":
        self._schema_property.name = name
        return self

    def type(self, type: str) -> "SchemaPropertyBuilder":
        self._schema_property.type = type
        return self

    def is_searchable(self, is_searchable: bool) -> "SchemaPropertyBuilder":
        self._schema_property.is_searchable = is_searchable
        return self

    def is_sortable(self, is_sortable: bool) -> "SchemaPropertyBuilder":
        self._schema_property.is_sortable = is_sortable
        return self

    def is_returnable(self, is_returnable: bool) -> "SchemaPropertyBuilder":
        self._schema_property.is_returnable = is_returnable
        return self

    def sort_options(self, sort_options: SchemaSortOptions) -> "SchemaPropertyBuilder":
        self._schema_property.sort_options = sort_options
        return self

    def type_definitions(self, type_definitions: SchemaTypeDefinitions) -> "SchemaPropertyBuilder":
        self._schema_property.type_definitions = type_definitions
        return self

    def search_options(self, search_options: SchemaSearchOptions) -> "SchemaPropertyBuilder":
        self._schema_property.search_options = search_options
        return self

    def is_filterable(self, is_filterable: bool) -> "SchemaPropertyBuilder":
        self._schema_property.is_filterable = is_filterable
        return self

    def filter_options(self, filter_options: SchemaFilterOptions) -> "SchemaPropertyBuilder":
        self._schema_property.filter_options = filter_options
        return self

    def build(self) -> "SchemaProperty":
        return self._schema_property
