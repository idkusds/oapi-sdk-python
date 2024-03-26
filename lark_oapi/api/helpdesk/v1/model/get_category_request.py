# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class GetCategoryRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.id: Optional[str] = None

    @staticmethod
    def builder() -> "GetCategoryRequestBuilder":
        return GetCategoryRequestBuilder()


class GetCategoryRequestBuilder(object):

    def __init__(self) -> None:
        get_category_request = GetCategoryRequest()
        get_category_request.http_method = HttpMethod.GET
        get_category_request.uri = "/open-apis/helpdesk/v1/categories/:id"
        get_category_request.token_types = {AccessTokenType.TENANT}
        self._get_category_request: GetCategoryRequest = get_category_request

    def id(self, id: str) -> "GetCategoryRequestBuilder":
        self._get_category_request.id = id
        self._get_category_request.paths["id"] = str(id)
        return self

    def build(self) -> GetCategoryRequest:
        return self._get_category_request
