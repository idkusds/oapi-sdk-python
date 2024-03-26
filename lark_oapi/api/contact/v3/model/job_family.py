# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n_content import I18nContent
from .i18n_content import I18nContent


class JobFamily(object):
    _types = {
        "name": str,
        "description": str,
        "parent_job_family_id": str,
        "status": bool,
        "i18n_name": List[I18nContent],
        "i18n_description": List[I18nContent],
        "job_family_id": str,
    }

    def __init__(self, d=None):
        self.name: Optional[str] = None
        self.description: Optional[str] = None
        self.parent_job_family_id: Optional[str] = None
        self.status: Optional[bool] = None
        self.i18n_name: Optional[List[I18nContent]] = None
        self.i18n_description: Optional[List[I18nContent]] = None
        self.job_family_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobFamilyBuilder":
        return JobFamilyBuilder()


class JobFamilyBuilder(object):
    def __init__(self) -> None:
        self._job_family = JobFamily()

    def name(self, name: str) -> "JobFamilyBuilder":
        self._job_family.name = name
        return self

    def description(self, description: str) -> "JobFamilyBuilder":
        self._job_family.description = description
        return self

    def parent_job_family_id(self, parent_job_family_id: str) -> "JobFamilyBuilder":
        self._job_family.parent_job_family_id = parent_job_family_id
        return self

    def status(self, status: bool) -> "JobFamilyBuilder":
        self._job_family.status = status
        return self

    def i18n_name(self, i18n_name: List[I18nContent]) -> "JobFamilyBuilder":
        self._job_family.i18n_name = i18n_name
        return self

    def i18n_description(self, i18n_description: List[I18nContent]) -> "JobFamilyBuilder":
        self._job_family.i18n_description = i18n_description
        return self

    def job_family_id(self, job_family_id: str) -> "JobFamilyBuilder":
        self._job_family.job_family_id = job_family_id
        return self

    def build(self) -> "JobFamily":
        return self._job_family
