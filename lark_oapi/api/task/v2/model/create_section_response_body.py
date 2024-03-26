# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .section import Section


class CreateSectionResponseBody(object):
    _types = {
        "section": Section,
    }

    def __init__(self, d=None):
        self.section: Optional[Section] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateSectionResponseBodyBuilder":
        return CreateSectionResponseBodyBuilder()


class CreateSectionResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_section_response_body = CreateSectionResponseBody()

    def section(self, section: Section) -> "CreateSectionResponseBodyBuilder":
        self._create_section_response_body.section = section
        return self

    def build(self) -> "CreateSectionResponseBody":
        return self._create_section_response_body
