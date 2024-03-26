# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class AppVisibleList(object):
    _types = {
        "open_ids": List[int],
        "department_ids": List[int],
        "group_ids": List[str],
    }

    def __init__(self, d=None):
        self.open_ids: Optional[List[int]] = None
        self.department_ids: Optional[List[int]] = None
        self.group_ids: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppVisibleListBuilder":
        return AppVisibleListBuilder()


class AppVisibleListBuilder(object):
    def __init__(self) -> None:
        self._app_visible_list = AppVisibleList()

    def open_ids(self, open_ids: List[int]) -> "AppVisibleListBuilder":
        self._app_visible_list.open_ids = open_ids
        return self

    def department_ids(self, department_ids: List[int]) -> "AppVisibleListBuilder":
        self._app_visible_list.department_ids = department_ids
        return self

    def group_ids(self, group_ids: List[str]) -> "AppVisibleListBuilder":
        self._app_visible_list.group_ids = group_ids
        return self

    def build(self) -> "AppVisibleList":
        return self._app_visible_list
