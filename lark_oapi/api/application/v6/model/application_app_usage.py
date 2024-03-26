# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ApplicationAppUsage(object):
    _types = {
        "metric_name": str,
        "metric_value": int,
    }

    def __init__(self, d=None):
        self.metric_name: Optional[str] = None
        self.metric_value: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApplicationAppUsageBuilder":
        return ApplicationAppUsageBuilder()


class ApplicationAppUsageBuilder(object):
    def __init__(self) -> None:
        self._application_app_usage = ApplicationAppUsage()

    def metric_name(self, metric_name: str) -> "ApplicationAppUsageBuilder":
        self._application_app_usage.metric_name = metric_name
        return self

    def metric_value(self, metric_value: int) -> "ApplicationAppUsageBuilder":
        self._application_app_usage.metric_value = metric_value
        return self

    def build(self) -> "ApplicationAppUsage":
        return self._application_app_usage
