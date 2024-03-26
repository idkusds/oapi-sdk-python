# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .batch_delete_public_mailbox_member_request_body import BatchDeletePublicMailboxMemberRequestBody


class BatchDeletePublicMailboxMemberRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.public_mailbox_id: Optional[str] = None
        self.request_body: Optional[BatchDeletePublicMailboxMemberRequestBody] = None

    @staticmethod
    def builder() -> "BatchDeletePublicMailboxMemberRequestBuilder":
        return BatchDeletePublicMailboxMemberRequestBuilder()


class BatchDeletePublicMailboxMemberRequestBuilder(object):

    def __init__(self) -> None:
        batch_delete_public_mailbox_member_request = BatchDeletePublicMailboxMemberRequest()
        batch_delete_public_mailbox_member_request.http_method = HttpMethod.DELETE
        batch_delete_public_mailbox_member_request.uri = "/open-apis/mail/v1/public_mailboxes/:public_mailbox_id/members/batch_delete"
        batch_delete_public_mailbox_member_request.token_types = {AccessTokenType.TENANT}
        self._batch_delete_public_mailbox_member_request: BatchDeletePublicMailboxMemberRequest = batch_delete_public_mailbox_member_request

    def public_mailbox_id(self, public_mailbox_id: str) -> "BatchDeletePublicMailboxMemberRequestBuilder":
        self._batch_delete_public_mailbox_member_request.public_mailbox_id = public_mailbox_id
        self._batch_delete_public_mailbox_member_request.paths["public_mailbox_id"] = str(public_mailbox_id)
        return self

    def request_body(self,
                     request_body: BatchDeletePublicMailboxMemberRequestBody) -> "BatchDeletePublicMailboxMemberRequestBuilder":
        self._batch_delete_public_mailbox_member_request.request_body = request_body
        self._batch_delete_public_mailbox_member_request.body = request_body
        return self

    def build(self) -> BatchDeletePublicMailboxMemberRequest:
        return self._batch_delete_public_mailbox_member_request
