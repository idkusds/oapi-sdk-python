# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class UndefinedElement(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UndefinedElementBuilder":
        return UndefinedElementBuilder()


class UndefinedElementBuilder(object):
    def __init__(self) -> None:
        self._undefined_element = UndefinedElement()

    def build(self) -> "UndefinedElement":
        return self._undefined_element
