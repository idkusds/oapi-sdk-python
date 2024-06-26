# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .delete_app_feed_card_batch_response_body import DeleteAppFeedCardBatchResponseBody


class DeleteAppFeedCardBatchResponse(BaseResponse):
    _types = {
        "data": DeleteAppFeedCardBatchResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[DeleteAppFeedCardBatchResponseBody] = None
        init(self, d, self._types)
