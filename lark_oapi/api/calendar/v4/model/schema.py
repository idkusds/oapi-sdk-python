# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class Schema(object):
    _types = {
        "ui_name": str,
        "ui_status": str,
        "app_link": str,
    }

    def __init__(self, d=None):
        self.ui_name: Optional[str] = None
        self.ui_status: Optional[str] = None
        self.app_link: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SchemaBuilder":
        return SchemaBuilder()


class SchemaBuilder(object):
    def __init__(self) -> None:
        self._schema = Schema()

    def ui_name(self, ui_name: str) -> "SchemaBuilder":
        self._schema.ui_name = ui_name
        return self

    def ui_status(self, ui_status: str) -> "SchemaBuilder":
        self._schema.ui_status = ui_status
        return self

    def app_link(self, app_link: str) -> "SchemaBuilder":
        self._schema.app_link = app_link
        return self

    def build(self) -> "Schema":
        return self._schema
