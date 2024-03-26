# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class SiteName(object):
    _types = {
        "zh_cn": str,
        "en_us": str,
    }

    def __init__(self, d=None):
        self.zh_cn: Optional[str] = None
        self.en_us: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SiteNameBuilder":
        return SiteNameBuilder()


class SiteNameBuilder(object):
    def __init__(self) -> None:
        self._site_name = SiteName()

    def zh_cn(self, zh_cn: str) -> "SiteNameBuilder":
        self._site_name.zh_cn = zh_cn
        return self

    def en_us(self, en_us: str) -> "SiteNameBuilder":
        self._site_name.en_us = en_us
        return self

    def build(self) -> "SiteName":
        return self._site_name
