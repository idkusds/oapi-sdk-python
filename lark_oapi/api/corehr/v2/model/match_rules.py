# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .match_rule import MatchRule


class MatchRules(object):
    _types = {
        "match_rules": List[MatchRule],
    }

    def __init__(self, d=None):
        self.match_rules: Optional[List[MatchRule]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MatchRulesBuilder":
        return MatchRulesBuilder()


class MatchRulesBuilder(object):
    def __init__(self) -> None:
        self._match_rules = MatchRules()

    def match_rules(self, match_rules: List[MatchRule]) -> "MatchRulesBuilder":
        self._match_rules.match_rules = match_rules
        return self

    def build(self) -> "MatchRules":
        return self._match_rules
