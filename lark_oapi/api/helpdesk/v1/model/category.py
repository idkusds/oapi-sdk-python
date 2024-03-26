# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class Category(object):
    _types = {
        "category_id": str,
        "id": str,
        "name": str,
        "parent_id": str,
        "helpdesk_id": str,
        "language": str,
    }

    def __init__(self, d=None):
        self.category_id: Optional[str] = None
        self.id: Optional[str] = None
        self.name: Optional[str] = None
        self.parent_id: Optional[str] = None
        self.helpdesk_id: Optional[str] = None
        self.language: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CategoryBuilder":
        return CategoryBuilder()


class CategoryBuilder(object):
    def __init__(self) -> None:
        self._category = Category()

    def category_id(self, category_id: str) -> "CategoryBuilder":
        self._category.category_id = category_id
        return self

    def id(self, id: str) -> "CategoryBuilder":
        self._category.id = id
        return self

    def name(self, name: str) -> "CategoryBuilder":
        self._category.name = name
        return self

    def parent_id(self, parent_id: str) -> "CategoryBuilder":
        self._category.parent_id = parent_id
        return self

    def helpdesk_id(self, helpdesk_id: str) -> "CategoryBuilder":
        self._category.helpdesk_id = helpdesk_id
        return self

    def language(self, language: str) -> "CategoryBuilder":
        self._category.language = language
        return self

    def build(self) -> "Category":
        return self._category
