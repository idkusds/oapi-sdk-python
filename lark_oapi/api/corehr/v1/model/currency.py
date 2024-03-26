# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n import I18n


class Currency(object):
    _types = {
        "id": str,
        "country_region_id": str,
        "currency_name": List[I18n],
        "numeric_code": int,
        "currency_alpha_3_code": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.country_region_id: Optional[str] = None
        self.currency_name: Optional[List[I18n]] = None
        self.numeric_code: Optional[int] = None
        self.currency_alpha_3_code: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CurrencyBuilder":
        return CurrencyBuilder()


class CurrencyBuilder(object):
    def __init__(self) -> None:
        self._currency = Currency()

    def id(self, id: str) -> "CurrencyBuilder":
        self._currency.id = id
        return self

    def country_region_id(self, country_region_id: str) -> "CurrencyBuilder":
        self._currency.country_region_id = country_region_id
        return self

    def currency_name(self, currency_name: List[I18n]) -> "CurrencyBuilder":
        self._currency.currency_name = currency_name
        return self

    def numeric_code(self, numeric_code: int) -> "CurrencyBuilder":
        self._currency.numeric_code = numeric_code
        return self

    def currency_alpha_3_code(self, currency_alpha_3_code: str) -> "CurrencyBuilder":
        self._currency.currency_alpha_3_code = currency_alpha_3_code
        return self

    def build(self) -> "Currency":
        return self._currency
