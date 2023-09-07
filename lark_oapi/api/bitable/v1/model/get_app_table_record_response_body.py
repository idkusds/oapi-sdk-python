# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .app_table_record import AppTableRecord


class GetAppTableRecordResponseBody(object):
    _types = {
        "record": AppTableRecord,
    }

    def __init__(self, d=None):
        self.record: Optional[AppTableRecord] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetAppTableRecordResponseBodyBuilder":
        return GetAppTableRecordResponseBodyBuilder()


class GetAppTableRecordResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_app_table_record_response_body = GetAppTableRecordResponseBody()

    def record(self, record: AppTableRecord) -> "GetAppTableRecordResponseBodyBuilder":
        self._get_app_table_record_response_body.record = record
        return self

    def build(self) -> "GetAppTableRecordResponseBody":
        return self._get_app_table_record_response_body
