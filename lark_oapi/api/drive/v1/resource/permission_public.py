# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.get_permission_public_request import GetPermissionPublicRequest
from ..model.get_permission_public_response import GetPermissionPublicResponse
from ..model.patch_permission_public_request import PatchPermissionPublicRequest
from ..model.patch_permission_public_response import PatchPermissionPublicResponse


class PermissionPublic(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def get(self, request: GetPermissionPublicRequest,
            option: Optional[RequestOption] = None) -> GetPermissionPublicResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetPermissionPublicResponse = JSON.unmarshal(str(resp.content, UTF_8), GetPermissionPublicResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchPermissionPublicRequest,
              option: Optional[RequestOption] = None) -> PatchPermissionPublicResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: PatchPermissionPublicResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                 PatchPermissionPublicResponse)
        response.raw = resp

        return response
