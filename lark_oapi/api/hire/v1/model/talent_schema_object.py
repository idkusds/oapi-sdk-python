# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n import I18n
from .talent_schema_option import TalentSchemaOption
from .talent_schema_child_object import TalentSchemaChildObject


class TalentSchemaObject(object):
    _types = {
        "id": str,
        "active_status": int,
        "is_customized": bool,
        "name": I18n,
        "option_list": List[TalentSchemaOption],
        "children": List[TalentSchemaChildObject],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.active_status: Optional[int] = None
        self.is_customized: Optional[bool] = None
        self.name: Optional[I18n] = None
        self.option_list: Optional[List[TalentSchemaOption]] = None
        self.children: Optional[List[TalentSchemaChildObject]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TalentSchemaObjectBuilder":
        return TalentSchemaObjectBuilder()


class TalentSchemaObjectBuilder(object):
    def __init__(self) -> None:
        self._talent_schema_object = TalentSchemaObject()

    def id(self, id: str) -> "TalentSchemaObjectBuilder":
        self._talent_schema_object.id = id
        return self

    def active_status(self, active_status: int) -> "TalentSchemaObjectBuilder":
        self._talent_schema_object.active_status = active_status
        return self

    def is_customized(self, is_customized: bool) -> "TalentSchemaObjectBuilder":
        self._talent_schema_object.is_customized = is_customized
        return self

    def name(self, name: I18n) -> "TalentSchemaObjectBuilder":
        self._talent_schema_object.name = name
        return self

    def option_list(self, option_list: List[TalentSchemaOption]) -> "TalentSchemaObjectBuilder":
        self._talent_schema_object.option_list = option_list
        return self

    def children(self, children: List[TalentSchemaChildObject]) -> "TalentSchemaObjectBuilder":
        self._talent_schema_object.children = children
        return self

    def build(self) -> "TalentSchemaObject":
        return self._talent_schema_object
