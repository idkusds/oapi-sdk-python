# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .i18n import I18n
from .object_field_data import ObjectFieldData


class WorkingHoursType(object):
    _types = {
        "id": str,
        "code": str,
        "name": List[I18n],
        "country_region_id_list": List[str],
        "default_for_job": bool,
        "active": bool,
        "custom_fields": List[ObjectFieldData],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.code: Optional[str] = None
        self.name: Optional[List[I18n]] = None
        self.country_region_id_list: Optional[List[str]] = None
        self.default_for_job: Optional[bool] = None
        self.active: Optional[bool] = None
        self.custom_fields: Optional[List[ObjectFieldData]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WorkingHoursTypeBuilder":
        return WorkingHoursTypeBuilder()


class WorkingHoursTypeBuilder(object):
    def __init__(self) -> None:
        self._working_hours_type = WorkingHoursType()

    def id(self, id: str) -> "WorkingHoursTypeBuilder":
        self._working_hours_type.id = id
        return self

    def code(self, code: str) -> "WorkingHoursTypeBuilder":
        self._working_hours_type.code = code
        return self

    def name(self, name: List[I18n]) -> "WorkingHoursTypeBuilder":
        self._working_hours_type.name = name
        return self

    def country_region_id_list(self, country_region_id_list: List[str]) -> "WorkingHoursTypeBuilder":
        self._working_hours_type.country_region_id_list = country_region_id_list
        return self

    def default_for_job(self, default_for_job: bool) -> "WorkingHoursTypeBuilder":
        self._working_hours_type.default_for_job = default_for_job
        return self

    def active(self, active: bool) -> "WorkingHoursTypeBuilder":
        self._working_hours_type.active = active
        return self

    def custom_fields(self, custom_fields: List[ObjectFieldData]) -> "WorkingHoursTypeBuilder":
        self._working_hours_type.custom_fields = custom_fields
        return self

    def build(self) -> "WorkingHoursType":
        return self._working_hours_type
