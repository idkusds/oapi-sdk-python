# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .meeting_user import MeetingUser


class KickoutMeetingRequestBody(object):
    _types = {
        "kickout_users": List[MeetingUser],
    }

    def __init__(self, d=None):
        self.kickout_users: Optional[List[MeetingUser]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "KickoutMeetingRequestBodyBuilder":
        return KickoutMeetingRequestBodyBuilder()


class KickoutMeetingRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._kickout_meeting_request_body = KickoutMeetingRequestBody()

    def kickout_users(self, kickout_users: List[MeetingUser]) -> "KickoutMeetingRequestBodyBuilder":
        self._kickout_meeting_request_body.kickout_users = kickout_users
        return self

    def build(self) -> "KickoutMeetingRequestBody":
        return self._kickout_meeting_request_body
