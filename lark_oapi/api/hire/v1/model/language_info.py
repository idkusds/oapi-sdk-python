# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class LanguageInfo(object):
    _types = {
        "language": int,
        "proficiency": int,
    }

    def __init__(self, d=None):
        self.language: Optional[int] = None
        self.proficiency: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "LanguageInfoBuilder":
        return LanguageInfoBuilder()


class LanguageInfoBuilder(object):
    def __init__(self) -> None:
        self._language_info = LanguageInfo()

    def language(self, language: int) -> "LanguageInfoBuilder":
        self._language_info.language = language
        return self

    def proficiency(self, proficiency: int) -> "LanguageInfoBuilder":
        self._language_info.proficiency = proficiency
        return self

    def build(self) -> "LanguageInfo":
        return self._language_info
