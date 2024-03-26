# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class Undefined(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UndefinedBuilder":
        return UndefinedBuilder()


class UndefinedBuilder(object):
    def __init__(self) -> None:
        self._undefined = Undefined()

    def build(self) -> "Undefined":
        return self._undefined
