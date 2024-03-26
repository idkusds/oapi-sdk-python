# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_app_role_member_response_body import ListAppRoleMemberResponseBody


class ListAppRoleMemberResponse(BaseResponse):
    _types = {
        "data": ListAppRoleMemberResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListAppRoleMemberResponseBody] = None
        init(self, d, self._types)
