# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ProfileSettingBankAccount(object):
    _types = {
        "country_region": str,
        "bank_name": str,
        "branch_name": str,
        "account_holder": str,
        "bank_account_number": str,
        "bank_account_usages": List[str],
        "bank_account_type": str,
        "bank_id": str,
        "branch_id": str,
    }

    def __init__(self, d=None):
        self.country_region: Optional[str] = None
        self.bank_name: Optional[str] = None
        self.branch_name: Optional[str] = None
        self.account_holder: Optional[str] = None
        self.bank_account_number: Optional[str] = None
        self.bank_account_usages: Optional[List[str]] = None
        self.bank_account_type: Optional[str] = None
        self.bank_id: Optional[str] = None
        self.branch_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ProfileSettingBankAccountBuilder":
        return ProfileSettingBankAccountBuilder()


class ProfileSettingBankAccountBuilder(object):
    def __init__(self) -> None:
        self._profile_setting_bank_account = ProfileSettingBankAccount()

    def country_region(self, country_region: str) -> "ProfileSettingBankAccountBuilder":
        self._profile_setting_bank_account.country_region = country_region
        return self

    def bank_name(self, bank_name: str) -> "ProfileSettingBankAccountBuilder":
        self._profile_setting_bank_account.bank_name = bank_name
        return self

    def branch_name(self, branch_name: str) -> "ProfileSettingBankAccountBuilder":
        self._profile_setting_bank_account.branch_name = branch_name
        return self

    def account_holder(self, account_holder: str) -> "ProfileSettingBankAccountBuilder":
        self._profile_setting_bank_account.account_holder = account_holder
        return self

    def bank_account_number(self, bank_account_number: str) -> "ProfileSettingBankAccountBuilder":
        self._profile_setting_bank_account.bank_account_number = bank_account_number
        return self

    def bank_account_usages(self, bank_account_usages: List[str]) -> "ProfileSettingBankAccountBuilder":
        self._profile_setting_bank_account.bank_account_usages = bank_account_usages
        return self

    def bank_account_type(self, bank_account_type: str) -> "ProfileSettingBankAccountBuilder":
        self._profile_setting_bank_account.bank_account_type = bank_account_type
        return self

    def bank_id(self, bank_id: str) -> "ProfileSettingBankAccountBuilder":
        self._profile_setting_bank_account.bank_id = bank_id
        return self

    def branch_id(self, branch_id: str) -> "ProfileSettingBankAccountBuilder":
        self._profile_setting_bank_account.branch_id = branch_id
        return self

    def build(self) -> "ProfileSettingBankAccount":
        return self._profile_setting_bank_account
