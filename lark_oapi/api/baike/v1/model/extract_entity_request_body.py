# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class ExtractEntityRequestBody(object):
    _types = {
        "text": str,
    }

    def __init__(self, d=None):
        self.text: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ExtractEntityRequestBodyBuilder":
        return ExtractEntityRequestBodyBuilder()


class ExtractEntityRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._extract_entity_request_body = ExtractEntityRequestBody()

    def text(self, text: str) -> "ExtractEntityRequestBodyBuilder":
        self._extract_entity_request_body.text = text
        return self

    def build(self) -> "ExtractEntityRequestBody":
        return self._extract_entity_request_body
