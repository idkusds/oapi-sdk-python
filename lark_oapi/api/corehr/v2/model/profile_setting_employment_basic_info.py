# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .profile_setting_phone import ProfileSettingPhone
from .profile_setting_custom_field import ProfileSettingCustomField


class ProfileSettingEmploymentBasicInfo(object):
    _types = {
        "employee_number": str,
        "effective_time": str,
        "regular_employee_start_date": str,
        "seniority_date": str,
        "work_email": str,
        "phone": ProfileSettingPhone,
        "custom_fields": List[ProfileSettingCustomField],
    }

    def __init__(self, d=None):
        self.employee_number: Optional[str] = None
        self.effective_time: Optional[str] = None
        self.regular_employee_start_date: Optional[str] = None
        self.seniority_date: Optional[str] = None
        self.work_email: Optional[str] = None
        self.phone: Optional[ProfileSettingPhone] = None
        self.custom_fields: Optional[List[ProfileSettingCustomField]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ProfileSettingEmploymentBasicInfoBuilder":
        return ProfileSettingEmploymentBasicInfoBuilder()


class ProfileSettingEmploymentBasicInfoBuilder(object):
    def __init__(self) -> None:
        self._profile_setting_employment_basic_info = ProfileSettingEmploymentBasicInfo()

    def employee_number(self, employee_number: str) -> "ProfileSettingEmploymentBasicInfoBuilder":
        self._profile_setting_employment_basic_info.employee_number = employee_number
        return self

    def effective_time(self, effective_time: str) -> "ProfileSettingEmploymentBasicInfoBuilder":
        self._profile_setting_employment_basic_info.effective_time = effective_time
        return self

    def regular_employee_start_date(self,
                                    regular_employee_start_date: str) -> "ProfileSettingEmploymentBasicInfoBuilder":
        self._profile_setting_employment_basic_info.regular_employee_start_date = regular_employee_start_date
        return self

    def seniority_date(self, seniority_date: str) -> "ProfileSettingEmploymentBasicInfoBuilder":
        self._profile_setting_employment_basic_info.seniority_date = seniority_date
        return self

    def work_email(self, work_email: str) -> "ProfileSettingEmploymentBasicInfoBuilder":
        self._profile_setting_employment_basic_info.work_email = work_email
        return self

    def phone(self, phone: ProfileSettingPhone) -> "ProfileSettingEmploymentBasicInfoBuilder":
        self._profile_setting_employment_basic_info.phone = phone
        return self

    def custom_fields(self,
                      custom_fields: List[ProfileSettingCustomField]) -> "ProfileSettingEmploymentBasicInfoBuilder":
        self._profile_setting_employment_basic_info.custom_fields = custom_fields
        return self

    def build(self) -> "ProfileSettingEmploymentBasicInfo":
        return self._profile_setting_employment_basic_info