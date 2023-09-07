# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class BasicPersonInfo(object):
    _types = {
        "person_id": str,
        "preferred_name": str,
        "preferred_local_full_name": str,
        "preferred_english_full_name": str,
    }

    def __init__(self, d=None):
        self.person_id: Optional[str] = None
        self.preferred_name: Optional[str] = None
        self.preferred_local_full_name: Optional[str] = None
        self.preferred_english_full_name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BasicPersonInfoBuilder":
        return BasicPersonInfoBuilder()


class BasicPersonInfoBuilder(object):
    def __init__(self) -> None:
        self._basic_person_info = BasicPersonInfo()

    def person_id(self, person_id: str) -> "BasicPersonInfoBuilder":
        self._basic_person_info.person_id = person_id
        return self

    def preferred_name(self, preferred_name: str) -> "BasicPersonInfoBuilder":
        self._basic_person_info.preferred_name = preferred_name
        return self

    def preferred_local_full_name(self, preferred_local_full_name: str) -> "BasicPersonInfoBuilder":
        self._basic_person_info.preferred_local_full_name = preferred_local_full_name
        return self

    def preferred_english_full_name(self, preferred_english_full_name: str) -> "BasicPersonInfoBuilder":
        self._basic_person_info.preferred_english_full_name = preferred_english_full_name
        return self

    def build(self) -> "BasicPersonInfo":
        return self._basic_person_info
