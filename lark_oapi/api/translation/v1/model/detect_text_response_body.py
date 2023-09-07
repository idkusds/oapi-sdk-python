# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class DetectTextResponseBody(object):
    _types = {
        "language": str,
    }

    def __init__(self, d=None):
        self.language: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DetectTextResponseBodyBuilder":
        return DetectTextResponseBodyBuilder()


class DetectTextResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._detect_text_response_body = DetectTextResponseBody()

    def language(self, language: str) -> "DetectTextResponseBodyBuilder":
        self._detect_text_response_body.language = language
        return self

    def build(self) -> "DetectTextResponseBody":
        return self._detect_text_response_body
