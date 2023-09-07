# Code generated by Lark OpenAPI.

from typing import Optional, Dict

from lark_oapi.core.construct import init
from .app_role_table_role_rec_rule import AppRoleTableRoleRecRule


class AppRoleTableRole(object):
    _types = {
        "table_perm": int,
        "table_name": str,
        "table_id": str,
        "rec_rule": AppRoleTableRoleRecRule,
        "field_perm": Dict[str, int],
        "allow_add_record": bool,
        "allow_delete_record": bool,
    }

    def __init__(self, d=None):
        self.table_perm: Optional[int] = None
        self.table_name: Optional[str] = None
        self.table_id: Optional[str] = None
        self.rec_rule: Optional[AppRoleTableRoleRecRule] = None
        self.field_perm: Optional[Dict[str, int]] = None
        self.allow_add_record: Optional[bool] = None
        self.allow_delete_record: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppRoleTableRoleBuilder":
        return AppRoleTableRoleBuilder()


class AppRoleTableRoleBuilder(object):
    def __init__(self) -> None:
        self._app_role_table_role = AppRoleTableRole()

    def table_perm(self, table_perm: int) -> "AppRoleTableRoleBuilder":
        self._app_role_table_role.table_perm = table_perm
        return self

    def table_name(self, table_name: str) -> "AppRoleTableRoleBuilder":
        self._app_role_table_role.table_name = table_name
        return self

    def table_id(self, table_id: str) -> "AppRoleTableRoleBuilder":
        self._app_role_table_role.table_id = table_id
        return self

    def rec_rule(self, rec_rule: AppRoleTableRoleRecRule) -> "AppRoleTableRoleBuilder":
        self._app_role_table_role.rec_rule = rec_rule
        return self

    def field_perm(self, field_perm: Dict[str, int]) -> "AppRoleTableRoleBuilder":
        self._app_role_table_role.field_perm = field_perm
        return self

    def allow_add_record(self, allow_add_record: bool) -> "AppRoleTableRoleBuilder":
        self._app_role_table_role.allow_add_record = allow_add_record
        return self

    def allow_delete_record(self, allow_delete_record: bool) -> "AppRoleTableRoleBuilder":
        self._app_role_table_role.allow_delete_record = allow_delete_record
        return self

    def build(self) -> "AppRoleTableRole":
        return self._app_role_table_role
