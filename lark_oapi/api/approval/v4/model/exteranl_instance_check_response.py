# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .external_instance_task import ExternalInstanceTask


class ExteranlInstanceCheckResponse(object):
    _types = {
        "instance_id": str,
        "update_time": int,
        "tasks": List[ExternalInstanceTask],
    }

    def __init__(self, d=None):
        self.instance_id: Optional[str] = None
        self.update_time: Optional[int] = None
        self.tasks: Optional[List[ExternalInstanceTask]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ExteranlInstanceCheckResponseBuilder":
        return ExteranlInstanceCheckResponseBuilder()


class ExteranlInstanceCheckResponseBuilder(object):
    def __init__(self) -> None:
        self._exteranl_instance_check_response = ExteranlInstanceCheckResponse()

    def instance_id(self, instance_id: str) -> "ExteranlInstanceCheckResponseBuilder":
        self._exteranl_instance_check_response.instance_id = instance_id
        return self

    def update_time(self, update_time: int) -> "ExteranlInstanceCheckResponseBuilder":
        self._exteranl_instance_check_response.update_time = update_time
        return self

    def tasks(self, tasks: List[ExternalInstanceTask]) -> "ExteranlInstanceCheckResponseBuilder":
        self._exteranl_instance_check_response.tasks = tasks
        return self

    def build(self) -> "ExteranlInstanceCheckResponse":
        return self._exteranl_instance_check_response
