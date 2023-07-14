# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class PeriodRule(object):
    _types = {
        "period_rule_id": str,
        "type": str,
        "length": int,
        "first_month": int,
    }

    def __init__(self, d):
        self.period_rule_id: Optional[str] = None
        self.type: Optional[str] = None
        self.length: Optional[int] = None
        self.first_month: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PeriodRuleBuilder":
        return PeriodRuleBuilder()


class PeriodRuleBuilder(object):
    def __init__(self, period_rule: PeriodRule = PeriodRule({})) -> None:
        self._period_rule: PeriodRule = period_rule
    
    def period_rule_id(self, period_rule_id: str) -> "PeriodRuleBuilder":
        self._period_rule.period_rule_id = period_rule_id
        return self
    
    def type(self, type: str) -> "PeriodRuleBuilder":
        self._period_rule.type = type
        return self
    
    def length(self, length: int) -> "PeriodRuleBuilder":
        self._period_rule.length = length
        return self
    
    def first_month(self, first_month: int) -> "PeriodRuleBuilder":
        self._period_rule.first_month = first_month
        return self
    
    def build(self) -> "PeriodRule":
        return self._period_rule