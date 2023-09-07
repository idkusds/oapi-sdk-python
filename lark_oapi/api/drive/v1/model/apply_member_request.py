# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class ApplyMemberRequest(object):
    _types = {
        "perm": str,
        "remark": str,
    }

    def __init__(self, d=None):
        self.perm: Optional[str] = None
        self.remark: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApplyMemberRequestBuilder":
        return ApplyMemberRequestBuilder()


class ApplyMemberRequestBuilder(object):
    def __init__(self) -> None:
        self._apply_member_request = ApplyMemberRequest()

    def perm(self, perm: str) -> "ApplyMemberRequestBuilder":
        self._apply_member_request.perm = perm
        return self

    def remark(self, remark: str) -> "ApplyMemberRequestBuilder":
        self._apply_member_request.remark = remark
        return self

    def build(self) -> "ApplyMemberRequest":
        return self._apply_member_request
