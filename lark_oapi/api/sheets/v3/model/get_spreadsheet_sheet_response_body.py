# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .sheet import Sheet


class GetSpreadsheetSheetResponseBody(object):
    _types = {
        "sheet": Sheet,
    }

    def __init__(self, d=None):
        self.sheet: Optional[Sheet] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetSpreadsheetSheetResponseBodyBuilder":
        return GetSpreadsheetSheetResponseBodyBuilder()


class GetSpreadsheetSheetResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_spreadsheet_sheet_response_body = GetSpreadsheetSheetResponseBody()

    def sheet(self, sheet: Sheet) -> "GetSpreadsheetSheetResponseBodyBuilder":
        self._get_spreadsheet_sheet_response_body.sheet = sheet
        return self

    def build(self) -> "GetSpreadsheetSheetResponseBody":
        return self._get_spreadsheet_sheet_response_body
