# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class I18n(object):
    _types = {
        "zh_cn": str,
        "en_us": str,
        "ja_jp": str,
    }

    def __init__(self, d=None):
        self.zh_cn: Optional[str] = None
        self.en_us: Optional[str] = None
        self.ja_jp: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "I18nBuilder":
        return I18nBuilder()


class I18nBuilder(object):
    def __init__(self) -> None:
        self._i18n = I18n()

    def zh_cn(self, zh_cn: str) -> "I18nBuilder":
        self._i18n.zh_cn = zh_cn
        return self

    def en_us(self, en_us: str) -> "I18nBuilder":
        self._i18n.en_us = en_us
        return self

    def ja_jp(self, ja_jp: str) -> "I18nBuilder":
        self._i18n.ja_jp = ja_jp
        return self

    def build(self) -> "I18n":
        return self._i18n
