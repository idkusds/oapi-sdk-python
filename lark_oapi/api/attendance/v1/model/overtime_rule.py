# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class OvertimeRule(object):
    _types = {
        "on_overtime": str,
        "off_overtime": str,
    }

    def __init__(self, d):
        self.on_overtime: Optional[str] = None
        self.off_overtime: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OvertimeRuleBuilder":
        return OvertimeRuleBuilder()


class OvertimeRuleBuilder(object):
    def __init__(self, overtime_rule: OvertimeRule = OvertimeRule({})) -> None:
        self._overtime_rule: OvertimeRule = overtime_rule
    
    def on_overtime(self, on_overtime: str) -> "OvertimeRuleBuilder":
        self._overtime_rule.on_overtime = on_overtime
        return self
    
    def off_overtime(self, off_overtime: str) -> "OvertimeRuleBuilder":
        self._overtime_rule.off_overtime = off_overtime
        return self
    
    def build(self) -> "OvertimeRule":
        return self._overtime_rule