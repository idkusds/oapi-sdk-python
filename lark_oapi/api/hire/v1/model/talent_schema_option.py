# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n import I18n


class TalentSchemaOption(object):
    _types = {
        "active_status": int,
        "value": str,
        "name": I18n,
    }

    def __init__(self, d=None):
        self.active_status: Optional[int] = None
        self.value: Optional[str] = None
        self.name: Optional[I18n] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TalentSchemaOptionBuilder":
        return TalentSchemaOptionBuilder()


class TalentSchemaOptionBuilder(object):
    def __init__(self) -> None:
        self._talent_schema_option = TalentSchemaOption()

    def active_status(self, active_status: int) -> "TalentSchemaOptionBuilder":
        self._talent_schema_option.active_status = active_status
        return self

    def value(self, value: str) -> "TalentSchemaOptionBuilder":
        self._talent_schema_option.value = value
        return self

    def name(self, name: I18n) -> "TalentSchemaOptionBuilder":
        self._talent_schema_option.name = name
        return self

    def build(self) -> "TalentSchemaOption":
        return self._talent_schema_option
