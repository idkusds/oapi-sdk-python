# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class ProtectedColumns(object):
    _types = {
        "sheet_id": str,
        "start_index": int,
        "end_index": int,
    }

    def __init__(self, d=None):
        self.sheet_id: Optional[str] = None
        self.start_index: Optional[int] = None
        self.end_index: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ProtectedColumnsBuilder":
        return ProtectedColumnsBuilder()


class ProtectedColumnsBuilder(object):
    def __init__(self) -> None:
        self._protected_columns = ProtectedColumns()

    def sheet_id(self, sheet_id: str) -> "ProtectedColumnsBuilder":
        self._protected_columns.sheet_id = sheet_id
        return self

    def start_index(self, start_index: int) -> "ProtectedColumnsBuilder":
        self._protected_columns.start_index = start_index
        return self

    def end_index(self, end_index: int) -> "ProtectedColumnsBuilder":
        self._protected_columns.end_index = end_index
        return self

    def build(self) -> "ProtectedColumns":
        return self._protected_columns
