# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.batch_create_functional_role_member_request import BatchCreateFunctionalRoleMemberRequest
from ..model.batch_create_functional_role_member_response import BatchCreateFunctionalRoleMemberResponse
from ..model.batch_delete_functional_role_member_request import BatchDeleteFunctionalRoleMemberRequest
from ..model.batch_delete_functional_role_member_response import BatchDeleteFunctionalRoleMemberResponse
from ..model.get_functional_role_member_request import GetFunctionalRoleMemberRequest
from ..model.get_functional_role_member_response import GetFunctionalRoleMemberResponse
from ..model.list_functional_role_member_request import ListFunctionalRoleMemberRequest
from ..model.list_functional_role_member_response import ListFunctionalRoleMemberResponse
from ..model.scopes_functional_role_member_request import ScopesFunctionalRoleMemberRequest
from ..model.scopes_functional_role_member_response import ScopesFunctionalRoleMemberResponse


class FunctionalRoleMember(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def batch_create(self, request: BatchCreateFunctionalRoleMemberRequest,
                     option: Optional[RequestOption] = None) -> BatchCreateFunctionalRoleMemberResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: BatchCreateFunctionalRoleMemberResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                           BatchCreateFunctionalRoleMemberResponse)
        response.raw = resp

        return response

    def batch_delete(self, request: BatchDeleteFunctionalRoleMemberRequest,
                     option: Optional[RequestOption] = None) -> BatchDeleteFunctionalRoleMemberResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: BatchDeleteFunctionalRoleMemberResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                           BatchDeleteFunctionalRoleMemberResponse)
        response.raw = resp

        return response

    def get(self, request: GetFunctionalRoleMemberRequest,
            option: Optional[RequestOption] = None) -> GetFunctionalRoleMemberResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetFunctionalRoleMemberResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                   GetFunctionalRoleMemberResponse)
        response.raw = resp

        return response

    def list(self, request: ListFunctionalRoleMemberRequest,
             option: Optional[RequestOption] = None) -> ListFunctionalRoleMemberResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListFunctionalRoleMemberResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                    ListFunctionalRoleMemberResponse)
        response.raw = resp

        return response

    def scopes(self, request: ScopesFunctionalRoleMemberRequest,
               option: Optional[RequestOption] = None) -> ScopesFunctionalRoleMemberResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ScopesFunctionalRoleMemberResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                      ScopesFunctionalRoleMemberResponse)
        response.raw = resp

        return response
