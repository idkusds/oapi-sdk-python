# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class GetNotificationRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.notification_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetNotificationRequestBuilder":
        return GetNotificationRequestBuilder()


class GetNotificationRequestBuilder(object):

    def __init__(self) -> None:
        get_notification_request = GetNotificationRequest()
        get_notification_request.http_method = HttpMethod.GET
        get_notification_request.uri = "/open-apis/helpdesk/v1/notifications/:notification_id"
        get_notification_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._get_notification_request: GetNotificationRequest = get_notification_request

    def user_id_type(self, user_id_type: str) -> "GetNotificationRequestBuilder":
        self._get_notification_request.user_id_type = user_id_type
        self._get_notification_request.add_query("user_id_type", user_id_type)
        return self

    def notification_id(self, notification_id: str) -> "GetNotificationRequestBuilder":
        self._get_notification_request.notification_id = notification_id
        self._get_notification_request.paths["notification_id"] = str(notification_id)
        return self

    def build(self) -> GetNotificationRequest:
        return self._get_notification_request
