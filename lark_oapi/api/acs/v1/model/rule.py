# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .device_external import DeviceExternal
from .user_external import UserExternal
from .user_external import UserExternal
from .opening_time_external import OpeningTimeExternal


class Rule(object):
    _types = {
        "id": int,
        "name": str,
        "devices": List[DeviceExternal],
        "user_count": int,
        "users": List[UserExternal],
        "visitor_count": int,
        "visitors": List[UserExternal],
        "remind_face": bool,
        "opening_time": OpeningTimeExternal,
        "is_temp": bool,
    }

    def __init__(self, d=None):
        self.id: Optional[int] = None
        self.name: Optional[str] = None
        self.devices: Optional[List[DeviceExternal]] = None
        self.user_count: Optional[int] = None
        self.users: Optional[List[UserExternal]] = None
        self.visitor_count: Optional[int] = None
        self.visitors: Optional[List[UserExternal]] = None
        self.remind_face: Optional[bool] = None
        self.opening_time: Optional[OpeningTimeExternal] = None
        self.is_temp: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RuleBuilder":
        return RuleBuilder()


class RuleBuilder(object):
    def __init__(self) -> None:
        self._rule = Rule()

    def id(self, id: int) -> "RuleBuilder":
        self._rule.id = id
        return self

    def name(self, name: str) -> "RuleBuilder":
        self._rule.name = name
        return self

    def devices(self, devices: List[DeviceExternal]) -> "RuleBuilder":
        self._rule.devices = devices
        return self

    def user_count(self, user_count: int) -> "RuleBuilder":
        self._rule.user_count = user_count
        return self

    def users(self, users: List[UserExternal]) -> "RuleBuilder":
        self._rule.users = users
        return self

    def visitor_count(self, visitor_count: int) -> "RuleBuilder":
        self._rule.visitor_count = visitor_count
        return self

    def visitors(self, visitors: List[UserExternal]) -> "RuleBuilder":
        self._rule.visitors = visitors
        return self

    def remind_face(self, remind_face: bool) -> "RuleBuilder":
        self._rule.remind_face = remind_face
        return self

    def opening_time(self, opening_time: OpeningTimeExternal) -> "RuleBuilder":
        self._rule.opening_time = opening_time
        return self

    def is_temp(self, is_temp: bool) -> "RuleBuilder":
        self._rule.is_temp = is_temp
        return self

    def build(self) -> "Rule":
        return self._rule
