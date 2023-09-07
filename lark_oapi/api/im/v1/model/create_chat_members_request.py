# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .create_chat_members_request_body import CreateChatMembersRequestBody


class CreateChatMembersRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.member_id_type: Optional[str] = None
        self.succeed_type: Optional[int] = None
        self.chat_id: Optional[str] = None
        self.request_body: Optional[CreateChatMembersRequestBody] = None

    @staticmethod
    def builder() -> "CreateChatMembersRequestBuilder":
        return CreateChatMembersRequestBuilder()


class CreateChatMembersRequestBuilder(object):

    def __init__(self) -> None:
        create_chat_members_request = CreateChatMembersRequest()
        create_chat_members_request.http_method = HttpMethod.POST
        create_chat_members_request.uri = "/open-apis/im/v1/chats/:chat_id/members"
        create_chat_members_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._create_chat_members_request: CreateChatMembersRequest = create_chat_members_request

    def member_id_type(self, member_id_type: str) -> "CreateChatMembersRequestBuilder":
        self._create_chat_members_request.member_id_type = member_id_type
        self._create_chat_members_request.add_query("member_id_type", member_id_type)
        return self

    def succeed_type(self, succeed_type: int) -> "CreateChatMembersRequestBuilder":
        self._create_chat_members_request.succeed_type = succeed_type
        self._create_chat_members_request.add_query("succeed_type", succeed_type)
        return self

    def chat_id(self, chat_id: str) -> "CreateChatMembersRequestBuilder":
        self._create_chat_members_request.chat_id = chat_id
        self._create_chat_members_request.paths["chat_id"] = str(chat_id)
        return self

    def request_body(self, request_body: CreateChatMembersRequestBody) -> "CreateChatMembersRequestBuilder":
        self._create_chat_members_request.request_body = request_body
        self._create_chat_members_request.body = request_body
        return self

    def build(self) -> CreateChatMembersRequest:
        return self._create_chat_members_request
