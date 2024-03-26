# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DurationItem(object):
    _types = {
        "date": str,
        "duration": float,
        "unit": int,
        "settlement_type": int,
    }

    def __init__(self, d=None):
        self.date: Optional[str] = None
        self.duration: Optional[float] = None
        self.unit: Optional[int] = None
        self.settlement_type: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DurationItemBuilder":
        return DurationItemBuilder()


class DurationItemBuilder(object):
    def __init__(self) -> None:
        self._duration_item = DurationItem()

    def date(self, date: str) -> "DurationItemBuilder":
        self._duration_item.date = date
        return self

    def duration(self, duration: float) -> "DurationItemBuilder":
        self._duration_item.duration = duration
        return self

    def unit(self, unit: int) -> "DurationItemBuilder":
        self._duration_item.unit = unit
        return self

    def settlement_type(self, settlement_type: int) -> "DurationItemBuilder":
        self._duration_item.settlement_type = settlement_type
        return self

    def build(self) -> "DurationItem":
        return self._duration_item
