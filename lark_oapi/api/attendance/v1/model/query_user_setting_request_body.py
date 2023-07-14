# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class QueryUserSettingRequestBody(object):
    _types = {
        "user_ids": List[str],
    }

    def __init__(self, d):
        self.user_ids: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QueryUserSettingRequestBodyBuilder":
        return QueryUserSettingRequestBodyBuilder()


class QueryUserSettingRequestBodyBuilder(object):
    def __init__(self, query_user_setting_request_body: QueryUserSettingRequestBody = QueryUserSettingRequestBody({})) -> None:
        self._query_user_setting_request_body: QueryUserSettingRequestBody = query_user_setting_request_body
    
    def user_ids(self, user_ids: List[str]) -> "QueryUserSettingRequestBodyBuilder":
        self._query_user_setting_request_body.user_ids = user_ids
        return self
    
    def build(self) -> "QueryUserSettingRequestBody":
        return self._query_user_setting_request_body