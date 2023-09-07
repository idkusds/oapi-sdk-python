# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class CreateFunctionalRoleResponseBody(object):
    _types = {
        "role_id": str,
    }

    def __init__(self, d=None):
        self.role_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateFunctionalRoleResponseBodyBuilder":
        return CreateFunctionalRoleResponseBodyBuilder()


class CreateFunctionalRoleResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_functional_role_response_body = CreateFunctionalRoleResponseBody()

    def role_id(self, role_id: str) -> "CreateFunctionalRoleResponseBodyBuilder":
        self._create_functional_role_response_body.role_id = role_id
        return self

    def build(self) -> "CreateFunctionalRoleResponseBody":
        return self._create_functional_role_response_body
