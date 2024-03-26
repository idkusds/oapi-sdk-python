# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_spreadsheet_sheet_filter_view_condition_response_body import \
    CreateSpreadsheetSheetFilterViewConditionResponseBody


class CreateSpreadsheetSheetFilterViewConditionResponse(BaseResponse):
    _types = {
        "data": CreateSpreadsheetSheetFilterViewConditionResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateSpreadsheetSheetFilterViewConditionResponseBody] = None
        init(self, d, self._types)
