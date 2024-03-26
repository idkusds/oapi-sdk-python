# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .patch_message_request_body import PatchMessageRequestBody


class PatchMessageRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.message_id: Optional[str] = None
        self.request_body: Optional[PatchMessageRequestBody] = None

    @staticmethod
    def builder() -> "PatchMessageRequestBuilder":
        return PatchMessageRequestBuilder()


class PatchMessageRequestBuilder(object):

    def __init__(self) -> None:
        patch_message_request = PatchMessageRequest()
        patch_message_request.http_method = HttpMethod.PATCH
        patch_message_request.uri = "/open-apis/im/v1/messages/:message_id"
        patch_message_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._patch_message_request: PatchMessageRequest = patch_message_request

    def message_id(self, message_id: str) -> "PatchMessageRequestBuilder":
        self._patch_message_request.message_id = message_id
        self._patch_message_request.paths["message_id"] = str(message_id)
        return self

    def request_body(self, request_body: PatchMessageRequestBody) -> "PatchMessageRequestBuilder":
        self._patch_message_request.request_body = request_body
        self._patch_message_request.body = request_body
        return self

    def build(self) -> PatchMessageRequest:
        return self._patch_message_request
