# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class FilterView(object):
    _types = {
        "filter_view_id": str,
        "filter_view_name": str,
        "range": str,
    }

    def __init__(self, d=None):
        self.filter_view_id: Optional[str] = None
        self.filter_view_name: Optional[str] = None
        self.range: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FilterViewBuilder":
        return FilterViewBuilder()


class FilterViewBuilder(object):
    def __init__(self) -> None:
        self._filter_view = FilterView()

    def filter_view_id(self, filter_view_id: str) -> "FilterViewBuilder":
        self._filter_view.filter_view_id = filter_view_id
        return self

    def filter_view_name(self, filter_view_name: str) -> "FilterViewBuilder":
        self._filter_view.filter_view_name = filter_view_name
        return self

    def range(self, range: str) -> "FilterViewBuilder":
        self._filter_view.range = range
        return self

    def build(self) -> "FilterView":
        return self._filter_view
