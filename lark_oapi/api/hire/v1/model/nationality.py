# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class Nationality(object):
    _types = {
        "nationality_code": str,
        "name": str,
        "en_name": str,
    }

    def __init__(self, d=None):
        self.nationality_code: Optional[str] = None
        self.name: Optional[str] = None
        self.en_name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "NationalityBuilder":
        return NationalityBuilder()


class NationalityBuilder(object):
    def __init__(self) -> None:
        self._nationality = Nationality()

    def nationality_code(self, nationality_code: str) -> "NationalityBuilder":
        self._nationality.nationality_code = nationality_code
        return self

    def name(self, name: str) -> "NationalityBuilder":
        self._nationality.name = name
        return self

    def en_name(self, en_name: str) -> "NationalityBuilder":
        self._nationality.en_name = en_name
        return self

    def build(self) -> "Nationality":
        return self._nationality
