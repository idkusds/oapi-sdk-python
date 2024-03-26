# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListFileRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.folder_token: Optional[str] = None
        self.order_by: Optional[str] = None
        self.direction: Optional[str] = None
        self.user_id_type: Optional[str] = None

    @staticmethod
    def builder() -> "ListFileRequestBuilder":
        return ListFileRequestBuilder()


class ListFileRequestBuilder(object):

    def __init__(self) -> None:
        list_file_request = ListFileRequest()
        list_file_request.http_method = HttpMethod.GET
        list_file_request.uri = "/open-apis/drive/v1/files"
        list_file_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._list_file_request: ListFileRequest = list_file_request

    def page_size(self, page_size: int) -> "ListFileRequestBuilder":
        self._list_file_request.page_size = page_size
        self._list_file_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListFileRequestBuilder":
        self._list_file_request.page_token = page_token
        self._list_file_request.add_query("page_token", page_token)
        return self

    def folder_token(self, folder_token: str) -> "ListFileRequestBuilder":
        self._list_file_request.folder_token = folder_token
        self._list_file_request.add_query("folder_token", folder_token)
        return self

    def order_by(self, order_by: str) -> "ListFileRequestBuilder":
        self._list_file_request.order_by = order_by
        self._list_file_request.add_query("order_by", order_by)
        return self

    def direction(self, direction: str) -> "ListFileRequestBuilder":
        self._list_file_request.direction = direction
        self._list_file_request.add_query("direction", direction)
        return self

    def user_id_type(self, user_id_type: str) -> "ListFileRequestBuilder":
        self._list_file_request.user_id_type = user_id_type
        self._list_file_request.add_query("user_id_type", user_id_type)
        return self

    def build(self) -> ListFileRequest:
        return self._list_file_request
