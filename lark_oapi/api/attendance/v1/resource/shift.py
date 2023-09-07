# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_shift_request import CreateShiftRequest
from ..model.create_shift_response import CreateShiftResponse
from ..model.delete_shift_request import DeleteShiftRequest
from ..model.delete_shift_response import DeleteShiftResponse
from ..model.get_shift_request import GetShiftRequest
from ..model.get_shift_response import GetShiftResponse
from ..model.list_shift_request import ListShiftRequest
from ..model.list_shift_response import ListShiftResponse
from ..model.query_shift_request import QueryShiftRequest
from ..model.query_shift_response import QueryShiftResponse


class Shift(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateShiftRequest, option: Optional[RequestOption] = None) -> CreateShiftResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateShiftResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateShiftResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteShiftRequest, option: Optional[RequestOption] = None) -> DeleteShiftResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteShiftResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteShiftResponse)
        response.raw = resp

        return response

    def get(self, request: GetShiftRequest, option: Optional[RequestOption] = None) -> GetShiftResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetShiftResponse = JSON.unmarshal(str(resp.content, UTF_8), GetShiftResponse)
        response.raw = resp

        return response

    def list(self, request: ListShiftRequest, option: Optional[RequestOption] = None) -> ListShiftResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListShiftResponse = JSON.unmarshal(str(resp.content, UTF_8), ListShiftResponse)
        response.raw = resp

        return response

    def query(self, request: QueryShiftRequest, option: Optional[RequestOption] = None) -> QueryShiftResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: QueryShiftResponse = JSON.unmarshal(str(resp.content, UTF_8), QueryShiftResponse)
        response.raw = resp

        return response
