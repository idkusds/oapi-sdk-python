# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .batch_get_tmp_download_url_media_response_body import BatchGetTmpDownloadUrlMediaResponseBody


class BatchGetTmpDownloadUrlMediaResponse(BaseResponse):
    _types = {
        "data": BatchGetTmpDownloadUrlMediaResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[BatchGetTmpDownloadUrlMediaResponseBody] = None
        init(self, d, self._types)
