# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class MetricItemRequest(object):
    _types = {
        "metric_item_id": str,
        "metric_initial_value": float,
        "metric_target_value": float,
        "metric_current_value": float,
        "supported_user_id": str,
    }

    def __init__(self, d=None):
        self.metric_item_id: Optional[str] = None
        self.metric_initial_value: Optional[float] = None
        self.metric_target_value: Optional[float] = None
        self.metric_current_value: Optional[float] = None
        self.supported_user_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MetricItemRequestBuilder":
        return MetricItemRequestBuilder()


class MetricItemRequestBuilder(object):
    def __init__(self) -> None:
        self._metric_item_request = MetricItemRequest()

    def metric_item_id(self, metric_item_id: str) -> "MetricItemRequestBuilder":
        self._metric_item_request.metric_item_id = metric_item_id
        return self

    def metric_initial_value(self, metric_initial_value: float) -> "MetricItemRequestBuilder":
        self._metric_item_request.metric_initial_value = metric_initial_value
        return self

    def metric_target_value(self, metric_target_value: float) -> "MetricItemRequestBuilder":
        self._metric_item_request.metric_target_value = metric_target_value
        return self

    def metric_current_value(self, metric_current_value: float) -> "MetricItemRequestBuilder":
        self._metric_item_request.metric_current_value = metric_current_value
        return self

    def supported_user_id(self, supported_user_id: str) -> "MetricItemRequestBuilder":
        self._metric_item_request.supported_user_id = supported_user_id
        return self

    def build(self) -> "MetricItemRequest":
        return self._metric_item_request
