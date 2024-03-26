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
from ..model.get_user_info_request import GetUserInfoRequest
from ..model.get_user_info_response import GetUserInfoResponse


class UserInfo(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def get(self, request: GetUserInfoRequest, option: Optional[RequestOption] = None) -> GetUserInfoResponse:
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
        response: GetUserInfoResponse = JSON.unmarshal(str(resp.content, UTF_8), GetUserInfoResponse)
        response.raw = resp

        return response

    async def aget(self, request: GetUserInfoRequest, option: Optional[RequestOption] = None) -> GetUserInfoResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: GetUserInfoResponse = JSON.unmarshal(str(resp.content, UTF_8), GetUserInfoResponse)
        response.raw = resp

        return response
