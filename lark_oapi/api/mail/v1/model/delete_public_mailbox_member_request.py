# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class DeletePublicMailboxMemberRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.public_mailbox_id: Optional[str] = None
        self.member_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeletePublicMailboxMemberRequestBuilder":
        return DeletePublicMailboxMemberRequestBuilder()


class DeletePublicMailboxMemberRequestBuilder(object):

    def __init__(self) -> None:
        delete_public_mailbox_member_request = DeletePublicMailboxMemberRequest()
        delete_public_mailbox_member_request.http_method = HttpMethod.DELETE
        delete_public_mailbox_member_request.uri = "/open-apis/mail/v1/public_mailboxes/:public_mailbox_id/members/:member_id"
        delete_public_mailbox_member_request.token_types = {AccessTokenType.TENANT}
        self._delete_public_mailbox_member_request: DeletePublicMailboxMemberRequest = delete_public_mailbox_member_request

    def public_mailbox_id(self, public_mailbox_id: str) -> "DeletePublicMailboxMemberRequestBuilder":
        self._delete_public_mailbox_member_request.public_mailbox_id = public_mailbox_id
        self._delete_public_mailbox_member_request.paths["public_mailbox_id"] = str(public_mailbox_id)
        return self

    def member_id(self, member_id: str) -> "DeletePublicMailboxMemberRequestBuilder":
        self._delete_public_mailbox_member_request.member_id = member_id
        self._delete_public_mailbox_member_request.paths["member_id"] = str(member_id)
        return self

    def build(self) -> DeletePublicMailboxMemberRequest:
        return self._delete_public_mailbox_member_request
