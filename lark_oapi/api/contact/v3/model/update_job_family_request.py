# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .job_family import JobFamily


class UpdateJobFamilyRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.job_family_id: Optional[str] = None
        self.request_body: Optional[JobFamily] = None

    @staticmethod
    def builder() -> "UpdateJobFamilyRequestBuilder":
        return UpdateJobFamilyRequestBuilder()


class UpdateJobFamilyRequestBuilder(object):

    def __init__(self) -> None:
        update_job_family_request = UpdateJobFamilyRequest()
        update_job_family_request.http_method = HttpMethod.PUT
        update_job_family_request.uri = "/open-apis/contact/v3/job_families/:job_family_id"
        update_job_family_request.token_types = {AccessTokenType.TENANT}
        self._update_job_family_request: UpdateJobFamilyRequest = update_job_family_request

    def job_family_id(self, job_family_id: str) -> "UpdateJobFamilyRequestBuilder":
        self._update_job_family_request.job_family_id = job_family_id
        self._update_job_family_request.paths["job_family_id"] = str(job_family_id)
        return self

    def request_body(self, request_body: JobFamily) -> "UpdateJobFamilyRequestBuilder":
        self._update_job_family_request.request_body = request_body
        self._update_job_family_request.body = request_body
        return self

    def build(self) -> UpdateJobFamilyRequest:
        return self._update_job_family_request
