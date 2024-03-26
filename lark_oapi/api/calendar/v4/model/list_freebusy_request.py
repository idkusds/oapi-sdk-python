# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .list_freebusy_request_body import ListFreebusyRequestBody


class ListFreebusyRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[ListFreebusyRequestBody] = None

    @staticmethod
    def builder() -> "ListFreebusyRequestBuilder":
        return ListFreebusyRequestBuilder()


class ListFreebusyRequestBuilder(object):

    def __init__(self) -> None:
        list_freebusy_request = ListFreebusyRequest()
        list_freebusy_request.http_method = HttpMethod.POST
        list_freebusy_request.uri = "/open-apis/calendar/v4/freebusy/list"
        list_freebusy_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._list_freebusy_request: ListFreebusyRequest = list_freebusy_request

    def user_id_type(self, user_id_type: str) -> "ListFreebusyRequestBuilder":
        self._list_freebusy_request.user_id_type = user_id_type
        self._list_freebusy_request.add_query("user_id_type", user_id_type)
        return self

    def request_body(self, request_body: ListFreebusyRequestBody) -> "ListFreebusyRequestBuilder":
        self._list_freebusy_request.request_body = request_body
        self._list_freebusy_request.body = request_body
        return self

    def build(self) -> ListFreebusyRequest:
        return self._list_freebusy_request
