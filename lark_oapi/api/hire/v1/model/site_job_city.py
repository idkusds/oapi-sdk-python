# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .site_name import SiteName


class SiteJobCity(object):
    _types = {
        "city_code": str,
        "name": SiteName,
    }

    def __init__(self, d):
        self.city_code: Optional[str] = None
        self.name: Optional[SiteName] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SiteJobCityBuilder":
        return SiteJobCityBuilder()


class SiteJobCityBuilder(object):
    def __init__(self, site_job_city: SiteJobCity = SiteJobCity({})) -> None:
        self._site_job_city: SiteJobCity = site_job_city
    
    def city_code(self, city_code: str) -> "SiteJobCityBuilder":
        self._site_job_city.city_code = city_code
        return self
    
    def name(self, name: SiteName) -> "SiteJobCityBuilder":
        self._site_job_city.name = name
        return self
    
    def build(self) -> "SiteJobCity":
        return self._site_job_city