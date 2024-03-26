# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .update_application_management_request_body import UpdateApplicationManagementRequestBody


class UpdateApplicationManagementRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.app_id: Optional[str] = None
        self.request_body: Optional[UpdateApplicationManagementRequestBody] = None

    @staticmethod
    def builder() -> "UpdateApplicationManagementRequestBuilder":
        return UpdateApplicationManagementRequestBuilder()


class UpdateApplicationManagementRequestBuilder(object):

    def __init__(self) -> None:
        update_application_management_request = UpdateApplicationManagementRequest()
        update_application_management_request.http_method = HttpMethod.PUT
        update_application_management_request.uri = "/open-apis/application/v6/applications/:app_id/management"
        update_application_management_request.token_types = {AccessTokenType.TENANT}
        self._update_application_management_request: UpdateApplicationManagementRequest = update_application_management_request

    def app_id(self, app_id: str) -> "UpdateApplicationManagementRequestBuilder":
        self._update_application_management_request.app_id = app_id
        self._update_application_management_request.paths["app_id"] = str(app_id)
        return self

    def request_body(self,
                     request_body: UpdateApplicationManagementRequestBody) -> "UpdateApplicationManagementRequestBuilder":
        self._update_application_management_request.request_body = request_body
        self._update_application_management_request.body = request_body
        return self

    def build(self) -> UpdateApplicationManagementRequest:
        return self._update_application_management_request
