# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class AddCustomFieldRequestBody(object):
    _types = {
        "resource_type": str,
        "resource_id": str,
    }

    def __init__(self, d=None):
        self.resource_type: Optional[str] = None
        self.resource_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AddCustomFieldRequestBodyBuilder":
        return AddCustomFieldRequestBodyBuilder()


class AddCustomFieldRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._add_custom_field_request_body = AddCustomFieldRequestBody()

    def resource_type(self, resource_type: str) -> "AddCustomFieldRequestBodyBuilder":
        self._add_custom_field_request_body.resource_type = resource_type
        return self

    def resource_id(self, resource_id: str) -> "AddCustomFieldRequestBodyBuilder":
        self._add_custom_field_request_body.resource_id = resource_id
        return self

    def build(self) -> "AddCustomFieldRequestBody":
        return self._add_custom_field_request_body
