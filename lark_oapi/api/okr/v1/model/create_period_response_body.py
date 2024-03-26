# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class CreatePeriodResponseBody(object):
    _types = {
        "period_id": str,
        "start_month": str,
        "end_month": str,
    }

    def __init__(self, d=None):
        self.period_id: Optional[str] = None
        self.start_month: Optional[str] = None
        self.end_month: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreatePeriodResponseBodyBuilder":
        return CreatePeriodResponseBodyBuilder()


class CreatePeriodResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_period_response_body = CreatePeriodResponseBody()

    def period_id(self, period_id: str) -> "CreatePeriodResponseBodyBuilder":
        self._create_period_response_body.period_id = period_id
        return self

    def start_month(self, start_month: str) -> "CreatePeriodResponseBodyBuilder":
        self._create_period_response_body.start_month = start_month
        return self

    def end_month(self, end_month: str) -> "CreatePeriodResponseBodyBuilder":
        self._create_period_response_body.end_month = end_month
        return self

    def build(self) -> "CreatePeriodResponseBody":
        return self._create_period_response_body
