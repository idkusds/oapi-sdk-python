# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .job_family import JobFamily


class PatchJobFamilyRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.client_token: Optional[str] = None
        self.job_family_id: Optional[str] = None
        self.request_body: Optional[JobFamily] = None

    @staticmethod
    def builder() -> "PatchJobFamilyRequestBuilder":
        return PatchJobFamilyRequestBuilder()


class PatchJobFamilyRequestBuilder(object):

    def __init__(self) -> None:
        patch_job_family_request = PatchJobFamilyRequest()
        patch_job_family_request.http_method = HttpMethod.PATCH
        patch_job_family_request.uri = "/open-apis/corehr/v1/job_families/:job_family_id"
        patch_job_family_request.token_types = {AccessTokenType.TENANT}
        self._patch_job_family_request: PatchJobFamilyRequest = patch_job_family_request

    def client_token(self, client_token: str) -> "PatchJobFamilyRequestBuilder":
        self._patch_job_family_request.client_token = client_token
        self._patch_job_family_request.add_query("client_token", client_token)
        return self

    def job_family_id(self, job_family_id: str) -> "PatchJobFamilyRequestBuilder":
        self._patch_job_family_request.job_family_id = job_family_id
        self._patch_job_family_request.paths["job_family_id"] = str(job_family_id)
        return self

    def request_body(self, request_body: JobFamily) -> "PatchJobFamilyRequestBuilder":
        self._patch_job_family_request.request_body = request_body
        self._patch_job_family_request.body = request_body
        return self

    def build(self) -> PatchJobFamilyRequest:
        return self._patch_job_family_request
