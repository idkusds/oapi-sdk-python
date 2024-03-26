# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .agenda_title_element import AgendaTitleElement


class AgendaItemTitle(object):
    _types = {
        "elements": List[AgendaTitleElement],
        "align": int,
    }

    def __init__(self, d=None):
        self.elements: Optional[List[AgendaTitleElement]] = None
        self.align: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AgendaItemTitleBuilder":
        return AgendaItemTitleBuilder()


class AgendaItemTitleBuilder(object):
    def __init__(self) -> None:
        self._agenda_item_title = AgendaItemTitle()

    def elements(self, elements: List[AgendaTitleElement]) -> "AgendaItemTitleBuilder":
        self._agenda_item_title.elements = elements
        return self

    def align(self, align: int) -> "AgendaItemTitleBuilder":
        self._agenda_item_title.align = align
        return self

    def build(self) -> "AgendaItemTitle":
        return self._agenda_item_title
