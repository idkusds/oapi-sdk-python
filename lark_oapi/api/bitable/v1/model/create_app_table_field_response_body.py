# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .app_table_field import AppTableField


class CreateAppTableFieldResponseBody(object):
    _types = {
        "field": AppTableField,
    }

    def __init__(self, d=None):
        self.field: Optional[AppTableField] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateAppTableFieldResponseBodyBuilder":
        return CreateAppTableFieldResponseBodyBuilder()


class CreateAppTableFieldResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_app_table_field_response_body = CreateAppTableFieldResponseBody()

    def field(self, field: AppTableField) -> "CreateAppTableFieldResponseBodyBuilder":
        self._create_app_table_field_response_body.field = field
        return self

    def build(self) -> "CreateAppTableFieldResponseBody":
        return self._create_app_table_field_response_body
