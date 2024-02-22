# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class MatchCompensationStandardRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.employment_id: Optional[str] = None
        self.reference_object_api: Optional[str] = None
        self.reference_object_id: Optional[str] = None
        self.department_id: Optional[str] = None
        self.work_location_id: Optional[str] = None
        self.company_id: Optional[str] = None
        self.job_family_id: Optional[str] = None
        self.job_level_id: Optional[str] = None
        self.employee_type_id: Optional[str] = None
        self.recruitment_type: Optional[str] = None
        self.cpst_change_reason_id: Optional[str] = None
        self.cpst_plan_id: Optional[str] = None
        self.cpst_salary_level_id: Optional[str] = None
        self.effective_time: Optional[str] = None

    @staticmethod
    def builder() -> "MatchCompensationStandardRequestBuilder":
        return MatchCompensationStandardRequestBuilder()


class MatchCompensationStandardRequestBuilder(object):

    def __init__(self) -> None:
        match_compensation_standard_request = MatchCompensationStandardRequest()
        match_compensation_standard_request.http_method = HttpMethod.GET
        match_compensation_standard_request.uri = "/open-apis/corehr/v1/compensation_standards/match"
        match_compensation_standard_request.token_types = {AccessTokenType.TENANT}
        self._match_compensation_standard_request: MatchCompensationStandardRequest = match_compensation_standard_request

    def user_id_type(self, user_id_type: str) -> "MatchCompensationStandardRequestBuilder":
        self._match_compensation_standard_request.user_id_type = user_id_type
        self._match_compensation_standard_request.add_query("user_id_type", user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "MatchCompensationStandardRequestBuilder":
        self._match_compensation_standard_request.department_id_type = department_id_type
        self._match_compensation_standard_request.add_query("department_id_type", department_id_type)
        return self

    def employment_id(self, employment_id: str) -> "MatchCompensationStandardRequestBuilder":
        self._match_compensation_standard_request.employment_id = employment_id
        self._match_compensation_standard_request.add_query("employment_id", employment_id)
        return self

    def reference_object_api(self, reference_object_api: str) -> "MatchCompensationStandardRequestBuilder":
        self._match_compensation_standard_request.reference_object_api = reference_object_api
        self._match_compensation_standard_request.add_query("reference_object_api", reference_object_api)
        return self

    def reference_object_id(self, reference_object_id: str) -> "MatchCompensationStandardRequestBuilder":
        self._match_compensation_standard_request.reference_object_id = reference_object_id
        self._match_compensation_standard_request.add_query("reference_object_id", reference_object_id)
        return self

    def department_id(self, department_id: str) -> "MatchCompensationStandardRequestBuilder":
        self._match_compensation_standard_request.department_id = department_id
        self._match_compensation_standard_request.add_query("department_id", department_id)
        return self

    def work_location_id(self, work_location_id: str) -> "MatchCompensationStandardRequestBuilder":
        self._match_compensation_standard_request.work_location_id = work_location_id
        self._match_compensation_standard_request.add_query("work_location_id", work_location_id)
        return self

    def company_id(self, company_id: str) -> "MatchCompensationStandardRequestBuilder":
        self._match_compensation_standard_request.company_id = company_id
        self._match_compensation_standard_request.add_query("company_id", company_id)
        return self

    def job_family_id(self, job_family_id: str) -> "MatchCompensationStandardRequestBuilder":
        self._match_compensation_standard_request.job_family_id = job_family_id
        self._match_compensation_standard_request.add_query("job_family_id", job_family_id)
        return self

    def job_level_id(self, job_level_id: str) -> "MatchCompensationStandardRequestBuilder":
        self._match_compensation_standard_request.job_level_id = job_level_id
        self._match_compensation_standard_request.add_query("job_level_id", job_level_id)
        return self

    def employee_type_id(self, employee_type_id: str) -> "MatchCompensationStandardRequestBuilder":
        self._match_compensation_standard_request.employee_type_id = employee_type_id
        self._match_compensation_standard_request.add_query("employee_type_id", employee_type_id)
        return self

    def recruitment_type(self, recruitment_type: str) -> "MatchCompensationStandardRequestBuilder":
        self._match_compensation_standard_request.recruitment_type = recruitment_type
        self._match_compensation_standard_request.add_query("recruitment_type", recruitment_type)
        return self

    def cpst_change_reason_id(self, cpst_change_reason_id: str) -> "MatchCompensationStandardRequestBuilder":
        self._match_compensation_standard_request.cpst_change_reason_id = cpst_change_reason_id
        self._match_compensation_standard_request.add_query("cpst_change_reason_id", cpst_change_reason_id)
        return self

    def cpst_plan_id(self, cpst_plan_id: str) -> "MatchCompensationStandardRequestBuilder":
        self._match_compensation_standard_request.cpst_plan_id = cpst_plan_id
        self._match_compensation_standard_request.add_query("cpst_plan_id", cpst_plan_id)
        return self

    def cpst_salary_level_id(self, cpst_salary_level_id: str) -> "MatchCompensationStandardRequestBuilder":
        self._match_compensation_standard_request.cpst_salary_level_id = cpst_salary_level_id
        self._match_compensation_standard_request.add_query("cpst_salary_level_id", cpst_salary_level_id)
        return self

    def effective_time(self, effective_time: str) -> "MatchCompensationStandardRequestBuilder":
        self._match_compensation_standard_request.effective_time = effective_time
        self._match_compensation_standard_request.add_query("effective_time", effective_time)
        return self

    def build(self) -> MatchCompensationStandardRequest:
        return self._match_compensation_standard_request