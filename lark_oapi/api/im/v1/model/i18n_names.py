# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class I18nNames(object):
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
    def builder() -> "I18nNamesBuilder":
        return I18nNamesBuilder()


class I18nNamesBuilder(object):
    def __init__(self) -> None:
        self._i18n_names = I18nNames()

    def zh_cn(self, zh_cn: str) -> "I18nNamesBuilder":
        self._i18n_names.zh_cn = zh_cn
        return self

    def en_us(self, en_us: str) -> "I18nNamesBuilder":
        self._i18n_names.en_us = en_us
        return self

    def ja_jp(self, ja_jp: str) -> "I18nNamesBuilder":
        self._i18n_names.ja_jp = ja_jp
        return self

    def build(self) -> "I18nNames":
        return self._i18n_names
