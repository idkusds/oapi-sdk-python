# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .modify_user_setting_request_body import ModifyUserSettingRequestBody


class ModifyUserSettingRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.employee_type: Optional[str] = None
        self.request_body: Optional[ModifyUserSettingRequestBody] = None

    @staticmethod
    def builder() -> "ModifyUserSettingRequestBuilder":
        return ModifyUserSettingRequestBuilder()


class ModifyUserSettingRequestBuilder(object):

    def __init__(self) -> None:
        modify_user_setting_request = ModifyUserSettingRequest()
        modify_user_setting_request.http_method = HttpMethod.POST
        modify_user_setting_request.uri = "/open-apis/attendance/v1/user_settings/modify"
        modify_user_setting_request.token_types = {AccessTokenType.TENANT}
        self._modify_user_setting_request: ModifyUserSettingRequest = modify_user_setting_request

    def employee_type(self, employee_type: str) -> "ModifyUserSettingRequestBuilder":
        self._modify_user_setting_request.employee_type = employee_type
        self._modify_user_setting_request.add_query("employee_type", employee_type)
        return self

    def request_body(self, request_body: ModifyUserSettingRequestBody) -> "ModifyUserSettingRequestBuilder":
        self._modify_user_setting_request.request_body = request_body
        self._modify_user_setting_request.body = request_body
        return self

    def build(self) -> ModifyUserSettingRequest:
        return self._modify_user_setting_request
