# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .patch_application_contacts_range_request_body import PatchApplicationContactsRangeRequestBody


class PatchApplicationContactsRangeRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.app_id: Optional[str] = None
        self.request_body: Optional[PatchApplicationContactsRangeRequestBody] = None

    @staticmethod
    def builder() -> "PatchApplicationContactsRangeRequestBuilder":
        return PatchApplicationContactsRangeRequestBuilder()


class PatchApplicationContactsRangeRequestBuilder(object):

    def __init__(self) -> None:
        patch_application_contacts_range_request = PatchApplicationContactsRangeRequest()
        patch_application_contacts_range_request.http_method = HttpMethod.PATCH
        patch_application_contacts_range_request.uri = "/open-apis/application/v6/applications/:app_id/contacts_range"
        patch_application_contacts_range_request.token_types = {AccessTokenType.TENANT}
        self._patch_application_contacts_range_request: PatchApplicationContactsRangeRequest = patch_application_contacts_range_request

    def user_id_type(self, user_id_type: str) -> "PatchApplicationContactsRangeRequestBuilder":
        self._patch_application_contacts_range_request.user_id_type = user_id_type
        self._patch_application_contacts_range_request.add_query("user_id_type", user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "PatchApplicationContactsRangeRequestBuilder":
        self._patch_application_contacts_range_request.department_id_type = department_id_type
        self._patch_application_contacts_range_request.add_query("department_id_type", department_id_type)
        return self

    def app_id(self, app_id: str) -> "PatchApplicationContactsRangeRequestBuilder":
        self._patch_application_contacts_range_request.app_id = app_id
        self._patch_application_contacts_range_request.paths["app_id"] = str(app_id)
        return self

    def request_body(self,
                     request_body: PatchApplicationContactsRangeRequestBody) -> "PatchApplicationContactsRangeRequestBuilder":
        self._patch_application_contacts_range_request.request_body = request_body
        self._patch_application_contacts_range_request.body = request_body
        return self

    def build(self) -> PatchApplicationContactsRangeRequest:
        return self._patch_application_contacts_range_request
