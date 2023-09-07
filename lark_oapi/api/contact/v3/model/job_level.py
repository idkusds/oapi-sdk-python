# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .i18n_content import I18nContent


class JobLevel(object):
    _types = {
        "name": str,
        "description": str,
        "order": int,
        "status": bool,
        "job_level_id": str,
        "i18n_name": List[I18nContent],
        "i18n_description": List[I18nContent],
    }

    def __init__(self, d=None):
        self.name: Optional[str] = None
        self.description: Optional[str] = None
        self.order: Optional[int] = None
        self.status: Optional[bool] = None
        self.job_level_id: Optional[str] = None
        self.i18n_name: Optional[List[I18nContent]] = None
        self.i18n_description: Optional[List[I18nContent]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobLevelBuilder":
        return JobLevelBuilder()


class JobLevelBuilder(object):
    def __init__(self) -> None:
        self._job_level = JobLevel()

    def name(self, name: str) -> "JobLevelBuilder":
        self._job_level.name = name
        return self

    def description(self, description: str) -> "JobLevelBuilder":
        self._job_level.description = description
        return self

    def order(self, order: int) -> "JobLevelBuilder":
        self._job_level.order = order
        return self

    def status(self, status: bool) -> "JobLevelBuilder":
        self._job_level.status = status
        return self

    def job_level_id(self, job_level_id: str) -> "JobLevelBuilder":
        self._job_level.job_level_id = job_level_id
        return self

    def i18n_name(self, i18n_name: List[I18nContent]) -> "JobLevelBuilder":
        self._job_level.i18n_name = i18n_name
        return self

    def i18n_description(self, i18n_description: List[I18nContent]) -> "JobLevelBuilder":
        self._job_level.i18n_description = i18n_description
        return self

    def build(self) -> "JobLevel":
        return self._job_level
