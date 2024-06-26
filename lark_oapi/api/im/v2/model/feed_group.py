# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .feed_group_rules import FeedGroupRules


class FeedGroup(object):
    _types = {
        "group_id": str,
        "type": str,
        "name": str,
        "rules": FeedGroupRules,
    }

    def __init__(self, d=None):
        self.group_id: Optional[str] = None
        self.type: Optional[str] = None
        self.name: Optional[str] = None
        self.rules: Optional[FeedGroupRules] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FeedGroupBuilder":
        return FeedGroupBuilder()


class FeedGroupBuilder(object):
    def __init__(self) -> None:
        self._feed_group = FeedGroup()

    def group_id(self, group_id: str) -> "FeedGroupBuilder":
        self._feed_group.group_id = group_id
        return self

    def type(self, type: str) -> "FeedGroupBuilder":
        self._feed_group.type = type
        return self

    def name(self, name: str) -> "FeedGroupBuilder":
        self._feed_group.name = name
        return self

    def rules(self, rules: FeedGroupRules) -> "FeedGroupBuilder":
        self._feed_group.rules = rules
        return self

    def build(self) -> "FeedGroup":
        return self._feed_group
