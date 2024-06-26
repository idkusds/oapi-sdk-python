# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class CreateTagFailReason(object):
    _types = {
        "duplicate_id": str,
    }

    def __init__(self, d=None):
        self.duplicate_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateTagFailReasonBuilder":
        return CreateTagFailReasonBuilder()


class CreateTagFailReasonBuilder(object):
    def __init__(self) -> None:
        self._create_tag_fail_reason = CreateTagFailReason()

    def duplicate_id(self, duplicate_id: str) -> "CreateTagFailReasonBuilder":
        self._create_tag_fail_reason.duplicate_id = duplicate_id
        return self

    def build(self) -> "CreateTagFailReason":
        return self._create_tag_fail_reason
