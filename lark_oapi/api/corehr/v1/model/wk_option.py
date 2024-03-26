# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .sort_option import SortOption


class WkOption(object):
    _types = {
        "count": bool,
        "offset": int,
        "limit": int,
        "sort_options": List[SortOption],
    }

    def __init__(self, d=None):
        self.count: Optional[bool] = None
        self.offset: Optional[int] = None
        self.limit: Optional[int] = None
        self.sort_options: Optional[List[SortOption]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WkOptionBuilder":
        return WkOptionBuilder()


class WkOptionBuilder(object):
    def __init__(self) -> None:
        self._wk_option = WkOption()

    def count(self, count: bool) -> "WkOptionBuilder":
        self._wk_option.count = count
        return self

    def offset(self, offset: int) -> "WkOptionBuilder":
        self._wk_option.offset = offset
        return self

    def limit(self, limit: int) -> "WkOptionBuilder":
        self._wk_option.limit = limit
        return self

    def sort_options(self, sort_options: List[SortOption]) -> "WkOptionBuilder":
        self._wk_option.sort_options = sort_options
        return self

    def build(self) -> "WkOption":
        return self._wk_option
