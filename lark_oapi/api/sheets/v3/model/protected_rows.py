# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ProtectedRows(object):
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
    def builder() -> "ProtectedRowsBuilder":
        return ProtectedRowsBuilder()


class ProtectedRowsBuilder(object):
    def __init__(self) -> None:
        self._protected_rows = ProtectedRows()

    def sheet_id(self, sheet_id: str) -> "ProtectedRowsBuilder":
        self._protected_rows.sheet_id = sheet_id
        return self

    def start_index(self, start_index: int) -> "ProtectedRowsBuilder":
        self._protected_rows.start_index = start_index
        return self

    def end_index(self, end_index: int) -> "ProtectedRowsBuilder":
        self._protected_rows.end_index = end_index
        return self

    def build(self) -> "ProtectedRows":
        return self._protected_rows
