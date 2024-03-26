# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .application_offer_basic_info import ApplicationOfferBasicInfo
from .application_offer_salary_plan import ApplicationOfferSalaryPlan
from .offer_job_info import OfferJobInfo
from .application_offer_custom_module import ApplicationOfferCustomModule


class Offer(object):
    _types = {
        "id": str,
        "application_id": str,
        "basic_info": ApplicationOfferBasicInfo,
        "salary_plan": ApplicationOfferSalaryPlan,
        "schema_id": str,
        "offer_status": int,
        "offer_type": int,
        "job_info": OfferJobInfo,
        "customized_module_list": List[ApplicationOfferCustomModule],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.application_id: Optional[str] = None
        self.basic_info: Optional[ApplicationOfferBasicInfo] = None
        self.salary_plan: Optional[ApplicationOfferSalaryPlan] = None
        self.schema_id: Optional[str] = None
        self.offer_status: Optional[int] = None
        self.offer_type: Optional[int] = None
        self.job_info: Optional[OfferJobInfo] = None
        self.customized_module_list: Optional[List[ApplicationOfferCustomModule]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OfferBuilder":
        return OfferBuilder()


class OfferBuilder(object):
    def __init__(self) -> None:
        self._offer = Offer()

    def id(self, id: str) -> "OfferBuilder":
        self._offer.id = id
        return self

    def application_id(self, application_id: str) -> "OfferBuilder":
        self._offer.application_id = application_id
        return self

    def basic_info(self, basic_info: ApplicationOfferBasicInfo) -> "OfferBuilder":
        self._offer.basic_info = basic_info
        return self

    def salary_plan(self, salary_plan: ApplicationOfferSalaryPlan) -> "OfferBuilder":
        self._offer.salary_plan = salary_plan
        return self

    def schema_id(self, schema_id: str) -> "OfferBuilder":
        self._offer.schema_id = schema_id
        return self

    def offer_status(self, offer_status: int) -> "OfferBuilder":
        self._offer.offer_status = offer_status
        return self

    def offer_type(self, offer_type: int) -> "OfferBuilder":
        self._offer.offer_type = offer_type
        return self

    def job_info(self, job_info: OfferJobInfo) -> "OfferBuilder":
        self._offer.job_info = job_info
        return self

    def customized_module_list(self, customized_module_list: List[ApplicationOfferCustomModule]) -> "OfferBuilder":
        self._offer.customized_module_list = customized_module_list
        return self

    def build(self) -> "Offer":
        return self._offer
