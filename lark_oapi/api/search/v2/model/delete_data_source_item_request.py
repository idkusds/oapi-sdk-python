# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteDataSourceItemRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.data_source_id: Optional[str] = None
        self.item_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteDataSourceItemRequestBuilder":
        return DeleteDataSourceItemRequestBuilder()


class DeleteDataSourceItemRequestBuilder(object):

    def __init__(self) -> None:
        delete_data_source_item_request = DeleteDataSourceItemRequest()
        delete_data_source_item_request.http_method = HttpMethod.DELETE
        delete_data_source_item_request.uri = "/open-apis/search/v2/data_sources/:data_source_id/items/:item_id"
        delete_data_source_item_request.token_types = {AccessTokenType.TENANT}
        self._delete_data_source_item_request: DeleteDataSourceItemRequest = delete_data_source_item_request

    def data_source_id(self, data_source_id: str) -> "DeleteDataSourceItemRequestBuilder":
        self._delete_data_source_item_request.data_source_id = data_source_id
        self._delete_data_source_item_request.paths["data_source_id"] = str(data_source_id)
        return self

    def item_id(self, item_id: str) -> "DeleteDataSourceItemRequestBuilder":
        self._delete_data_source_item_request.item_id = item_id
        self._delete_data_source_item_request.paths["item_id"] = str(item_id)
        return self

    def build(self) -> DeleteDataSourceItemRequest:
        return self._delete_data_source_item_request
