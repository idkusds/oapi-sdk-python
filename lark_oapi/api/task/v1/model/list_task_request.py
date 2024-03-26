# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListTaskRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.start_create_time: Optional[int] = None
        self.end_create_time: Optional[int] = None
        self.task_completed: Optional[bool] = None
        self.user_id_type: Optional[str] = None

    @staticmethod
    def builder() -> "ListTaskRequestBuilder":
        return ListTaskRequestBuilder()


class ListTaskRequestBuilder(object):

    def __init__(self) -> None:
        list_task_request = ListTaskRequest()
        list_task_request.http_method = HttpMethod.GET
        list_task_request.uri = "/open-apis/task/v1/tasks"
        list_task_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._list_task_request: ListTaskRequest = list_task_request

    def page_size(self, page_size: int) -> "ListTaskRequestBuilder":
        self._list_task_request.page_size = page_size
        self._list_task_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListTaskRequestBuilder":
        self._list_task_request.page_token = page_token
        self._list_task_request.add_query("page_token", page_token)
        return self

    def start_create_time(self, start_create_time: int) -> "ListTaskRequestBuilder":
        self._list_task_request.start_create_time = start_create_time
        self._list_task_request.add_query("start_create_time", start_create_time)
        return self

    def end_create_time(self, end_create_time: int) -> "ListTaskRequestBuilder":
        self._list_task_request.end_create_time = end_create_time
        self._list_task_request.add_query("end_create_time", end_create_time)
        return self

    def task_completed(self, task_completed: bool) -> "ListTaskRequestBuilder":
        self._list_task_request.task_completed = task_completed
        self._list_task_request.add_query("task_completed", task_completed)
        return self

    def user_id_type(self, user_id_type: str) -> "ListTaskRequestBuilder":
        self._list_task_request.user_id_type = user_id_type
        self._list_task_request.add_query("user_id_type", user_id_type)
        return self

    def build(self) -> ListTaskRequest:
        return self._list_task_request
