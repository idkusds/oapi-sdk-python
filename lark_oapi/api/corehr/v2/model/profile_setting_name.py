# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ProfileSettingName(object):
    _types = {
        "additional_name_type": str,
        "country_region": str,
        "full_name": str,
        "hereditary": str,
        "middle_name": str,
        "secondary": str,
        "social": str,
        "tertiary": str,
        "local_first_name_2": str,
        "local_middle_name": str,
        "local_primary": str,
        "local_primary_2": str,
        "local_secondary": str,
        "title": str,
        "local_first_name": str,
        "custom_local_name": str,
        "custom_western_name": str,
        "name_type": str,
        "first_name": str,
        "name_primary": str,
    }

    def __init__(self, d=None):
        self.additional_name_type: Optional[str] = None
        self.country_region: Optional[str] = None
        self.full_name: Optional[str] = None
        self.hereditary: Optional[str] = None
        self.middle_name: Optional[str] = None
        self.secondary: Optional[str] = None
        self.social: Optional[str] = None
        self.tertiary: Optional[str] = None
        self.local_first_name_2: Optional[str] = None
        self.local_middle_name: Optional[str] = None
        self.local_primary: Optional[str] = None
        self.local_primary_2: Optional[str] = None
        self.local_secondary: Optional[str] = None
        self.title: Optional[str] = None
        self.local_first_name: Optional[str] = None
        self.custom_local_name: Optional[str] = None
        self.custom_western_name: Optional[str] = None
        self.name_type: Optional[str] = None
        self.first_name: Optional[str] = None
        self.name_primary: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ProfileSettingNameBuilder":
        return ProfileSettingNameBuilder()


class ProfileSettingNameBuilder(object):
    def __init__(self) -> None:
        self._profile_setting_name = ProfileSettingName()

    def additional_name_type(self, additional_name_type: str) -> "ProfileSettingNameBuilder":
        self._profile_setting_name.additional_name_type = additional_name_type
        return self

    def country_region(self, country_region: str) -> "ProfileSettingNameBuilder":
        self._profile_setting_name.country_region = country_region
        return self

    def full_name(self, full_name: str) -> "ProfileSettingNameBuilder":
        self._profile_setting_name.full_name = full_name
        return self

    def hereditary(self, hereditary: str) -> "ProfileSettingNameBuilder":
        self._profile_setting_name.hereditary = hereditary
        return self

    def middle_name(self, middle_name: str) -> "ProfileSettingNameBuilder":
        self._profile_setting_name.middle_name = middle_name
        return self

    def secondary(self, secondary: str) -> "ProfileSettingNameBuilder":
        self._profile_setting_name.secondary = secondary
        return self

    def social(self, social: str) -> "ProfileSettingNameBuilder":
        self._profile_setting_name.social = social
        return self

    def tertiary(self, tertiary: str) -> "ProfileSettingNameBuilder":
        self._profile_setting_name.tertiary = tertiary
        return self

    def local_first_name_2(self, local_first_name_2: str) -> "ProfileSettingNameBuilder":
        self._profile_setting_name.local_first_name_2 = local_first_name_2
        return self

    def local_middle_name(self, local_middle_name: str) -> "ProfileSettingNameBuilder":
        self._profile_setting_name.local_middle_name = local_middle_name
        return self

    def local_primary(self, local_primary: str) -> "ProfileSettingNameBuilder":
        self._profile_setting_name.local_primary = local_primary
        return self

    def local_primary_2(self, local_primary_2: str) -> "ProfileSettingNameBuilder":
        self._profile_setting_name.local_primary_2 = local_primary_2
        return self

    def local_secondary(self, local_secondary: str) -> "ProfileSettingNameBuilder":
        self._profile_setting_name.local_secondary = local_secondary
        return self

    def title(self, title: str) -> "ProfileSettingNameBuilder":
        self._profile_setting_name.title = title
        return self

    def local_first_name(self, local_first_name: str) -> "ProfileSettingNameBuilder":
        self._profile_setting_name.local_first_name = local_first_name
        return self

    def custom_local_name(self, custom_local_name: str) -> "ProfileSettingNameBuilder":
        self._profile_setting_name.custom_local_name = custom_local_name
        return self

    def custom_western_name(self, custom_western_name: str) -> "ProfileSettingNameBuilder":
        self._profile_setting_name.custom_western_name = custom_western_name
        return self

    def name_type(self, name_type: str) -> "ProfileSettingNameBuilder":
        self._profile_setting_name.name_type = name_type
        return self

    def first_name(self, first_name: str) -> "ProfileSettingNameBuilder":
        self._profile_setting_name.first_name = first_name
        return self

    def name_primary(self, name_primary: str) -> "ProfileSettingNameBuilder":
        self._profile_setting_name.name_primary = name_primary
        return self

    def build(self) -> "ProfileSettingName":
        return self._profile_setting_name