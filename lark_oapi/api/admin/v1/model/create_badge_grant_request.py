# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .grant import Grant


class CreateBadgeGrantRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.badge_id: Optional[str] = None
        self.request_body: Optional[Grant] = None

    @staticmethod
    def builder() -> "CreateBadgeGrantRequestBuilder":
        return CreateBadgeGrantRequestBuilder()


class CreateBadgeGrantRequestBuilder(object):

    def __init__(self) -> None:
        create_badge_grant_request = CreateBadgeGrantRequest()
        create_badge_grant_request.http_method = HttpMethod.POST
        create_badge_grant_request.uri = "/open-apis/admin/v1/badges/:badge_id/grants"
        create_badge_grant_request.token_types = {AccessTokenType.TENANT}
        self._create_badge_grant_request: CreateBadgeGrantRequest = create_badge_grant_request

    def user_id_type(self, user_id_type: str) -> "CreateBadgeGrantRequestBuilder":
        self._create_badge_grant_request.user_id_type = user_id_type
        self._create_badge_grant_request.add_query("user_id_type", user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "CreateBadgeGrantRequestBuilder":
        self._create_badge_grant_request.department_id_type = department_id_type
        self._create_badge_grant_request.add_query("department_id_type", department_id_type)
        return self

    def badge_id(self, badge_id: str) -> "CreateBadgeGrantRequestBuilder":
        self._create_badge_grant_request.badge_id = badge_id
        self._create_badge_grant_request.paths["badge_id"] = str(badge_id)
        return self

    def request_body(self, request_body: Grant) -> "CreateBadgeGrantRequestBuilder":
        self._create_badge_grant_request.request_body = request_body
        self._create_badge_grant_request.body = request_body
        return self

    def build(self) -> CreateBadgeGrantRequest:
        return self._create_badge_grant_request
