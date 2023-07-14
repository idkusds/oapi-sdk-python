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
from lark_oapi.api.drive.v1.model.auth_permission_member_request import AuthPermissionMemberRequest
from lark_oapi.api.drive.v1.model.auth_permission_member_response import AuthPermissionMemberResponse
from lark_oapi.api.drive.v1.model.create_permission_member_request import CreatePermissionMemberRequest
from lark_oapi.api.drive.v1.model.create_permission_member_response import CreatePermissionMemberResponse
from lark_oapi.api.drive.v1.model.delete_permission_member_request import DeletePermissionMemberRequest
from lark_oapi.api.drive.v1.model.delete_permission_member_response import DeletePermissionMemberResponse
from lark_oapi.api.drive.v1.model.list_permission_member_request import ListPermissionMemberRequest
from lark_oapi.api.drive.v1.model.list_permission_member_response import ListPermissionMemberResponse
from lark_oapi.api.drive.v1.model.transfer_owner_permission_member_request import TransferOwnerPermissionMemberRequest
from lark_oapi.api.drive.v1.model.transfer_owner_permission_member_response import TransferOwnerPermissionMemberResponse
from lark_oapi.api.drive.v1.model.update_permission_member_request import UpdatePermissionMemberRequest
from lark_oapi.api.drive.v1.model.update_permission_member_response import UpdatePermissionMemberResponse


class PermissionMember(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def auth(self, request: AuthPermissionMemberRequest, option: RequestOption = RequestOption()) -> AuthPermissionMemberResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: AuthPermissionMemberResponse = JSON.unmarshal(str(resp.content, UTF_8), AuthPermissionMemberResponse)
        response.raw = resp

        return response

    def create(self, request: CreatePermissionMemberRequest, option: RequestOption = RequestOption()) -> CreatePermissionMemberResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: CreatePermissionMemberResponse = JSON.unmarshal(str(resp.content, UTF_8), CreatePermissionMemberResponse)
        response.raw = resp

        return response

    def delete(self, request: DeletePermissionMemberRequest, option: RequestOption = RequestOption()) -> DeletePermissionMemberResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: DeletePermissionMemberResponse = JSON.unmarshal(str(resp.content, UTF_8), DeletePermissionMemberResponse)
        response.raw = resp

        return response

    def list(self, request: ListPermissionMemberRequest, option: RequestOption = RequestOption()) -> ListPermissionMemberResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: ListPermissionMemberResponse = JSON.unmarshal(str(resp.content, UTF_8), ListPermissionMemberResponse)
        response.raw = resp

        return response

    def transfer_owner(self, request: TransferOwnerPermissionMemberRequest, option: RequestOption = RequestOption()) -> TransferOwnerPermissionMemberResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: TransferOwnerPermissionMemberResponse = JSON.unmarshal(str(resp.content, UTF_8), TransferOwnerPermissionMemberResponse)
        response.raw = resp

        return response

    def update(self, request: UpdatePermissionMemberRequest, option: RequestOption = RequestOption()) -> UpdatePermissionMemberResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: UpdatePermissionMemberResponse = JSON.unmarshal(str(resp.content, UTF_8), UpdatePermissionMemberResponse)
        response.raw = resp

        return response

    