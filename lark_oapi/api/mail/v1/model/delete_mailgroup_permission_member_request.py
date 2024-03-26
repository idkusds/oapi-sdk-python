# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class DeleteMailgroupPermissionMemberRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.mailgroup_id: Optional[str] = None
        self.permission_member_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteMailgroupPermissionMemberRequestBuilder":
        return DeleteMailgroupPermissionMemberRequestBuilder()


class DeleteMailgroupPermissionMemberRequestBuilder(object):

    def __init__(self) -> None:
        delete_mailgroup_permission_member_request = DeleteMailgroupPermissionMemberRequest()
        delete_mailgroup_permission_member_request.http_method = HttpMethod.DELETE
        delete_mailgroup_permission_member_request.uri = "/open-apis/mail/v1/mailgroups/:mailgroup_id/permission_members/:permission_member_id"
        delete_mailgroup_permission_member_request.token_types = {AccessTokenType.TENANT}
        self._delete_mailgroup_permission_member_request: DeleteMailgroupPermissionMemberRequest = delete_mailgroup_permission_member_request

    def mailgroup_id(self, mailgroup_id: str) -> "DeleteMailgroupPermissionMemberRequestBuilder":
        self._delete_mailgroup_permission_member_request.mailgroup_id = mailgroup_id
        self._delete_mailgroup_permission_member_request.paths["mailgroup_id"] = str(mailgroup_id)
        return self

    def permission_member_id(self, permission_member_id: str) -> "DeleteMailgroupPermissionMemberRequestBuilder":
        self._delete_mailgroup_permission_member_request.permission_member_id = permission_member_id
        self._delete_mailgroup_permission_member_request.paths["permission_member_id"] = str(permission_member_id)
        return self

    def build(self) -> DeleteMailgroupPermissionMemberRequest:
        return self._delete_mailgroup_permission_member_request
