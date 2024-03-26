# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DateTime(object):
    _types = {
        "date_time": str,
    }

    def __init__(self, d=None):
        self.date_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DateTimeBuilder":
        return DateTimeBuilder()


class DateTimeBuilder(object):
    def __init__(self) -> None:
        self._date_time = DateTime()

    def date_time(self, date_time: str) -> "DateTimeBuilder":
        self._date_time.date_time = date_time
        return self

    def build(self) -> "DateTime":
        return self._date_time
