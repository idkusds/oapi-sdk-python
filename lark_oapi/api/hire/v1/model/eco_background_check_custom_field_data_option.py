# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n import I18n


class EcoBackgroundCheckCustomFieldDataOption(object):
    _types = {
        "key": str,
        "name": I18n,
    }

    def __init__(self, d=None):
        self.key: Optional[str] = None
        self.name: Optional[I18n] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EcoBackgroundCheckCustomFieldDataOptionBuilder":
        return EcoBackgroundCheckCustomFieldDataOptionBuilder()


class EcoBackgroundCheckCustomFieldDataOptionBuilder(object):
    def __init__(self) -> None:
        self._eco_background_check_custom_field_data_option = EcoBackgroundCheckCustomFieldDataOption()

    def key(self, key: str) -> "EcoBackgroundCheckCustomFieldDataOptionBuilder":
        self._eco_background_check_custom_field_data_option.key = key
        return self

    def name(self, name: I18n) -> "EcoBackgroundCheckCustomFieldDataOptionBuilder":
        self._eco_background_check_custom_field_data_option.name = name
        return self

    def build(self) -> "EcoBackgroundCheckCustomFieldDataOption":
        return self._eco_background_check_custom_field_data_option
