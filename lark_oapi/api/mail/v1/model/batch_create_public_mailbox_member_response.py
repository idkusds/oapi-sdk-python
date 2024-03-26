# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .batch_create_public_mailbox_member_response_body import BatchCreatePublicMailboxMemberResponseBody


class BatchCreatePublicMailboxMemberResponse(BaseResponse):
    _types = {
        "data": BatchCreatePublicMailboxMemberResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[BatchCreatePublicMailboxMemberResponseBody] = None
        init(self, d, self._types)
