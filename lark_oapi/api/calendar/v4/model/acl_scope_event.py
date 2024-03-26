# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .user_id import UserId


class AclScopeEvent(object):
    _types = {
        "type": str,
        "user_id": UserId,
    }

    def __init__(self, d=None):
        self.type: Optional[str] = None
        self.user_id: Optional[UserId] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AclScopeEventBuilder":
        return AclScopeEventBuilder()


class AclScopeEventBuilder(object):
    def __init__(self) -> None:
        self._acl_scope_event = AclScopeEvent()

    def type(self, type: str) -> "AclScopeEventBuilder":
        self._acl_scope_event.type = type
        return self

    def user_id(self, user_id: UserId) -> "AclScopeEventBuilder":
        self._acl_scope_event.user_id = user_id
        return self

    def build(self) -> "AclScopeEvent":
        return self._acl_scope_event
