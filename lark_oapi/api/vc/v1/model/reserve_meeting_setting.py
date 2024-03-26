# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .reserve_action_permission import ReserveActionPermission
from .reserve_call_setting import ReserveCallSetting
from .reserve_assign_host import ReserveAssignHost


class ReserveMeetingSetting(object):
    _types = {
        "topic": str,
        "action_permissions": List[ReserveActionPermission],
        "meeting_initial_type": int,
        "call_setting": ReserveCallSetting,
        "auto_record": bool,
        "assign_host_list": List[ReserveAssignHost],
    }

    def __init__(self, d=None):
        self.topic: Optional[str] = None
        self.action_permissions: Optional[List[ReserveActionPermission]] = None
        self.meeting_initial_type: Optional[int] = None
        self.call_setting: Optional[ReserveCallSetting] = None
        self.auto_record: Optional[bool] = None
        self.assign_host_list: Optional[List[ReserveAssignHost]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ReserveMeetingSettingBuilder":
        return ReserveMeetingSettingBuilder()


class ReserveMeetingSettingBuilder(object):
    def __init__(self) -> None:
        self._reserve_meeting_setting = ReserveMeetingSetting()

    def topic(self, topic: str) -> "ReserveMeetingSettingBuilder":
        self._reserve_meeting_setting.topic = topic
        return self

    def action_permissions(self, action_permissions: List[ReserveActionPermission]) -> "ReserveMeetingSettingBuilder":
        self._reserve_meeting_setting.action_permissions = action_permissions
        return self

    def meeting_initial_type(self, meeting_initial_type: int) -> "ReserveMeetingSettingBuilder":
        self._reserve_meeting_setting.meeting_initial_type = meeting_initial_type
        return self

    def call_setting(self, call_setting: ReserveCallSetting) -> "ReserveMeetingSettingBuilder":
        self._reserve_meeting_setting.call_setting = call_setting
        return self

    def auto_record(self, auto_record: bool) -> "ReserveMeetingSettingBuilder":
        self._reserve_meeting_setting.auto_record = auto_record
        return self

    def assign_host_list(self, assign_host_list: List[ReserveAssignHost]) -> "ReserveMeetingSettingBuilder":
        self._reserve_meeting_setting.assign_host_list = assign_host_list
        return self

    def build(self) -> "ReserveMeetingSetting":
        return self._reserve_meeting_setting
