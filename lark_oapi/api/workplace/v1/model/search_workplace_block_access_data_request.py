# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class SearchWorkplaceBlockAccessDataRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.from_date: Optional[str] = None
        self.to_date: Optional[str] = None
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.block_id: Optional[str] = None

    @staticmethod
    def builder() -> "SearchWorkplaceBlockAccessDataRequestBuilder":
        return SearchWorkplaceBlockAccessDataRequestBuilder()


class SearchWorkplaceBlockAccessDataRequestBuilder(object):

    def __init__(self) -> None:
        search_workplace_block_access_data_request = SearchWorkplaceBlockAccessDataRequest()
        search_workplace_block_access_data_request.http_method = HttpMethod.POST
        search_workplace_block_access_data_request.uri = "/open-apis/workplace/v1/workplace_block_access_data/search"
        search_workplace_block_access_data_request.token_types = {AccessTokenType.TENANT}
        self._search_workplace_block_access_data_request: SearchWorkplaceBlockAccessDataRequest = search_workplace_block_access_data_request

    def from_date(self, from_date: str) -> "SearchWorkplaceBlockAccessDataRequestBuilder":
        self._search_workplace_block_access_data_request.from_date = from_date
        self._search_workplace_block_access_data_request.add_query("from_date", from_date)
        return self

    def to_date(self, to_date: str) -> "SearchWorkplaceBlockAccessDataRequestBuilder":
        self._search_workplace_block_access_data_request.to_date = to_date
        self._search_workplace_block_access_data_request.add_query("to_date", to_date)
        return self

    def page_size(self, page_size: int) -> "SearchWorkplaceBlockAccessDataRequestBuilder":
        self._search_workplace_block_access_data_request.page_size = page_size
        self._search_workplace_block_access_data_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "SearchWorkplaceBlockAccessDataRequestBuilder":
        self._search_workplace_block_access_data_request.page_token = page_token
        self._search_workplace_block_access_data_request.add_query("page_token", page_token)
        return self

    def block_id(self, block_id: str) -> "SearchWorkplaceBlockAccessDataRequestBuilder":
        self._search_workplace_block_access_data_request.block_id = block_id
        self._search_workplace_block_access_data_request.add_query("block_id", block_id)
        return self

    def build(self) -> SearchWorkplaceBlockAccessDataRequest:
        return self._search_workplace_block_access_data_request
