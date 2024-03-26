# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .enum import Enum
from .hiberarchy_common import HiberarchyCommon
from .object_field_data import ObjectFieldData
from .enum import Enum


class DepartmentCreate(object):
    _types = {
        "id": str,
        "sub_type": Enum,
        "manager": str,
        "is_confidential": bool,
        "hiberarchy_common": HiberarchyCommon,
        "effective_time": str,
        "expiration_time": str,
        "custom_fields": List[ObjectFieldData],
        "cost_center_id": str,
        "staffing_model": Enum,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.sub_type: Optional[Enum] = None
        self.manager: Optional[str] = None
        self.is_confidential: Optional[bool] = None
        self.hiberarchy_common: Optional[HiberarchyCommon] = None
        self.effective_time: Optional[str] = None
        self.expiration_time: Optional[str] = None
        self.custom_fields: Optional[List[ObjectFieldData]] = None
        self.cost_center_id: Optional[str] = None
        self.staffing_model: Optional[Enum] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DepartmentCreateBuilder":
        return DepartmentCreateBuilder()


class DepartmentCreateBuilder(object):
    def __init__(self) -> None:
        self._department_create = DepartmentCreate()

    def id(self, id: str) -> "DepartmentCreateBuilder":
        self._department_create.id = id
        return self

    def sub_type(self, sub_type: Enum) -> "DepartmentCreateBuilder":
        self._department_create.sub_type = sub_type
        return self

    def manager(self, manager: str) -> "DepartmentCreateBuilder":
        self._department_create.manager = manager
        return self

    def is_confidential(self, is_confidential: bool) -> "DepartmentCreateBuilder":
        self._department_create.is_confidential = is_confidential
        return self

    def hiberarchy_common(self, hiberarchy_common: HiberarchyCommon) -> "DepartmentCreateBuilder":
        self._department_create.hiberarchy_common = hiberarchy_common
        return self

    def effective_time(self, effective_time: str) -> "DepartmentCreateBuilder":
        self._department_create.effective_time = effective_time
        return self

    def expiration_time(self, expiration_time: str) -> "DepartmentCreateBuilder":
        self._department_create.expiration_time = expiration_time
        return self

    def custom_fields(self, custom_fields: List[ObjectFieldData]) -> "DepartmentCreateBuilder":
        self._department_create.custom_fields = custom_fields
        return self

    def cost_center_id(self, cost_center_id: str) -> "DepartmentCreateBuilder":
        self._department_create.cost_center_id = cost_center_id
        return self

    def staffing_model(self, staffing_model: Enum) -> "DepartmentCreateBuilder":
        self._department_create.staffing_model = staffing_model
        return self

    def build(self) -> "DepartmentCreate":
        return self._department_create
