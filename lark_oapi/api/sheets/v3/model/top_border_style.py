# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class TopBorderStyle(object):
    _types = {
        "style": str,
        "color": str,
    }

    def __init__(self, d=None):
        self.style: Optional[str] = None
        self.color: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TopBorderStyleBuilder":
        return TopBorderStyleBuilder()


class TopBorderStyleBuilder(object):
    def __init__(self) -> None:
        self._top_border_style = TopBorderStyle()

    def style(self, style: str) -> "TopBorderStyleBuilder":
        self._top_border_style.style = style
        return self

    def color(self, color: str) -> "TopBorderStyleBuilder":
        self._top_border_style.color = color
        return self

    def build(self) -> "TopBorderStyle":
        return self._top_border_style
