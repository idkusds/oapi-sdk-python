# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class JobLevel(object):
    _types = {
        "id": int,
        "name": str,
    }

    def __init__(self, d=None):
        self.id: Optional[int] = None
        self.name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobLevelBuilder":
        return JobLevelBuilder()


class JobLevelBuilder(object):
    def __init__(self) -> None:
        self._job_level = JobLevel()

    def id(self, id: int) -> "JobLevelBuilder":
        self._job_level.id = id
        return self

    def name(self, name: str) -> "JobLevelBuilder":
        self._job_level.name = name
        return self

    def build(self) -> "JobLevel":
        return self._job_level
