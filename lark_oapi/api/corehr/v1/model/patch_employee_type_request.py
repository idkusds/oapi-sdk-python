# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .employee_type import EmployeeType


class PatchEmployeeTypeRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.client_token: Optional[str] = None
        self.employee_type_id: Optional[str] = None
        self.request_body: Optional[EmployeeType] = None

    @staticmethod
    def builder() -> "PatchEmployeeTypeRequestBuilder":
        return PatchEmployeeTypeRequestBuilder()


class PatchEmployeeTypeRequestBuilder(object):

    def __init__(self) -> None:
        patch_employee_type_request = PatchEmployeeTypeRequest()
        patch_employee_type_request.http_method = HttpMethod.PATCH
        patch_employee_type_request.uri = "/open-apis/corehr/v1/employee_types/:employee_type_id"
        patch_employee_type_request.token_types = {AccessTokenType.TENANT}
        self._patch_employee_type_request: PatchEmployeeTypeRequest = patch_employee_type_request

    def client_token(self, client_token: str) -> "PatchEmployeeTypeRequestBuilder":
        self._patch_employee_type_request.client_token = client_token
        self._patch_employee_type_request.add_query("client_token", client_token)
        return self

    def employee_type_id(self, employee_type_id: str) -> "PatchEmployeeTypeRequestBuilder":
        self._patch_employee_type_request.employee_type_id = employee_type_id
        self._patch_employee_type_request.paths["employee_type_id"] = str(employee_type_id)
        return self

    def request_body(self, request_body: EmployeeType) -> "PatchEmployeeTypeRequestBuilder":
        self._patch_employee_type_request.request_body = request_body
        self._patch_employee_type_request.body = request_body
        return self

    def build(self) -> PatchEmployeeTypeRequest:
        return self._patch_employee_type_request
