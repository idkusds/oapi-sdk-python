# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .enum import Enum
from .enum import Enum
from .enum import Enum
from .enum import Enum


class PersonName(object):
    _types = {
        "local_primary": str,
        "local_first_name": str,
        "country_region_id": str,
        "name_type": Enum,
        "local_first_name_2": str,
        "local_primary_2": str,
        "additional_name_type": Enum,
        "first_name": str,
        "full_name": str,
        "hereditary": str,
        "custom_name": str,
        "custom_local_name": str,
        "middle_name": str,
        "name_primary": str,
        "secondary": str,
        "social": Enum,
        "tertiary": str,
        "title": Enum,
        "local_middle_name": str,
        "local_secondary": str,
        "display_name_local_and_western_script": str,
        "display_name_local_script": str,
        "display_name_western_script": str,
    }

    def __init__(self, d=None):
        self.local_primary: Optional[str] = None
        self.local_first_name: Optional[str] = None
        self.country_region_id: Optional[str] = None
        self.name_type: Optional[Enum] = None
        self.local_first_name_2: Optional[str] = None
        self.local_primary_2: Optional[str] = None
        self.additional_name_type: Optional[Enum] = None
        self.first_name: Optional[str] = None
        self.full_name: Optional[str] = None
        self.hereditary: Optional[str] = None
        self.custom_name: Optional[str] = None
        self.custom_local_name: Optional[str] = None
        self.middle_name: Optional[str] = None
        self.name_primary: Optional[str] = None
        self.secondary: Optional[str] = None
        self.social: Optional[Enum] = None
        self.tertiary: Optional[str] = None
        self.title: Optional[Enum] = None
        self.local_middle_name: Optional[str] = None
        self.local_secondary: Optional[str] = None
        self.display_name_local_and_western_script: Optional[str] = None
        self.display_name_local_script: Optional[str] = None
        self.display_name_western_script: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PersonNameBuilder":
        return PersonNameBuilder()


class PersonNameBuilder(object):
    def __init__(self) -> None:
        self._person_name = PersonName()

    def local_primary(self, local_primary: str) -> "PersonNameBuilder":
        self._person_name.local_primary = local_primary
        return self

    def local_first_name(self, local_first_name: str) -> "PersonNameBuilder":
        self._person_name.local_first_name = local_first_name
        return self

    def country_region_id(self, country_region_id: str) -> "PersonNameBuilder":
        self._person_name.country_region_id = country_region_id
        return self

    def name_type(self, name_type: Enum) -> "PersonNameBuilder":
        self._person_name.name_type = name_type
        return self

    def local_first_name_2(self, local_first_name_2: str) -> "PersonNameBuilder":
        self._person_name.local_first_name_2 = local_first_name_2
        return self

    def local_primary_2(self, local_primary_2: str) -> "PersonNameBuilder":
        self._person_name.local_primary_2 = local_primary_2
        return self

    def additional_name_type(self, additional_name_type: Enum) -> "PersonNameBuilder":
        self._person_name.additional_name_type = additional_name_type
        return self

    def first_name(self, first_name: str) -> "PersonNameBuilder":
        self._person_name.first_name = first_name
        return self

    def full_name(self, full_name: str) -> "PersonNameBuilder":
        self._person_name.full_name = full_name
        return self

    def hereditary(self, hereditary: str) -> "PersonNameBuilder":
        self._person_name.hereditary = hereditary
        return self

    def custom_name(self, custom_name: str) -> "PersonNameBuilder":
        self._person_name.custom_name = custom_name
        return self

    def custom_local_name(self, custom_local_name: str) -> "PersonNameBuilder":
        self._person_name.custom_local_name = custom_local_name
        return self

    def middle_name(self, middle_name: str) -> "PersonNameBuilder":
        self._person_name.middle_name = middle_name
        return self

    def name_primary(self, name_primary: str) -> "PersonNameBuilder":
        self._person_name.name_primary = name_primary
        return self

    def secondary(self, secondary: str) -> "PersonNameBuilder":
        self._person_name.secondary = secondary
        return self

    def social(self, social: Enum) -> "PersonNameBuilder":
        self._person_name.social = social
        return self

    def tertiary(self, tertiary: str) -> "PersonNameBuilder":
        self._person_name.tertiary = tertiary
        return self

    def title(self, title: Enum) -> "PersonNameBuilder":
        self._person_name.title = title
        return self

    def local_middle_name(self, local_middle_name: str) -> "PersonNameBuilder":
        self._person_name.local_middle_name = local_middle_name
        return self

    def local_secondary(self, local_secondary: str) -> "PersonNameBuilder":
        self._person_name.local_secondary = local_secondary
        return self

    def display_name_local_and_western_script(self, display_name_local_and_western_script: str) -> "PersonNameBuilder":
        self._person_name.display_name_local_and_western_script = display_name_local_and_western_script
        return self

    def display_name_local_script(self, display_name_local_script: str) -> "PersonNameBuilder":
        self._person_name.display_name_local_script = display_name_local_script
        return self

    def display_name_western_script(self, display_name_western_script: str) -> "PersonNameBuilder":
        self._person_name.display_name_western_script = display_name_western_script
        return self

    def build(self) -> "PersonName":
        return self._person_name
