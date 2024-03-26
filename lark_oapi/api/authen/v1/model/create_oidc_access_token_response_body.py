# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class CreateOidcAccessTokenResponseBody(object):
    _types = {
        "access_token": str,
        "refresh_token": str,
        "token_type": str,
        "expires_in": int,
        "refresh_expires_in": int,
        "scope": str,
    }

    def __init__(self, d=None):
        self.access_token: Optional[str] = None
        self.refresh_token: Optional[str] = None
        self.token_type: Optional[str] = None
        self.expires_in: Optional[int] = None
        self.refresh_expires_in: Optional[int] = None
        self.scope: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateOidcAccessTokenResponseBodyBuilder":
        return CreateOidcAccessTokenResponseBodyBuilder()


class CreateOidcAccessTokenResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_oidc_access_token_response_body = CreateOidcAccessTokenResponseBody()

    def access_token(self, access_token: str) -> "CreateOidcAccessTokenResponseBodyBuilder":
        self._create_oidc_access_token_response_body.access_token = access_token
        return self

    def refresh_token(self, refresh_token: str) -> "CreateOidcAccessTokenResponseBodyBuilder":
        self._create_oidc_access_token_response_body.refresh_token = refresh_token
        return self

    def token_type(self, token_type: str) -> "CreateOidcAccessTokenResponseBodyBuilder":
        self._create_oidc_access_token_response_body.token_type = token_type
        return self

    def expires_in(self, expires_in: int) -> "CreateOidcAccessTokenResponseBodyBuilder":
        self._create_oidc_access_token_response_body.expires_in = expires_in
        return self

    def refresh_expires_in(self, refresh_expires_in: int) -> "CreateOidcAccessTokenResponseBodyBuilder":
        self._create_oidc_access_token_response_body.refresh_expires_in = refresh_expires_in
        return self

    def scope(self, scope: str) -> "CreateOidcAccessTokenResponseBodyBuilder":
        self._create_oidc_access_token_response_body.scope = scope
        return self

    def build(self) -> "CreateOidcAccessTokenResponseBody":
        return self._create_oidc_access_token_response_body
