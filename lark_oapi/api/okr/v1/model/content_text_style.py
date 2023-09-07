# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .content_color import ContentColor
from .content_link import ContentLink


class ContentTextStyle(object):
    _types = {
        "bold": bool,
        "strike_through": bool,
        "back_color": ContentColor,
        "text_color": ContentColor,
        "link": ContentLink,
    }

    def __init__(self, d=None):
        self.bold: Optional[bool] = None
        self.strike_through: Optional[bool] = None
        self.back_color: Optional[ContentColor] = None
        self.text_color: Optional[ContentColor] = None
        self.link: Optional[ContentLink] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ContentTextStyleBuilder":
        return ContentTextStyleBuilder()


class ContentTextStyleBuilder(object):
    def __init__(self) -> None:
        self._content_text_style = ContentTextStyle()

    def bold(self, bold: bool) -> "ContentTextStyleBuilder":
        self._content_text_style.bold = bold
        return self

    def strike_through(self, strike_through: bool) -> "ContentTextStyleBuilder":
        self._content_text_style.strike_through = strike_through
        return self

    def back_color(self, back_color: ContentColor) -> "ContentTextStyleBuilder":
        self._content_text_style.back_color = back_color
        return self

    def text_color(self, text_color: ContentColor) -> "ContentTextStyleBuilder":
        self._content_text_style.text_color = text_color
        return self

    def link(self, link: ContentLink) -> "ContentTextStyleBuilder":
        self._content_text_style.link = link
        return self

    def build(self) -> "ContentTextStyle":
        return self._content_text_style
