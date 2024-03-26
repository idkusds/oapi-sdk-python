# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class GetDepartmentRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.department_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetDepartmentRequestBuilder":
        return GetDepartmentRequestBuilder()


class GetDepartmentRequestBuilder(object):

    def __init__(self) -> None:
        get_department_request = GetDepartmentRequest()
        get_department_request.http_method = HttpMethod.GET
        get_department_request.uri = "/open-apis/corehr/v1/departments/:department_id"
        get_department_request.token_types = {AccessTokenType.TENANT}
        self._get_department_request: GetDepartmentRequest = get_department_request

    def user_id_type(self, user_id_type: str) -> "GetDepartmentRequestBuilder":
        self._get_department_request.user_id_type = user_id_type
        self._get_department_request.add_query("user_id_type", user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "GetDepartmentRequestBuilder":
        self._get_department_request.department_id_type = department_id_type
        self._get_department_request.add_query("department_id_type", department_id_type)
        return self

    def department_id(self, department_id: str) -> "GetDepartmentRequestBuilder":
        self._get_department_request.department_id = department_id
        self._get_department_request.paths["department_id"] = str(department_id)
        return self

    def build(self) -> GetDepartmentRequest:
        return self._get_department_request
