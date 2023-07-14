# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class ClearStyleMultiRange(object):
    _types = {
        "ranges": List[str],
    }

    def __init__(self, d):
        self.ranges: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ClearStyleMultiRangeBuilder":
        return ClearStyleMultiRangeBuilder()


class ClearStyleMultiRangeBuilder(object):
    def __init__(self, clear_style_multi_range: ClearStyleMultiRange = ClearStyleMultiRange({})) -> None:
        self._clear_style_multi_range: ClearStyleMultiRange = clear_style_multi_range
    
    def ranges(self, ranges: List[str]) -> "ClearStyleMultiRangeBuilder":
        self._clear_style_multi_range.ranges = ranges
        return self
    
    def build(self) -> "ClearStyleMultiRange":
        return self._clear_style_multi_range