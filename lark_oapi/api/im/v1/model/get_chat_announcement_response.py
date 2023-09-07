# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_chat_announcement_response_body import GetChatAnnouncementResponseBody


class GetChatAnnouncementResponse(BaseResponse):
    _types = {
        "data": GetChatAnnouncementResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetChatAnnouncementResponseBody] = None
        init(self, d, self._types)
