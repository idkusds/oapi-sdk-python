# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .batch_create_app_table_record_request_body import BatchCreateAppTableRecordRequestBody


class BatchCreateAppTableRecordRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.client_token: Optional[str] = None
        self.app_token: Optional[str] = None
        self.table_id: Optional[str] = None
        self.request_body: Optional[BatchCreateAppTableRecordRequestBody] = None

    @staticmethod
    def builder() -> "BatchCreateAppTableRecordRequestBuilder":
        return BatchCreateAppTableRecordRequestBuilder()


class BatchCreateAppTableRecordRequestBuilder(object):

    def __init__(self) -> None:
        batch_create_app_table_record_request = BatchCreateAppTableRecordRequest()
        batch_create_app_table_record_request.http_method = HttpMethod.POST
        batch_create_app_table_record_request.uri = "/open-apis/bitable/v1/apps/:app_token/tables/:table_id/records/batch_create"
        batch_create_app_table_record_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._batch_create_app_table_record_request: BatchCreateAppTableRecordRequest = batch_create_app_table_record_request

    def user_id_type(self, user_id_type: str) -> "BatchCreateAppTableRecordRequestBuilder":
        self._batch_create_app_table_record_request.user_id_type = user_id_type
        self._batch_create_app_table_record_request.add_query("user_id_type", user_id_type)
        return self

    def client_token(self, client_token: str) -> "BatchCreateAppTableRecordRequestBuilder":
        self._batch_create_app_table_record_request.client_token = client_token
        self._batch_create_app_table_record_request.add_query("client_token", client_token)
        return self

    def app_token(self, app_token: str) -> "BatchCreateAppTableRecordRequestBuilder":
        self._batch_create_app_table_record_request.app_token = app_token
        self._batch_create_app_table_record_request.paths["app_token"] = str(app_token)
        return self

    def table_id(self, table_id: str) -> "BatchCreateAppTableRecordRequestBuilder":
        self._batch_create_app_table_record_request.table_id = table_id
        self._batch_create_app_table_record_request.paths["table_id"] = str(table_id)
        return self

    def request_body(self,
                     request_body: BatchCreateAppTableRecordRequestBody) -> "BatchCreateAppTableRecordRequestBuilder":
        self._batch_create_app_table_record_request.request_body = request_body
        self._batch_create_app_table_record_request.body = request_body
        return self

    def build(self) -> BatchCreateAppTableRecordRequest:
        return self._batch_create_app_table_record_request
