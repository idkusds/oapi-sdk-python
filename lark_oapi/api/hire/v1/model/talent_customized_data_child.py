# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .i18n import I18n
from .talent_customized_value import TalentCustomizedValue


class TalentCustomizedDataChild(object):
    _types = {
        "object_id": str,
        "name": I18n,
        "object_type": int,
        "value": TalentCustomizedValue,
    }

    def __init__(self, d=None):
        self.object_id: Optional[str] = None
        self.name: Optional[I18n] = None
        self.object_type: Optional[int] = None
        self.value: Optional[TalentCustomizedValue] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TalentCustomizedDataChildBuilder":
        return TalentCustomizedDataChildBuilder()


class TalentCustomizedDataChildBuilder(object):
    def __init__(self) -> None:
        self._talent_customized_data_child = TalentCustomizedDataChild()

    def object_id(self, object_id: str) -> "TalentCustomizedDataChildBuilder":
        self._talent_customized_data_child.object_id = object_id
        return self

    def name(self, name: I18n) -> "TalentCustomizedDataChildBuilder":
        self._talent_customized_data_child.name = name
        return self

    def object_type(self, object_type: int) -> "TalentCustomizedDataChildBuilder":
        self._talent_customized_data_child.object_type = object_type
        return self

    def value(self, value: TalentCustomizedValue) -> "TalentCustomizedDataChildBuilder":
        self._talent_customized_data_child.value = value
        return self

    def build(self) -> "TalentCustomizedDataChild":
        return self._talent_customized_data_child
