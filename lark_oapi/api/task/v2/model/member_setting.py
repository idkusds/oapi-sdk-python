# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class MemberSetting(object):
    _types = {
        "multi": bool,
    }

    def __init__(self, d=None):
        self.multi: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MemberSettingBuilder":
        return MemberSettingBuilder()


class MemberSettingBuilder(object):
    def __init__(self) -> None:
        self._member_setting = MemberSetting()

    def multi(self, multi: bool) -> "MemberSettingBuilder":
        self._member_setting.multi = multi
        return self

    def build(self) -> "MemberSetting":
        return self._member_setting
