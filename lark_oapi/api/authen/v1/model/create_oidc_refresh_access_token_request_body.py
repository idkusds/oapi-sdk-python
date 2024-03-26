# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class CreateOidcRefreshAccessTokenRequestBody(object):
    _types = {
        "grant_type": str,
        "refresh_token": str,
    }

    def __init__(self, d=None):
        self.grant_type: Optional[str] = None
        self.refresh_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateOidcRefreshAccessTokenRequestBodyBuilder":
        return CreateOidcRefreshAccessTokenRequestBodyBuilder()


class CreateOidcRefreshAccessTokenRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._create_oidc_refresh_access_token_request_body = CreateOidcRefreshAccessTokenRequestBody()

    def grant_type(self, grant_type: str) -> "CreateOidcRefreshAccessTokenRequestBodyBuilder":
        self._create_oidc_refresh_access_token_request_body.grant_type = grant_type
        return self

    def refresh_token(self, refresh_token: str) -> "CreateOidcRefreshAccessTokenRequestBodyBuilder":
        self._create_oidc_refresh_access_token_request_body.refresh_token = refresh_token
        return self

    def build(self) -> "CreateOidcRefreshAccessTokenRequestBody":
        return self._create_oidc_refresh_access_token_request_body
