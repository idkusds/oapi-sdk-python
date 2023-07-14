# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class ExtractEntityRequestBody(object):
    _types = {
        "text": str,
    }

    def __init__(self, d):
        self.text: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ExtractEntityRequestBodyBuilder":
        return ExtractEntityRequestBodyBuilder()


class ExtractEntityRequestBodyBuilder(object):
    def __init__(self, extract_entity_request_body: ExtractEntityRequestBody = ExtractEntityRequestBody({})) -> None:
        self._extract_entity_request_body: ExtractEntityRequestBody = extract_entity_request_body
    
    def text(self, text: str) -> "ExtractEntityRequestBodyBuilder":
        self._extract_entity_request_body.text = text
        return self
    
    def build(self) -> "ExtractEntityRequestBody":
        return self._extract_entity_request_body