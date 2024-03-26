# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .urgent_receivers import UrgentReceivers


class UrgentAppMessageRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.message_id: Optional[str] = None
        self.request_body: Optional[UrgentReceivers] = None

    @staticmethod
    def builder() -> "UrgentAppMessageRequestBuilder":
        return UrgentAppMessageRequestBuilder()


class UrgentAppMessageRequestBuilder(object):

    def __init__(self) -> None:
        urgent_app_message_request = UrgentAppMessageRequest()
        urgent_app_message_request.http_method = HttpMethod.PATCH
        urgent_app_message_request.uri = "/open-apis/im/v1/messages/:message_id/urgent_app"
        urgent_app_message_request.token_types = {AccessTokenType.TENANT}
        self._urgent_app_message_request: UrgentAppMessageRequest = urgent_app_message_request

    def user_id_type(self, user_id_type: str) -> "UrgentAppMessageRequestBuilder":
        self._urgent_app_message_request.user_id_type = user_id_type
        self._urgent_app_message_request.add_query("user_id_type", user_id_type)
        return self

    def message_id(self, message_id: str) -> "UrgentAppMessageRequestBuilder":
        self._urgent_app_message_request.message_id = message_id
        self._urgent_app_message_request.paths["message_id"] = str(message_id)
        return self

    def request_body(self, request_body: UrgentReceivers) -> "UrgentAppMessageRequestBuilder":
        self._urgent_app_message_request.request_body = request_body
        self._urgent_app_message_request.body = request_body
        return self

    def build(self) -> UrgentAppMessageRequest:
        return self._urgent_app_message_request
