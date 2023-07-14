# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .external_interview import ExternalInterview


class CreateExternalInterviewRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[ExternalInterview] = None

    @staticmethod
    def builder() -> "CreateExternalInterviewRequestBuilder":
        return CreateExternalInterviewRequestBuilder()


class CreateExternalInterviewRequestBuilder(object):

    def __init__(self, create_external_interview_request: CreateExternalInterviewRequest = CreateExternalInterviewRequest()) -> None:
        create_external_interview_request.http_method = HttpMethod.POST
        create_external_interview_request.uri = "/open-apis/hire/v1/external_interviews"
        create_external_interview_request.token_types = {AccessTokenType.TENANT}
        self._create_external_interview_request: CreateExternalInterviewRequest = create_external_interview_request
    
    def request_body(self, request_body: ExternalInterview) -> "CreateExternalInterviewRequestBuilder":
        self._create_external_interview_request.request_body = request_body
        self._create_external_interview_request.body = request_body
        return self

    def build(self) -> CreateExternalInterviewRequest:
        return self._create_external_interview_request