# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class JobRecruitmentType(object):
    _types = {
        "id": str,
        "zh_name": str,
        "en_name": str,
        "active_status": int,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.zh_name: Optional[str] = None
        self.en_name: Optional[str] = None
        self.active_status: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobRecruitmentTypeBuilder":
        return JobRecruitmentTypeBuilder()


class JobRecruitmentTypeBuilder(object):
    def __init__(self) -> None:
        self._job_recruitment_type = JobRecruitmentType()

    def id(self, id: str) -> "JobRecruitmentTypeBuilder":
        self._job_recruitment_type.id = id
        return self

    def zh_name(self, zh_name: str) -> "JobRecruitmentTypeBuilder":
        self._job_recruitment_type.zh_name = zh_name
        return self

    def en_name(self, en_name: str) -> "JobRecruitmentTypeBuilder":
        self._job_recruitment_type.en_name = en_name
        return self

    def active_status(self, active_status: int) -> "JobRecruitmentTypeBuilder":
        self._job_recruitment_type.active_status = active_status
        return self

    def build(self) -> "JobRecruitmentType":
        return self._job_recruitment_type
