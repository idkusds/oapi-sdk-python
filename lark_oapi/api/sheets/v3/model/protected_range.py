# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .protected_rows import ProtectedRows
from .protected_columns import ProtectedColumns
from .protected_sheet import ProtectedSheet
from .protected_range_editors import ProtectedRangeEditors


class ProtectedRange(object):
    _types = {
        "protected_id": str,
        "description": str,
        "protected_dimension": str,
        "protected_rows": ProtectedRows,
        "protected_columns": ProtectedColumns,
        "protected_sheet": ProtectedSheet,
        "editors": ProtectedRangeEditors,
    }

    def __init__(self, d=None):
        self.protected_id: Optional[str] = None
        self.description: Optional[str] = None
        self.protected_dimension: Optional[str] = None
        self.protected_rows: Optional[ProtectedRows] = None
        self.protected_columns: Optional[ProtectedColumns] = None
        self.protected_sheet: Optional[ProtectedSheet] = None
        self.editors: Optional[ProtectedRangeEditors] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ProtectedRangeBuilder":
        return ProtectedRangeBuilder()


class ProtectedRangeBuilder(object):
    def __init__(self) -> None:
        self._protected_range = ProtectedRange()

    def protected_id(self, protected_id: str) -> "ProtectedRangeBuilder":
        self._protected_range.protected_id = protected_id
        return self

    def description(self, description: str) -> "ProtectedRangeBuilder":
        self._protected_range.description = description
        return self

    def protected_dimension(self, protected_dimension: str) -> "ProtectedRangeBuilder":
        self._protected_range.protected_dimension = protected_dimension
        return self

    def protected_rows(self, protected_rows: ProtectedRows) -> "ProtectedRangeBuilder":
        self._protected_range.protected_rows = protected_rows
        return self

    def protected_columns(self, protected_columns: ProtectedColumns) -> "ProtectedRangeBuilder":
        self._protected_range.protected_columns = protected_columns
        return self

    def protected_sheet(self, protected_sheet: ProtectedSheet) -> "ProtectedRangeBuilder":
        self._protected_range.protected_sheet = protected_sheet
        return self

    def editors(self, editors: ProtectedRangeEditors) -> "ProtectedRangeBuilder":
        self._protected_range.editors = editors
        return self

    def build(self) -> "ProtectedRange":
        return self._protected_range
