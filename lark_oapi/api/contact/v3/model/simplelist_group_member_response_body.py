# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .memberlist import Memberlist


class SimplelistGroupMemberResponseBody(object):
    _types = {
        "memberlist": List[Memberlist],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.memberlist: Optional[List[Memberlist]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SimplelistGroupMemberResponseBodyBuilder":
        return SimplelistGroupMemberResponseBodyBuilder()


class SimplelistGroupMemberResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._simplelist_group_member_response_body = SimplelistGroupMemberResponseBody()

    def memberlist(self, memberlist: List[Memberlist]) -> "SimplelistGroupMemberResponseBodyBuilder":
        self._simplelist_group_member_response_body.memberlist = memberlist
        return self

    def page_token(self, page_token: str) -> "SimplelistGroupMemberResponseBodyBuilder":
        self._simplelist_group_member_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "SimplelistGroupMemberResponseBodyBuilder":
        self._simplelist_group_member_response_body.has_more = has_more
        return self

    def build(self) -> "SimplelistGroupMemberResponseBody":
        return self._simplelist_group_member_response_body
