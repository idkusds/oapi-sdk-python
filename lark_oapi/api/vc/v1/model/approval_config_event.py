# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .subscribe_user_event import SubscribeUserEvent


class ApprovalConfigEvent(object):
    _types = {
        "approval_switch": int,
        "approval_condition": int,
        "meeting_duration": float,
        "approvers": List[SubscribeUserEvent],
    }

    def __init__(self, d=None):
        self.approval_switch: Optional[int] = None
        self.approval_condition: Optional[int] = None
        self.meeting_duration: Optional[float] = None
        self.approvers: Optional[List[SubscribeUserEvent]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApprovalConfigEventBuilder":
        return ApprovalConfigEventBuilder()


class ApprovalConfigEventBuilder(object):
    def __init__(self) -> None:
        self._approval_config_event = ApprovalConfigEvent()

    def approval_switch(self, approval_switch: int) -> "ApprovalConfigEventBuilder":
        self._approval_config_event.approval_switch = approval_switch
        return self

    def approval_condition(self, approval_condition: int) -> "ApprovalConfigEventBuilder":
        self._approval_config_event.approval_condition = approval_condition
        return self

    def meeting_duration(self, meeting_duration: float) -> "ApprovalConfigEventBuilder":
        self._approval_config_event.meeting_duration = meeting_duration
        return self

    def approvers(self, approvers: List[SubscribeUserEvent]) -> "ApprovalConfigEventBuilder":
        self._approval_config_event.approvers = approvers
        return self

    def build(self) -> "ApprovalConfigEvent":
        return self._approval_config_event
