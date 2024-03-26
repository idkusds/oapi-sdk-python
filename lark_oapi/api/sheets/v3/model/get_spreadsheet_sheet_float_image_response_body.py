# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .float_image import FloatImage


class GetSpreadsheetSheetFloatImageResponseBody(object):
    _types = {
        "float_image": FloatImage,
    }

    def __init__(self, d=None):
        self.float_image: Optional[FloatImage] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetSpreadsheetSheetFloatImageResponseBodyBuilder":
        return GetSpreadsheetSheetFloatImageResponseBodyBuilder()


class GetSpreadsheetSheetFloatImageResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_spreadsheet_sheet_float_image_response_body = GetSpreadsheetSheetFloatImageResponseBody()

    def float_image(self, float_image: FloatImage) -> "GetSpreadsheetSheetFloatImageResponseBodyBuilder":
        self._get_spreadsheet_sheet_float_image_response_body.float_image = float_image
        return self

    def build(self) -> "GetSpreadsheetSheetFloatImageResponseBody":
        return self._get_spreadsheet_sheet_float_image_response_body
