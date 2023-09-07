# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteEmployeeTypeRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.employee_type_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteEmployeeTypeRequestBuilder":
        return DeleteEmployeeTypeRequestBuilder()


class DeleteEmployeeTypeRequestBuilder(object):

    def __init__(self) -> None:
        delete_employee_type_request = DeleteEmployeeTypeRequest()
        delete_employee_type_request.http_method = HttpMethod.DELETE
        delete_employee_type_request.uri = "/open-apis/corehr/v1/employee_types/:employee_type_id"
        delete_employee_type_request.token_types = {AccessTokenType.TENANT}
        self._delete_employee_type_request: DeleteEmployeeTypeRequest = delete_employee_type_request

    def employee_type_id(self, employee_type_id: str) -> "DeleteEmployeeTypeRequestBuilder":
        self._delete_employee_type_request.employee_type_id = employee_type_id
        self._delete_employee_type_request.paths["employee_type_id"] = str(employee_type_id)
        return self

    def build(self) -> DeleteEmployeeTypeRequest:
        return self._delete_employee_type_request
