# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .application_basic_info import ApplicationBasicInfo
from .application_job import ApplicationJob
from .application_prehire_offer import ApplicationPrehireOffer
from .application_talent import ApplicationTalent


class ApplicationPrehire(object):
    _types = {
        "id": str,
        "basic_info": ApplicationBasicInfo,
        "talent": ApplicationTalent,
        "job": ApplicationJob,
        "offer": ApplicationPrehireOffer,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.basic_info: Optional[ApplicationBasicInfo] = None
        self.talent: Optional[ApplicationTalent] = None
        self.job: Optional[ApplicationJob] = None
        self.offer: Optional[ApplicationPrehireOffer] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApplicationPrehireBuilder":
        return ApplicationPrehireBuilder()


class ApplicationPrehireBuilder(object):
    def __init__(self) -> None:
        self._application_prehire = ApplicationPrehire()

    def id(self, id: str) -> "ApplicationPrehireBuilder":
        self._application_prehire.id = id
        return self

    def basic_info(self, basic_info: ApplicationBasicInfo) -> "ApplicationPrehireBuilder":
        self._application_prehire.basic_info = basic_info
        return self

    def talent(self, talent: ApplicationTalent) -> "ApplicationPrehireBuilder":
        self._application_prehire.talent = talent
        return self

    def job(self, job: ApplicationJob) -> "ApplicationPrehireBuilder":
        self._application_prehire.job = job
        return self

    def offer(self, offer: ApplicationPrehireOffer) -> "ApplicationPrehireBuilder":
        self._application_prehire.offer = offer
        return self

    def build(self) -> "ApplicationPrehire":
        return self._application_prehire
