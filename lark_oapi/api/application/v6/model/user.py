# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .user_id import UserId


class User(object):
    _types = {
        "user_id": UserId,
    }

    def __init__(self, d=None):
        self.user_id: Optional[UserId] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserBuilder":
        return UserBuilder()


class UserBuilder(object):
    def __init__(self) -> None:
        self._user = User()

    def user_id(self, user_id: UserId) -> "UserBuilder":
        self._user.user_id = user_id
        return self

    def build(self) -> "User":
        return self._user
