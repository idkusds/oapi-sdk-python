# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .member import Member


class CreateSpaceMemberRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.need_notification: Optional[bool] = None
        self.space_id: Optional[str] = None
        self.request_body: Optional[Member] = None

    @staticmethod
    def builder() -> "CreateSpaceMemberRequestBuilder":
        return CreateSpaceMemberRequestBuilder()


class CreateSpaceMemberRequestBuilder(object):

    def __init__(self) -> None:
        create_space_member_request = CreateSpaceMemberRequest()
        create_space_member_request.http_method = HttpMethod.POST
        create_space_member_request.uri = "/open-apis/wiki/v2/spaces/:space_id/members"
        create_space_member_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._create_space_member_request: CreateSpaceMemberRequest = create_space_member_request

    def need_notification(self, need_notification: bool) -> "CreateSpaceMemberRequestBuilder":
        self._create_space_member_request.need_notification = need_notification
        self._create_space_member_request.add_query("need_notification", need_notification)
        return self

    def space_id(self, space_id: str) -> "CreateSpaceMemberRequestBuilder":
        self._create_space_member_request.space_id = space_id
        self._create_space_member_request.paths["space_id"] = str(space_id)
        return self

    def request_body(self, request_body: Member) -> "CreateSpaceMemberRequestBuilder":
        self._create_space_member_request.request_body = request_body
        self._create_space_member_request.body = request_body
        return self

    def build(self) -> CreateSpaceMemberRequest:
        return self._create_space_member_request
