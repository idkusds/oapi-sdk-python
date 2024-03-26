# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .report import Report


class GetDailyReportResponseBody(object):
    _types = {
        "meeting_report": Report,
    }

    def __init__(self, d=None):
        self.meeting_report: Optional[Report] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetDailyReportResponseBodyBuilder":
        return GetDailyReportResponseBodyBuilder()


class GetDailyReportResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_daily_report_response_body = GetDailyReportResponseBody()

    def meeting_report(self, meeting_report: Report) -> "GetDailyReportResponseBodyBuilder":
        self._get_daily_report_response_body.meeting_report = meeting_report
        return self

    def build(self) -> "GetDailyReportResponseBody":
        return self._get_daily_report_response_body
