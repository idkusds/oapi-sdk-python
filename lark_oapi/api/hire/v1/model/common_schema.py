# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n import I18n
from .i18n import I18n
from .common_schema_setting import CommonSchemaSetting
from .common_schema_child import CommonSchemaChild


class CommonSchema(object):
    _types = {
        "id": str,
        "name": I18n,
        "description": I18n,
        "setting": CommonSchemaSetting,
        "is_customized": bool,
        "is_required": bool,
        "is_visible": bool,
        "active_status": int,
        "children_list": List[CommonSchemaChild],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[I18n] = None
        self.description: Optional[I18n] = None
        self.setting: Optional[CommonSchemaSetting] = None
        self.is_customized: Optional[bool] = None
        self.is_required: Optional[bool] = None
        self.is_visible: Optional[bool] = None
        self.active_status: Optional[int] = None
        self.children_list: Optional[List[CommonSchemaChild]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CommonSchemaBuilder":
        return CommonSchemaBuilder()


class CommonSchemaBuilder(object):
    def __init__(self) -> None:
        self._common_schema = CommonSchema()

    def id(self, id: str) -> "CommonSchemaBuilder":
        self._common_schema.id = id
        return self

    def name(self, name: I18n) -> "CommonSchemaBuilder":
        self._common_schema.name = name
        return self

    def description(self, description: I18n) -> "CommonSchemaBuilder":
        self._common_schema.description = description
        return self

    def setting(self, setting: CommonSchemaSetting) -> "CommonSchemaBuilder":
        self._common_schema.setting = setting
        return self

    def is_customized(self, is_customized: bool) -> "CommonSchemaBuilder":
        self._common_schema.is_customized = is_customized
        return self

    def is_required(self, is_required: bool) -> "CommonSchemaBuilder":
        self._common_schema.is_required = is_required
        return self

    def is_visible(self, is_visible: bool) -> "CommonSchemaBuilder":
        self._common_schema.is_visible = is_visible
        return self

    def active_status(self, active_status: int) -> "CommonSchemaBuilder":
        self._common_schema.active_status = active_status
        return self

    def children_list(self, children_list: List[CommonSchemaChild]) -> "CommonSchemaBuilder":
        self._common_schema.children_list = children_list
        return self

    def build(self) -> "CommonSchema":
        return self._common_schema
