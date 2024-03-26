# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListTasklistRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.user_id_type: Optional[str] = None

    @staticmethod
    def builder() -> "ListTasklistRequestBuilder":
        return ListTasklistRequestBuilder()


class ListTasklistRequestBuilder(object):

    def __init__(self) -> None:
        list_tasklist_request = ListTasklistRequest()
        list_tasklist_request.http_method = HttpMethod.GET
        list_tasklist_request.uri = "/open-apis/task/v2/tasklists"
        list_tasklist_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._list_tasklist_request: ListTasklistRequest = list_tasklist_request

    def page_size(self, page_size: int) -> "ListTasklistRequestBuilder":
        self._list_tasklist_request.page_size = page_size
        self._list_tasklist_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListTasklistRequestBuilder":
        self._list_tasklist_request.page_token = page_token
        self._list_tasklist_request.add_query("page_token", page_token)
        return self

    def user_id_type(self, user_id_type: str) -> "ListTasklistRequestBuilder":
        self._list_tasklist_request.user_id_type = user_id_type
        self._list_tasklist_request.add_query("user_id_type", user_id_type)
        return self

    def build(self) -> ListTasklistRequest:
        return self._list_tasklist_request
