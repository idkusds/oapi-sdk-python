# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .enum import Enum
from .enum import Enum
from .object_field_data import ObjectFieldData
from .email import Email
from .enum import Enum
from .job_data_cost_center import JobDataCostCenter
from .enum import Enum
from .enum import Enum
from .enum import Enum


class Employment(object):
    _types = {
        "prehire_id": str,
        "employee_type_id": str,
        "tenure": str,
        "department_id": str,
        "job_level_id": str,
        "work_location_id": str,
        "job_family_id": str,
        "job_id": str,
        "company_id": str,
        "working_hours_type_id": str,
        "id": str,
        "seniority_date": str,
        "employee_number": str,
        "effective_time": str,
        "expiration_time": str,
        "employment_type": Enum,
        "person_id": str,
        "probation_period": int,
        "on_probation": str,
        "probation_end_date": str,
        "primary_employment": bool,
        "employment_status": Enum,
        "custom_fields": List[ObjectFieldData],
        "work_email_list": List[Email],
        "email_address": str,
        "reason_for_offboarding": Enum,
        "cost_center_list": List[JobDataCostCenter],
        "ats_application_id": str,
        "rehire": Enum,
        "rehire_employment_id": str,
        "service_company": str,
        "compensation_type": Enum,
        "work_shift": Enum,
    }

    def __init__(self, d=None):
        self.prehire_id: Optional[str] = None
        self.employee_type_id: Optional[str] = None
        self.tenure: Optional[str] = None
        self.department_id: Optional[str] = None
        self.job_level_id: Optional[str] = None
        self.work_location_id: Optional[str] = None
        self.job_family_id: Optional[str] = None
        self.job_id: Optional[str] = None
        self.company_id: Optional[str] = None
        self.working_hours_type_id: Optional[str] = None
        self.id: Optional[str] = None
        self.seniority_date: Optional[str] = None
        self.employee_number: Optional[str] = None
        self.effective_time: Optional[str] = None
        self.expiration_time: Optional[str] = None
        self.employment_type: Optional[Enum] = None
        self.person_id: Optional[str] = None
        self.probation_period: Optional[int] = None
        self.on_probation: Optional[str] = None
        self.probation_end_date: Optional[str] = None
        self.primary_employment: Optional[bool] = None
        self.employment_status: Optional[Enum] = None
        self.custom_fields: Optional[List[ObjectFieldData]] = None
        self.work_email_list: Optional[List[Email]] = None
        self.email_address: Optional[str] = None
        self.reason_for_offboarding: Optional[Enum] = None
        self.cost_center_list: Optional[List[JobDataCostCenter]] = None
        self.ats_application_id: Optional[str] = None
        self.rehire: Optional[Enum] = None
        self.rehire_employment_id: Optional[str] = None
        self.service_company: Optional[str] = None
        self.compensation_type: Optional[Enum] = None
        self.work_shift: Optional[Enum] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EmploymentBuilder":
        return EmploymentBuilder()


class EmploymentBuilder(object):
    def __init__(self) -> None:
        self._employment = Employment()

    def prehire_id(self, prehire_id: str) -> "EmploymentBuilder":
        self._employment.prehire_id = prehire_id
        return self

    def employee_type_id(self, employee_type_id: str) -> "EmploymentBuilder":
        self._employment.employee_type_id = employee_type_id
        return self

    def tenure(self, tenure: str) -> "EmploymentBuilder":
        self._employment.tenure = tenure
        return self

    def department_id(self, department_id: str) -> "EmploymentBuilder":
        self._employment.department_id = department_id
        return self

    def job_level_id(self, job_level_id: str) -> "EmploymentBuilder":
        self._employment.job_level_id = job_level_id
        return self

    def work_location_id(self, work_location_id: str) -> "EmploymentBuilder":
        self._employment.work_location_id = work_location_id
        return self

    def job_family_id(self, job_family_id: str) -> "EmploymentBuilder":
        self._employment.job_family_id = job_family_id
        return self

    def job_id(self, job_id: str) -> "EmploymentBuilder":
        self._employment.job_id = job_id
        return self

    def company_id(self, company_id: str) -> "EmploymentBuilder":
        self._employment.company_id = company_id
        return self

    def working_hours_type_id(self, working_hours_type_id: str) -> "EmploymentBuilder":
        self._employment.working_hours_type_id = working_hours_type_id
        return self

    def id(self, id: str) -> "EmploymentBuilder":
        self._employment.id = id
        return self

    def seniority_date(self, seniority_date: str) -> "EmploymentBuilder":
        self._employment.seniority_date = seniority_date
        return self

    def employee_number(self, employee_number: str) -> "EmploymentBuilder":
        self._employment.employee_number = employee_number
        return self

    def effective_time(self, effective_time: str) -> "EmploymentBuilder":
        self._employment.effective_time = effective_time
        return self

    def expiration_time(self, expiration_time: str) -> "EmploymentBuilder":
        self._employment.expiration_time = expiration_time
        return self

    def employment_type(self, employment_type: Enum) -> "EmploymentBuilder":
        self._employment.employment_type = employment_type
        return self

    def person_id(self, person_id: str) -> "EmploymentBuilder":
        self._employment.person_id = person_id
        return self

    def probation_period(self, probation_period: int) -> "EmploymentBuilder":
        self._employment.probation_period = probation_period
        return self

    def on_probation(self, on_probation: str) -> "EmploymentBuilder":
        self._employment.on_probation = on_probation
        return self

    def probation_end_date(self, probation_end_date: str) -> "EmploymentBuilder":
        self._employment.probation_end_date = probation_end_date
        return self

    def primary_employment(self, primary_employment: bool) -> "EmploymentBuilder":
        self._employment.primary_employment = primary_employment
        return self

    def employment_status(self, employment_status: Enum) -> "EmploymentBuilder":
        self._employment.employment_status = employment_status
        return self

    def custom_fields(self, custom_fields: List[ObjectFieldData]) -> "EmploymentBuilder":
        self._employment.custom_fields = custom_fields
        return self

    def work_email_list(self, work_email_list: List[Email]) -> "EmploymentBuilder":
        self._employment.work_email_list = work_email_list
        return self

    def email_address(self, email_address: str) -> "EmploymentBuilder":
        self._employment.email_address = email_address
        return self

    def reason_for_offboarding(self, reason_for_offboarding: Enum) -> "EmploymentBuilder":
        self._employment.reason_for_offboarding = reason_for_offboarding
        return self

    def cost_center_list(self, cost_center_list: List[JobDataCostCenter]) -> "EmploymentBuilder":
        self._employment.cost_center_list = cost_center_list
        return self

    def ats_application_id(self, ats_application_id: str) -> "EmploymentBuilder":
        self._employment.ats_application_id = ats_application_id
        return self

    def rehire(self, rehire: Enum) -> "EmploymentBuilder":
        self._employment.rehire = rehire
        return self

    def rehire_employment_id(self, rehire_employment_id: str) -> "EmploymentBuilder":
        self._employment.rehire_employment_id = rehire_employment_id
        return self

    def service_company(self, service_company: str) -> "EmploymentBuilder":
        self._employment.service_company = service_company
        return self

    def compensation_type(self, compensation_type: Enum) -> "EmploymentBuilder":
        self._employment.compensation_type = compensation_type
        return self

    def work_shift(self, work_shift: Enum) -> "EmploymentBuilder":
        self._employment.work_shift = work_shift
        return self

    def build(self) -> "Employment":
        return self._employment
