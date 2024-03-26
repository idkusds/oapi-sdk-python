# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .admin_dept_stat import AdminDeptStat


class ListAdminDeptStatResponseBody(object):
    _types = {
        "has_more": bool,
        "page_token": str,
        "items": List[AdminDeptStat],
    }

    def __init__(self, d=None):
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        self.items: Optional[List[AdminDeptStat]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListAdminDeptStatResponseBodyBuilder":
        return ListAdminDeptStatResponseBodyBuilder()


class ListAdminDeptStatResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_admin_dept_stat_response_body = ListAdminDeptStatResponseBody()

    def has_more(self, has_more: bool) -> "ListAdminDeptStatResponseBodyBuilder":
        self._list_admin_dept_stat_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListAdminDeptStatResponseBodyBuilder":
        self._list_admin_dept_stat_response_body.page_token = page_token
        return self

    def items(self, items: List[AdminDeptStat]) -> "ListAdminDeptStatResponseBodyBuilder":
        self._list_admin_dept_stat_response_body.items = items
        return self

    def build(self) -> "ListAdminDeptStatResponseBody":
        return self._list_admin_dept_stat_response_body
