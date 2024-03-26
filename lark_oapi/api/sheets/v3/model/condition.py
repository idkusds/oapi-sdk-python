# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class Condition(object):
    _types = {
        "filter_type": str,
        "compare_type": str,
        "expected": List[str],
    }

    def __init__(self, d=None):
        self.filter_type: Optional[str] = None
        self.compare_type: Optional[str] = None
        self.expected: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ConditionBuilder":
        return ConditionBuilder()


class ConditionBuilder(object):
    def __init__(self) -> None:
        self._condition = Condition()

    def filter_type(self, filter_type: str) -> "ConditionBuilder":
        self._condition.filter_type = filter_type
        return self

    def compare_type(self, compare_type: str) -> "ConditionBuilder":
        self._condition.compare_type = compare_type
        return self

    def expected(self, expected: List[str]) -> "ConditionBuilder":
        self._condition.expected = expected
        return self

    def build(self) -> "Condition":
        return self._condition
