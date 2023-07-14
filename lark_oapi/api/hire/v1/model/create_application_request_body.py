# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class CreateApplicationRequestBody(object):
    _types = {
        "talent_id": str,
        "job_id": str,
        "resume_source_id": str,
        "application_preferred_city_code_list": List[str],
    }

    def __init__(self, d):
        self.talent_id: Optional[str] = None
        self.job_id: Optional[str] = None
        self.resume_source_id: Optional[str] = None
        self.application_preferred_city_code_list: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateApplicationRequestBodyBuilder":
        return CreateApplicationRequestBodyBuilder()


class CreateApplicationRequestBodyBuilder(object):
    def __init__(self, create_application_request_body: CreateApplicationRequestBody = CreateApplicationRequestBody({})) -> None:
        self._create_application_request_body: CreateApplicationRequestBody = create_application_request_body
    
    def talent_id(self, talent_id: str) -> "CreateApplicationRequestBodyBuilder":
        self._create_application_request_body.talent_id = talent_id
        return self
    
    def job_id(self, job_id: str) -> "CreateApplicationRequestBodyBuilder":
        self._create_application_request_body.job_id = job_id
        return self
    
    def resume_source_id(self, resume_source_id: str) -> "CreateApplicationRequestBodyBuilder":
        self._create_application_request_body.resume_source_id = resume_source_id
        return self
    
    def application_preferred_city_code_list(self, application_preferred_city_code_list: List[str]) -> "CreateApplicationRequestBodyBuilder":
        self._create_application_request_body.application_preferred_city_code_list = application_preferred_city_code_list
        return self
    
    def build(self) -> "CreateApplicationRequestBody":
        return self._create_application_request_body