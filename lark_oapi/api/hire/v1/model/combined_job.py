# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .combined_job_object_value_map import CombinedJobObjectValueMap
from .job_manager import JobManager


class CombinedJob(object):
    _types = {
        "id": str,
        "code": str,
        "experience": int,
        "expiry_time": int,
        "customized_data_list": List[CombinedJobObjectValueMap],
        "min_level_id": str,
        "min_salary": int,
        "title": str,
        "job_managers": JobManager,
        "job_process_id": str,
        "process_type": int,
        "subject_id": str,
        "job_function_id": str,
        "department_id": str,
        "head_count": int,
        "is_never_expired": bool,
        "max_salary": int,
        "requirement": str,
        "description": str,
        "highlight_list": List[str],
        "job_type_id": str,
        "max_level_id": str,
        "recruitment_type_id": str,
        "required_degree": int,
        "job_category_id": str,
        "address_id_list": List[str],
        "job_attribute": int,
        "expiry_timestamp": str,
        "interview_registration_schema_id": str,
        "onboard_registration_schema_id": str,
        "target_major_id_list": List[str],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.code: Optional[str] = None
        self.experience: Optional[int] = None
        self.expiry_time: Optional[int] = None
        self.customized_data_list: Optional[List[CombinedJobObjectValueMap]] = None
        self.min_level_id: Optional[str] = None
        self.min_salary: Optional[int] = None
        self.title: Optional[str] = None
        self.job_managers: Optional[JobManager] = None
        self.job_process_id: Optional[str] = None
        self.process_type: Optional[int] = None
        self.subject_id: Optional[str] = None
        self.job_function_id: Optional[str] = None
        self.department_id: Optional[str] = None
        self.head_count: Optional[int] = None
        self.is_never_expired: Optional[bool] = None
        self.max_salary: Optional[int] = None
        self.requirement: Optional[str] = None
        self.description: Optional[str] = None
        self.highlight_list: Optional[List[str]] = None
        self.job_type_id: Optional[str] = None
        self.max_level_id: Optional[str] = None
        self.recruitment_type_id: Optional[str] = None
        self.required_degree: Optional[int] = None
        self.job_category_id: Optional[str] = None
        self.address_id_list: Optional[List[str]] = None
        self.job_attribute: Optional[int] = None
        self.expiry_timestamp: Optional[str] = None
        self.interview_registration_schema_id: Optional[str] = None
        self.onboard_registration_schema_id: Optional[str] = None
        self.target_major_id_list: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CombinedJobBuilder":
        return CombinedJobBuilder()


class CombinedJobBuilder(object):
    def __init__(self) -> None:
        self._combined_job = CombinedJob()

    def id(self, id: str) -> "CombinedJobBuilder":
        self._combined_job.id = id
        return self

    def code(self, code: str) -> "CombinedJobBuilder":
        self._combined_job.code = code
        return self

    def experience(self, experience: int) -> "CombinedJobBuilder":
        self._combined_job.experience = experience
        return self

    def expiry_time(self, expiry_time: int) -> "CombinedJobBuilder":
        self._combined_job.expiry_time = expiry_time
        return self

    def customized_data_list(self, customized_data_list: List[CombinedJobObjectValueMap]) -> "CombinedJobBuilder":
        self._combined_job.customized_data_list = customized_data_list
        return self

    def min_level_id(self, min_level_id: str) -> "CombinedJobBuilder":
        self._combined_job.min_level_id = min_level_id
        return self

    def min_salary(self, min_salary: int) -> "CombinedJobBuilder":
        self._combined_job.min_salary = min_salary
        return self

    def title(self, title: str) -> "CombinedJobBuilder":
        self._combined_job.title = title
        return self

    def job_managers(self, job_managers: JobManager) -> "CombinedJobBuilder":
        self._combined_job.job_managers = job_managers
        return self

    def job_process_id(self, job_process_id: str) -> "CombinedJobBuilder":
        self._combined_job.job_process_id = job_process_id
        return self

    def process_type(self, process_type: int) -> "CombinedJobBuilder":
        self._combined_job.process_type = process_type
        return self

    def subject_id(self, subject_id: str) -> "CombinedJobBuilder":
        self._combined_job.subject_id = subject_id
        return self

    def job_function_id(self, job_function_id: str) -> "CombinedJobBuilder":
        self._combined_job.job_function_id = job_function_id
        return self

    def department_id(self, department_id: str) -> "CombinedJobBuilder":
        self._combined_job.department_id = department_id
        return self

    def head_count(self, head_count: int) -> "CombinedJobBuilder":
        self._combined_job.head_count = head_count
        return self

    def is_never_expired(self, is_never_expired: bool) -> "CombinedJobBuilder":
        self._combined_job.is_never_expired = is_never_expired
        return self

    def max_salary(self, max_salary: int) -> "CombinedJobBuilder":
        self._combined_job.max_salary = max_salary
        return self

    def requirement(self, requirement: str) -> "CombinedJobBuilder":
        self._combined_job.requirement = requirement
        return self

    def description(self, description: str) -> "CombinedJobBuilder":
        self._combined_job.description = description
        return self

    def highlight_list(self, highlight_list: List[str]) -> "CombinedJobBuilder":
        self._combined_job.highlight_list = highlight_list
        return self

    def job_type_id(self, job_type_id: str) -> "CombinedJobBuilder":
        self._combined_job.job_type_id = job_type_id
        return self

    def max_level_id(self, max_level_id: str) -> "CombinedJobBuilder":
        self._combined_job.max_level_id = max_level_id
        return self

    def recruitment_type_id(self, recruitment_type_id: str) -> "CombinedJobBuilder":
        self._combined_job.recruitment_type_id = recruitment_type_id
        return self

    def required_degree(self, required_degree: int) -> "CombinedJobBuilder":
        self._combined_job.required_degree = required_degree
        return self

    def job_category_id(self, job_category_id: str) -> "CombinedJobBuilder":
        self._combined_job.job_category_id = job_category_id
        return self

    def address_id_list(self, address_id_list: List[str]) -> "CombinedJobBuilder":
        self._combined_job.address_id_list = address_id_list
        return self

    def job_attribute(self, job_attribute: int) -> "CombinedJobBuilder":
        self._combined_job.job_attribute = job_attribute
        return self

    def expiry_timestamp(self, expiry_timestamp: str) -> "CombinedJobBuilder":
        self._combined_job.expiry_timestamp = expiry_timestamp
        return self

    def interview_registration_schema_id(self, interview_registration_schema_id: str) -> "CombinedJobBuilder":
        self._combined_job.interview_registration_schema_id = interview_registration_schema_id
        return self

    def onboard_registration_schema_id(self, onboard_registration_schema_id: str) -> "CombinedJobBuilder":
        self._combined_job.onboard_registration_schema_id = onboard_registration_schema_id
        return self

    def target_major_id_list(self, target_major_id_list: List[str]) -> "CombinedJobBuilder":
        self._combined_job.target_major_id_list = target_major_id_list
        return self

    def build(self) -> "CombinedJob":
        return self._combined_job
