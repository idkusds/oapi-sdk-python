# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class AppScopes(object):
    _types = {
        "high_level_scopes": List[str],
        "low_level_scopes": List[str],
    }

    def __init__(self, d=None):
        self.high_level_scopes: Optional[List[str]] = None
        self.low_level_scopes: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppScopesBuilder":
        return AppScopesBuilder()


class AppScopesBuilder(object):
    def __init__(self) -> None:
        self._app_scopes = AppScopes()

    def high_level_scopes(self, high_level_scopes: List[str]) -> "AppScopesBuilder":
        self._app_scopes.high_level_scopes = high_level_scopes
        return self

    def low_level_scopes(self, low_level_scopes: List[str]) -> "AppScopesBuilder":
        self._app_scopes.low_level_scopes = low_level_scopes
        return self

    def build(self) -> "AppScopes":
        return self._app_scopes
