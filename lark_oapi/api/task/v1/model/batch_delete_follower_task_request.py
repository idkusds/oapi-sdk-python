# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .follower import Follower


class BatchDeleteFollowerTaskRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.task_id: Optional[str] = None
        self.request_body: Optional[Follower] = None

    @staticmethod
    def builder() -> "BatchDeleteFollowerTaskRequestBuilder":
        return BatchDeleteFollowerTaskRequestBuilder()


class BatchDeleteFollowerTaskRequestBuilder(object):

    def __init__(self) -> None:
        batch_delete_follower_task_request = BatchDeleteFollowerTaskRequest()
        batch_delete_follower_task_request.http_method = HttpMethod.POST
        batch_delete_follower_task_request.uri = "/open-apis/task/v1/tasks/:task_id/batch_delete_follower"
        batch_delete_follower_task_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._batch_delete_follower_task_request: BatchDeleteFollowerTaskRequest = batch_delete_follower_task_request

    def user_id_type(self, user_id_type: str) -> "BatchDeleteFollowerTaskRequestBuilder":
        self._batch_delete_follower_task_request.user_id_type = user_id_type
        self._batch_delete_follower_task_request.add_query("user_id_type", user_id_type)
        return self

    def task_id(self, task_id: str) -> "BatchDeleteFollowerTaskRequestBuilder":
        self._batch_delete_follower_task_request.task_id = task_id
        self._batch_delete_follower_task_request.paths["task_id"] = str(task_id)
        return self

    def request_body(self, request_body: Follower) -> "BatchDeleteFollowerTaskRequestBuilder":
        self._batch_delete_follower_task_request.request_body = request_body
        self._batch_delete_follower_task_request.body = request_body
        return self

    def build(self) -> BatchDeleteFollowerTaskRequest:
        return self._batch_delete_follower_task_request
