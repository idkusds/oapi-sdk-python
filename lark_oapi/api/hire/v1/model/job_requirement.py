# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .job_requirement_customized_data import JobRequirementCustomizedData


class JobRequirement(object):
    _types = {
        "short_code": str,
        "name": str,
        "display_progress": int,
        "head_count": int,
        "recruitment_type_id": str,
        "max_level_id": str,
        "min_level_id": str,
        "sequence_id": str,
        "category": int,
        "department_id": str,
        "recruiter_id_list": List[str],
        "jr_hiring_manager_id_list": List[str],
        "direct_leader_id_list": List[str],
        "start_time": str,
        "deadline": str,
        "priority": int,
        "required_degree": int,
        "max_salary": str,
        "min_salary": str,
        "address_id": str,
        "description": str,
        "customized_data_list": List[JobRequirementCustomizedData],
    }

    def __init__(self, d=None):
        self.short_code: Optional[str] = None
        self.name: Optional[str] = None
        self.display_progress: Optional[int] = None
        self.head_count: Optional[int] = None
        self.recruitment_type_id: Optional[str] = None
        self.max_level_id: Optional[str] = None
        self.min_level_id: Optional[str] = None
        self.sequence_id: Optional[str] = None
        self.category: Optional[int] = None
        self.department_id: Optional[str] = None
        self.recruiter_id_list: Optional[List[str]] = None
        self.jr_hiring_manager_id_list: Optional[List[str]] = None
        self.direct_leader_id_list: Optional[List[str]] = None
        self.start_time: Optional[str] = None
        self.deadline: Optional[str] = None
        self.priority: Optional[int] = None
        self.required_degree: Optional[int] = None
        self.max_salary: Optional[str] = None
        self.min_salary: Optional[str] = None
        self.address_id: Optional[str] = None
        self.description: Optional[str] = None
        self.customized_data_list: Optional[List[JobRequirementCustomizedData]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobRequirementBuilder":
        return JobRequirementBuilder()


class JobRequirementBuilder(object):
    def __init__(self) -> None:
        self._job_requirement = JobRequirement()

    def short_code(self, short_code: str) -> "JobRequirementBuilder":
        self._job_requirement.short_code = short_code
        return self

    def name(self, name: str) -> "JobRequirementBuilder":
        self._job_requirement.name = name
        return self

    def display_progress(self, display_progress: int) -> "JobRequirementBuilder":
        self._job_requirement.display_progress = display_progress
        return self

    def head_count(self, head_count: int) -> "JobRequirementBuilder":
        self._job_requirement.head_count = head_count
        return self

    def recruitment_type_id(self, recruitment_type_id: str) -> "JobRequirementBuilder":
        self._job_requirement.recruitment_type_id = recruitment_type_id
        return self

    def max_level_id(self, max_level_id: str) -> "JobRequirementBuilder":
        self._job_requirement.max_level_id = max_level_id
        return self

    def min_level_id(self, min_level_id: str) -> "JobRequirementBuilder":
        self._job_requirement.min_level_id = min_level_id
        return self

    def sequence_id(self, sequence_id: str) -> "JobRequirementBuilder":
        self._job_requirement.sequence_id = sequence_id
        return self

    def category(self, category: int) -> "JobRequirementBuilder":
        self._job_requirement.category = category
        return self

    def department_id(self, department_id: str) -> "JobRequirementBuilder":
        self._job_requirement.department_id = department_id
        return self

    def recruiter_id_list(self, recruiter_id_list: List[str]) -> "JobRequirementBuilder":
        self._job_requirement.recruiter_id_list = recruiter_id_list
        return self

    def jr_hiring_manager_id_list(self, jr_hiring_manager_id_list: List[str]) -> "JobRequirementBuilder":
        self._job_requirement.jr_hiring_manager_id_list = jr_hiring_manager_id_list
        return self

    def direct_leader_id_list(self, direct_leader_id_list: List[str]) -> "JobRequirementBuilder":
        self._job_requirement.direct_leader_id_list = direct_leader_id_list
        return self

    def start_time(self, start_time: str) -> "JobRequirementBuilder":
        self._job_requirement.start_time = start_time
        return self

    def deadline(self, deadline: str) -> "JobRequirementBuilder":
        self._job_requirement.deadline = deadline
        return self

    def priority(self, priority: int) -> "JobRequirementBuilder":
        self._job_requirement.priority = priority
        return self

    def required_degree(self, required_degree: int) -> "JobRequirementBuilder":
        self._job_requirement.required_degree = required_degree
        return self

    def max_salary(self, max_salary: str) -> "JobRequirementBuilder":
        self._job_requirement.max_salary = max_salary
        return self

    def min_salary(self, min_salary: str) -> "JobRequirementBuilder":
        self._job_requirement.min_salary = min_salary
        return self

    def address_id(self, address_id: str) -> "JobRequirementBuilder":
        self._job_requirement.address_id = address_id
        return self

    def description(self, description: str) -> "JobRequirementBuilder":
        self._job_requirement.description = description
        return self

    def customized_data_list(self, customized_data_list: List[JobRequirementCustomizedData]) -> "JobRequirementBuilder":
        self._job_requirement.customized_data_list = customized_data_list
        return self

    def build(self) -> "JobRequirement":
        return self._job_requirement
