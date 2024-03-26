# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class SystemStatusUserOpenParam(object):
    _types = {
        "user_id": str,
        "end_time": str,
    }

    def __init__(self, d=None):
        self.user_id: Optional[str] = None
        self.end_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SystemStatusUserOpenParamBuilder":
        return SystemStatusUserOpenParamBuilder()


class SystemStatusUserOpenParamBuilder(object):
    def __init__(self) -> None:
        self._system_status_user_open_param = SystemStatusUserOpenParam()

    def user_id(self, user_id: str) -> "SystemStatusUserOpenParamBuilder":
        self._system_status_user_open_param.user_id = user_id
        return self

    def end_time(self, end_time: str) -> "SystemStatusUserOpenParamBuilder":
        self._system_status_user_open_param.end_time = end_time
        return self

    def build(self) -> "SystemStatusUserOpenParam":
        return self._system_status_user_open_param
