# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class QueryTaskRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.user_id: Optional[str] = None
        self.topic: Optional[int] = None
        self.user_id_type: Optional[str] = None

    @staticmethod
    def builder() -> "QueryTaskRequestBuilder":
        return QueryTaskRequestBuilder()


class QueryTaskRequestBuilder(object):

    def __init__(self) -> None:
        query_task_request = QueryTaskRequest()
        query_task_request.http_method = HttpMethod.GET
        query_task_request.uri = "/open-apis/approval/v4/tasks/query"
        query_task_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._query_task_request: QueryTaskRequest = query_task_request

    def page_size(self, page_size: int) -> "QueryTaskRequestBuilder":
        self._query_task_request.page_size = page_size
        self._query_task_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "QueryTaskRequestBuilder":
        self._query_task_request.page_token = page_token
        self._query_task_request.add_query("page_token", page_token)
        return self

    def user_id(self, user_id: str) -> "QueryTaskRequestBuilder":
        self._query_task_request.user_id = user_id
        self._query_task_request.add_query("user_id", user_id)
        return self

    def topic(self, topic: int) -> "QueryTaskRequestBuilder":
        self._query_task_request.topic = topic
        self._query_task_request.add_query("topic", topic)
        return self

    def user_id_type(self, user_id_type: str) -> "QueryTaskRequestBuilder":
        self._query_task_request.user_id_type = user_id_type
        self._query_task_request.add_query("user_id_type", user_id_type)
        return self

    def build(self) -> QueryTaskRequest:
        return self._query_task_request
