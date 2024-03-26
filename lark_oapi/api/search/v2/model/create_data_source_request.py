# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .data_source import DataSource


class CreateDataSourceRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[DataSource] = None

    @staticmethod
    def builder() -> "CreateDataSourceRequestBuilder":
        return CreateDataSourceRequestBuilder()


class CreateDataSourceRequestBuilder(object):

    def __init__(self) -> None:
        create_data_source_request = CreateDataSourceRequest()
        create_data_source_request.http_method = HttpMethod.POST
        create_data_source_request.uri = "/open-apis/search/v2/data_sources"
        create_data_source_request.token_types = {AccessTokenType.TENANT}
        self._create_data_source_request: CreateDataSourceRequest = create_data_source_request

    def request_body(self, request_body: DataSource) -> "CreateDataSourceRequestBuilder":
        self._create_data_source_request.request_body = request_body
        self._create_data_source_request.body = request_body
        return self

    def build(self) -> CreateDataSourceRequest:
        return self._create_data_source_request
