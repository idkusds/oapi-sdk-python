# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .site_name import SiteName


class Site(object):
    _types = {
        "id": str,
        "name": SiteName,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[SiteName] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SiteBuilder":
        return SiteBuilder()


class SiteBuilder(object):
    def __init__(self) -> None:
        self._site = Site()

    def id(self, id: str) -> "SiteBuilder":
        self._site.id = id
        return self

    def name(self, name: SiteName) -> "SiteBuilder":
        self._site.name = name
        return self

    def build(self) -> "Site":
        return self._site
