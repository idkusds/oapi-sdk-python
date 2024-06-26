# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class AssignedOrganizationWithCode(object):
    _types = {
        "org_key": str,
        "org_ids": List[str],
        "org_codes": List[str],
    }

    def __init__(self, d=None):
        self.org_key: Optional[str] = None
        self.org_ids: Optional[List[str]] = None
        self.org_codes: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AssignedOrganizationWithCodeBuilder":
        return AssignedOrganizationWithCodeBuilder()


class AssignedOrganizationWithCodeBuilder(object):
    def __init__(self) -> None:
        self._assigned_organization_with_code = AssignedOrganizationWithCode()

    def org_key(self, org_key: str) -> "AssignedOrganizationWithCodeBuilder":
        self._assigned_organization_with_code.org_key = org_key
        return self

    def org_ids(self, org_ids: List[str]) -> "AssignedOrganizationWithCodeBuilder":
        self._assigned_organization_with_code.org_ids = org_ids
        return self

    def org_codes(self, org_codes: List[str]) -> "AssignedOrganizationWithCodeBuilder":
        self._assigned_organization_with_code.org_codes = org_codes
        return self

    def build(self) -> "AssignedOrganizationWithCode":
        return self._assigned_organization_with_code
