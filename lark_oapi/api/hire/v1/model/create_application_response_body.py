# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class CreateApplicationResponseBody(object):
    _types = {
        "id": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateApplicationResponseBodyBuilder":
        return CreateApplicationResponseBodyBuilder()


class CreateApplicationResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_application_response_body = CreateApplicationResponseBody()

    def id(self, id: str) -> "CreateApplicationResponseBodyBuilder":
        self._create_application_response_body.id = id
        return self

    def build(self) -> "CreateApplicationResponseBody":
        return self._create_application_response_body
