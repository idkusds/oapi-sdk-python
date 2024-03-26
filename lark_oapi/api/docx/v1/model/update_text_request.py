# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .text_element import TextElement
from .text_style import TextStyle


class UpdateTextRequest(object):
    _types = {
        "elements": List[TextElement],
        "style": TextStyle,
        "fields": List[int],
    }

    def __init__(self, d=None):
        self.elements: Optional[List[TextElement]] = None
        self.style: Optional[TextStyle] = None
        self.fields: Optional[List[int]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdateTextRequestBuilder":
        return UpdateTextRequestBuilder()


class UpdateTextRequestBuilder(object):
    def __init__(self) -> None:
        self._update_text_request = UpdateTextRequest()

    def elements(self, elements: List[TextElement]) -> "UpdateTextRequestBuilder":
        self._update_text_request.elements = elements
        return self

    def style(self, style: TextStyle) -> "UpdateTextRequestBuilder":
        self._update_text_request.style = style
        return self

    def fields(self, fields: List[int]) -> "UpdateTextRequestBuilder":
        self._update_text_request.fields = fields
        return self

    def build(self) -> "UpdateTextRequest":
        return self._update_text_request
