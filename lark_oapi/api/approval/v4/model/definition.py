# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class Definition(object):
    _types = {
        "approval_code": str,
        "approval_name": str,
        "group_name": str,
        "description": str,
        "icon_url": str,
        "group_code": str,
        "is_external": bool,
        "create_link_pc": str,
        "create_link_mobile": str,
    }

    def __init__(self, d=None):
        self.approval_code: Optional[str] = None
        self.approval_name: Optional[str] = None
        self.group_name: Optional[str] = None
        self.description: Optional[str] = None
        self.icon_url: Optional[str] = None
        self.group_code: Optional[str] = None
        self.is_external: Optional[bool] = None
        self.create_link_pc: Optional[str] = None
        self.create_link_mobile: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DefinitionBuilder":
        return DefinitionBuilder()


class DefinitionBuilder(object):
    def __init__(self) -> None:
        self._definition = Definition()

    def approval_code(self, approval_code: str) -> "DefinitionBuilder":
        self._definition.approval_code = approval_code
        return self

    def approval_name(self, approval_name: str) -> "DefinitionBuilder":
        self._definition.approval_name = approval_name
        return self

    def group_name(self, group_name: str) -> "DefinitionBuilder":
        self._definition.group_name = group_name
        return self

    def description(self, description: str) -> "DefinitionBuilder":
        self._definition.description = description
        return self

    def icon_url(self, icon_url: str) -> "DefinitionBuilder":
        self._definition.icon_url = icon_url
        return self

    def group_code(self, group_code: str) -> "DefinitionBuilder":
        self._definition.group_code = group_code
        return self

    def is_external(self, is_external: bool) -> "DefinitionBuilder":
        self._definition.is_external = is_external
        return self

    def create_link_pc(self, create_link_pc: str) -> "DefinitionBuilder":
        self._definition.create_link_pc = create_link_pc
        return self

    def create_link_mobile(self, create_link_mobile: str) -> "DefinitionBuilder":
        self._definition.create_link_mobile = create_link_mobile
        return self

    def build(self) -> "Definition":
        return self._definition
