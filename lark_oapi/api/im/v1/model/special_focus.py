# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class SpecialFocus(object):
    _types = {
        "id": str,
        "id_type": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.id_type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SpecialFocusBuilder":
        return SpecialFocusBuilder()


class SpecialFocusBuilder(object):
    def __init__(self) -> None:
        self._special_focus = SpecialFocus()

    def id(self, id: str) -> "SpecialFocusBuilder":
        self._special_focus.id = id
        return self

    def id_type(self, id_type: str) -> "SpecialFocusBuilder":
        self._special_focus.id_type = id_type
        return self

    def build(self) -> "SpecialFocus":
        return self._special_focus
