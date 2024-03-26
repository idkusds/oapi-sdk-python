# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .entity import Entity


class SearchEntityResponseBody(object):
    _types = {
        "entities": List[Entity],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.entities: Optional[List[Entity]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchEntityResponseBodyBuilder":
        return SearchEntityResponseBodyBuilder()


class SearchEntityResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._search_entity_response_body = SearchEntityResponseBody()

    def entities(self, entities: List[Entity]) -> "SearchEntityResponseBodyBuilder":
        self._search_entity_response_body.entities = entities
        return self

    def page_token(self, page_token: str) -> "SearchEntityResponseBodyBuilder":
        self._search_entity_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "SearchEntityResponseBodyBuilder":
        self._search_entity_response_body.has_more = has_more
        return self

    def build(self) -> "SearchEntityResponseBody":
        return self._search_entity_response_body
