# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.copy_app_request import CopyAppRequest
from ..model.copy_app_response import CopyAppResponse
from ..model.create_app_request import CreateAppRequest
from ..model.create_app_response import CreateAppResponse
from ..model.get_app_request import GetAppRequest
from ..model.get_app_response import GetAppResponse
from ..model.update_app_request import UpdateAppRequest
from ..model.update_app_response import UpdateAppResponse


class App(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def copy(self, request: CopyAppRequest, option: Optional[RequestOption] = None) -> CopyAppResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CopyAppResponse = JSON.unmarshal(str(resp.content, UTF_8), CopyAppResponse)
        response.raw = resp

        return response

    def create(self, request: CreateAppRequest, option: Optional[RequestOption] = None) -> CreateAppResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateAppResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateAppResponse)
        response.raw = resp

        return response

    def get(self, request: GetAppRequest, option: Optional[RequestOption] = None) -> GetAppResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetAppResponse = JSON.unmarshal(str(resp.content, UTF_8), GetAppResponse)
        response.raw = resp

        return response

    def update(self, request: UpdateAppRequest, option: Optional[RequestOption] = None) -> UpdateAppResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: UpdateAppResponse = JSON.unmarshal(str(resp.content, UTF_8), UpdateAppResponse)
        response.raw = resp

        return response
