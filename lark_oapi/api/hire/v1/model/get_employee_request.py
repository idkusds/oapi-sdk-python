# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetEmployeeRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.employee_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetEmployeeRequestBuilder":
        return GetEmployeeRequestBuilder()


class GetEmployeeRequestBuilder(object):

    def __init__(self) -> None:
        get_employee_request = GetEmployeeRequest()
        get_employee_request.http_method = HttpMethod.GET
        get_employee_request.uri = "/open-apis/hire/v1/employees/:employee_id"
        get_employee_request.token_types = {AccessTokenType.TENANT}
        self._get_employee_request: GetEmployeeRequest = get_employee_request

    def user_id_type(self, user_id_type: str) -> "GetEmployeeRequestBuilder":
        self._get_employee_request.user_id_type = user_id_type
        self._get_employee_request.add_query("user_id_type", user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "GetEmployeeRequestBuilder":
        self._get_employee_request.department_id_type = department_id_type
        self._get_employee_request.add_query("department_id_type", department_id_type)
        return self

    def employee_id(self, employee_id: str) -> "GetEmployeeRequestBuilder":
        self._get_employee_request.employee_id = employee_id
        self._get_employee_request.paths["employee_id"] = str(employee_id)
        return self

    def build(self) -> GetEmployeeRequest:
        return self._get_employee_request
