# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .update_public_mailbox_response_body import UpdatePublicMailboxResponseBody


class UpdatePublicMailboxResponse(BaseResponse):
    _types = {
        "data": UpdatePublicMailboxResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[UpdatePublicMailboxResponseBody] = None
        init(self, d, self._types)
