# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_message_reaction_response_body import ListMessageReactionResponseBody


class ListMessageReactionResponse(BaseResponse):
    _types = {
        "data": ListMessageReactionResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListMessageReactionResponseBody] = None
        init(self, d, self._types)
