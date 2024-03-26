# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class Param(object):
    _types = {
        "key": str,
        "value": str,
    }

    def __init__(self, d=None):
        self.key: Optional[str] = None
        self.value: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ParamBuilder":
        return ParamBuilder()


class ParamBuilder(object):
    def __init__(self) -> None:
        self._param = Param()

    def key(self, key: str) -> "ParamBuilder":
        self._param.key = key
        return self

    def value(self, value: str) -> "ParamBuilder":
        self._param.value = value
        return self

    def build(self) -> "Param":
        return self._param
