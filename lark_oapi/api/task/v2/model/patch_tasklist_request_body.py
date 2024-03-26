# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .input_tasklist import InputTasklist


class PatchTasklistRequestBody(object):
    _types = {
        "tasklist": InputTasklist,
        "update_fields": List[str],
        "origin_owner_to_role": str,
    }

    def __init__(self, d=None):
        self.tasklist: Optional[InputTasklist] = None
        self.update_fields: Optional[List[str]] = None
        self.origin_owner_to_role: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchTasklistRequestBodyBuilder":
        return PatchTasklistRequestBodyBuilder()


class PatchTasklistRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._patch_tasklist_request_body = PatchTasklistRequestBody()

    def tasklist(self, tasklist: InputTasklist) -> "PatchTasklistRequestBodyBuilder":
        self._patch_tasklist_request_body.tasklist = tasklist
        return self

    def update_fields(self, update_fields: List[str]) -> "PatchTasklistRequestBodyBuilder":
        self._patch_tasklist_request_body.update_fields = update_fields
        return self

    def origin_owner_to_role(self, origin_owner_to_role: str) -> "PatchTasklistRequestBodyBuilder":
        self._patch_tasklist_request_body.origin_owner_to_role = origin_owner_to_role
        return self

    def build(self) -> "PatchTasklistRequestBody":
        return self._patch_tasklist_request_body
