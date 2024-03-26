# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class FindByDepartmentUserRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.department_id: Optional[str] = None
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None

    @staticmethod
    def builder() -> "FindByDepartmentUserRequestBuilder":
        return FindByDepartmentUserRequestBuilder()


class FindByDepartmentUserRequestBuilder(object):

    def __init__(self) -> None:
        find_by_department_user_request = FindByDepartmentUserRequest()
        find_by_department_user_request.http_method = HttpMethod.GET
        find_by_department_user_request.uri = "/open-apis/contact/v3/users/find_by_department"
        find_by_department_user_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._find_by_department_user_request: FindByDepartmentUserRequest = find_by_department_user_request

    def user_id_type(self, user_id_type: str) -> "FindByDepartmentUserRequestBuilder":
        self._find_by_department_user_request.user_id_type = user_id_type
        self._find_by_department_user_request.add_query("user_id_type", user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "FindByDepartmentUserRequestBuilder":
        self._find_by_department_user_request.department_id_type = department_id_type
        self._find_by_department_user_request.add_query("department_id_type", department_id_type)
        return self

    def department_id(self, department_id: str) -> "FindByDepartmentUserRequestBuilder":
        self._find_by_department_user_request.department_id = department_id
        self._find_by_department_user_request.add_query("department_id", department_id)
        return self

    def page_size(self, page_size: int) -> "FindByDepartmentUserRequestBuilder":
        self._find_by_department_user_request.page_size = page_size
        self._find_by_department_user_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "FindByDepartmentUserRequestBuilder":
        self._find_by_department_user_request.page_token = page_token
        self._find_by_department_user_request.add_query("page_token", page_token)
        return self

    def build(self) -> FindByDepartmentUserRequest:
        return self._find_by_department_user_request
