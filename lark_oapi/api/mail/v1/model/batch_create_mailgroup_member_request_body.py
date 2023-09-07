# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .mailgroup_member import MailgroupMember


class BatchCreateMailgroupMemberRequestBody(object):
    _types = {
        "items": List[MailgroupMember],
    }

    def __init__(self, d=None):
        self.items: Optional[List[MailgroupMember]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchCreateMailgroupMemberRequestBodyBuilder":
        return BatchCreateMailgroupMemberRequestBodyBuilder()


class BatchCreateMailgroupMemberRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._batch_create_mailgroup_member_request_body = BatchCreateMailgroupMemberRequestBody()

    def items(self, items: List[MailgroupMember]) -> "BatchCreateMailgroupMemberRequestBodyBuilder":
        self._batch_create_mailgroup_member_request_body.items = items
        return self

    def build(self) -> "BatchCreateMailgroupMemberRequestBody":
        return self._batch_create_mailgroup_member_request_body
