# Code generated by Lark OpenAPI.

import io
from typing import *
from typing import IO
from lark_oapi.core.const import UTF_8, CONTENT_TYPE
from lark_oapi.core import JSON
from lark_oapi.core.token import verify
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.utils import Files
from requests_toolbelt import MultipartEncoder
from lark_oapi.api.im.v1.model.create_chat_tab_request import CreateChatTabRequest
from lark_oapi.api.im.v1.model.create_chat_tab_response import CreateChatTabResponse
from lark_oapi.api.im.v1.model.delete_tabs_chat_tab_request import DeleteTabsChatTabRequest
from lark_oapi.api.im.v1.model.delete_tabs_chat_tab_response import DeleteTabsChatTabResponse
from lark_oapi.api.im.v1.model.list_tabs_chat_tab_request import ListTabsChatTabRequest
from lark_oapi.api.im.v1.model.list_tabs_chat_tab_response import ListTabsChatTabResponse
from lark_oapi.api.im.v1.model.sort_tabs_chat_tab_request import SortTabsChatTabRequest
from lark_oapi.api.im.v1.model.sort_tabs_chat_tab_response import SortTabsChatTabResponse
from lark_oapi.api.im.v1.model.update_tabs_chat_tab_request import UpdateTabsChatTabRequest
from lark_oapi.api.im.v1.model.update_tabs_chat_tab_response import UpdateTabsChatTabResponse


class ChatTab(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreateChatTabRequest, option: RequestOption = RequestOption()) -> CreateChatTabResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: CreateChatTabResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateChatTabResponse)
        response.raw = resp

        return response

    def delete_tabs(self, request: DeleteTabsChatTabRequest, option: RequestOption = RequestOption()) -> DeleteTabsChatTabResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: DeleteTabsChatTabResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteTabsChatTabResponse)
        response.raw = resp

        return response

    def list_tabs(self, request: ListTabsChatTabRequest, option: RequestOption = RequestOption()) -> ListTabsChatTabResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: ListTabsChatTabResponse = JSON.unmarshal(str(resp.content, UTF_8), ListTabsChatTabResponse)
        response.raw = resp

        return response

    def sort_tabs(self, request: SortTabsChatTabRequest, option: RequestOption = RequestOption()) -> SortTabsChatTabResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: SortTabsChatTabResponse = JSON.unmarshal(str(resp.content, UTF_8), SortTabsChatTabResponse)
        response.raw = resp

        return response

    def update_tabs(self, request: UpdateTabsChatTabRequest, option: RequestOption = RequestOption()) -> UpdateTabsChatTabResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: UpdateTabsChatTabResponse = JSON.unmarshal(str(resp.content, UTF_8), UpdateTabsChatTabResponse)
        response.raw = resp

        return response

    