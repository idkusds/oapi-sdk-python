# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .grant import Grant


class GetBadgeGrantResponseBody(object):
    _types = {
        "grant": Grant,
    }

    def __init__(self, d=None):
        self.grant: Optional[Grant] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetBadgeGrantResponseBodyBuilder":
        return GetBadgeGrantResponseBodyBuilder()


class GetBadgeGrantResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_badge_grant_response_body = GetBadgeGrantResponseBody()

    def grant(self, grant: Grant) -> "GetBadgeGrantResponseBodyBuilder":
        self._get_badge_grant_response_body.grant = grant
        return self

    def build(self) -> "GetBadgeGrantResponseBody":
        return self._get_badge_grant_response_body
