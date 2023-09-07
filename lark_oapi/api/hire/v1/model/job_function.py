# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .i18n import I18n


class JobFunction(object):
    _types = {
        "id": str,
        "name": I18n,
        "active_status": int,
        "parent_id": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[I18n] = None
        self.active_status: Optional[int] = None
        self.parent_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobFunctionBuilder":
        return JobFunctionBuilder()


class JobFunctionBuilder(object):
    def __init__(self) -> None:
        self._job_function = JobFunction()

    def id(self, id: str) -> "JobFunctionBuilder":
        self._job_function.id = id
        return self

    def name(self, name: I18n) -> "JobFunctionBuilder":
        self._job_function.name = name
        return self

    def active_status(self, active_status: int) -> "JobFunctionBuilder":
        self._job_function.active_status = active_status
        return self

    def parent_id(self, parent_id: str) -> "JobFunctionBuilder":
        self._job_function.parent_id = parent_id
        return self

    def build(self) -> "JobFunction":
        return self._job_function
