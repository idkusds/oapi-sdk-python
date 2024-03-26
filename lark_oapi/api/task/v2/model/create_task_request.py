# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .input_task import InputTask


class CreateTaskRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[InputTask] = None

    @staticmethod
    def builder() -> "CreateTaskRequestBuilder":
        return CreateTaskRequestBuilder()


class CreateTaskRequestBuilder(object):

    def __init__(self) -> None:
        create_task_request = CreateTaskRequest()
        create_task_request.http_method = HttpMethod.POST
        create_task_request.uri = "/open-apis/task/v2/tasks"
        create_task_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._create_task_request: CreateTaskRequest = create_task_request

    def user_id_type(self, user_id_type: str) -> "CreateTaskRequestBuilder":
        self._create_task_request.user_id_type = user_id_type
        self._create_task_request.add_query("user_id_type", user_id_type)
        return self

    def request_body(self, request_body: InputTask) -> "CreateTaskRequestBuilder":
        self._create_task_request.request_body = request_body
        self._create_task_request.body = request_body
        return self

    def build(self) -> CreateTaskRequest:
        return self._create_task_request
