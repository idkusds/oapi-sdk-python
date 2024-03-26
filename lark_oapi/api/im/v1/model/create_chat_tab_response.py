# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_chat_tab_response_body import CreateChatTabResponseBody


class CreateChatTabResponse(BaseResponse):
    _types = {
        "data": CreateChatTabResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateChatTabResponseBody] = None
        init(self, d, self._types)
