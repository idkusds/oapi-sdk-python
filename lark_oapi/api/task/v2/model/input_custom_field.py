# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .number_setting import NumberSetting
from .member_setting import MemberSetting
from .datetime_setting import DatetimeSetting
from .select_setting import SelectSetting
from .select_setting import SelectSetting
from .text_setting import TextSetting


class InputCustomField(object):
    _types = {
        "resource_type": str,
        "resource_id": str,
        "name": str,
        "type": str,
        "number_setting": NumberSetting,
        "member_setting": MemberSetting,
        "datetime_setting": DatetimeSetting,
        "single_select_setting": SelectSetting,
        "multi_select_setting": SelectSetting,
        "text_setting": TextSetting,
    }

    def __init__(self, d=None):
        self.resource_type: Optional[str] = None
        self.resource_id: Optional[str] = None
        self.name: Optional[str] = None
        self.type: Optional[str] = None
        self.number_setting: Optional[NumberSetting] = None
        self.member_setting: Optional[MemberSetting] = None
        self.datetime_setting: Optional[DatetimeSetting] = None
        self.single_select_setting: Optional[SelectSetting] = None
        self.multi_select_setting: Optional[SelectSetting] = None
        self.text_setting: Optional[TextSetting] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InputCustomFieldBuilder":
        return InputCustomFieldBuilder()


class InputCustomFieldBuilder(object):
    def __init__(self) -> None:
        self._input_custom_field = InputCustomField()

    def resource_type(self, resource_type: str) -> "InputCustomFieldBuilder":
        self._input_custom_field.resource_type = resource_type
        return self

    def resource_id(self, resource_id: str) -> "InputCustomFieldBuilder":
        self._input_custom_field.resource_id = resource_id
        return self

    def name(self, name: str) -> "InputCustomFieldBuilder":
        self._input_custom_field.name = name
        return self

    def type(self, type: str) -> "InputCustomFieldBuilder":
        self._input_custom_field.type = type
        return self

    def number_setting(self, number_setting: NumberSetting) -> "InputCustomFieldBuilder":
        self._input_custom_field.number_setting = number_setting
        return self

    def member_setting(self, member_setting: MemberSetting) -> "InputCustomFieldBuilder":
        self._input_custom_field.member_setting = member_setting
        return self

    def datetime_setting(self, datetime_setting: DatetimeSetting) -> "InputCustomFieldBuilder":
        self._input_custom_field.datetime_setting = datetime_setting
        return self

    def single_select_setting(self, single_select_setting: SelectSetting) -> "InputCustomFieldBuilder":
        self._input_custom_field.single_select_setting = single_select_setting
        return self

    def multi_select_setting(self, multi_select_setting: SelectSetting) -> "InputCustomFieldBuilder":
        self._input_custom_field.multi_select_setting = multi_select_setting
        return self

    def text_setting(self, text_setting: TextSetting) -> "InputCustomFieldBuilder":
        self._input_custom_field.text_setting = text_setting
        return self

    def build(self) -> "InputCustomField":
        return self._input_custom_field
