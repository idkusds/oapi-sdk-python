# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .condition import Condition


class UpdateSheetFilter(object):
    _types = {
        "col": str,
        "condition": Condition,
    }

    def __init__(self, d=None):
        self.col: Optional[str] = None
        self.condition: Optional[Condition] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdateSheetFilterBuilder":
        return UpdateSheetFilterBuilder()


class UpdateSheetFilterBuilder(object):
    def __init__(self) -> None:
        self._update_sheet_filter = UpdateSheetFilter()

    def col(self, col: str) -> "UpdateSheetFilterBuilder":
        self._update_sheet_filter.col = col
        return self

    def condition(self, condition: Condition) -> "UpdateSheetFilterBuilder":
        self._update_sheet_filter.condition = condition
        return self

    def build(self) -> "UpdateSheetFilter":
        return self._update_sheet_filter
