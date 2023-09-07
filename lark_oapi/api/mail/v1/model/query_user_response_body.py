# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .user import User


class QueryUserResponseBody(object):
    _types = {
        "user_list": List[User],
    }

    def __init__(self, d=None):
        self.user_list: Optional[List[User]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QueryUserResponseBodyBuilder":
        return QueryUserResponseBodyBuilder()


class QueryUserResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._query_user_response_body = QueryUserResponseBody()

    def user_list(self, user_list: List[User]) -> "QueryUserResponseBodyBuilder":
        self._query_user_response_body.user_list = user_list
        return self

    def build(self) -> "QueryUserResponseBody":
        return self._query_user_response_body
