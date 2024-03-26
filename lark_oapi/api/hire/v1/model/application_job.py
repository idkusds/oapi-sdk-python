# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .city import City
from .department import Department
from .recruitment_type import RecruitmentType
from .application_job_address import ApplicationJobAddress
from .country import Country


class ApplicationJob(object):
    _types = {
        "id": str,
        "title": str,
        "city": City,
        "department": Department,
        "recruitment_type": RecruitmentType,
        "description": str,
        "job_process_id": str,
        "code": str,
        "address": ApplicationJobAddress,
        "country": Country,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.title: Optional[str] = None
        self.city: Optional[City] = None
        self.department: Optional[Department] = None
        self.recruitment_type: Optional[RecruitmentType] = None
        self.description: Optional[str] = None
        self.job_process_id: Optional[str] = None
        self.code: Optional[str] = None
        self.address: Optional[ApplicationJobAddress] = None
        self.country: Optional[Country] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApplicationJobBuilder":
        return ApplicationJobBuilder()


class ApplicationJobBuilder(object):
    def __init__(self) -> None:
        self._application_job = ApplicationJob()

    def id(self, id: str) -> "ApplicationJobBuilder":
        self._application_job.id = id
        return self

    def title(self, title: str) -> "ApplicationJobBuilder":
        self._application_job.title = title
        return self

    def city(self, city: City) -> "ApplicationJobBuilder":
        self._application_job.city = city
        return self

    def department(self, department: Department) -> "ApplicationJobBuilder":
        self._application_job.department = department
        return self

    def recruitment_type(self, recruitment_type: RecruitmentType) -> "ApplicationJobBuilder":
        self._application_job.recruitment_type = recruitment_type
        return self

    def description(self, description: str) -> "ApplicationJobBuilder":
        self._application_job.description = description
        return self

    def job_process_id(self, job_process_id: str) -> "ApplicationJobBuilder":
        self._application_job.job_process_id = job_process_id
        return self

    def code(self, code: str) -> "ApplicationJobBuilder":
        self._application_job.code = code
        return self

    def address(self, address: ApplicationJobAddress) -> "ApplicationJobBuilder":
        self._application_job.address = address
        return self

    def country(self, country: Country) -> "ApplicationJobBuilder":
        self._application_job.country = country
        return self

    def build(self) -> "ApplicationJob":
        return self._application_job
