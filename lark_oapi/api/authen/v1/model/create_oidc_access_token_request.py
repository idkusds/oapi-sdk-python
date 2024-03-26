# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .create_oidc_access_token_request_body import CreateOidcAccessTokenRequestBody


class CreateOidcAccessTokenRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[CreateOidcAccessTokenRequestBody] = None

    @staticmethod
    def builder() -> "CreateOidcAccessTokenRequestBuilder":
        return CreateOidcAccessTokenRequestBuilder()


class CreateOidcAccessTokenRequestBuilder(object):

    def __init__(self) -> None:
        create_oidc_access_token_request = CreateOidcAccessTokenRequest()
        create_oidc_access_token_request.http_method = HttpMethod.POST
        create_oidc_access_token_request.uri = "/open-apis/authen/v1/oidc/access_token"
        create_oidc_access_token_request.token_types = {AccessTokenType.APP}
        self._create_oidc_access_token_request: CreateOidcAccessTokenRequest = create_oidc_access_token_request

    def request_body(self, request_body: CreateOidcAccessTokenRequestBody) -> "CreateOidcAccessTokenRequestBuilder":
        self._create_oidc_access_token_request.request_body = request_body
        self._create_oidc_access_token_request.body = request_body
        return self

    def build(self) -> CreateOidcAccessTokenRequest:
        return self._create_oidc_access_token_request
