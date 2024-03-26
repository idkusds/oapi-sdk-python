# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .query_user_task_remedy_request_body import QueryUserTaskRemedyRequestBody


class QueryUserTaskRemedyRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.employee_type: Optional[str] = None
        self.request_body: Optional[QueryUserTaskRemedyRequestBody] = None

    @staticmethod
    def builder() -> "QueryUserTaskRemedyRequestBuilder":
        return QueryUserTaskRemedyRequestBuilder()


class QueryUserTaskRemedyRequestBuilder(object):

    def __init__(self) -> None:
        query_user_task_remedy_request = QueryUserTaskRemedyRequest()
        query_user_task_remedy_request.http_method = HttpMethod.POST
        query_user_task_remedy_request.uri = "/open-apis/attendance/v1/user_task_remedys/query"
        query_user_task_remedy_request.token_types = {AccessTokenType.TENANT}
        self._query_user_task_remedy_request: QueryUserTaskRemedyRequest = query_user_task_remedy_request

    def employee_type(self, employee_type: str) -> "QueryUserTaskRemedyRequestBuilder":
        self._query_user_task_remedy_request.employee_type = employee_type
        self._query_user_task_remedy_request.add_query("employee_type", employee_type)
        return self

    def request_body(self, request_body: QueryUserTaskRemedyRequestBody) -> "QueryUserTaskRemedyRequestBuilder":
        self._query_user_task_remedy_request.request_body = request_body
        self._query_user_task_remedy_request.body = request_body
        return self

    def build(self) -> QueryUserTaskRemedyRequest:
        return self._query_user_task_remedy_request
