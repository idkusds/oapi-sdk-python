# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .query_offboarding_request_body import QueryOffboardingRequestBody


class QueryOffboardingRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[QueryOffboardingRequestBody] = None

    @staticmethod
    def builder() -> "QueryOffboardingRequestBuilder":
        return QueryOffboardingRequestBuilder()


class QueryOffboardingRequestBuilder(object):

    def __init__(self) -> None:
        query_offboarding_request = QueryOffboardingRequest()
        query_offboarding_request.http_method = HttpMethod.POST
        query_offboarding_request.uri = "/open-apis/corehr/v1/offboardings/query"
        query_offboarding_request.token_types = {AccessTokenType.TENANT}
        self._query_offboarding_request: QueryOffboardingRequest = query_offboarding_request

    def request_body(self, request_body: QueryOffboardingRequestBody) -> "QueryOffboardingRequestBuilder":
        self._query_offboarding_request.request_body = request_body
        self._query_offboarding_request.body = request_body
        return self

    def build(self) -> QueryOffboardingRequest:
        return self._query_offboarding_request
