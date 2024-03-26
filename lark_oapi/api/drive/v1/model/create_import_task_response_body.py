# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class CreateImportTaskResponseBody(object):
    _types = {
        "ticket": str,
    }

    def __init__(self, d=None):
        self.ticket: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateImportTaskResponseBodyBuilder":
        return CreateImportTaskResponseBodyBuilder()


class CreateImportTaskResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_import_task_response_body = CreateImportTaskResponseBody()

    def ticket(self, ticket: str) -> "CreateImportTaskResponseBodyBuilder":
        self._create_import_task_response_body.ticket = ticket
        return self

    def build(self) -> "CreateImportTaskResponseBody":
        return self._create_import_task_response_body
