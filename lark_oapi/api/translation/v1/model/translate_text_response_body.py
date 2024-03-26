# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class TranslateTextResponseBody(object):
    _types = {
        "text": str,
    }

    def __init__(self, d=None):
        self.text: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TranslateTextResponseBodyBuilder":
        return TranslateTextResponseBodyBuilder()


class TranslateTextResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._translate_text_response_body = TranslateTextResponseBody()

    def text(self, text: str) -> "TranslateTextResponseBodyBuilder":
        self._translate_text_response_body.text = text
        return self

    def build(self) -> "TranslateTextResponseBody":
        return self._translate_text_response_body
