# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_national_id_type_request import CreateNationalIdTypeRequest
from ..model.create_national_id_type_response import CreateNationalIdTypeResponse
from ..model.delete_national_id_type_request import DeleteNationalIdTypeRequest
from ..model.delete_national_id_type_response import DeleteNationalIdTypeResponse
from ..model.get_national_id_type_request import GetNationalIdTypeRequest
from ..model.get_national_id_type_response import GetNationalIdTypeResponse
from ..model.list_national_id_type_request import ListNationalIdTypeRequest
from ..model.list_national_id_type_response import ListNationalIdTypeResponse
from ..model.patch_national_id_type_request import PatchNationalIdTypeRequest
from ..model.patch_national_id_type_response import PatchNationalIdTypeResponse


class NationalIdType(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateNationalIdTypeRequest,
               option: Optional[RequestOption] = None) -> CreateNationalIdTypeResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateNationalIdTypeResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateNationalIdTypeResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteNationalIdTypeRequest,
               option: Optional[RequestOption] = None) -> DeleteNationalIdTypeResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteNationalIdTypeResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteNationalIdTypeResponse)
        response.raw = resp

        return response

    def get(self, request: GetNationalIdTypeRequest,
            option: Optional[RequestOption] = None) -> GetNationalIdTypeResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetNationalIdTypeResponse = JSON.unmarshal(str(resp.content, UTF_8), GetNationalIdTypeResponse)
        response.raw = resp

        return response

    def list(self, request: ListNationalIdTypeRequest,
             option: Optional[RequestOption] = None) -> ListNationalIdTypeResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListNationalIdTypeResponse = JSON.unmarshal(str(resp.content, UTF_8), ListNationalIdTypeResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchNationalIdTypeRequest,
              option: Optional[RequestOption] = None) -> PatchNationalIdTypeResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: PatchNationalIdTypeResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchNationalIdTypeResponse)
        response.raw = resp

        return response
