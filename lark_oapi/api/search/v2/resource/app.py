# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_app_request import CreateAppRequest
from ..model.create_app_response import CreateAppResponse


class App(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

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
