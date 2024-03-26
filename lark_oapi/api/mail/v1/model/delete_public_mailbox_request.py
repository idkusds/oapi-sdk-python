# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class DeletePublicMailboxRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.public_mailbox_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeletePublicMailboxRequestBuilder":
        return DeletePublicMailboxRequestBuilder()


class DeletePublicMailboxRequestBuilder(object):

    def __init__(self) -> None:
        delete_public_mailbox_request = DeletePublicMailboxRequest()
        delete_public_mailbox_request.http_method = HttpMethod.DELETE
        delete_public_mailbox_request.uri = "/open-apis/mail/v1/public_mailboxes/:public_mailbox_id"
        delete_public_mailbox_request.token_types = {AccessTokenType.TENANT}
        self._delete_public_mailbox_request: DeletePublicMailboxRequest = delete_public_mailbox_request

    def public_mailbox_id(self, public_mailbox_id: str) -> "DeletePublicMailboxRequestBuilder":
        self._delete_public_mailbox_request.public_mailbox_id = public_mailbox_id
        self._delete_public_mailbox_request.paths["public_mailbox_id"] = str(public_mailbox_id)
        return self

    def build(self) -> DeletePublicMailboxRequest:
        return self._delete_public_mailbox_request
