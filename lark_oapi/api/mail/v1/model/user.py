# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class User(object):
    _types = {
        "email": str,
        "status": int,
        "type": int,
    }

    def __init__(self, d=None):
        self.email: Optional[str] = None
        self.status: Optional[int] = None
        self.type: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserBuilder":
        return UserBuilder()


class UserBuilder(object):
    def __init__(self) -> None:
        self._user = User()

    def email(self, email: str) -> "UserBuilder":
        self._user.email = email
        return self

    def status(self, status: int) -> "UserBuilder":
        self._user.status = status
        return self

    def type(self, type: int) -> "UserBuilder":
        self._user.type = type
        return self

    def build(self) -> "User":
        return self._user
