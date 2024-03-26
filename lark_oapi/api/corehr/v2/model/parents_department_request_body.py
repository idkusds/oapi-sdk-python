# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ParentsDepartmentRequestBody(object):
    _types = {
        "department_id_list": List[str],
    }

    def __init__(self, d=None):
        self.department_id_list: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ParentsDepartmentRequestBodyBuilder":
        return ParentsDepartmentRequestBodyBuilder()


class ParentsDepartmentRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._parents_department_request_body = ParentsDepartmentRequestBody()

    def department_id_list(self, department_id_list: List[str]) -> "ParentsDepartmentRequestBodyBuilder":
        self._parents_department_request_body.department_id_list = department_id_list
        return self

    def build(self) -> "ParentsDepartmentRequestBody":
        return self._parents_department_request_body
