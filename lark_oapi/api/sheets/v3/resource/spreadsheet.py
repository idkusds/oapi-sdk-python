# Code generated by Lark OpenAPI.

import io
from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core import JSON
from lark_oapi.core.token import verify
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.utils import Files
from requests_toolbelt import MultipartEncoder
from ..model.create_spreadsheet_request import CreateSpreadsheetRequest
from ..model.create_spreadsheet_response import CreateSpreadsheetResponse
from ..model.get_spreadsheet_request import GetSpreadsheetRequest
from ..model.get_spreadsheet_response import GetSpreadsheetResponse
from ..model.patch_spreadsheet_request import PatchSpreadsheetRequest
from ..model.patch_spreadsheet_response import PatchSpreadsheetResponse


class Spreadsheet(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateSpreadsheetRequest,
               option: Optional[RequestOption] = None) -> CreateSpreadsheetResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateSpreadsheetResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateSpreadsheetResponse)
        response.raw = resp

        return response

    async def acreate(self, request: CreateSpreadsheetRequest,
                      option: Optional[RequestOption] = None) -> CreateSpreadsheetResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: CreateSpreadsheetResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateSpreadsheetResponse)
        response.raw = resp

        return response

    def get(self, request: GetSpreadsheetRequest, option: Optional[RequestOption] = None) -> GetSpreadsheetResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetSpreadsheetResponse = JSON.unmarshal(str(resp.content, UTF_8), GetSpreadsheetResponse)
        response.raw = resp

        return response

    async def aget(self, request: GetSpreadsheetRequest,
                   option: Optional[RequestOption] = None) -> GetSpreadsheetResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: GetSpreadsheetResponse = JSON.unmarshal(str(resp.content, UTF_8), GetSpreadsheetResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchSpreadsheetRequest,
              option: Optional[RequestOption] = None) -> PatchSpreadsheetResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: PatchSpreadsheetResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchSpreadsheetResponse)
        response.raw = resp

        return response

    async def apatch(self, request: PatchSpreadsheetRequest,
                     option: Optional[RequestOption] = None) -> PatchSpreadsheetResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: PatchSpreadsheetResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchSpreadsheetResponse)
        response.raw = resp

        return response
