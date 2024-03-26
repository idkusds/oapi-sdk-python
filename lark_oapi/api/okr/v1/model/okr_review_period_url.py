# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class OkrReviewPeriodUrl(object):
    _types = {
        "url": str,
        "create_time": int,
    }

    def __init__(self, d=None):
        self.url: Optional[str] = None
        self.create_time: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OkrReviewPeriodUrlBuilder":
        return OkrReviewPeriodUrlBuilder()


class OkrReviewPeriodUrlBuilder(object):
    def __init__(self) -> None:
        self._okr_review_period_url = OkrReviewPeriodUrl()

    def url(self, url: str) -> "OkrReviewPeriodUrlBuilder":
        self._okr_review_period_url.url = url
        return self

    def create_time(self, create_time: int) -> "OkrReviewPeriodUrlBuilder":
        self._okr_review_period_url.create_time = create_time
        return self

    def build(self) -> "OkrReviewPeriodUrl":
        return self._okr_review_period_url
