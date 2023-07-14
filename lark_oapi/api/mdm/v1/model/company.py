# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class Company(object):
    _types = {
        "company_code": str,
        "company_name": str,
        "company_uid": str,
        "legal_entity_code": str,
        "co_area_code": str,
        "currency_code": str,
        "country_code": str,
        "company_name_en": str,
    }

    def __init__(self, d):
        self.company_code: Optional[str] = None
        self.company_name: Optional[str] = None
        self.company_uid: Optional[str] = None
        self.legal_entity_code: Optional[str] = None
        self.co_area_code: Optional[str] = None
        self.currency_code: Optional[str] = None
        self.country_code: Optional[str] = None
        self.company_name_en: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CompanyBuilder":
        return CompanyBuilder()


class CompanyBuilder(object):
    def __init__(self, company: Company = Company({})) -> None:
        self._company: Company = company
    
    def company_code(self, company_code: str) -> "CompanyBuilder":
        self._company.company_code = company_code
        return self
    
    def company_name(self, company_name: str) -> "CompanyBuilder":
        self._company.company_name = company_name
        return self
    
    def company_uid(self, company_uid: str) -> "CompanyBuilder":
        self._company.company_uid = company_uid
        return self
    
    def legal_entity_code(self, legal_entity_code: str) -> "CompanyBuilder":
        self._company.legal_entity_code = legal_entity_code
        return self
    
    def co_area_code(self, co_area_code: str) -> "CompanyBuilder":
        self._company.co_area_code = co_area_code
        return self
    
    def currency_code(self, currency_code: str) -> "CompanyBuilder":
        self._company.currency_code = currency_code
        return self
    
    def country_code(self, country_code: str) -> "CompanyBuilder":
        self._company.country_code = country_code
        return self
    
    def company_name_en(self, company_name_en: str) -> "CompanyBuilder":
        self._company.company_name_en = company_name_en
        return self
    
    def build(self) -> "Company":
        return self._company