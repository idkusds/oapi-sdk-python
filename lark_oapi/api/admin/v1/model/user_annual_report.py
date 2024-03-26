# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .user_report2021 import UserReport2021
from .user_report2022 import UserReport2022
from .user_report2023 import UserReport2023


class UserAnnualReport(object):
    _types = {
        "year_2021": UserReport2021,
        "year_2022": UserReport2022,
        "year_2023": UserReport2023,
    }

    def __init__(self, d=None):
        self.year_2021: Optional[UserReport2021] = None
        self.year_2022: Optional[UserReport2022] = None
        self.year_2023: Optional[UserReport2023] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserAnnualReportBuilder":
        return UserAnnualReportBuilder()


class UserAnnualReportBuilder(object):
    def __init__(self) -> None:
        self._user_annual_report = UserAnnualReport()

    def year_2021(self, year_2021: UserReport2021) -> "UserAnnualReportBuilder":
        self._user_annual_report.year_2021 = year_2021
        return self

    def year_2022(self, year_2022: UserReport2022) -> "UserAnnualReportBuilder":
        self._user_annual_report.year_2022 = year_2022
        return self

    def year_2023(self, year_2023: UserReport2023) -> "UserAnnualReportBuilder":
        self._user_annual_report.year_2023 = year_2023
        return self

    def build(self) -> "UserAnnualReport":
        return self._user_annual_report
