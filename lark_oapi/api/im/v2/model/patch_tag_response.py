# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .patch_tag_response_body import PatchTagResponseBody


class PatchTagResponse(BaseResponse):
    _types = {
        "data": PatchTagResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[PatchTagResponseBody] = None
        init(self, d, self._types)