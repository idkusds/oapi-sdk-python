# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .employee_type import EmployeeType


class PatchEmployeeTypeResponseBody(object):
    _types = {
        "employee_type": EmployeeType,
    }

    def __init__(self, d=None):
        self.employee_type: Optional[EmployeeType] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchEmployeeTypeResponseBodyBuilder":
        return PatchEmployeeTypeResponseBodyBuilder()


class PatchEmployeeTypeResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._patch_employee_type_response_body = PatchEmployeeTypeResponseBody()

    def employee_type(self, employee_type: EmployeeType) -> "PatchEmployeeTypeResponseBodyBuilder":
        self._patch_employee_type_response_body.employee_type = employee_type
        return self

    def build(self) -> "PatchEmployeeTypeResponseBody":
        return self._patch_employee_type_response_body
