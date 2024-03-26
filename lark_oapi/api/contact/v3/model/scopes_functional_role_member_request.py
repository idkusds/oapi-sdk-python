# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .scopes_functional_role_member_request_body import ScopesFunctionalRoleMemberRequestBody


class ScopesFunctionalRoleMemberRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.role_id: Optional[str] = None
        self.request_body: Optional[ScopesFunctionalRoleMemberRequestBody] = None

    @staticmethod
    def builder() -> "ScopesFunctionalRoleMemberRequestBuilder":
        return ScopesFunctionalRoleMemberRequestBuilder()


class ScopesFunctionalRoleMemberRequestBuilder(object):

    def __init__(self) -> None:
        scopes_functional_role_member_request = ScopesFunctionalRoleMemberRequest()
        scopes_functional_role_member_request.http_method = HttpMethod.PATCH
        scopes_functional_role_member_request.uri = "/open-apis/contact/v3/functional_roles/:role_id/members/scopes"
        scopes_functional_role_member_request.token_types = {AccessTokenType.TENANT}
        self._scopes_functional_role_member_request: ScopesFunctionalRoleMemberRequest = scopes_functional_role_member_request

    def user_id_type(self, user_id_type: str) -> "ScopesFunctionalRoleMemberRequestBuilder":
        self._scopes_functional_role_member_request.user_id_type = user_id_type
        self._scopes_functional_role_member_request.add_query("user_id_type", user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "ScopesFunctionalRoleMemberRequestBuilder":
        self._scopes_functional_role_member_request.department_id_type = department_id_type
        self._scopes_functional_role_member_request.add_query("department_id_type", department_id_type)
        return self

    def role_id(self, role_id: str) -> "ScopesFunctionalRoleMemberRequestBuilder":
        self._scopes_functional_role_member_request.role_id = role_id
        self._scopes_functional_role_member_request.paths["role_id"] = str(role_id)
        return self

    def request_body(self,
                     request_body: ScopesFunctionalRoleMemberRequestBody) -> "ScopesFunctionalRoleMemberRequestBuilder":
        self._scopes_functional_role_member_request.request_body = request_body
        self._scopes_functional_role_member_request.body = request_body
        return self

    def build(self) -> ScopesFunctionalRoleMemberRequest:
        return self._scopes_functional_role_member_request
