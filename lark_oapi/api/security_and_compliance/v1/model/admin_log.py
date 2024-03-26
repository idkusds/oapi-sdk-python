# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class AdminLog(object):
    _types = {
        "unique_id": str,
        "user_id": str,
        "category_name": str,
        "event_name": str,
        "ip_address": str,
        "create_time": str,
        "content": str,
        "operation_status": int,
    }

    def __init__(self, d=None):
        self.unique_id: Optional[str] = None
        self.user_id: Optional[str] = None
        self.category_name: Optional[str] = None
        self.event_name: Optional[str] = None
        self.ip_address: Optional[str] = None
        self.create_time: Optional[str] = None
        self.content: Optional[str] = None
        self.operation_status: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AdminLogBuilder":
        return AdminLogBuilder()


class AdminLogBuilder(object):
    def __init__(self) -> None:
        self._admin_log = AdminLog()

    def unique_id(self, unique_id: str) -> "AdminLogBuilder":
        self._admin_log.unique_id = unique_id
        return self

    def user_id(self, user_id: str) -> "AdminLogBuilder":
        self._admin_log.user_id = user_id
        return self

    def category_name(self, category_name: str) -> "AdminLogBuilder":
        self._admin_log.category_name = category_name
        return self

    def event_name(self, event_name: str) -> "AdminLogBuilder":
        self._admin_log.event_name = event_name
        return self

    def ip_address(self, ip_address: str) -> "AdminLogBuilder":
        self._admin_log.ip_address = ip_address
        return self

    def create_time(self, create_time: str) -> "AdminLogBuilder":
        self._admin_log.create_time = create_time
        return self

    def content(self, content: str) -> "AdminLogBuilder":
        self._admin_log.content = content
        return self

    def operation_status(self, operation_status: int) -> "AdminLogBuilder":
        self._admin_log.operation_status = operation_status
        return self

    def build(self) -> "AdminLog":
        return self._admin_log
