# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_permission_public_password_response_body import CreatePermissionPublicPasswordResponseBody


class CreatePermissionPublicPasswordResponse(BaseResponse):
    _types = {
        "data": CreatePermissionPublicPasswordResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreatePermissionPublicPasswordResponseBody] = None
        init(self, d, self._types)
