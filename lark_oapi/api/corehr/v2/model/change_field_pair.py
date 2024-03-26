# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .custom_field_data import CustomFieldData
from .custom_field_data import CustomFieldData


class ChangeFieldPair(object):
    _types = {
        "origin_value": CustomFieldData,
        "target_value": CustomFieldData,
    }

    def __init__(self, d=None):
        self.origin_value: Optional[CustomFieldData] = None
        self.target_value: Optional[CustomFieldData] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ChangeFieldPairBuilder":
        return ChangeFieldPairBuilder()


class ChangeFieldPairBuilder(object):
    def __init__(self) -> None:
        self._change_field_pair = ChangeFieldPair()

    def origin_value(self, origin_value: CustomFieldData) -> "ChangeFieldPairBuilder":
        self._change_field_pair.origin_value = origin_value
        return self

    def target_value(self, target_value: CustomFieldData) -> "ChangeFieldPairBuilder":
        self._change_field_pair.target_value = target_value
        return self

    def build(self) -> "ChangeFieldPair":
        return self._change_field_pair
