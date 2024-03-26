# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class GetUserRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.user_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetUserRequestBuilder":
        return GetUserRequestBuilder()


class GetUserRequestBuilder(object):

    def __init__(self) -> None:
        get_user_request = GetUserRequest()
        get_user_request.http_method = HttpMethod.GET
        get_user_request.uri = "/open-apis/contact/v3/users/:user_id"
        get_user_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._get_user_request: GetUserRequest = get_user_request

    def user_id_type(self, user_id_type: str) -> "GetUserRequestBuilder":
        self._get_user_request.user_id_type = user_id_type
        self._get_user_request.add_query("user_id_type", user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "GetUserRequestBuilder":
        self._get_user_request.department_id_type = department_id_type
        self._get_user_request.add_query("department_id_type", department_id_type)
        return self

    def user_id(self, user_id: str) -> "GetUserRequestBuilder":
        self._get_user_request.user_id = user_id
        self._get_user_request.paths["user_id"] = str(user_id)
        return self

    def build(self) -> GetUserRequest:
        return self._get_user_request
