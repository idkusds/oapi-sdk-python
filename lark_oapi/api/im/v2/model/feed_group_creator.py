# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .feed_group_rules import FeedGroupRules


class FeedGroupCreator(object):
    _types = {
        "type": str,
        "name": str,
        "rules": FeedGroupRules,
    }

    def __init__(self, d=None):
        self.type: Optional[str] = None
        self.name: Optional[str] = None
        self.rules: Optional[FeedGroupRules] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FeedGroupCreatorBuilder":
        return FeedGroupCreatorBuilder()


class FeedGroupCreatorBuilder(object):
    def __init__(self) -> None:
        self._feed_group_creator = FeedGroupCreator()

    def type(self, type: str) -> "FeedGroupCreatorBuilder":
        self._feed_group_creator.type = type
        return self

    def name(self, name: str) -> "FeedGroupCreatorBuilder":
        self._feed_group_creator.name = name
        return self

    def rules(self, rules: FeedGroupRules) -> "FeedGroupCreatorBuilder":
        self._feed_group_creator.rules = rules
        return self

    def build(self) -> "FeedGroupCreator":
        return self._feed_group_creator
