# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .punch_time_simple_rule import PunchTimeSimpleRule


class UserTmpDailyShift(object):
    _types = {
        "group_id": str,
        "user_id": str,
        "date": int,
        "shift_name": str,
        "punch_time_simple_rules": List[PunchTimeSimpleRule],
    }

    def __init__(self, d=None):
        self.group_id: Optional[str] = None
        self.user_id: Optional[str] = None
        self.date: Optional[int] = None
        self.shift_name: Optional[str] = None
        self.punch_time_simple_rules: Optional[List[PunchTimeSimpleRule]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserTmpDailyShiftBuilder":
        return UserTmpDailyShiftBuilder()


class UserTmpDailyShiftBuilder(object):
    def __init__(self) -> None:
        self._user_tmp_daily_shift = UserTmpDailyShift()

    def group_id(self, group_id: str) -> "UserTmpDailyShiftBuilder":
        self._user_tmp_daily_shift.group_id = group_id
        return self

    def user_id(self, user_id: str) -> "UserTmpDailyShiftBuilder":
        self._user_tmp_daily_shift.user_id = user_id
        return self

    def date(self, date: int) -> "UserTmpDailyShiftBuilder":
        self._user_tmp_daily_shift.date = date
        return self

    def shift_name(self, shift_name: str) -> "UserTmpDailyShiftBuilder":
        self._user_tmp_daily_shift.shift_name = shift_name
        return self

    def punch_time_simple_rules(self, punch_time_simple_rules: List[PunchTimeSimpleRule]) -> "UserTmpDailyShiftBuilder":
        self._user_tmp_daily_shift.punch_time_simple_rules = punch_time_simple_rules
        return self

    def build(self) -> "UserTmpDailyShift":
        return self._user_tmp_daily_shift
