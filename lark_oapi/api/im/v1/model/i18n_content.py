# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class I18nContent(object):
    _types = {
        "content": str,
        "language": str,
    }

    def __init__(self, d=None):
        self.content: Optional[str] = None
        self.language: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "I18nContentBuilder":
        return I18nContentBuilder()


class I18nContentBuilder(object):
    def __init__(self) -> None:
        self._i18n_content = I18nContent()

    def content(self, content: str) -> "I18nContentBuilder":
        self._i18n_content.content = content
        return self

    def language(self, language: str) -> "I18nContentBuilder":
        self._i18n_content.language = language
        return self

    def build(self) -> "I18nContent":
        return self._i18n_content
