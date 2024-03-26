# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class BpmDataengineI18n(object):
    _types = {
        "zh_cn": str,
        "en_us": str,
    }

    def __init__(self, d=None):
        self.zh_cn: Optional[str] = None
        self.en_us: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BpmDataengineI18nBuilder":
        return BpmDataengineI18nBuilder()


class BpmDataengineI18nBuilder(object):
    def __init__(self) -> None:
        self._bpm_dataengine_i18n = BpmDataengineI18n()

    def zh_cn(self, zh_cn: str) -> "BpmDataengineI18nBuilder":
        self._bpm_dataengine_i18n.zh_cn = zh_cn
        return self

    def en_us(self, en_us: str) -> "BpmDataengineI18nBuilder":
        self._bpm_dataengine_i18n.en_us = en_us
        return self

    def build(self) -> "BpmDataengineI18n":
        return self._bpm_dataengine_i18n
