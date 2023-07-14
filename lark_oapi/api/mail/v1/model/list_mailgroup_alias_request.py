# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListMailgroupAliasRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.mailgroup_id: Optional[str] = None

    @staticmethod
    def builder() -> "ListMailgroupAliasRequestBuilder":
        return ListMailgroupAliasRequestBuilder()


class ListMailgroupAliasRequestBuilder(object):

    def __init__(self, list_mailgroup_alias_request: ListMailgroupAliasRequest = ListMailgroupAliasRequest()) -> None:
        list_mailgroup_alias_request.http_method = HttpMethod.GET
        list_mailgroup_alias_request.uri = "/open-apis/mail/v1/mailgroups/:mailgroup_id/aliases"
        list_mailgroup_alias_request.token_types = {AccessTokenType.TENANT}
        self._list_mailgroup_alias_request: ListMailgroupAliasRequest = list_mailgroup_alias_request
    
    def mailgroup_id(self, mailgroup_id: str) -> "ListMailgroupAliasRequestBuilder":
        self._list_mailgroup_alias_request.mailgroup_id = mailgroup_id
        self._list_mailgroup_alias_request.paths["mailgroup_id"] = mailgroup_id
        return self
    

    def build(self) -> ListMailgroupAliasRequest:
        return self._list_mailgroup_alias_request