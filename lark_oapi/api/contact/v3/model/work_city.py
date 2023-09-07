# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .i18n_content import I18nContent


class WorkCity(object):
    _types = {
        "work_city_id": str,
        "name": str,
        "i18n_name": List[I18nContent],
        "status": bool,
    }

    def __init__(self, d=None):
        self.work_city_id: Optional[str] = None
        self.name: Optional[str] = None
        self.i18n_name: Optional[List[I18nContent]] = None
        self.status: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WorkCityBuilder":
        return WorkCityBuilder()


class WorkCityBuilder(object):
    def __init__(self) -> None:
        self._work_city = WorkCity()

    def work_city_id(self, work_city_id: str) -> "WorkCityBuilder":
        self._work_city.work_city_id = work_city_id
        return self

    def name(self, name: str) -> "WorkCityBuilder":
        self._work_city.name = name
        return self

    def i18n_name(self, i18n_name: List[I18nContent]) -> "WorkCityBuilder":
        self._work_city.i18n_name = i18n_name
        return self

    def status(self, status: bool) -> "WorkCityBuilder":
        self._work_city.status = status
        return self

    def build(self) -> "WorkCity":
        return self._work_city
