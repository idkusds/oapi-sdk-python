# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .combined_job import CombinedJob


class CombinedCreateJobRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.job_level_id_type: Optional[str] = None
        self.job_family_id_type: Optional[str] = None
        self.request_body: Optional[CombinedJob] = None

    @staticmethod
    def builder() -> "CombinedCreateJobRequestBuilder":
        return CombinedCreateJobRequestBuilder()


class CombinedCreateJobRequestBuilder(object):

    def __init__(self) -> None:
        combined_create_job_request = CombinedCreateJobRequest()
        combined_create_job_request.http_method = HttpMethod.POST
        combined_create_job_request.uri = "/open-apis/hire/v1/jobs/combined_create"
        combined_create_job_request.token_types = {AccessTokenType.TENANT}
        self._combined_create_job_request: CombinedCreateJobRequest = combined_create_job_request

    def user_id_type(self, user_id_type: str) -> "CombinedCreateJobRequestBuilder":
        self._combined_create_job_request.user_id_type = user_id_type
        self._combined_create_job_request.add_query("user_id_type", user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "CombinedCreateJobRequestBuilder":
        self._combined_create_job_request.department_id_type = department_id_type
        self._combined_create_job_request.add_query("department_id_type", department_id_type)
        return self

    def job_level_id_type(self, job_level_id_type: str) -> "CombinedCreateJobRequestBuilder":
        self._combined_create_job_request.job_level_id_type = job_level_id_type
        self._combined_create_job_request.add_query("job_level_id_type", job_level_id_type)
        return self

    def job_family_id_type(self, job_family_id_type: str) -> "CombinedCreateJobRequestBuilder":
        self._combined_create_job_request.job_family_id_type = job_family_id_type
        self._combined_create_job_request.add_query("job_family_id_type", job_family_id_type)
        return self

    def request_body(self, request_body: CombinedJob) -> "CombinedCreateJobRequestBuilder":
        self._combined_create_job_request.request_body = request_body
        self._combined_create_job_request.body = request_body
        return self

    def build(self) -> CombinedCreateJobRequest:
        return self._combined_create_job_request
