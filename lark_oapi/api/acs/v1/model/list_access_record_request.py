# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListAccessRecordRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.from_: Optional[int] = None
        self.to: Optional[int] = None
        self.device_id: Optional[int] = None
        self.user_id_type: Optional[str] = None

    @staticmethod
    def builder() -> "ListAccessRecordRequestBuilder":
        return ListAccessRecordRequestBuilder()


class ListAccessRecordRequestBuilder(object):

    def __init__(self) -> None:
        list_access_record_request = ListAccessRecordRequest()
        list_access_record_request.http_method = HttpMethod.GET
        list_access_record_request.uri = "/open-apis/acs/v1/access_records"
        list_access_record_request.token_types = {AccessTokenType.TENANT}
        self._list_access_record_request: ListAccessRecordRequest = list_access_record_request

    def page_size(self, page_size: int) -> "ListAccessRecordRequestBuilder":
        self._list_access_record_request.page_size = page_size
        self._list_access_record_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListAccessRecordRequestBuilder":
        self._list_access_record_request.page_token = page_token
        self._list_access_record_request.add_query("page_token", page_token)
        return self

    def from_(self, from_: int) -> "ListAccessRecordRequestBuilder":
        self._list_access_record_request.from_ = from_
        self._list_access_record_request.add_query("from_", from_)
        return self

    def to(self, to: int) -> "ListAccessRecordRequestBuilder":
        self._list_access_record_request.to = to
        self._list_access_record_request.add_query("to", to)
        return self

    def device_id(self, device_id: int) -> "ListAccessRecordRequestBuilder":
        self._list_access_record_request.device_id = device_id
        self._list_access_record_request.add_query("device_id", device_id)
        return self

    def user_id_type(self, user_id_type: str) -> "ListAccessRecordRequestBuilder":
        self._list_access_record_request.user_id_type = user_id_type
        self._list_access_record_request.add_query("user_id_type", user_id_type)
        return self

    def build(self) -> ListAccessRecordRequest:
        return self._list_access_record_request
