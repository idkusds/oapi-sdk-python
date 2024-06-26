# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class PatchTagFailReason(object):
    _types = {
        "duplicate_id": str,
    }

    def __init__(self, d=None):
        self.duplicate_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchTagFailReasonBuilder":
        return PatchTagFailReasonBuilder()


class PatchTagFailReasonBuilder(object):
    def __init__(self) -> None:
        self._patch_tag_fail_reason = PatchTagFailReason()

    def duplicate_id(self, duplicate_id: str) -> "PatchTagFailReasonBuilder":
        self._patch_tag_fail_reason.duplicate_id = duplicate_id
        return self

    def build(self) -> "PatchTagFailReason":
        return self._patch_tag_fail_reason
