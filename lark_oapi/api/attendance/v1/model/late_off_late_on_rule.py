# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class LateOffLateOnRule(object):
    _types = {
        "late_off_minutes": int,
        "late_on_minutes": int,
    }

    def __init__(self, d=None):
        self.late_off_minutes: Optional[int] = None
        self.late_on_minutes: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "LateOffLateOnRuleBuilder":
        return LateOffLateOnRuleBuilder()


class LateOffLateOnRuleBuilder(object):
    def __init__(self) -> None:
        self._late_off_late_on_rule = LateOffLateOnRule()

    def late_off_minutes(self, late_off_minutes: int) -> "LateOffLateOnRuleBuilder":
        self._late_off_late_on_rule.late_off_minutes = late_off_minutes
        return self

    def late_on_minutes(self, late_on_minutes: int) -> "LateOffLateOnRuleBuilder":
        self._late_off_late_on_rule.late_on_minutes = late_on_minutes
        return self

    def build(self) -> "LateOffLateOnRule":
        return self._late_off_late_on_rule
