# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .profile_setting_phone import ProfileSettingPhone
from .profile_setting_custom_field import ProfileSettingCustomField


class ProfileSettingEmpBasicInfoForUpdate(object):
    _types = {
        "employee_number": str,
        "regular_employee_start_date": str,
        "seniority_date": str,
        "work_email": str,
        "phone": ProfileSettingPhone,
        "custom_fields": List[ProfileSettingCustomField],
    }

    def __init__(self, d=None):
        self.employee_number: Optional[str] = None
        self.regular_employee_start_date: Optional[str] = None
        self.seniority_date: Optional[str] = None
        self.work_email: Optional[str] = None
        self.phone: Optional[ProfileSettingPhone] = None
        self.custom_fields: Optional[List[ProfileSettingCustomField]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ProfileSettingEmpBasicInfoForUpdateBuilder":
        return ProfileSettingEmpBasicInfoForUpdateBuilder()


class ProfileSettingEmpBasicInfoForUpdateBuilder(object):
    def __init__(self) -> None:
        self._profile_setting_emp_basic_info_for_update = ProfileSettingEmpBasicInfoForUpdate()

    def employee_number(self, employee_number: str) -> "ProfileSettingEmpBasicInfoForUpdateBuilder":
        self._profile_setting_emp_basic_info_for_update.employee_number = employee_number
        return self

    def regular_employee_start_date(self,
                                    regular_employee_start_date: str) -> "ProfileSettingEmpBasicInfoForUpdateBuilder":
        self._profile_setting_emp_basic_info_for_update.regular_employee_start_date = regular_employee_start_date
        return self

    def seniority_date(self, seniority_date: str) -> "ProfileSettingEmpBasicInfoForUpdateBuilder":
        self._profile_setting_emp_basic_info_for_update.seniority_date = seniority_date
        return self

    def work_email(self, work_email: str) -> "ProfileSettingEmpBasicInfoForUpdateBuilder":
        self._profile_setting_emp_basic_info_for_update.work_email = work_email
        return self

    def phone(self, phone: ProfileSettingPhone) -> "ProfileSettingEmpBasicInfoForUpdateBuilder":
        self._profile_setting_emp_basic_info_for_update.phone = phone
        return self

    def custom_fields(self,
                      custom_fields: List[ProfileSettingCustomField]) -> "ProfileSettingEmpBasicInfoForUpdateBuilder":
        self._profile_setting_emp_basic_info_for_update.custom_fields = custom_fields
        return self

    def build(self) -> "ProfileSettingEmpBasicInfoForUpdate":
        return self._profile_setting_emp_basic_info_for_update
