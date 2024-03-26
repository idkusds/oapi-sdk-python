# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .pre_hire import PreHire


class PatchPreHireResponseBody(object):
    _types = {
        "pre_hire": PreHire,
    }

    def __init__(self, d=None):
        self.pre_hire: Optional[PreHire] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchPreHireResponseBodyBuilder":
        return PatchPreHireResponseBodyBuilder()


class PatchPreHireResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._patch_pre_hire_response_body = PatchPreHireResponseBody()

    def pre_hire(self, pre_hire: PreHire) -> "PatchPreHireResponseBodyBuilder":
        self._patch_pre_hire_response_body.pre_hire = pre_hire
        return self

    def build(self) -> "PatchPreHireResponseBody":
        return self._patch_pre_hire_response_body
