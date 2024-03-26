# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .user import User


class PatchUserRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.user_id: Optional[str] = None
        self.request_body: Optional[User] = None

    @staticmethod
    def builder() -> "PatchUserRequestBuilder":
        return PatchUserRequestBuilder()


class PatchUserRequestBuilder(object):

    def __init__(self) -> None:
        patch_user_request = PatchUserRequest()
        patch_user_request.http_method = HttpMethod.PATCH
        patch_user_request.uri = "/open-apis/acs/v1/users/:user_id"
        patch_user_request.token_types = {AccessTokenType.TENANT}
        self._patch_user_request: PatchUserRequest = patch_user_request

    def user_id_type(self, user_id_type: str) -> "PatchUserRequestBuilder":
        self._patch_user_request.user_id_type = user_id_type
        self._patch_user_request.add_query("user_id_type", user_id_type)
        return self

    def user_id(self, user_id: str) -> "PatchUserRequestBuilder":
        self._patch_user_request.user_id = user_id
        self._patch_user_request.paths["user_id"] = str(user_id)
        return self

    def request_body(self, request_body: User) -> "PatchUserRequestBuilder":
        self._patch_user_request.request_body = request_body
        self._patch_user_request.body = request_body
        return self

    def build(self) -> PatchUserRequest:
        return self._patch_user_request
