# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class ContentList(object):
    _types = {
        "type": str,
        "indent_level": int,
        "number": int,
    }

    def __init__(self, d=None):
        self.type: Optional[str] = None
        self.indent_level: Optional[int] = None
        self.number: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ContentListBuilder":
        return ContentListBuilder()


class ContentListBuilder(object):
    def __init__(self) -> None:
        self._content_list = ContentList()

    def type(self, type: str) -> "ContentListBuilder":
        self._content_list.type = type
        return self

    def indent_level(self, indent_level: int) -> "ContentListBuilder":
        self._content_list.indent_level = indent_level
        return self

    def number(self, number: int) -> "ContentListBuilder":
        self._content_list.number = number
        return self

    def build(self) -> "ContentList":
        return self._content_list
