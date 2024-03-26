# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_job_requirement_response_body import CreateJobRequirementResponseBody


class CreateJobRequirementResponse(BaseResponse):
    _types = {
        "data": CreateJobRequirementResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateJobRequirementResponseBody] = None
        init(self, d, self._types)
