# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .business_entity import BusinessEntity


class BusinessLicense(object):
    _types = {
        "entities": List[BusinessEntity],
    }

    def __init__(self, d=None):
        self.entities: Optional[List[BusinessEntity]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BusinessLicenseBuilder":
        return BusinessLicenseBuilder()


class BusinessLicenseBuilder(object):
    def __init__(self) -> None:
        self._business_license = BusinessLicense()

    def entities(self, entities: List[BusinessEntity]) -> "BusinessLicenseBuilder":
        self._business_license.entities = entities
        return self

    def build(self) -> "BusinessLicense":
        return self._business_license
