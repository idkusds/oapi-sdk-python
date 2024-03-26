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
from ..model.create_space_request import CreateSpaceRequest
from ..model.create_space_response import CreateSpaceResponse
from ..model.get_space_request import GetSpaceRequest
from ..model.get_space_response import GetSpaceResponse
from ..model.get_node_space_request import GetNodeSpaceRequest
from ..model.get_node_space_response import GetNodeSpaceResponse
from ..model.list_space_request import ListSpaceRequest
from ..model.list_space_response import ListSpaceResponse


class Space(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateSpaceRequest, option: Optional[RequestOption] = None) -> CreateSpaceResponse:
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
        response: CreateSpaceResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateSpaceResponse)
        response.raw = resp

        return response

    async def acreate(self, request: CreateSpaceRequest, option: Optional[RequestOption] = None) -> CreateSpaceResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: CreateSpaceResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateSpaceResponse)
        response.raw = resp

        return response

    def get(self, request: GetSpaceRequest, option: Optional[RequestOption] = None) -> GetSpaceResponse:
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
        response: GetSpaceResponse = JSON.unmarshal(str(resp.content, UTF_8), GetSpaceResponse)
        response.raw = resp

        return response

    async def aget(self, request: GetSpaceRequest, option: Optional[RequestOption] = None) -> GetSpaceResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: GetSpaceResponse = JSON.unmarshal(str(resp.content, UTF_8), GetSpaceResponse)
        response.raw = resp

        return response

    def get_node(self, request: GetNodeSpaceRequest, option: Optional[RequestOption] = None) -> GetNodeSpaceResponse:
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
        response: GetNodeSpaceResponse = JSON.unmarshal(str(resp.content, UTF_8), GetNodeSpaceResponse)
        response.raw = resp

        return response

    async def aget_node(self, request: GetNodeSpaceRequest,
                        option: Optional[RequestOption] = None) -> GetNodeSpaceResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: GetNodeSpaceResponse = JSON.unmarshal(str(resp.content, UTF_8), GetNodeSpaceResponse)
        response.raw = resp

        return response

    def list(self, request: ListSpaceRequest, option: Optional[RequestOption] = None) -> ListSpaceResponse:
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
        response: ListSpaceResponse = JSON.unmarshal(str(resp.content, UTF_8), ListSpaceResponse)
        response.raw = resp

        return response

    async def alist(self, request: ListSpaceRequest, option: Optional[RequestOption] = None) -> ListSpaceResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: ListSpaceResponse = JSON.unmarshal(str(resp.content, UTF_8), ListSpaceResponse)
        response.raw = resp

        return response
