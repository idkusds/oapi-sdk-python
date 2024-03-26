# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class QueryUserDailyShiftRequestBody(object):
    _types = {
        "user_ids": List[str],
        "check_date_from": int,
        "check_date_to": int,
    }

    def __init__(self, d=None):
        self.user_ids: Optional[List[str]] = None
        self.check_date_from: Optional[int] = None
        self.check_date_to: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QueryUserDailyShiftRequestBodyBuilder":
        return QueryUserDailyShiftRequestBodyBuilder()


class QueryUserDailyShiftRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._query_user_daily_shift_request_body = QueryUserDailyShiftRequestBody()

    def user_ids(self, user_ids: List[str]) -> "QueryUserDailyShiftRequestBodyBuilder":
        self._query_user_daily_shift_request_body.user_ids = user_ids
        return self

    def check_date_from(self, check_date_from: int) -> "QueryUserDailyShiftRequestBodyBuilder":
        self._query_user_daily_shift_request_body.check_date_from = check_date_from
        return self

    def check_date_to(self, check_date_to: int) -> "QueryUserDailyShiftRequestBodyBuilder":
        self._query_user_daily_shift_request_body.check_date_to = check_date_to
        return self

    def build(self) -> "QueryUserDailyShiftRequestBody":
        return self._query_user_daily_shift_request_body
