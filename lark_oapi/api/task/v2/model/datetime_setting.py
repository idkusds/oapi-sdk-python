# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DatetimeSetting(object):
    _types = {
        "format": str,
    }

    def __init__(self, d=None):
        self.format: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DatetimeSettingBuilder":
        return DatetimeSettingBuilder()


class DatetimeSettingBuilder(object):
    def __init__(self) -> None:
        self._datetime_setting = DatetimeSetting()

    def format(self, format: str) -> "DatetimeSettingBuilder":
        self._datetime_setting.format = format
        return self

    def build(self) -> "DatetimeSetting":
        return self._datetime_setting
