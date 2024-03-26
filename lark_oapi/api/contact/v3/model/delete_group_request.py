# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class DeleteGroupRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.group_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteGroupRequestBuilder":
        return DeleteGroupRequestBuilder()


class DeleteGroupRequestBuilder(object):

    def __init__(self) -> None:
        delete_group_request = DeleteGroupRequest()
        delete_group_request.http_method = HttpMethod.DELETE
        delete_group_request.uri = "/open-apis/contact/v3/group/:group_id"
        delete_group_request.token_types = {AccessTokenType.TENANT}
        self._delete_group_request: DeleteGroupRequest = delete_group_request

    def group_id(self, group_id: str) -> "DeleteGroupRequestBuilder":
        self._delete_group_request.group_id = group_id
        self._delete_group_request.paths["group_id"] = str(group_id)
        return self

    def build(self) -> DeleteGroupRequest:
        return self._delete_group_request
