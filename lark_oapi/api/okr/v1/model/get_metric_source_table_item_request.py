# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class GetMetricSourceTableItemRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.metric_source_id: Optional[str] = None
        self.metric_table_id: Optional[str] = None
        self.metric_item_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetMetricSourceTableItemRequestBuilder":
        return GetMetricSourceTableItemRequestBuilder()


class GetMetricSourceTableItemRequestBuilder(object):

    def __init__(self, get_metric_source_table_item_request: GetMetricSourceTableItemRequest = GetMetricSourceTableItemRequest()) -> None:
        get_metric_source_table_item_request.http_method = HttpMethod.GET
        get_metric_source_table_item_request.uri = "/open-apis/okr/v1/metric_sources/:metric_source_id/tables/:metric_table_id/items/:metric_item_id"
        get_metric_source_table_item_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._get_metric_source_table_item_request: GetMetricSourceTableItemRequest = get_metric_source_table_item_request
    
    def user_id_type(self, user_id_type: str) -> "GetMetricSourceTableItemRequestBuilder":
        self._get_metric_source_table_item_request.user_id_type = user_id_type
        self._get_metric_source_table_item_request.queries["user_id_type"] = str(user_id_type)
        return self
    
    def metric_source_id(self, metric_source_id: str) -> "GetMetricSourceTableItemRequestBuilder":
        self._get_metric_source_table_item_request.metric_source_id = metric_source_id
        self._get_metric_source_table_item_request.paths["metric_source_id"] = metric_source_id
        return self
    
    def metric_table_id(self, metric_table_id: str) -> "GetMetricSourceTableItemRequestBuilder":
        self._get_metric_source_table_item_request.metric_table_id = metric_table_id
        self._get_metric_source_table_item_request.paths["metric_table_id"] = metric_table_id
        return self
    
    def metric_item_id(self, metric_item_id: str) -> "GetMetricSourceTableItemRequestBuilder":
        self._get_metric_source_table_item_request.metric_item_id = metric_item_id
        self._get_metric_source_table_item_request.paths["metric_item_id"] = metric_item_id
        return self
    

    def build(self) -> GetMetricSourceTableItemRequest:
        return self._get_metric_source_table_item_request