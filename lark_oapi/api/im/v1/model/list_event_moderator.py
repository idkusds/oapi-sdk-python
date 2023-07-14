# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .user_id import UserId


class ListEventModerator(object):
    _types = {
        "tenant_key": str,
        "user_id": UserId,
    }

    def __init__(self, d):
        self.tenant_key: Optional[str] = None
        self.user_id: Optional[UserId] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListEventModeratorBuilder":
        return ListEventModeratorBuilder()


class ListEventModeratorBuilder(object):
    def __init__(self, list_event_moderator: ListEventModerator = ListEventModerator({})) -> None:
        self._list_event_moderator: ListEventModerator = list_event_moderator
    
    def tenant_key(self, tenant_key: str) -> "ListEventModeratorBuilder":
        self._list_event_moderator.tenant_key = tenant_key
        return self
    
    def user_id(self, user_id: UserId) -> "ListEventModeratorBuilder":
        self._list_event_moderator.user_id = user_id
        return self
    
    def build(self) -> "ListEventModerator":
        return self._list_event_moderator