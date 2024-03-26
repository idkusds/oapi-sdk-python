# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .member import Member


class InputCustomFieldValue(object):
    _types = {
        "guid": str,
        "number_value": str,
        "member_value": List[Member],
        "datetime_value": str,
        "single_select_value": str,
        "multi_select_value": List[str],
        "text_value": str,
    }

    def __init__(self, d=None):
        self.guid: Optional[str] = None
        self.number_value: Optional[str] = None
        self.member_value: Optional[List[Member]] = None
        self.datetime_value: Optional[str] = None
        self.single_select_value: Optional[str] = None
        self.multi_select_value: Optional[List[str]] = None
        self.text_value: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InputCustomFieldValueBuilder":
        return InputCustomFieldValueBuilder()


class InputCustomFieldValueBuilder(object):
    def __init__(self) -> None:
        self._input_custom_field_value = InputCustomFieldValue()

    def guid(self, guid: str) -> "InputCustomFieldValueBuilder":
        self._input_custom_field_value.guid = guid
        return self

    def number_value(self, number_value: str) -> "InputCustomFieldValueBuilder":
        self._input_custom_field_value.number_value = number_value
        return self

    def member_value(self, member_value: List[Member]) -> "InputCustomFieldValueBuilder":
        self._input_custom_field_value.member_value = member_value
        return self

    def datetime_value(self, datetime_value: str) -> "InputCustomFieldValueBuilder":
        self._input_custom_field_value.datetime_value = datetime_value
        return self

    def single_select_value(self, single_select_value: str) -> "InputCustomFieldValueBuilder":
        self._input_custom_field_value.single_select_value = single_select_value
        return self

    def multi_select_value(self, multi_select_value: List[str]) -> "InputCustomFieldValueBuilder":
        self._input_custom_field_value.multi_select_value = multi_select_value
        return self

    def text_value(self, text_value: str) -> "InputCustomFieldValueBuilder":
        self._input_custom_field_value.text_value = text_value
        return self

    def build(self) -> "InputCustomFieldValue":
        return self._input_custom_field_value
