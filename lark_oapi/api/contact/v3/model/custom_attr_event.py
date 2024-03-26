# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class CustomAttrEvent(object):
    _types = {
        "contact_field_key": List[str],
        "allow_open_query": bool,
    }

    def __init__(self, d=None):
        self.contact_field_key: Optional[List[str]] = None
        self.allow_open_query: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CustomAttrEventBuilder":
        return CustomAttrEventBuilder()


class CustomAttrEventBuilder(object):
    def __init__(self) -> None:
        self._custom_attr_event = CustomAttrEvent()

    def contact_field_key(self, contact_field_key: List[str]) -> "CustomAttrEventBuilder":
        self._custom_attr_event.contact_field_key = contact_field_key
        return self

    def allow_open_query(self, allow_open_query: bool) -> "CustomAttrEventBuilder":
        self._custom_attr_event.allow_open_query = allow_open_query
        return self

    def build(self) -> "CustomAttrEvent":
        return self._custom_attr_event
