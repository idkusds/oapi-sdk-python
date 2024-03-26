# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .workhour import Workhour


class WorkhourSetting(object):
    _types = {
        "timezone": str,
        "workhours": List[Workhour],
        "enable_work_hour": bool,
        "user_id": str,
    }

    def __init__(self, d=None):
        self.timezone: Optional[str] = None
        self.workhours: Optional[List[Workhour]] = None
        self.enable_work_hour: Optional[bool] = None
        self.user_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WorkhourSettingBuilder":
        return WorkhourSettingBuilder()


class WorkhourSettingBuilder(object):
    def __init__(self) -> None:
        self._workhour_setting = WorkhourSetting()

    def timezone(self, timezone: str) -> "WorkhourSettingBuilder":
        self._workhour_setting.timezone = timezone
        return self

    def workhours(self, workhours: List[Workhour]) -> "WorkhourSettingBuilder":
        self._workhour_setting.workhours = workhours
        return self

    def enable_work_hour(self, enable_work_hour: bool) -> "WorkhourSettingBuilder":
        self._workhour_setting.enable_work_hour = enable_work_hour
        return self

    def user_id(self, user_id: str) -> "WorkhourSettingBuilder":
        self._workhour_setting.user_id = user_id
        return self

    def build(self) -> "WorkhourSetting":
        return self._workhour_setting
