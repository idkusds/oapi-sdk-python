# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class PunchTimeSimpleRule(object):
    _types = {
        "on_time": str,
        "off_time": str,
    }

    def __init__(self, d=None):
        self.on_time: Optional[str] = None
        self.off_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PunchTimeSimpleRuleBuilder":
        return PunchTimeSimpleRuleBuilder()


class PunchTimeSimpleRuleBuilder(object):
    def __init__(self) -> None:
        self._punch_time_simple_rule = PunchTimeSimpleRule()

    def on_time(self, on_time: str) -> "PunchTimeSimpleRuleBuilder":
        self._punch_time_simple_rule.on_time = on_time
        return self

    def off_time(self, off_time: str) -> "PunchTimeSimpleRuleBuilder":
        self._punch_time_simple_rule.off_time = off_time
        return self

    def build(self) -> "PunchTimeSimpleRule":
        return self._punch_time_simple_rule
