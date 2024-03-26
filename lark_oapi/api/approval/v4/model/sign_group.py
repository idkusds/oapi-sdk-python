# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .user_id import UserId


class SignGroup(object):
    _types = {
        "instance_code": str,
        "user_id": UserId,
        "account_code": str,
        "boilerplate_unique_code": str,
        "start_time": int,
        "end_time": int,
        "type": str,
    }

    def __init__(self, d=None):
        self.instance_code: Optional[str] = None
        self.user_id: Optional[UserId] = None
        self.account_code: Optional[str] = None
        self.boilerplate_unique_code: Optional[str] = None
        self.start_time: Optional[int] = None
        self.end_time: Optional[int] = None
        self.type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SignGroupBuilder":
        return SignGroupBuilder()


class SignGroupBuilder(object):
    def __init__(self) -> None:
        self._sign_group = SignGroup()

    def instance_code(self, instance_code: str) -> "SignGroupBuilder":
        self._sign_group.instance_code = instance_code
        return self

    def user_id(self, user_id: UserId) -> "SignGroupBuilder":
        self._sign_group.user_id = user_id
        return self

    def account_code(self, account_code: str) -> "SignGroupBuilder":
        self._sign_group.account_code = account_code
        return self

    def boilerplate_unique_code(self, boilerplate_unique_code: str) -> "SignGroupBuilder":
        self._sign_group.boilerplate_unique_code = boilerplate_unique_code
        return self

    def start_time(self, start_time: int) -> "SignGroupBuilder":
        self._sign_group.start_time = start_time
        return self

    def end_time(self, end_time: int) -> "SignGroupBuilder":
        self._sign_group.end_time = end_time
        return self

    def type(self, type: str) -> "SignGroupBuilder":
        self._sign_group.type = type
        return self

    def build(self) -> "SignGroup":
        return self._sign_group
