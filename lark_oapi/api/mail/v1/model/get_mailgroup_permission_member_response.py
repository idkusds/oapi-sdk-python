# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_mailgroup_permission_member_response_body import GetMailgroupPermissionMemberResponseBody


class GetMailgroupPermissionMemberResponse(BaseResponse):
    _types = {
        "data": GetMailgroupPermissionMemberResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetMailgroupPermissionMemberResponseBody] = None
        init(self, d, self._types)
