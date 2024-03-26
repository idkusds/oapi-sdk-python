# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class MyAiVcMeetingContentCommonResult(object):
    _types = {
        "meeting_content_reply": str,
    }

    def __init__(self, d=None):
        self.meeting_content_reply: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MyAiVcMeetingContentCommonResultBuilder":
        return MyAiVcMeetingContentCommonResultBuilder()


class MyAiVcMeetingContentCommonResultBuilder(object):
    def __init__(self) -> None:
        self._my_ai_vc_meeting_content_common_result = MyAiVcMeetingContentCommonResult()

    def meeting_content_reply(self, meeting_content_reply: str) -> "MyAiVcMeetingContentCommonResultBuilder":
        self._my_ai_vc_meeting_content_common_result.meeting_content_reply = meeting_content_reply
        return self

    def build(self) -> "MyAiVcMeetingContentCommonResult":
        return self._my_ai_vc_meeting_content_common_result
