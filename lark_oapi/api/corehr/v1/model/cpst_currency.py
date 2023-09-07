# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .cpst_i18n import CpstI18n


class CpstCurrency(object):
    _types = {
        "currency_id": str,
        "code": str,
        "name": CpstI18n,
    }

    def __init__(self, d=None):
        self.currency_id: Optional[str] = None
        self.code: Optional[str] = None
        self.name: Optional[CpstI18n] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CpstCurrencyBuilder":
        return CpstCurrencyBuilder()


class CpstCurrencyBuilder(object):
    def __init__(self) -> None:
        self._cpst_currency = CpstCurrency()

    def currency_id(self, currency_id: str) -> "CpstCurrencyBuilder":
        self._cpst_currency.currency_id = currency_id
        return self

    def code(self, code: str) -> "CpstCurrencyBuilder":
        self._cpst_currency.code = code
        return self

    def name(self, name: CpstI18n) -> "CpstCurrencyBuilder":
        self._cpst_currency.name = name
        return self

    def build(self) -> "CpstCurrency":
        return self._cpst_currency
