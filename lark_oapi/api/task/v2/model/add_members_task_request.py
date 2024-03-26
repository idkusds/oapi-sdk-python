# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .add_members_task_request_body import AddMembersTaskRequestBody


class AddMembersTaskRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.task_guid: Optional[str] = None
        self.request_body: Optional[AddMembersTaskRequestBody] = None

    @staticmethod
    def builder() -> "AddMembersTaskRequestBuilder":
        return AddMembersTaskRequestBuilder()


class AddMembersTaskRequestBuilder(object):

    def __init__(self) -> None:
        add_members_task_request = AddMembersTaskRequest()
        add_members_task_request.http_method = HttpMethod.POST
        add_members_task_request.uri = "/open-apis/task/v2/tasks/:task_guid/add_members"
        add_members_task_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._add_members_task_request: AddMembersTaskRequest = add_members_task_request

    def user_id_type(self, user_id_type: str) -> "AddMembersTaskRequestBuilder":
        self._add_members_task_request.user_id_type = user_id_type
        self._add_members_task_request.add_query("user_id_type", user_id_type)
        return self

    def task_guid(self, task_guid: str) -> "AddMembersTaskRequestBuilder":
        self._add_members_task_request.task_guid = task_guid
        self._add_members_task_request.paths["task_guid"] = str(task_guid)
        return self

    def request_body(self, request_body: AddMembersTaskRequestBody) -> "AddMembersTaskRequestBuilder":
        self._add_members_task_request.request_body = request_body
        self._add_members_task_request.body = request_body
        return self

    def build(self) -> AddMembersTaskRequest:
        return self._add_members_task_request
