# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class JobProcessesStage(object):
    _types = {
        "id": str,
        "zh_name": str,
        "en_name": str,
        "type": int,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.zh_name: Optional[str] = None
        self.en_name: Optional[str] = None
        self.type: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobProcessesStageBuilder":
        return JobProcessesStageBuilder()


class JobProcessesStageBuilder(object):
    def __init__(self) -> None:
        self._job_processes_stage = JobProcessesStage()

    def id(self, id: str) -> "JobProcessesStageBuilder":
        self._job_processes_stage.id = id
        return self

    def zh_name(self, zh_name: str) -> "JobProcessesStageBuilder":
        self._job_processes_stage.zh_name = zh_name
        return self

    def en_name(self, en_name: str) -> "JobProcessesStageBuilder":
        self._job_processes_stage.en_name = en_name
        return self

    def type(self, type: int) -> "JobProcessesStageBuilder":
        self._job_processes_stage.type = type
        return self

    def build(self) -> "JobProcessesStage":
        return self._job_processes_stage
