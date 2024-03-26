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
from ..model.detect_text_request import DetectTextRequest
from ..model.detect_text_response import DetectTextResponse
from ..model.translate_text_request import TranslateTextRequest
from ..model.translate_text_response import TranslateTextResponse


class Text(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def detect(self, request: DetectTextRequest, option: Optional[RequestOption] = None) -> DetectTextResponse:
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
        response: DetectTextResponse = JSON.unmarshal(str(resp.content, UTF_8), DetectTextResponse)
        response.raw = resp

        return response

    async def adetect(self, request: DetectTextRequest, option: Optional[RequestOption] = None) -> DetectTextResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: DetectTextResponse = JSON.unmarshal(str(resp.content, UTF_8), DetectTextResponse)
        response.raw = resp

        return response

    def translate(self, request: TranslateTextRequest, option: Optional[RequestOption] = None) -> TranslateTextResponse:
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
        response: TranslateTextResponse = JSON.unmarshal(str(resp.content, UTF_8), TranslateTextResponse)
        response.raw = resp

        return response

    async def atranslate(self, request: TranslateTextRequest,
                         option: Optional[RequestOption] = None) -> TranslateTextResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: TranslateTextResponse = JSON.unmarshal(str(resp.content, UTF_8), TranslateTextResponse)
        response.raw = resp

        return response
