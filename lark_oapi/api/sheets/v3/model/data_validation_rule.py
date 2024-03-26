# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .single_option import SingleOption
from .multiple_option import MultipleOption


class DataValidationRule(object):
    _types = {
        "type": str,
        "single_option": SingleOption,
        "multiple_option": MultipleOption,
    }

    def __init__(self, d=None):
        self.type: Optional[str] = None
        self.single_option: Optional[SingleOption] = None
        self.multiple_option: Optional[MultipleOption] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DataValidationRuleBuilder":
        return DataValidationRuleBuilder()


class DataValidationRuleBuilder(object):
    def __init__(self) -> None:
        self._data_validation_rule = DataValidationRule()

    def type(self, type: str) -> "DataValidationRuleBuilder":
        self._data_validation_rule.type = type
        return self

    def single_option(self, single_option: SingleOption) -> "DataValidationRuleBuilder":
        self._data_validation_rule.single_option = single_option
        return self

    def multiple_option(self, multiple_option: MultipleOption) -> "DataValidationRuleBuilder":
        self._data_validation_rule.multiple_option = multiple_option
        return self

    def build(self) -> "DataValidationRule":
        return self._data_validation_rule
