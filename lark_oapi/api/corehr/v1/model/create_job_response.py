# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_job_response_body import CreateJobResponseBody


class CreateJobResponse(BaseResponse):
    _types = {
        "data": CreateJobResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateJobResponseBody] = None
        init(self, d, self._types)
