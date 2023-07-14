# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .shift import Shift


class CreateShiftRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[Shift] = None

    @staticmethod
    def builder() -> "CreateShiftRequestBuilder":
        return CreateShiftRequestBuilder()


class CreateShiftRequestBuilder(object):

    def __init__(self, create_shift_request: CreateShiftRequest = CreateShiftRequest()) -> None:
        create_shift_request.http_method = HttpMethod.POST
        create_shift_request.uri = "/open-apis/attendance/v1/shifts"
        create_shift_request.token_types = {AccessTokenType.TENANT}
        self._create_shift_request: CreateShiftRequest = create_shift_request
    
    def request_body(self, request_body: Shift) -> "CreateShiftRequestBuilder":
        self._create_shift_request.request_body = request_body
        self._create_shift_request.body = request_body
        return self

    def build(self) -> CreateShiftRequest:
        return self._create_shift_request