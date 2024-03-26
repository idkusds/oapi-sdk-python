# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .batch_create_mailgroup_permission_member_request_body import BatchCreateMailgroupPermissionMemberRequestBody


class BatchCreateMailgroupPermissionMemberRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.mailgroup_id: Optional[str] = None
        self.request_body: Optional[BatchCreateMailgroupPermissionMemberRequestBody] = None

    @staticmethod
    def builder() -> "BatchCreateMailgroupPermissionMemberRequestBuilder":
        return BatchCreateMailgroupPermissionMemberRequestBuilder()


class BatchCreateMailgroupPermissionMemberRequestBuilder(object):

    def __init__(self) -> None:
        batch_create_mailgroup_permission_member_request = BatchCreateMailgroupPermissionMemberRequest()
        batch_create_mailgroup_permission_member_request.http_method = HttpMethod.POST
        batch_create_mailgroup_permission_member_request.uri = "/open-apis/mail/v1/mailgroups/:mailgroup_id/permission_members/batch_create"
        batch_create_mailgroup_permission_member_request.token_types = {AccessTokenType.TENANT}
        self._batch_create_mailgroup_permission_member_request: BatchCreateMailgroupPermissionMemberRequest = batch_create_mailgroup_permission_member_request

    def user_id_type(self, user_id_type: str) -> "BatchCreateMailgroupPermissionMemberRequestBuilder":
        self._batch_create_mailgroup_permission_member_request.user_id_type = user_id_type
        self._batch_create_mailgroup_permission_member_request.add_query("user_id_type", user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "BatchCreateMailgroupPermissionMemberRequestBuilder":
        self._batch_create_mailgroup_permission_member_request.department_id_type = department_id_type
        self._batch_create_mailgroup_permission_member_request.add_query("department_id_type", department_id_type)
        return self

    def mailgroup_id(self, mailgroup_id: str) -> "BatchCreateMailgroupPermissionMemberRequestBuilder":
        self._batch_create_mailgroup_permission_member_request.mailgroup_id = mailgroup_id
        self._batch_create_mailgroup_permission_member_request.paths["mailgroup_id"] = str(mailgroup_id)
        return self

    def request_body(self,
                     request_body: BatchCreateMailgroupPermissionMemberRequestBody) -> "BatchCreateMailgroupPermissionMemberRequestBuilder":
        self._batch_create_mailgroup_permission_member_request.request_body = request_body
        self._batch_create_mailgroup_permission_member_request.body = request_body
        return self

    def build(self) -> BatchCreateMailgroupPermissionMemberRequest:
        return self._batch_create_mailgroup_permission_member_request
