# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .custom_attr_option import CustomAttrOption


class CustomAttrOptions(object):
    _types = {
        "default_option_id": str,
        "option_type": str,
        "options": List[CustomAttrOption],
    }

    def __init__(self, d=None):
        self.default_option_id: Optional[str] = None
        self.option_type: Optional[str] = None
        self.options: Optional[List[CustomAttrOption]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CustomAttrOptionsBuilder":
        return CustomAttrOptionsBuilder()


class CustomAttrOptionsBuilder(object):
    def __init__(self) -> None:
        self._custom_attr_options = CustomAttrOptions()

    def default_option_id(self, default_option_id: str) -> "CustomAttrOptionsBuilder":
        self._custom_attr_options.default_option_id = default_option_id
        return self

    def option_type(self, option_type: str) -> "CustomAttrOptionsBuilder":
        self._custom_attr_options.option_type = option_type
        return self

    def options(self, options: List[CustomAttrOption]) -> "CustomAttrOptionsBuilder":
        self._custom_attr_options.options = options
        return self

    def build(self) -> "CustomAttrOptions":
        return self._custom_attr_options
