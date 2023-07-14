# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class DeleteSpreadsheetSheetFilterViewConditionRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.spreadsheet_token: Optional[str] = None
        self.sheet_id: Optional[str] = None
        self.filter_view_id: Optional[str] = None
        self.condition_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteSpreadsheetSheetFilterViewConditionRequestBuilder":
        return DeleteSpreadsheetSheetFilterViewConditionRequestBuilder()


class DeleteSpreadsheetSheetFilterViewConditionRequestBuilder(object):

    def __init__(self, delete_spreadsheet_sheet_filter_view_condition_request: DeleteSpreadsheetSheetFilterViewConditionRequest = DeleteSpreadsheetSheetFilterViewConditionRequest()) -> None:
        delete_spreadsheet_sheet_filter_view_condition_request.http_method = HttpMethod.DELETE
        delete_spreadsheet_sheet_filter_view_condition_request.uri = "/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/filter_views/:filter_view_id/conditions/:condition_id"
        delete_spreadsheet_sheet_filter_view_condition_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._delete_spreadsheet_sheet_filter_view_condition_request: DeleteSpreadsheetSheetFilterViewConditionRequest = delete_spreadsheet_sheet_filter_view_condition_request
    
    def spreadsheet_token(self, spreadsheet_token: str) -> "DeleteSpreadsheetSheetFilterViewConditionRequestBuilder":
        self._delete_spreadsheet_sheet_filter_view_condition_request.spreadsheet_token = spreadsheet_token
        self._delete_spreadsheet_sheet_filter_view_condition_request.paths["spreadsheet_token"] = spreadsheet_token
        return self
    
    def sheet_id(self, sheet_id: str) -> "DeleteSpreadsheetSheetFilterViewConditionRequestBuilder":
        self._delete_spreadsheet_sheet_filter_view_condition_request.sheet_id = sheet_id
        self._delete_spreadsheet_sheet_filter_view_condition_request.paths["sheet_id"] = sheet_id
        return self
    
    def filter_view_id(self, filter_view_id: str) -> "DeleteSpreadsheetSheetFilterViewConditionRequestBuilder":
        self._delete_spreadsheet_sheet_filter_view_condition_request.filter_view_id = filter_view_id
        self._delete_spreadsheet_sheet_filter_view_condition_request.paths["filter_view_id"] = filter_view_id
        return self
    
    def condition_id(self, condition_id: str) -> "DeleteSpreadsheetSheetFilterViewConditionRequestBuilder":
        self._delete_spreadsheet_sheet_filter_view_condition_request.condition_id = condition_id
        self._delete_spreadsheet_sheet_filter_view_condition_request.paths["condition_id"] = condition_id
        return self
    

    def build(self) -> DeleteSpreadsheetSheetFilterViewConditionRequest:
        return self._delete_spreadsheet_sheet_filter_view_condition_request