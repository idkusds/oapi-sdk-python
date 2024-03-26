# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ReadUser(object):
    _types = {
        "user_id_type": str,
        "user_id": str,
        "timestamp": str,
        "tenant_key": str,
    }

    def __init__(self, d=None):
        self.user_id_type: Optional[str] = None
        self.user_id: Optional[str] = None
        self.timestamp: Optional[str] = None
        self.tenant_key: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ReadUserBuilder":
        return ReadUserBuilder()


class ReadUserBuilder(object):
    def __init__(self) -> None:
        self._read_user = ReadUser()

    def user_id_type(self, user_id_type: str) -> "ReadUserBuilder":
        self._read_user.user_id_type = user_id_type
        return self

    def user_id(self, user_id: str) -> "ReadUserBuilder":
        self._read_user.user_id = user_id
        return self

    def timestamp(self, timestamp: str) -> "ReadUserBuilder":
        self._read_user.timestamp = timestamp
        return self

    def tenant_key(self, tenant_key: str) -> "ReadUserBuilder":
        self._read_user.tenant_key = tenant_key
        return self

    def build(self) -> "ReadUser":
        return self._read_user
