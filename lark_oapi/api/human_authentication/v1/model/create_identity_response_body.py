# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class CreateIdentityResponseBody(object):
    _types = {
        "verify_uid": str,
    }

    def __init__(self, d=None):
        self.verify_uid: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateIdentityResponseBodyBuilder":
        return CreateIdentityResponseBodyBuilder()


class CreateIdentityResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_identity_response_body = CreateIdentityResponseBody()

    def verify_uid(self, verify_uid: str) -> "CreateIdentityResponseBodyBuilder":
        self._create_identity_response_body.verify_uid = verify_uid
        return self

    def build(self) -> "CreateIdentityResponseBody":
        return self._create_identity_response_body
