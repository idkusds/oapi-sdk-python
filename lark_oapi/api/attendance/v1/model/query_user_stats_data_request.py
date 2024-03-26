# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .query_user_stats_data_request_body import QueryUserStatsDataRequestBody


class QueryUserStatsDataRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.employee_type: Optional[str] = None
        self.request_body: Optional[QueryUserStatsDataRequestBody] = None

    @staticmethod
    def builder() -> "QueryUserStatsDataRequestBuilder":
        return QueryUserStatsDataRequestBuilder()


class QueryUserStatsDataRequestBuilder(object):

    def __init__(self) -> None:
        query_user_stats_data_request = QueryUserStatsDataRequest()
        query_user_stats_data_request.http_method = HttpMethod.POST
        query_user_stats_data_request.uri = "/open-apis/attendance/v1/user_stats_datas/query"
        query_user_stats_data_request.token_types = {AccessTokenType.TENANT}
        self._query_user_stats_data_request: QueryUserStatsDataRequest = query_user_stats_data_request

    def employee_type(self, employee_type: str) -> "QueryUserStatsDataRequestBuilder":
        self._query_user_stats_data_request.employee_type = employee_type
        self._query_user_stats_data_request.add_query("employee_type", employee_type)
        return self

    def request_body(self, request_body: QueryUserStatsDataRequestBody) -> "QueryUserStatsDataRequestBuilder":
        self._query_user_stats_data_request.request_body = request_body
        self._query_user_stats_data_request.body = request_body
        return self

    def build(self) -> QueryUserStatsDataRequest:
        return self._query_user_stats_data_request
