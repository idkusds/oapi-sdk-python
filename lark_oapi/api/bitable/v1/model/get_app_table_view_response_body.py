# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .app_table_view import AppTableView


class GetAppTableViewResponseBody(object):
    _types = {
        "view": AppTableView,
    }

    def __init__(self, d=None):
        self.view: Optional[AppTableView] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetAppTableViewResponseBodyBuilder":
        return GetAppTableViewResponseBodyBuilder()


class GetAppTableViewResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_app_table_view_response_body = GetAppTableViewResponseBody()

    def view(self, view: AppTableView) -> "GetAppTableViewResponseBodyBuilder":
        self._get_app_table_view_response_body.view = view
        return self

    def build(self) -> "GetAppTableViewResponseBody":
        return self._get_app_table_view_response_body
