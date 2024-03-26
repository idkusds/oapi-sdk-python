# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class AppContactsRangeIdList(object):
    _types = {
        "user_ids": List[str],
        "department_ids": List[str],
        "group_ids": List[str],
    }

    def __init__(self, d=None):
        self.user_ids: Optional[List[str]] = None
        self.department_ids: Optional[List[str]] = None
        self.group_ids: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppContactsRangeIdListBuilder":
        return AppContactsRangeIdListBuilder()


class AppContactsRangeIdListBuilder(object):
    def __init__(self) -> None:
        self._app_contacts_range_id_list = AppContactsRangeIdList()

    def user_ids(self, user_ids: List[str]) -> "AppContactsRangeIdListBuilder":
        self._app_contacts_range_id_list.user_ids = user_ids
        return self

    def department_ids(self, department_ids: List[str]) -> "AppContactsRangeIdListBuilder":
        self._app_contacts_range_id_list.department_ids = department_ids
        return self

    def group_ids(self, group_ids: List[str]) -> "AppContactsRangeIdListBuilder":
        self._app_contacts_range_id_list.group_ids = group_ids
        return self

    def build(self) -> "AppContactsRangeIdList":
        return self._app_contacts_range_id_list
