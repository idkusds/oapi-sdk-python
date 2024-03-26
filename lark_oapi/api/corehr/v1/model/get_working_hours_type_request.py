# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class GetWorkingHoursTypeRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.working_hours_type_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetWorkingHoursTypeRequestBuilder":
        return GetWorkingHoursTypeRequestBuilder()


class GetWorkingHoursTypeRequestBuilder(object):

    def __init__(self) -> None:
        get_working_hours_type_request = GetWorkingHoursTypeRequest()
        get_working_hours_type_request.http_method = HttpMethod.GET
        get_working_hours_type_request.uri = "/open-apis/corehr/v1/working_hours_types/:working_hours_type_id"
        get_working_hours_type_request.token_types = {AccessTokenType.TENANT}
        self._get_working_hours_type_request: GetWorkingHoursTypeRequest = get_working_hours_type_request

    def working_hours_type_id(self, working_hours_type_id: str) -> "GetWorkingHoursTypeRequestBuilder":
        self._get_working_hours_type_request.working_hours_type_id = working_hours_type_id
        self._get_working_hours_type_request.paths["working_hours_type_id"] = str(working_hours_type_id)
        return self

    def build(self) -> GetWorkingHoursTypeRequest:
        return self._get_working_hours_type_request
