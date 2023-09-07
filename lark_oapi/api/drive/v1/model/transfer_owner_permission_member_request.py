# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .owner import Owner


class TransferOwnerPermissionMemberRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.type: Optional[str] = None
        self.need_notification: Optional[bool] = None
        self.remove_old_owner: Optional[bool] = None
        self.stay_put: Optional[bool] = None
        self.token: Optional[str] = None
        self.request_body: Optional[Owner] = None

    @staticmethod
    def builder() -> "TransferOwnerPermissionMemberRequestBuilder":
        return TransferOwnerPermissionMemberRequestBuilder()


class TransferOwnerPermissionMemberRequestBuilder(object):

    def __init__(self) -> None:
        transfer_owner_permission_member_request = TransferOwnerPermissionMemberRequest()
        transfer_owner_permission_member_request.http_method = HttpMethod.POST
        transfer_owner_permission_member_request.uri = "/open-apis/drive/v1/permissions/:token/members/transfer_owner"
        transfer_owner_permission_member_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._transfer_owner_permission_member_request: TransferOwnerPermissionMemberRequest = transfer_owner_permission_member_request

    def type(self, type: str) -> "TransferOwnerPermissionMemberRequestBuilder":
        self._transfer_owner_permission_member_request.type = type
        self._transfer_owner_permission_member_request.add_query("type", type)
        return self

    def need_notification(self, need_notification: bool) -> "TransferOwnerPermissionMemberRequestBuilder":
        self._transfer_owner_permission_member_request.need_notification = need_notification
        self._transfer_owner_permission_member_request.add_query("need_notification", need_notification)
        return self

    def remove_old_owner(self, remove_old_owner: bool) -> "TransferOwnerPermissionMemberRequestBuilder":
        self._transfer_owner_permission_member_request.remove_old_owner = remove_old_owner
        self._transfer_owner_permission_member_request.add_query("remove_old_owner", remove_old_owner)
        return self

    def stay_put(self, stay_put: bool) -> "TransferOwnerPermissionMemberRequestBuilder":
        self._transfer_owner_permission_member_request.stay_put = stay_put
        self._transfer_owner_permission_member_request.add_query("stay_put", stay_put)
        return self

    def token(self, token: str) -> "TransferOwnerPermissionMemberRequestBuilder":
        self._transfer_owner_permission_member_request.token = token
        self._transfer_owner_permission_member_request.paths["token"] = str(token)
        return self

    def request_body(self, request_body: Owner) -> "TransferOwnerPermissionMemberRequestBuilder":
        self._transfer_owner_permission_member_request.request_body = request_body
        self._transfer_owner_permission_member_request.body = request_body
        return self

    def build(self) -> TransferOwnerPermissionMemberRequest:
        return self._transfer_owner_permission_member_request
