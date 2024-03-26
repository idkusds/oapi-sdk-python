# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class GetPublicMailboxMemberRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.public_mailbox_id: Optional[str] = None
        self.member_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetPublicMailboxMemberRequestBuilder":
        return GetPublicMailboxMemberRequestBuilder()


class GetPublicMailboxMemberRequestBuilder(object):

    def __init__(self) -> None:
        get_public_mailbox_member_request = GetPublicMailboxMemberRequest()
        get_public_mailbox_member_request.http_method = HttpMethod.GET
        get_public_mailbox_member_request.uri = "/open-apis/mail/v1/public_mailboxes/:public_mailbox_id/members/:member_id"
        get_public_mailbox_member_request.token_types = {AccessTokenType.TENANT}
        self._get_public_mailbox_member_request: GetPublicMailboxMemberRequest = get_public_mailbox_member_request

    def user_id_type(self, user_id_type: str) -> "GetPublicMailboxMemberRequestBuilder":
        self._get_public_mailbox_member_request.user_id_type = user_id_type
        self._get_public_mailbox_member_request.add_query("user_id_type", user_id_type)
        return self

    def public_mailbox_id(self, public_mailbox_id: str) -> "GetPublicMailboxMemberRequestBuilder":
        self._get_public_mailbox_member_request.public_mailbox_id = public_mailbox_id
        self._get_public_mailbox_member_request.paths["public_mailbox_id"] = str(public_mailbox_id)
        return self

    def member_id(self, member_id: str) -> "GetPublicMailboxMemberRequestBuilder":
        self._get_public_mailbox_member_request.member_id = member_id
        self._get_public_mailbox_member_request.paths["member_id"] = str(member_id)
        return self

    def build(self) -> GetPublicMailboxMemberRequest:
        return self._get_public_mailbox_member_request
