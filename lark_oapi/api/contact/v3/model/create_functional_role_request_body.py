# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class CreateFunctionalRoleRequestBody(object):
    _types = {
        "role_name": str,
    }

    def __init__(self, d=None):
        self.role_name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateFunctionalRoleRequestBodyBuilder":
        return CreateFunctionalRoleRequestBodyBuilder()


class CreateFunctionalRoleRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._create_functional_role_request_body = CreateFunctionalRoleRequestBody()

    def role_name(self, role_name: str) -> "CreateFunctionalRoleRequestBodyBuilder":
        self._create_functional_role_request_body.role_name = role_name
        return self

    def build(self) -> "CreateFunctionalRoleRequestBody":
        return self._create_functional_role_request_body
