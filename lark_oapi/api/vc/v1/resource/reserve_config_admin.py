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
from lark_oapi.api.vc.v1.model.get_reserve_config_admin_request import GetReserveConfigAdminRequest
from lark_oapi.api.vc.v1.model.get_reserve_config_admin_response import GetReserveConfigAdminResponse
from lark_oapi.api.vc.v1.model.patch_reserve_config_admin_request import PatchReserveConfigAdminRequest
from lark_oapi.api.vc.v1.model.patch_reserve_config_admin_response import PatchReserveConfigAdminResponse


class ReserveConfigAdmin(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def get(self, request: GetReserveConfigAdminRequest, option: RequestOption = RequestOption()) -> GetReserveConfigAdminResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: GetReserveConfigAdminResponse = JSON.unmarshal(str(resp.content, UTF_8), GetReserveConfigAdminResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchReserveConfigAdminRequest, option: RequestOption = RequestOption()) -> PatchReserveConfigAdminResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: PatchReserveConfigAdminResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchReserveConfigAdminResponse)
        response.raw = resp

        return response

    