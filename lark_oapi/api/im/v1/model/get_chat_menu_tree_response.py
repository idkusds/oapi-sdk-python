# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_chat_menu_tree_response_body import GetChatMenuTreeResponseBody


class GetChatMenuTreeResponse(BaseResponse):
    _types = {
        "data": GetChatMenuTreeResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetChatMenuTreeResponseBody] = None
        init(self, d, self._types)
