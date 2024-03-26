# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class CreatePublicMailboxMemberResponseBody(object):
    _types = {
        "member_id": str,
        "user_id": str,
        "type": str,
    }

    def __init__(self, d=None):
        self.member_id: Optional[str] = None
        self.user_id: Optional[str] = None
        self.type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreatePublicMailboxMemberResponseBodyBuilder":
        return CreatePublicMailboxMemberResponseBodyBuilder()


class CreatePublicMailboxMemberResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_public_mailbox_member_response_body = CreatePublicMailboxMemberResponseBody()

    def member_id(self, member_id: str) -> "CreatePublicMailboxMemberResponseBodyBuilder":
        self._create_public_mailbox_member_response_body.member_id = member_id
        return self

    def user_id(self, user_id: str) -> "CreatePublicMailboxMemberResponseBodyBuilder":
        self._create_public_mailbox_member_response_body.user_id = user_id
        return self

    def type(self, type: str) -> "CreatePublicMailboxMemberResponseBodyBuilder":
        self._create_public_mailbox_member_response_body.type = type
        return self

    def build(self) -> "CreatePublicMailboxMemberResponseBody":
        return self._create_public_mailbox_member_response_body
