# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .update_job_family_response_body import UpdateJobFamilyResponseBody


class UpdateJobFamilyResponse(BaseResponse):
    _types = {
        "data": UpdateJobFamilyResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[UpdateJobFamilyResponseBody] = None
        init(self, d, self._types)
