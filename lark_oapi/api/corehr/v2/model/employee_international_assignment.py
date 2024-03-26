# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .international_assignment_v2 import InternationalAssignmentV2


class EmployeeInternationalAssignment(object):
    _types = {
        "employment_id": str,
        "international_assignments": List[InternationalAssignmentV2],
    }

    def __init__(self, d=None):
        self.employment_id: Optional[str] = None
        self.international_assignments: Optional[List[InternationalAssignmentV2]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EmployeeInternationalAssignmentBuilder":
        return EmployeeInternationalAssignmentBuilder()


class EmployeeInternationalAssignmentBuilder(object):
    def __init__(self) -> None:
        self._employee_international_assignment = EmployeeInternationalAssignment()

    def employment_id(self, employment_id: str) -> "EmployeeInternationalAssignmentBuilder":
        self._employee_international_assignment.employment_id = employment_id
        return self

    def international_assignments(self, international_assignments: List[
        InternationalAssignmentV2]) -> "EmployeeInternationalAssignmentBuilder":
        self._employee_international_assignment.international_assignments = international_assignments
        return self

    def build(self) -> "EmployeeInternationalAssignment":
        return self._employee_international_assignment
