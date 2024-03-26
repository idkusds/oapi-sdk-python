# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class GetSpreadsheetSheetFilterViewRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.spreadsheet_token: Optional[str] = None
        self.sheet_id: Optional[str] = None
        self.filter_view_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetSpreadsheetSheetFilterViewRequestBuilder":
        return GetSpreadsheetSheetFilterViewRequestBuilder()


class GetSpreadsheetSheetFilterViewRequestBuilder(object):

    def __init__(self) -> None:
        get_spreadsheet_sheet_filter_view_request = GetSpreadsheetSheetFilterViewRequest()
        get_spreadsheet_sheet_filter_view_request.http_method = HttpMethod.GET
        get_spreadsheet_sheet_filter_view_request.uri = "/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/filter_views/:filter_view_id"
        get_spreadsheet_sheet_filter_view_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._get_spreadsheet_sheet_filter_view_request: GetSpreadsheetSheetFilterViewRequest = get_spreadsheet_sheet_filter_view_request

    def spreadsheet_token(self, spreadsheet_token: str) -> "GetSpreadsheetSheetFilterViewRequestBuilder":
        self._get_spreadsheet_sheet_filter_view_request.spreadsheet_token = spreadsheet_token
        self._get_spreadsheet_sheet_filter_view_request.paths["spreadsheet_token"] = str(spreadsheet_token)
        return self

    def sheet_id(self, sheet_id: str) -> "GetSpreadsheetSheetFilterViewRequestBuilder":
        self._get_spreadsheet_sheet_filter_view_request.sheet_id = sheet_id
        self._get_spreadsheet_sheet_filter_view_request.paths["sheet_id"] = str(sheet_id)
        return self

    def filter_view_id(self, filter_view_id: str) -> "GetSpreadsheetSheetFilterViewRequestBuilder":
        self._get_spreadsheet_sheet_filter_view_request.filter_view_id = filter_view_id
        self._get_spreadsheet_sheet_filter_view_request.paths["filter_view_id"] = str(filter_view_id)
        return self

    def build(self) -> GetSpreadsheetSheetFilterViewRequest:
        return self._get_spreadsheet_sheet_filter_view_request
