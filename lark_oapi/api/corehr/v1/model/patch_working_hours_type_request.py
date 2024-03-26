# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .working_hours_type import WorkingHoursType


class PatchWorkingHoursTypeRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.client_token: Optional[str] = None
        self.working_hours_type_id: Optional[str] = None
        self.request_body: Optional[WorkingHoursType] = None

    @staticmethod
    def builder() -> "PatchWorkingHoursTypeRequestBuilder":
        return PatchWorkingHoursTypeRequestBuilder()


class PatchWorkingHoursTypeRequestBuilder(object):

    def __init__(self) -> None:
        patch_working_hours_type_request = PatchWorkingHoursTypeRequest()
        patch_working_hours_type_request.http_method = HttpMethod.PATCH
        patch_working_hours_type_request.uri = "/open-apis/corehr/v1/working_hours_types/:working_hours_type_id"
        patch_working_hours_type_request.token_types = {AccessTokenType.TENANT}
        self._patch_working_hours_type_request: PatchWorkingHoursTypeRequest = patch_working_hours_type_request

    def client_token(self, client_token: str) -> "PatchWorkingHoursTypeRequestBuilder":
        self._patch_working_hours_type_request.client_token = client_token
        self._patch_working_hours_type_request.add_query("client_token", client_token)
        return self

    def working_hours_type_id(self, working_hours_type_id: str) -> "PatchWorkingHoursTypeRequestBuilder":
        self._patch_working_hours_type_request.working_hours_type_id = working_hours_type_id
        self._patch_working_hours_type_request.paths["working_hours_type_id"] = str(working_hours_type_id)
        return self

    def request_body(self, request_body: WorkingHoursType) -> "PatchWorkingHoursTypeRequestBuilder":
        self._patch_working_hours_type_request.request_body = request_body
        self._patch_working_hours_type_request.body = request_body
        return self

    def build(self) -> PatchWorkingHoursTypeRequest:
        return self._patch_working_hours_type_request
