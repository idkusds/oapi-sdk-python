# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .config_job_response_body import ConfigJobResponseBody


class ConfigJobResponse(BaseResponse):
    _types = {
        "data": ConfigJobResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ConfigJobResponseBody] = None
        init(self, d, self._types)
