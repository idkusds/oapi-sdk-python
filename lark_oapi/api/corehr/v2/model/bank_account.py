# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .custom_field_data import CustomFieldData
from .enum import Enum


class BankAccount(object):
    _types = {
        "bank_name": str,
        "bank_account_number": str,
        "account_holder": str,
        "branch_name": str,
        "country_region_id": str,
        "bank_account_usage": List[Enum],
        "bank_account_type": Enum,
        "currency_id": str,
        "custom_fields": List[CustomFieldData],
    }

    def __init__(self, d=None):
        self.bank_name: Optional[str] = None
        self.bank_account_number: Optional[str] = None
        self.account_holder: Optional[str] = None
        self.branch_name: Optional[str] = None
        self.country_region_id: Optional[str] = None
        self.bank_account_usage: Optional[List[Enum]] = None
        self.bank_account_type: Optional[Enum] = None
        self.currency_id: Optional[str] = None
        self.custom_fields: Optional[List[CustomFieldData]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BankAccountBuilder":
        return BankAccountBuilder()


class BankAccountBuilder(object):
    def __init__(self) -> None:
        self._bank_account = BankAccount()

    def bank_name(self, bank_name: str) -> "BankAccountBuilder":
        self._bank_account.bank_name = bank_name
        return self

    def bank_account_number(self, bank_account_number: str) -> "BankAccountBuilder":
        self._bank_account.bank_account_number = bank_account_number
        return self

    def account_holder(self, account_holder: str) -> "BankAccountBuilder":
        self._bank_account.account_holder = account_holder
        return self

    def branch_name(self, branch_name: str) -> "BankAccountBuilder":
        self._bank_account.branch_name = branch_name
        return self

    def country_region_id(self, country_region_id: str) -> "BankAccountBuilder":
        self._bank_account.country_region_id = country_region_id
        return self

    def bank_account_usage(self, bank_account_usage: List[Enum]) -> "BankAccountBuilder":
        self._bank_account.bank_account_usage = bank_account_usage
        return self

    def bank_account_type(self, bank_account_type: Enum) -> "BankAccountBuilder":
        self._bank_account.bank_account_type = bank_account_type
        return self

    def currency_id(self, currency_id: str) -> "BankAccountBuilder":
        self._bank_account.currency_id = currency_id
        return self

    def custom_fields(self, custom_fields: List[CustomFieldData]) -> "BankAccountBuilder":
        self._bank_account.custom_fields = custom_fields
        return self

    def build(self) -> "BankAccount":
        return self._bank_account
