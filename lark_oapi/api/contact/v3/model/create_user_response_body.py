# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .user import User


class CreateUserResponseBody(object):
    _types = {
        "user": User,
    }

    def __init__(self, d=None):
        self.user: Optional[User] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateUserResponseBodyBuilder":
        return CreateUserResponseBodyBuilder()


class CreateUserResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_user_response_body = CreateUserResponseBody()

    def user(self, user: User) -> "CreateUserResponseBodyBuilder":
        self._create_user_response_body.user = user
        return self

    def build(self) -> "CreateUserResponseBody":
        return self._create_user_response_body
