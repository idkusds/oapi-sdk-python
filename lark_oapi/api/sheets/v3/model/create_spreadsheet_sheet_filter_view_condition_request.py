# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .filter_view_condition import FilterViewCondition


class CreateSpreadsheetSheetFilterViewConditionRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.spreadsheet_token: Optional[str] = None
        self.sheet_id: Optional[str] = None
        self.filter_view_id: Optional[str] = None
        self.request_body: Optional[FilterViewCondition] = None

    @staticmethod
    def builder() -> "CreateSpreadsheetSheetFilterViewConditionRequestBuilder":
        return CreateSpreadsheetSheetFilterViewConditionRequestBuilder()


class CreateSpreadsheetSheetFilterViewConditionRequestBuilder(object):

    def __init__(self) -> None:
        create_spreadsheet_sheet_filter_view_condition_request = CreateSpreadsheetSheetFilterViewConditionRequest()
        create_spreadsheet_sheet_filter_view_condition_request.http_method = HttpMethod.POST
        create_spreadsheet_sheet_filter_view_condition_request.uri = "/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/filter_views/:filter_view_id/conditions"
        create_spreadsheet_sheet_filter_view_condition_request.token_types = {AccessTokenType.TENANT,
                                                                              AccessTokenType.USER}
        self._create_spreadsheet_sheet_filter_view_condition_request: CreateSpreadsheetSheetFilterViewConditionRequest = create_spreadsheet_sheet_filter_view_condition_request

    def spreadsheet_token(self, spreadsheet_token: str) -> "CreateSpreadsheetSheetFilterViewConditionRequestBuilder":
        self._create_spreadsheet_sheet_filter_view_condition_request.spreadsheet_token = spreadsheet_token
        self._create_spreadsheet_sheet_filter_view_condition_request.paths["spreadsheet_token"] = str(spreadsheet_token)
        return self

    def sheet_id(self, sheet_id: str) -> "CreateSpreadsheetSheetFilterViewConditionRequestBuilder":
        self._create_spreadsheet_sheet_filter_view_condition_request.sheet_id = sheet_id
        self._create_spreadsheet_sheet_filter_view_condition_request.paths["sheet_id"] = str(sheet_id)
        return self

    def filter_view_id(self, filter_view_id: str) -> "CreateSpreadsheetSheetFilterViewConditionRequestBuilder":
        self._create_spreadsheet_sheet_filter_view_condition_request.filter_view_id = filter_view_id
        self._create_spreadsheet_sheet_filter_view_condition_request.paths["filter_view_id"] = str(filter_view_id)
        return self

    def request_body(self,
                     request_body: FilterViewCondition) -> "CreateSpreadsheetSheetFilterViewConditionRequestBuilder":
        self._create_spreadsheet_sheet_filter_view_condition_request.request_body = request_body
        self._create_spreadsheet_sheet_filter_view_condition_request.body = request_body
        return self

    def build(self) -> CreateSpreadsheetSheetFilterViewConditionRequest:
        return self._create_spreadsheet_sheet_filter_view_condition_request
