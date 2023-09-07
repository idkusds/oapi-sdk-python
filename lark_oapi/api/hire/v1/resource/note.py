# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_note_request import CreateNoteRequest
from ..model.create_note_response import CreateNoteResponse
from ..model.get_note_request import GetNoteRequest
from ..model.get_note_response import GetNoteResponse
from ..model.list_note_request import ListNoteRequest
from ..model.list_note_response import ListNoteResponse
from ..model.patch_note_request import PatchNoteRequest
from ..model.patch_note_response import PatchNoteResponse


class Note(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateNoteRequest, option: Optional[RequestOption] = None) -> CreateNoteResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateNoteResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateNoteResponse)
        response.raw = resp

        return response

    def get(self, request: GetNoteRequest, option: Optional[RequestOption] = None) -> GetNoteResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetNoteResponse = JSON.unmarshal(str(resp.content, UTF_8), GetNoteResponse)
        response.raw = resp

        return response

    def list(self, request: ListNoteRequest, option: Optional[RequestOption] = None) -> ListNoteResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListNoteResponse = JSON.unmarshal(str(resp.content, UTF_8), ListNoteResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchNoteRequest, option: Optional[RequestOption] = None) -> PatchNoteResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: PatchNoteResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchNoteResponse)
        response.raw = resp

        return response
