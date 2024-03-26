# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n import I18n
from .i18n import I18n
from .common_schema_setting import CommonSchemaSetting


class CommonSchemaChild(object):
    _types = {
        "id": str,
        "name": I18n,
        "description": I18n,
        "setting": CommonSchemaSetting,
        "parent_id": str,
        "is_customized": bool,
        "is_required": bool,
        "is_visible": bool,
        "active_status": int,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[I18n] = None
        self.description: Optional[I18n] = None
        self.setting: Optional[CommonSchemaSetting] = None
        self.parent_id: Optional[str] = None
        self.is_customized: Optional[bool] = None
        self.is_required: Optional[bool] = None
        self.is_visible: Optional[bool] = None
        self.active_status: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CommonSchemaChildBuilder":
        return CommonSchemaChildBuilder()


class CommonSchemaChildBuilder(object):
    def __init__(self) -> None:
        self._common_schema_child = CommonSchemaChild()

    def id(self, id: str) -> "CommonSchemaChildBuilder":
        self._common_schema_child.id = id
        return self

    def name(self, name: I18n) -> "CommonSchemaChildBuilder":
        self._common_schema_child.name = name
        return self

    def description(self, description: I18n) -> "CommonSchemaChildBuilder":
        self._common_schema_child.description = description
        return self

    def setting(self, setting: CommonSchemaSetting) -> "CommonSchemaChildBuilder":
        self._common_schema_child.setting = setting
        return self

    def parent_id(self, parent_id: str) -> "CommonSchemaChildBuilder":
        self._common_schema_child.parent_id = parent_id
        return self

    def is_customized(self, is_customized: bool) -> "CommonSchemaChildBuilder":
        self._common_schema_child.is_customized = is_customized
        return self

    def is_required(self, is_required: bool) -> "CommonSchemaChildBuilder":
        self._common_schema_child.is_required = is_required
        return self

    def is_visible(self, is_visible: bool) -> "CommonSchemaChildBuilder":
        self._common_schema_child.is_visible = is_visible
        return self

    def active_status(self, active_status: int) -> "CommonSchemaChildBuilder":
        self._common_schema_child.active_status = active_status
        return self

    def build(self) -> "CommonSchemaChild":
        return self._common_schema_child
