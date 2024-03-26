# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .text_element_style import TextElementStyle


class Equation(object):
    _types = {
        "content": str,
        "text_element_style": TextElementStyle,
    }

    def __init__(self, d=None):
        self.content: Optional[str] = None
        self.text_element_style: Optional[TextElementStyle] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EquationBuilder":
        return EquationBuilder()


class EquationBuilder(object):
    def __init__(self) -> None:
        self._equation = Equation()

    def content(self, content: str) -> "EquationBuilder":
        self._equation.content = content
        return self

    def text_element_style(self, text_element_style: TextElementStyle) -> "EquationBuilder":
        self._equation.text_element_style = text_element_style
        return self

    def build(self) -> "Equation":
        return self._equation
