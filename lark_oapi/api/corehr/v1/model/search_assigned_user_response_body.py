# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .role_authorization import RoleAuthorization


class SearchAssignedUserResponseBody(object):
    _types = {
        "items": List[RoleAuthorization],
        "has_more": bool,
        "page_token": str,
    }

    def __init__(self, d):
        self.items: Optional[List[RoleAuthorization]] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchAssignedUserResponseBodyBuilder":
        return SearchAssignedUserResponseBodyBuilder()


class SearchAssignedUserResponseBodyBuilder(object):
    def __init__(self, search_assigned_user_response_body: SearchAssignedUserResponseBody = SearchAssignedUserResponseBody({})) -> None:
        self._search_assigned_user_response_body: SearchAssignedUserResponseBody = search_assigned_user_response_body
    
    def items(self, items: List[RoleAuthorization]) -> "SearchAssignedUserResponseBodyBuilder":
        self._search_assigned_user_response_body.items = items
        return self
    
    def has_more(self, has_more: bool) -> "SearchAssignedUserResponseBodyBuilder":
        self._search_assigned_user_response_body.has_more = has_more
        return self
    
    def page_token(self, page_token: str) -> "SearchAssignedUserResponseBodyBuilder":
        self._search_assigned_user_response_body.page_token = page_token
        return self
    
    def build(self) -> "SearchAssignedUserResponseBody":
        return self._search_assigned_user_response_body