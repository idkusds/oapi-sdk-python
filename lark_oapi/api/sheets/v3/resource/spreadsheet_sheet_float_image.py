# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_spreadsheet_sheet_float_image_request import CreateSpreadsheetSheetFloatImageRequest
from ..model.create_spreadsheet_sheet_float_image_response import CreateSpreadsheetSheetFloatImageResponse
from ..model.delete_spreadsheet_sheet_float_image_request import DeleteSpreadsheetSheetFloatImageRequest
from ..model.delete_spreadsheet_sheet_float_image_response import DeleteSpreadsheetSheetFloatImageResponse
from ..model.get_spreadsheet_sheet_float_image_request import GetSpreadsheetSheetFloatImageRequest
from ..model.get_spreadsheet_sheet_float_image_response import GetSpreadsheetSheetFloatImageResponse
from ..model.patch_spreadsheet_sheet_float_image_request import PatchSpreadsheetSheetFloatImageRequest
from ..model.patch_spreadsheet_sheet_float_image_response import PatchSpreadsheetSheetFloatImageResponse
from ..model.query_spreadsheet_sheet_float_image_request import QuerySpreadsheetSheetFloatImageRequest
from ..model.query_spreadsheet_sheet_float_image_response import QuerySpreadsheetSheetFloatImageResponse


class SpreadsheetSheetFloatImage(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateSpreadsheetSheetFloatImageRequest,
               option: Optional[RequestOption] = None) -> CreateSpreadsheetSheetFloatImageResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateSpreadsheetSheetFloatImageResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                            CreateSpreadsheetSheetFloatImageResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteSpreadsheetSheetFloatImageRequest,
               option: Optional[RequestOption] = None) -> DeleteSpreadsheetSheetFloatImageResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteSpreadsheetSheetFloatImageResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                            DeleteSpreadsheetSheetFloatImageResponse)
        response.raw = resp

        return response

    def get(self, request: GetSpreadsheetSheetFloatImageRequest,
            option: Optional[RequestOption] = None) -> GetSpreadsheetSheetFloatImageResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetSpreadsheetSheetFloatImageResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                         GetSpreadsheetSheetFloatImageResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchSpreadsheetSheetFloatImageRequest,
              option: Optional[RequestOption] = None) -> PatchSpreadsheetSheetFloatImageResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: PatchSpreadsheetSheetFloatImageResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                           PatchSpreadsheetSheetFloatImageResponse)
        response.raw = resp

        return response

    def query(self, request: QuerySpreadsheetSheetFloatImageRequest,
              option: Optional[RequestOption] = None) -> QuerySpreadsheetSheetFloatImageResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: QuerySpreadsheetSheetFloatImageResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                           QuerySpreadsheetSheetFloatImageResponse)
        response.raw = resp

        return response
